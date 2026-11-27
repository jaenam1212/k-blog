import Link from 'next/link';
import { Locale, DICTIONARY } from '@/lib/i18n';
import { LanguageSwitcher } from './LanguageSwitcher';

export function Header({ lang }: { lang: Locale }) {
  const dict = DICTIONARY[lang] || DICTIONARY.en;

  return (
    <header className="sticky top-0 z-50 bg-white/95 dark:bg-zinc-950/95 backdrop-blur border-b border-zinc-200/80 dark:border-zinc-800/80">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 h-14 flex items-center justify-between">
        <div className="flex items-center gap-6">
          <Link
            href={`/${lang}`}
            className="text-base font-bold tracking-tight text-zinc-900 dark:text-zinc-100 hover:opacity-75 transition-opacity"
          >
            K-Trend Archive
          </Link>

          <nav className="hidden sm:flex items-center gap-5 text-xs font-medium text-zinc-500 dark:text-zinc-400">
            <Link
              href={`/${lang}/convenience-food`}
              className="hover:text-zinc-900 dark:hover:text-zinc-100 transition-colors"
            >
              {dict.convenienceFood}
            </Link>
            <Link
              href={`/${lang}/k-beauty`}
              className="hover:text-zinc-900 dark:hover:text-zinc-100 transition-colors"
            >
              {dict.kBeauty}
            </Link>
            <Link
              href={`/${lang}/k-fashion`}
              className="hover:text-zinc-900 dark:hover:text-zinc-100 transition-colors"
            >
              {dict.kFashion}
            </Link>
            <Link
              href={`/${lang}/tech`}
              className="hover:text-zinc-900 dark:hover:text-zinc-100 transition-colors"
            >
              {dict.tech}
            </Link>
            <a
              href="https://signal.k-trand.store"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1 text-zinc-900 dark:text-zinc-100 hover:opacity-70 transition-opacity"
              title="K-Trend Radar (K-Signal)"
            >
              <span className="w-1 h-1 rounded-full bg-zinc-900 dark:bg-zinc-100" aria-hidden="true" />
              <span>{dict.signalNav}</span>
              <span className="text-zinc-400" aria-hidden="true">↗</span>
            </a>
          </nav>
        </div>

        <div className="flex items-center gap-4">
          <LanguageSwitcher currentLang={lang} />
        </div>
      </div>
    </header>
  );
}
