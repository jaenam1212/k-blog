import Link from 'next/link';
import { Product } from '@/lib/products';
import { Locale, DICTIONARY } from '@/lib/i18n';

export function ProductCard({ product, lang }: { product: Product; lang: Locale }) {
  const dict = DICTIONARY[lang] || DICTIONARY.en;
  const content = product.i18n[lang] || product.i18n.en;

  const categoryLabels: Record<string, string> = {
    'convenience-food': dict.convenienceFood,
    'k-beauty': dict.kBeauty,
    'k-fashion': dict.kFashion,
  };

  return (
    <article className="group bg-white dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 rounded-2xl overflow-hidden hover:shadow-xl hover:border-rose-300 dark:hover:border-rose-800 transition-all flex flex-col">
      <Link href={`/${lang}/post/${product.slug}`} className="relative block aspect-[16/10] overflow-hidden bg-neutral-100 dark:bg-neutral-800">
        <img
          src={product.imageUrl}
          alt={content.title}
          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
          loading="lazy"
        />
        <div className="absolute top-3 left-3 flex gap-2">
          <span className="px-2.5 py-1 bg-neutral-900/80 backdrop-blur text-white text-xs font-bold rounded-full">
            {product.store}
          </span>
          <span className="px-2.5 py-1 bg-rose-600/90 backdrop-blur text-white text-xs font-bold rounded-full">
            {categoryLabels[product.category]}
          </span>
        </div>
      </Link>

      <div className="p-5 flex-1 flex flex-col justify-between">
        <div>
          <div className="flex items-center justify-between text-xs text-neutral-500 mb-2">
            <span>{product.releaseDate}</span>
            <span className="text-amber-500 font-bold">★ {product.rating.toFixed(1)}</span>
          </div>

          <h2 className="text-base font-bold text-neutral-900 dark:text-neutral-100 group-hover:text-rose-600 transition-colors line-clamp-2 leading-snug">
            <Link href={`/${lang}/post/${product.slug}`}>
              {content.title}
            </Link>
          </h2>

          <p className="mt-2 text-xs text-neutral-600 dark:text-neutral-400 line-clamp-2">
            {content.summary}
          </p>
        </div>

        <div className="mt-4 pt-3 border-t border-neutral-100 dark:border-neutral-800 flex items-center justify-between">
          <span className="text-sm font-extrabold text-neutral-900 dark:text-neutral-100">
            ₩{product.priceKrw.toLocaleString('ko-KR')}
          </span>
          <Link
            href={`/${lang}/post/${product.slug}`}
            className="text-xs font-semibold text-rose-600 dark:text-rose-400 group-hover:translate-x-1 transition-transform"
          >
            {dict.readMore} →
          </Link>
        </div>
      </div>
    </article>
  );
}
