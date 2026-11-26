import { NextRequest, NextResponse } from 'next/server';
import { revalidatePath, revalidateTag } from 'next/cache';
import {
  INVALID_SECRET_MESSAGE,
  SECRET_NOT_CONFIGURED_MESSAGE,
  isRevalidateSecretConfigured,
  isValidRevalidateSecret,
} from '@/lib/revalidate-auth';

function guard(given: string | null | undefined) {
  if (!isRevalidateSecretConfigured()) {
    return NextResponse.json({ error: SECRET_NOT_CONFIGURED_MESSAGE }, { status: 500 });
  }
  if (!isValidRevalidateSecret(given)) {
    return NextResponse.json({ error: INVALID_SECRET_MESSAGE }, { status: 401 });
  }
  return null;
}

export async function GET(req: NextRequest) {
  const denied = guard(req.nextUrl.searchParams.get('secret'));
  if (denied) return denied;

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
    const denied = guard(body.secret || req.nextUrl.searchParams.get('secret'));
    if (denied) return denied;

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
