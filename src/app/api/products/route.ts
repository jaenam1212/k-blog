import { NextRequest, NextResponse } from 'next/server';
import { PRODUCTS, getProductsByCategory, searchProducts } from '@/lib/products';
import { Locale } from '@/lib/i18n';

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const category = searchParams.get('category') || 'all';
  const query = searchParams.get('q');
  const lang = (searchParams.get('lang') || 'en') as Locale;

  let items = category === 'all' ? PRODUCTS : getProductsByCategory(category);

  if (query) {
    items = searchProducts(query, lang);
  }

  const localizedItems = items.map((p) => {
    const loc = p.i18n[lang] || p.i18n.en;
    return {
      id: p.id,
      slug: p.slug,
      category: p.category,
      store: p.store,
      priceKrw: p.priceKrw,
      releaseDate: p.releaseDate,
      rating: p.rating,
      title: loc.title,
      summary: loc.summary,
      tasteReview: loc.tasteReview,
      tips: loc.tips,
      url: `https://k-trendbox.com/${lang}/post/${p.slug}`,
      affiliateUrl: p.affiliateUrl,
    };
  });

  return NextResponse.json({
    total: localizedItems.length,
    language: lang,
    products: localizedItems,
  });
}
