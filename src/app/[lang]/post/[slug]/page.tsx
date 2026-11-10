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

  const languagesObj: Record<string, string> = {};
  for (const l of LOCALES) {
    languagesObj[l] = `https://k-trendbox.com/${l}/post/${slug}`;
  }

  return {
    title: `${content.title} | K-Trend Box`,
    description: content.summary,
    alternates: {
      canonical: `https://k-trendbox.com/${lang}/post/${slug}`,
      languages: languagesObj,
    },
    openGraph: {
      title: content.title,
      description: content.summary,
      images: [product.imageUrl],
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

  // Schema.org Structured Data for Google Rich Snippets & AI Engines (Perplexity, SearchGPT)
  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: content.title,
    image: [product.imageUrl],
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
        name: 'K-Trend Box Editorial Team',
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
    <article className="max-w-3xl mx-auto">
      {/* Inject Structured Data JSON-LD */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />

      <div className="mb-6">
        <Link
          href={`/${currentLang}/${product.category}`}
          className="text-xs font-semibold text-rose-600 dark:text-rose-400 hover:underline inline-block mb-3"
        >
          ← {product.category}
        </Link>

        <div className="flex flex-wrap items-center gap-2 mb-3">
          <span className="px-2.5 py-1 bg-neutral-900 text-white text-xs font-bold rounded-full">
            {product.store}
          </span>
          <span className="text-xs text-neutral-500">
            {dict.releasedDate}: {product.releaseDate}
          </span>
          <span className="text-xs text-amber-500 font-bold ml-auto">
            ★ {product.rating.toFixed(1)} / 5.0
          </span>
        </div>

        <h1 className="text-2xl sm:text-3xl font-black text-neutral-900 dark:text-neutral-100 leading-snug">
          {content.title}
        </h1>

        <p className="mt-3 text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed font-medium">
          {content.summary}
        </p>
      </div>

      {/* Featured Image */}
      <div className="rounded-2xl overflow-hidden aspect-[16/10] bg-neutral-100 dark:bg-neutral-800 mb-6 shadow-md">
        <img
          src={product.imageUrl}
          alt={content.title}
          className="w-full h-full object-cover"
        />
      </div>

      {/* Top AdSense Banner */}
      <AdSenseSlot slotId="post-top-content" />

      {/* Main Review Body */}
      <div className="prose dark:prose-invert max-w-none text-neutral-800 dark:text-neutral-200 text-sm sm:text-base leading-relaxed space-y-6">
        <p>{content.description}</p>

        <div className="my-6 p-5 bg-neutral-100 dark:bg-neutral-900 rounded-2xl border border-neutral-200 dark:border-neutral-800">
          <h2 className="text-base font-bold text-neutral-900 dark:text-neutral-100 mb-3 flex items-center gap-2">
            <span>✨</span>
            <span>{dict.tasteSummary}</span>
          </h2>
          <ul className="space-y-2 list-disc list-inside text-xs sm:text-sm text-neutral-700 dark:text-neutral-300">
            {content.tasteReview.map((point, idx) => (
              <li key={idx} className="leading-relaxed">
                {point}
              </li>
            ))}
          </ul>
        </div>

        <div className="my-6 p-4 bg-amber-50 dark:bg-amber-950/40 rounded-xl border border-amber-200 dark:border-amber-900/60 text-amber-900 dark:text-amber-200 text-xs sm:text-sm">
          <strong>💡 Local Pro Tip: </strong>
          <span>{content.tips}</span>
        </div>
      </div>

      {/* Affiliate Purchase CTA */}
      <AffiliateButton
        url={product.affiliateUrl}
        platform={product.affiliatePlatform}
        priceKrw={product.priceKrw}
        lang={currentLang}
      />

      {/* Bottom AdSense Banner */}
      <AdSenseSlot slotId="post-bottom-content" />
    </article>
  );
}
