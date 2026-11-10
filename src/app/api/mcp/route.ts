import { NextRequest, NextResponse } from 'next/server';
import {
  SERVER_INFO,
  PROTOCOL_VERSION,
  MCP_TOOLS,
  executeMcpTool,
} from '@/lib/mcp-tools';

export const dynamic = 'force-dynamic';

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, MCP-Protocol-Version',
};

const jsonRpc = (id: any, result: any) =>
  NextResponse.json({ jsonrpc: '2.0', id, result }, { headers: CORS_HEADERS });

const jsonRpcError = (id: any, code: number, message: string) =>
  NextResponse.json(
    { jsonrpc: '2.0', id, error: { code, message } },
    { status: 400, headers: CORS_HEADERS }
  );

export async function OPTIONS() {
  return new NextResponse(null, { status: 204, headers: CORS_HEADERS });
}

export async function GET() {
  return NextResponse.json(
    {
      status: 'active',
      server: SERVER_INFO,
      protocolVersion: PROTOCOL_VERSION,
      discoveryUrl: '/.well-known/mcp.json',
      toolsCount: MCP_TOOLS.length,
      tools: MCP_TOOLS.map((t) => ({ name: t.name, description: t.description })),
      documentation: 'Send POST requests with JSON-RPC 2.0 payload to interact with MCP tools.',
    },
    { headers: CORS_HEADERS }
  );
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { id = null, method, params = {} } = body;

    if (!method) {
      return jsonRpcError(id, -32600, 'Invalid Request: Missing method');
    }

    if (method === 'initialize') {
      return jsonRpc(id, {
        protocolVersion: PROTOCOL_VERSION,
        capabilities: {
          tools: {
            listChanged: false,
          },
        },
        serverInfo: SERVER_INFO,
      });
    }

    if (method === 'tools/list') {
      return jsonRpc(id, { tools: MCP_TOOLS });
    }

    if (method === 'tools/call') {
      const { name, arguments: args = {} } = params;
      if (!name) {
        return jsonRpcError(id, -32602, 'Missing tool name in params');
      }

      try {
        const result = await executeMcpTool(name, args);
        return jsonRpc(id, result);
      } catch (err: any) {
        return jsonRpcError(id, -32603, err?.message || 'Tool execution error');
      }
    }

    if (method === 'ping') {
      return jsonRpc(id, {});
    }

    return jsonRpcError(id, -32601, `Method not found: ${method}`);
  } catch (error: any) {
    return jsonRpcError(null, -32700, `Parse error: ${error?.message}`);
  }
}
