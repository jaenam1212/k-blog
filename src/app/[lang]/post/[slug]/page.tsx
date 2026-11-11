import { notFound } from 'next/navigation';
import Link from 'next/link';
import { getProductBySlugAsync, fetchProductsFromDb } from '@/lib/products';
import { Locale, DICTIONARY, LOCALES } from '@/lib/i18n';
import { AdSenseSlot } from '@/components/AdSenseSlot';
import { AffiliateButton } from '@/components/AffiliateButton';

export const revalidate = 60;

export async function generateStaticParams() {
  const products = await fetchProductsFromDb();
  const params: { lang: string; slug: string }[] = [];
  for (const lang of LOCALES) {
    for (const product of products) {
      params.push({ lang, slug: product.slug });
    }
  }
  return params;
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ lang: string; slug: string }>;
}) {
  const { lang, slug } = await params;
  const product = await getProductBySlugAsync(slug);
  if (!product) return {};

  const content = product.i18n[lang as Locale] || product.i18n.en;

  const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://k-blog-ten.vercel.app';
  const languagesObj: Record<string, string> = {};
  for (const l of LOCALES) {
    languagesObj[l] = `${siteUrl}/${l}/post/${slug}`;
  }

  const allImages = product.images && product.images.length > 0 ? product.images : [product.imageUrl];

  return {
    title: `${content.title} | K-Trend Archive`,
    description: content.summary,
    alternates: {
      canonical: `${siteUrl}/${lang}/post/${slug}`,
      languages: languagesObj,
    },
    openGraph: {
      title: content.title,
      description: content.summary,
      images: allImages,
    },
  };
}

export default async function ProductDetailPage({
  params,
}: {
  params: Promise<{ lang: string; slug: string }>;
}) {
  const { lang, slug } = await params;
  const currentLang = lang as Locale;
  const product = await getProductBySlugAsync(slug);

  if (!product) {
    notFound();
  }

  const dict = DICTIONARY[currentLang] || DICTIONARY.en;
  const content = product.i18n[currentLang] || product.i18n.en;

  const categoryLabels: Record<string, string> = {
    'convenience-food': dict.convenienceFood,
    'k-beauty': dict.kBeauty,
    'k-fashion': dict.kFashion,
  };

  const allImages = product.images && product.images.length > 0 ? product.images : [product.imageUrl];

  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: content.title,
    image: allImages,
    description: content.description,
    brand: {
      '@type': 'Brand',
      name: product.store,
    },
    offers: {
      '@type': 'Offer',
      priceCurrency: 'KRW',
      price: product.priceKrw,
      availability: 'https://schema.org/InStock',
      url: product.affiliateUrl,
    },
    review: {
      '@type': 'Review',
      reviewRating: {
        '@type': 'Rating',
        ratingValue: product.rating,
        bestRating: '5',
      },
      author: {
        '@type': 'Person',
        name: 'K-Trend Archive',
      },
      reviewBody: content.description,
    },
    aggregateRating: {
      '@type': 'AggregateRating',
      ratingValue: product.rating,
      reviewCount: 42,
    },
  };

  return (
    <article className="max-w-2xl mx-auto py-4">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />

      {/* Back Link */}
      <div className="mb-6">
        <Link
          href={`/${currentLang}/${product.category}`}
          className="text-xs text-zinc-400 hover:text-zinc-700 dark:hover:text-zinc-300 transition-colors inline-flex items-center gap-1"
        >
          <span>←</span>
          <span>{categoryLabels[product.category] || product.category}</span>
        </Link>
      </div>

      {/* Header Info */}
      <header className="mb-8">
        <div className="flex items-center gap-2 text-xs font-mono text-zinc-400 dark:text-zinc-500 mb-3">
          <span>{product.store}</span>
          <span>·</span>
          <span>{product.releaseDate}</span>
          <span>·</span>
          <span className="font-semibold text-zinc-700 dark:text-zinc-300">
            ₩{product.priceKrw.toLocaleString('ko-KR')}
          </span>
        </div>

        <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-zinc-900 dark:text-zinc-100 leading-snug">
          {content.title}
        </h1>

        <p className="mt-4 text-sm sm:text-base text-zinc-500 dark:text-zinc-400 leading-relaxed">
          {content.summary}
        </p>
      </header>

      {/* Featured Main Image (Full silhouette framing, no head/hem cropping) */}
      <div className="rounded-xl overflow-hidden bg-zinc-100 dark:bg-zinc-900 my-8 border border-zinc-200/80 dark:border-zinc-800/80 flex items-center justify-center p-2 sm:p-4">
        <img
          src={product.imageUrl}
          alt={content.title}
          className="w-full h-auto max-h-[720px] object-contain rounded-lg mx-auto"
        />
      </div>

      {/* Lookbook / Multi-photo Gallery */}
      {product.images && product.images.length > 1 && (
        <section className="my-10">
          <div className="flex items-center justify-between mb-4 border-b border-zinc-200/80 dark:border-zinc-800 pb-2">
            <h2 className="text-xs font-mono uppercase tracking-wider text-zinc-500 dark:text-zinc-400">
              Lookbook & Detailed Cuts ({product.images.length})
            </h2>
            <span className="text-[11px] font-mono text-zinc-400">High-Res Gallery</span>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {product.images.map((imgUrl, idx) => (
              <div
                key={idx}
                className="group relative rounded-xl overflow-hidden bg-zinc-100 dark:bg-zinc-900 border border-zinc-200/80 dark:border-zinc-800 aspect-[3/4] flex items-center justify-center"
              >
                <img
                  src={imgUrl}
                  alt={`${content.title} - ${idx + 1}`}
                  className="w-full h-full object-cover group-hover:scale-102 transition-transform duration-300"
                  loading="lazy"
                />
                <span className="absolute bottom-2.5 left-2.5 bg-black/60 backdrop-blur-sm text-white text-[10px] font-mono px-2 py-0.5 rounded">
                  #{idx + 1}
                </span>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Top AdSense Banner */}
      <AdSenseSlot slotId="post-top-content" />

      {/* Main Review Body */}
      <div className="text-sm sm:text-base leading-relaxed text-zinc-700 dark:text-zinc-300 space-y-6">
        <p className="whitespace-pre-line leading-relaxed">
          {content.description}
        </p>

        {/* Recommended Example Items Grid (실물 추천 아이템 갤러리) */}
        {product.exampleItems && product.exampleItems.length > 0 && (
          <section className="my-8 pt-6 border-t border-zinc-200 dark:border-zinc-800">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xs font-mono uppercase tracking-wider text-zinc-900 dark:text-zinc-100 font-bold flex items-center gap-1.5">
                <span>💡 실전 추천 코디 아이템</span>
                <span className="text-zinc-400 font-normal">({product.exampleItems.length})</span>
              </h2>
              <span className="text-[11px] font-mono text-zinc-400">무신사 & SPA 실시간</span>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 sm:gap-4">
              {product.exampleItems.map((item, idx) => {
                const itemTargetUrl =
                  item.url && !item.url.includes('/curator/s/') && !item.url.includes('k-trand.store')
                    ? item.url
                    : `https://www.musinsa.com/search/goods?keyword=${encodeURIComponent(item.name)}&gf=A`;

                return (
                  <a
                    key={idx}
                    href={itemTargetUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="group flex flex-col rounded-xl overflow-hidden bg-zinc-50 dark:bg-zinc-900/50 border border-zinc-200/80 dark:border-zinc-800 hover:border-zinc-400 dark:hover:border-zinc-600 transition-all p-2.5 sm:p-3"
                  >
                    <div className="aspect-[3/4] rounded-lg overflow-hidden bg-zinc-100 dark:bg-zinc-800 mb-2.5 relative flex items-center justify-center">
                      <img
                        src={item.imageUrl}
                        alt={item.name}
                        className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                        loading="lazy"
                      />
                      <span className="absolute top-2 left-2 bg-black/75 backdrop-blur-sm text-white text-[9px] font-mono px-1.5 py-0.5 rounded">
                        {item.brand}
                      </span>
                    </div>
                    <div className="flex-1 flex flex-col justify-between">
                      <h3 className="text-xs font-medium text-zinc-800 dark:text-zinc-200 line-clamp-2 leading-snug group-hover:text-zinc-900 dark:group-hover:text-white">
                        {item.name}
                      </h3>
                      <div className="mt-2.5 pt-2 border-t border-zinc-200/60 dark:border-zinc-800/80 flex items-center justify-between">
                        <span className="text-xs font-bold text-zinc-900 dark:text-zinc-100 font-mono">
                          ₩{item.priceKrw.toLocaleString('ko-KR')}
                        </span>
                        <span className="text-[10px] font-mono text-zinc-400 group-hover:text-zinc-800 dark:group-hover:text-zinc-200">
                          보기 ↗
                        </span>
                      </div>
                    </div>
                  </a>
                );
              })}
            </div>
          </section>
        )}

        {/* Highlights box */}
        <div className="my-8 p-6 rounded-xl border border-zinc-200/80 dark:border-zinc-800 bg-zinc-50/50 dark:bg-zinc-900/30">
          <h2 className="text-xs font-mono uppercase tracking-wider text-zinc-400 dark:text-zinc-500 mb-3">
            {dict.tasteSummary}
          </h2>
          <ul className="space-y-2 text-xs sm:text-sm text-zinc-600 dark:text-zinc-400">
            {content.tasteReview.map((point, idx) => (
              <li key={idx} className="flex items-start gap-2 leading-relaxed">
                <span className="text-zinc-400 select-none">•</span>
                <span>{point}</span>
              </li>
            ))}
          </ul>
        </div>

        {/* Editor Tip */}
        <div className="my-6 pl-4 border-l-2 border-zinc-900 dark:border-zinc-200 py-1 text-xs sm:text-sm text-zinc-600 dark:text-zinc-400">
          <span className="font-semibold text-zinc-900 dark:text-zinc-100 mr-2">Note:</span>
          <span>{content.tips}</span>
        </div>
      </div>

      {/* Affiliate Purchase CTA (Coupang, Musinsa, Brand Store) */}
      <AffiliateButton
        url={product.affiliateUrl}
        platform={product.affiliatePlatform}
        priceKrw={product.priceKrw}
        lang={currentLang}
        productTitle={content.title}
        category={product.category}
      />

      {/* Bottom AdSense Banner */}
      <AdSenseSlot slotId="post-bottom-content" />
    </article>
  );
}
