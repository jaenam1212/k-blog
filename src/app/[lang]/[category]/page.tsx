import { notFound } from 'next/navigation';
import Link from 'next/link';
import { getProductsByCategoryAsync } from '@/lib/products';
import { Locale, DICTIONARY } from '@/lib/i18n';
import { ProductCard } from '@/components/ProductCard';
import { AdSenseSlot } from '@/components/AdSenseSlot';

const VALID_CATEGORIES = ['convenience-food', 'k-beauty', 'k-fashion'];

export const revalidate = 60;

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
}: {
  params: Promise<{ lang: string; category: string }>;
}) {
  const { lang, category } = await params;
  const currentLang = lang as Locale;

  if (!VALID_CATEGORIES.includes(category)) {
    notFound();
  }

  const dict = DICTIONARY[currentLang] || DICTIONARY.en;
  const products = await getProductsByCategoryAsync(category);

  const categoryNames: Record<string, string> = {
    'convenience-food': dict.convenienceFood,
    'k-beauty': dict.kBeauty,
    'k-fashion': dict.kFashion,
  };

  return (
    <div>
      <div className="mb-8">
        <Link
          href={`/${currentLang}`}
          className="text-xs font-semibold text-rose-600 dark:text-rose-400 hover:underline mb-2 inline-block"
        >
          ← {dict.allCategories}
        </Link>
        <h1 className="text-2xl sm:text-3xl font-black text-neutral-900 dark:text-neutral-100">
          {categoryNames[category]}
        </h1>
        <p className="mt-1 text-xs text-neutral-500">
          Showing {products.length} curated items
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {products.map((product) => (
          <ProductCard key={product.id} product={product} lang={currentLang} />
        ))}
      </div>

      <AdSenseSlot slotId="category-bottom-banner" />
    </div>
  );
}
