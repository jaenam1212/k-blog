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
    <article className="group flex flex-col justify-between p-5 rounded-xl border border-zinc-200/90 dark:border-zinc-800 bg-white dark:bg-zinc-900/30 hover:border-zinc-400 dark:hover:border-zinc-600 transition-all">
      <div>
        <Link
          href={`/${lang}/post/${product.slug}`}
          className="block aspect-[3/4] overflow-hidden rounded-lg bg-zinc-100 dark:bg-zinc-800 mb-4 border border-zinc-100 dark:border-zinc-800/60 relative"
        >
          <img
            src={product.imageUrl}
            alt={content.title}
            className="w-full h-full object-cover group-hover:scale-102 transition-transform duration-300"
            loading="lazy"
          />
          {product.images && product.images.length > 1 && (
            <span className="absolute bottom-2 right-2 bg-black/60 backdrop-blur-sm text-white text-[10px] font-mono px-1.5 py-0.5 rounded flex items-center gap-1">
              <span>📷</span>
              <span>{product.images.length}</span>
            </span>
          )}
        </Link>

        <div className="flex flex-wrap items-center gap-x-2 gap-y-0.5 text-[11px] font-mono text-zinc-400 dark:text-zinc-500 mb-2">
          <span className="whitespace-nowrap">{product.store}</span>
          <span className="text-zinc-300 dark:text-zinc-700 select-none">·</span>
          <span className="whitespace-nowrap">{categoryLabels[product.category] || product.category}</span>
          <span className="text-zinc-300 dark:text-zinc-700 select-none">·</span>
          <span className="whitespace-nowrap">{product.releaseDate}</span>
        </div>

        <h2 className="text-base font-semibold text-zinc-900 dark:text-zinc-100 group-hover:text-zinc-600 dark:group-hover:text-zinc-300 transition-colors leading-snug tracking-tight">
          <Link href={`/${lang}/post/${product.slug}`}>
            {content.title}
          </Link>
        </h2>

        <p className="mt-2 text-xs text-zinc-500 dark:text-zinc-400 line-clamp-2 leading-relaxed">
          {content.summary}
        </p>
      </div>

      <div className="mt-4 pt-3 border-t border-zinc-100 dark:border-zinc-800/80 flex items-center justify-between text-xs">
        <span className="font-semibold text-zinc-900 dark:text-zinc-100 font-mono">
          ₩{product.priceKrw.toLocaleString('ko-KR')}
        </span>
        <Link
          href={`/${lang}/post/${product.slug}`}
          className="text-zinc-500 dark:text-zinc-400 group-hover:text-zinc-900 dark:group-hover:text-zinc-100 font-medium inline-flex items-center gap-1 transition-colors"
        >
          {dict.readMore}
          <span>→</span>
        </Link>
      </div>
    </article>
  );
}
