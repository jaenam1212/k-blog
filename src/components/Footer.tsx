import Link from 'next/link';
import { Locale, DICTIONARY } from '@/lib/i18n';

export function Footer({ lang }: { lang: Locale }) {
  const dict = DICTIONARY[lang] || DICTIONARY.en;

  return (
    <footer className="border-t border-zinc-200/80 dark:border-zinc-800/80 mt-20 py-12 text-xs text-zinc-500">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-6">
        <div>
          <p className="font-semibold text-zinc-800 dark:text-zinc-200 text-sm">
            {dict.siteName}
          </p>
          <p className="mt-1 text-xs text-zinc-400">
            {dict.siteTagline}
          </p>
          <p className="mt-3 text-[11px] text-zinc-400">
            © 2026 K-Trend Archive. All rights reserved.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-3 text-[11px] font-mono text-zinc-400">
          <Link href="/llms.txt" className="hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors">
            llms.txt
          </Link>
          <span>/</span>
          <Link href="/api/mcp" className="hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors">
            mcp
          </Link>
          <span>/</span>
          <Link href="/api/products" className="hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors">
            api
          </Link>
        </div>
      </div>
    </footer>
  );
}
