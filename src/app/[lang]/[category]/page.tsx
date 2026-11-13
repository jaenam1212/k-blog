import { notFound } from 'next/navigation';
import Link from 'next/link';
import { getProductsByCategoryAsync } from '@/lib/products';
import { Locale, DICTIONARY } from '@/lib/i18n';
import { ProductCard } from '@/components/ProductCard';
import { Pagination } from '@/components/Pagination';
import { AdSenseSlot } from '@/components/AdSenseSlot';

const VALID_CATEGORIES = ['convenience-food', 'k-beauty', 'k-fashion', 'tech'];

export const revalidate = 60;

const PAGE_SIZE = 9;

export async function generateStaticParams() {
  const params: { lang: string; category: string }[] = [];
  const locales = ['ko', 'en', 'ja', 'zh'];
  for (const lang of locales) {
    for (const category of VALID_CATEGORIES) {
      params.push({ lang, category });
    }
  }
  return params;
}

export default async function CategoryPage({
  params,
  searchParams,
}: {
  params: Promise<{ lang: string; category: string }>;
  searchParams: Promise<{ page?: string }>;
}) {
  const { lang, category } = await params;
  const { page } = (await searchParams) || {};
  const currentLang = lang as Locale;

  if (!VALID_CATEGORIES.includes(category)) {
    notFound();
  }

  const dict = DICTIONARY[currentLang] || DICTIONARY.en;
  const allProducts = await getProductsByCategoryAsync(category);

  const categoryNames: Record<string, string> = {
    'convenience-food': dict.convenienceFood,
    'k-beauty': dict.kBeauty,
    'k-fashion': dict.kFashion,
    tech: dict.tech || 'Tech',
  };

  const totalCount = allProducts.length;
  const totalPages = Math.ceil(totalCount / PAGE_SIZE) || 1;
  const parsedPage = parseInt(page || '1', 10);
  const currentPage = Math.min(Math.max(1, isNaN(parsedPage) ? 1 : parsedPage), totalPages);

  const startIndex = (currentPage - 1) * PAGE_SIZE;
  const paginatedProducts = allProducts.slice(startIndex, startIndex + PAGE_SIZE);

  return (
    <div>
      <div className="py-6 sm:py-10 border-b border-zinc-200/80 dark:border-zinc-800/80 mb-8">
        <Link
          href={`/${currentLang}`}
          className="text-xs text-zinc-400 hover:text-zinc-700 dark:hover:text-zinc-300 transition-colors inline-block mb-3"
        >
          ← {dict.allCategories}
        </Link>
        <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-zinc-900 dark:text-zinc-100">
          {categoryNames[category]}
        </h1>
        <p className="mt-2 text-xs text-zinc-400 font-mono">
          {totalCount} {totalCount === 1 ? 'article' : 'articles'} {totalPages > 1 && `(Page ${currentPage} of ${totalPages})`}
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
        {paginatedProducts.map((product) => (
          <ProductCard key={product.id} product={product} lang={currentLang} />
        ))}
      </div>

      <Pagination
        currentPage={currentPage}
        totalPages={totalPages}
        lang={currentLang}
        category={category}
      />

      <AdSenseSlot slotId="category-bottom-banner" />
    </div>
  );
}
