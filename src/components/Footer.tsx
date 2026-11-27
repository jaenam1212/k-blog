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

        <div className="flex flex-col sm:items-end gap-2">
          <a
            href="https://signal.k-trand.store"
            target="_blank"
            rel="noopener noreferrer"
            className="group flex items-start gap-2 rounded-lg border border-zinc-200/80 dark:border-zinc-800 px-3 py-2 mb-1 hover:border-zinc-400 dark:hover:border-zinc-600 transition-colors"
          >
            <span className="mt-0.5 text-[10px] font-mono text-zinc-400">RADAR</span>
            <span className="flex flex-col">
              <span className="text-xs font-semibold text-zinc-800 dark:text-zinc-200 group-hover:text-zinc-900 dark:group-hover:text-white">
                {dict.signalEyebrow} ({dict.signalNav}) ↗
              </span>
              <span className="mt-0.5 text-[10px] text-zinc-400 leading-relaxed">
                {dict.signalTitle}
              </span>
            </span>
          </a>

          <div className="flex flex-wrap items-center gap-3 text-[11px] font-mono text-zinc-500 dark:text-zinc-400">
            <Link href="/about" className="hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors">
              About
            </Link>
            <span>·</span>
            <Link href="/privacy" className="hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors">
              Privacy Policy
            </Link>
            <span>·</span>
            <Link href="/terms" className="hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors">
              Terms
            </Link>
          </div>

          <div className="flex flex-wrap items-center gap-3 text-[10px] font-mono text-zinc-400">
            <Link href="/llms.txt" className="hover:text-zinc-600 dark:hover:text-zinc-300 transition-colors">
              llms.txt
            </Link>
            <span>/</span>
            <Link href="/api/mcp" className="hover:text-zinc-600 dark:hover:text-zinc-300 transition-colors">
              mcp
            </Link>
            <span>/</span>
            <Link href="/api/products" className="hover:text-zinc-600 dark:hover:text-zinc-300 transition-colors">
              api
            </Link>
          </div>
        </div>
      </div>
    </footer>
  );
}
