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
      {/* Editorial Header */}
      <section className="py-8 sm:py-12 border-b border-zinc-200/80 dark:border-zinc-800/80 mb-10">
        <h1 className="text-3xl sm:text-4xl font-bold tracking-tight text-zinc-900 dark:text-zinc-100">
          {dict.siteName}
        </h1>
        <p className="mt-3 text-sm sm:text-base text-zinc-500 dark:text-zinc-400 max-w-xl leading-relaxed">
          {dict.siteTagline}
        </p>

        {/* Category Filter Pills */}
        <div className="mt-6 flex flex-wrap items-center gap-2 text-xs">
          <Link
            href={`/${currentLang}`}
            className="px-3 py-1.5 rounded-full bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900 font-medium"
          >
            {dict.allCategories}
          </Link>
          <Link
            href={`/${currentLang}/convenience-food`}
            className="px-3 py-1.5 rounded-full border border-zinc-200 dark:border-zinc-800 text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100 hover:border-zinc-400 dark:hover:border-zinc-600 transition-colors"
          >
            {dict.convenienceFood}
          </Link>
          <Link
            href={`/${currentLang}/k-beauty`}
            className="px-3 py-1.5 rounded-full border border-zinc-200 dark:border-zinc-800 text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100 hover:border-zinc-400 dark:hover:border-zinc-600 transition-colors"
          >
            {dict.kBeauty}
          </Link>
          <Link
            href={`/${currentLang}/k-fashion`}
            className="px-3 py-1.5 rounded-full border border-zinc-200 dark:border-zinc-800 text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100 hover:border-zinc-400 dark:hover:border-zinc-600 transition-colors"
          >
            {dict.kFashion}
          </Link>
        </div>
      </section>

      {/* Main Grid */}
      <section>
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-xs font-mono uppercase tracking-wider text-zinc-400 dark:text-zinc-500">
            Recent Articles
          </h2>
          <span className="text-xs text-zinc-400 font-mono">
            {products.length} {products.length === 1 ? 'item' : 'items'}
          </span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
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
