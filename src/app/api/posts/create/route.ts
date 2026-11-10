import { NextRequest, NextResponse } from 'next/server';
import { revalidatePath, revalidateTag } from 'next/cache';
import { Product } from '@/lib/products';

const SUPABASE_URL = process.env.NEXT_PUBLIC_SUPABASE_URL || 'https://jmuqmvxubuwhoocuknnt.supabase.co';
const SUPABASE_SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY || 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptdXFtdnh1YnV3aG9vY3Vrbm50Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDMwODA3NywiZXhwIjoyMTA5ODg0MDc3fQ.ELyAmyRJrWdQoIHRu4thMGvjAnjJfVZ4S8Cfpb9MiDY';

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { secret, post } = body;

    const validSecret = process.env.REVALIDATE_SECRET || 'kblog2026';
    if (secret !== validSecret) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    if (!post || !post.slug || !post.i18n) {
      return NextResponse.json({ error: 'Invalid post payload' }, { status: 400 });
    }

    // Insert into Supabase posts table
    const res = await fetch(`${SUPABASE_URL}/rest/v1/posts`, {
      method: 'POST',
      headers: {
        apikey: SUPABASE_SERVICE_KEY,
        Authorization: `Bearer ${SUPABASE_SERVICE_KEY}`,
        'Content-Type': 'application/json',
        Prefer: 'return=representation',
      },
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
      url: `https://k-blog-ten.vercel.app/ko/post/${post.slug}`,
    });
  } catch (err: any) {
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
