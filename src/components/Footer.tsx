import Link from 'next/link';
import { Locale, DICTIONARY } from '@/lib/i18n';

export function Footer({ lang }: { lang: Locale }) {
  const dict = DICTIONARY[lang] || DICTIONARY.en;

  return (
    <footer className="border-t border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950 py-10 mt-16 text-xs text-neutral-500">
      <div className="max-w-5xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center gap-6">
        <div>
          <p className="font-bold text-neutral-800 dark:text-neutral-200 text-sm mb-1">
            {dict.siteName}
          </p>
          <p>{dict.siteTagline}</p>
          <p className="mt-2 text-[11px] text-neutral-400">
            © 2026 K-Trend Box. Built with Next.js & Model Context Protocol.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-4">
          <Link href="/llms.txt" className="hover:text-rose-500 underline underline-offset-4">
            llms.txt
          </Link>
          <Link href="/llms-full.txt" className="hover:text-rose-500 underline underline-offset-4">
            llms-full.txt
          </Link>
          <Link href="/api/mcp" className="hover:text-rose-500 underline underline-offset-4 font-mono">
            /api/mcp (JSON-RPC)
          </Link>
          <Link href="/api/products" className="hover:text-rose-500 underline underline-offset-4 font-mono">
            /api/products
          </Link>
        </div>
      </div>
    </footer>
  );
}
