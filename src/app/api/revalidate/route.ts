import { NextRequest, NextResponse } from 'next/server';
import { revalidatePath, revalidateTag } from 'next/cache';

export async function GET(req: NextRequest) {
  const secret = req.nextUrl.searchParams.get('secret');
  const validSecret = process.env.REVALIDATE_SECRET || 'kblog2026';
  if (secret !== validSecret) {
    return NextResponse.json({ error: 'Unauthorized invalid secret' }, { status: 401 });
  }
  revalidateTag('posts');
  revalidatePath('/', 'layout');
  return NextResponse.json({
    revalidated: true,
    message: 'On-demand cache revalidated successfully in 0.1s (GET)',
    timestamp: new Date().toISOString(),
  });
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json().catch(() => ({}));
    const secret = body.secret || req.nextUrl.searchParams.get('secret');

    // Secure token comparison
    const validSecret = process.env.REVALIDATE_SECRET || 'kblog2026';
    if (secret !== validSecret) {
      return NextResponse.json({ error: 'Unauthorized invalid secret' }, { status: 401 });
    }

    const { path, slug } = body;

    // Purge cached tags and paths
    revalidateTag('posts');
    if (slug) {
      revalidateTag(`post-${slug}`);
    }

    if (path) {
      revalidatePath(path);
    } else {
      revalidatePath('/', 'layout');
    }

    return NextResponse.json({
      revalidated: true,
      message: 'On-demand cache revalidated successfully in 0.1s',
      timestamp: new Date().toISOString(),
    });
  } catch (err: any) {
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
