import { NextRequest, NextResponse } from 'next/server';
import { revalidatePath, revalidateTag } from 'next/cache';
import { Product } from '@/lib/products';
import { siteUrl } from '@/lib/site';
import { supabaseAuthHeaders } from '@/lib/supabase-headers';
import {
  INVALID_SECRET_MESSAGE,
  SECRET_NOT_CONFIGURED_MESSAGE,
  isRevalidateSecretConfigured,
  isValidRevalidateSecret,
} from '@/lib/revalidate-auth';

/**
 * Supabase admin connection, read from the environment only.
 * The repository is public, so no key may be baked into the source.
 */
function supabaseConfig() {
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL?.trim();
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY?.trim();
  const missing: string[] = [];
  if (!url) missing.push('NEXT_PUBLIC_SUPABASE_URL');
  if (!serviceKey) missing.push('SUPABASE_SERVICE_ROLE_KEY');
  return { url, serviceKey, missing };
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { secret, post } = body;

    if (!isRevalidateSecretConfigured()) {
      return NextResponse.json({ error: SECRET_NOT_CONFIGURED_MESSAGE }, { status: 500 });
    }
    if (!isValidRevalidateSecret(secret)) {
      return NextResponse.json({ error: INVALID_SECRET_MESSAGE }, { status: 401 });
    }

    if (!post || !post.slug || !post.i18n) {
      return NextResponse.json({ error: 'Invalid post payload' }, { status: 400 });
    }

    const { url: supabaseUrl, serviceKey, missing } = supabaseConfig();
    if (missing.length > 0) {
      return NextResponse.json(
        { error: `Server is missing required environment variables: ${missing.join(', ')}` },
        { status: 500 },
      );
    }

    // Insert into Supabase posts table
    const res = await fetch(`${supabaseUrl}/rest/v1/posts`, {
      method: 'POST',
      headers: supabaseAuthHeaders(serviceKey as string, {
        'Content-Type': 'application/json',
        Prefer: 'return=representation',
      }),
      body: JSON.stringify({
        slug: post.slug,
        data: post,
      }),
    });

    if (!res.ok) {
      const errText = await res.text();
      return NextResponse.json({ error: `Supabase insert failed: ${errText}` }, { status: 500 });
    }

    const insertedRows = await res.json();

    // Trigger instant ISR cache invalidation
    revalidateTag('posts');
    revalidateTag(`post-${post.slug}`);
    revalidatePath('/', 'layout');

    return NextResponse.json({
      success: true,
      inserted: insertedRows[0],
      message: 'Post published and cache revalidated instantly without redeployment!',
      url: siteUrl(`/ko/post/${post.slug}`),
    });
  } catch (err: any) {
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
