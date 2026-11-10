import Link from 'next/link';
import { fetchProductsFromDb } from '@/lib/products';
import { Locale, DICTIONARY } from '@/lib/i18n';
import { ProductCard } from '@/components/ProductCard';
import { AdSenseSlot } from '@/components/AdSenseSlot';

export const revalidate = 60;

export default async function HomePage({
  params,
}: {
  params: Promise<{ lang: string }>;
}) {
  const { lang } = await params;
  const currentLang = lang as Locale;
  const dict = DICTIONARY[currentLang] || DICTIONARY.en;
  const products = await fetchProductsFromDb();

  return (
    <div>
      {/* Hero section */}
      <section className="mb-10 text-center py-8 px-4 rounded-3xl bg-gradient-to-b from-rose-50/70 to-amber-50/40 dark:from-neutral-900 dark:to-neutral-900/50 border border-rose-100 dark:border-neutral-800">
        <div className="inline-flex items-center gap-2 px-3 py-1 bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded-full text-xs font-semibold text-rose-600 dark:text-rose-400 mb-4 shadow-sm">
          <span>{dict.aiSearchNotice}</span>
        </div>
        <h1 className="text-3xl sm:text-4xl font-black text-neutral-900 dark:text-neutral-100 tracking-tight leading-tight">
          {dict.siteName}
        </h1>
        <p className="mt-3 text-sm sm:text-base text-neutral-600 dark:text-neutral-400 max-w-2xl mx-auto">
          {dict.siteTagline}
        </p>

        {/* Category Pills */}
        <div className="mt-6 flex flex-wrap justify-center gap-2">
          <Link
            href={`/${currentLang}`}
            className="px-4 py-2 bg-neutral-900 text-white dark:bg-white dark:text-neutral-900 text-xs font-bold rounded-xl shadow-sm"
          >
            {dict.allCategories}
          </Link>
          <Link
            href={`/${currentLang}/convenience-food`}
            className="px-4 py-2 bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 hover:border-rose-400 text-neutral-700 dark:text-neutral-300 text-xs font-bold rounded-xl transition-colors"
          >
            🍙 {dict.convenienceFood}
          </Link>
          <Link
            href={`/${currentLang}/k-beauty`}
            className="px-4 py-2 bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 hover:border-rose-400 text-neutral-700 dark:text-neutral-300 text-xs font-bold rounded-xl transition-colors"
          >
            ✨ {dict.kBeauty}
          </Link>
          <Link
            href={`/${currentLang}/k-fashion`}
            className="px-4 py-2 bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 hover:border-rose-400 text-neutral-700 dark:text-neutral-300 text-xs font-bold rounded-xl transition-colors"
          >
            🧥 {dict.kFashion}
          </Link>
        </div>
      </section>

      {/* Main Grid */}
      <section>
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-lg font-black text-neutral-900 dark:text-neutral-100 flex items-center gap-2">
            <span>🔥</span>
            <span>Latest 2026 Releases ({products.length})</span>
          </h2>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {products.map((product) => (
            <ProductCard key={product.id} product={product} lang={currentLang} />
          ))}
        </div>
      </section>

      {/* AdSense In-feed Ad Banner */}
      <AdSenseSlot slotId="home-feed-banner" />
    </div>
  );
}
