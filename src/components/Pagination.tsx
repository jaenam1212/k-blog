import Link from 'next/link';

interface PaginationProps {
  currentPage: number;
  totalPages: number;
  lang: string;
  category?: string;
}

export function Pagination({ currentPage, totalPages, lang, category }: PaginationProps) {
  if (totalPages <= 1) return null;

  const basePath = category ? `/${lang}/${category}` : `/${lang}`;
  const getPageUrl = (page: number) => (page === 1 ? basePath : `${basePath}?page=${page}`);

  const pages = [];
  for (let i = 1; i <= totalPages; i++) {
    pages.push(i);
  }

  return (
    <nav className="mt-12 mb-6 flex items-center justify-center gap-1.5" aria-label="Pagination">
      {currentPage > 1 ? (
        <Link
          href={getPageUrl(currentPage - 1)}
          className="px-3 py-1.5 text-xs font-mono rounded border border-zinc-200 dark:border-zinc-800 text-zinc-700 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors"
        >
          ← Prev
        </Link>
      ) : (
        <span className="px-3 py-1.5 text-xs font-mono rounded border border-zinc-100 dark:border-zinc-900 text-zinc-300 dark:text-zinc-700 cursor-not-allowed">
          ← Prev
        </span>
      )}

      {pages.map((p) => {
        const isCurrent = p === currentPage;
        return isCurrent ? (
          <span
            key={p}
            className="px-3 py-1.5 text-xs font-mono rounded bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900 font-bold"
          >
            {p}
          </span>
        ) : (
          <Link
            key={p}
            href={getPageUrl(p)}
            className="px-3 py-1.5 text-xs font-mono rounded border border-zinc-200 dark:border-zinc-800 text-zinc-700 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors"
          >
            {p}
          </Link>
        );
      })}

      {currentPage < totalPages ? (
        <Link
          href={getPageUrl(currentPage + 1)}
          className="px-3 py-1.5 text-xs font-mono rounded border border-zinc-200 dark:border-zinc-800 text-zinc-700 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors"
        >
          Next →
        </Link>
      ) : (
        <span className="px-3 py-1.5 text-xs font-mono rounded border border-zinc-100 dark:border-zinc-900 text-zinc-300 dark:text-zinc-700 cursor-not-allowed">
          Next →
        </span>
      )}
    </nav>
  );
}
