import Link from 'next/link';
import { Locale, DICTIONARY } from '@/lib/i18n';
import { LanguageSwitcher } from './LanguageSwitcher';

export function Header({ lang }: { lang: Locale }) {
  const dict = DICTIONARY[lang] || DICTIONARY.en;

  return (
    <header className="sticky top-0 z-50 bg-white/90 dark:bg-neutral-900/90 backdrop-blur border-b border-neutral-200 dark:border-neutral-800">
      <div className="max-w-5xl mx-auto px-4 h-16 flex items-center justify-between">
        <div className="flex items-center gap-4">
          <Link href={`/${lang}`} className="flex items-center gap-2 group">
            <span className="text-xl font-black bg-gradient-to-r from-rose-500 to-amber-500 bg-clip-text text-transparent">
              K-TREND BOX
            </span>
            <span className="hidden sm:inline-block text-[11px] font-semibold uppercase px-2 py-0.5 bg-rose-50 dark:bg-rose-950/50 text-rose-600 dark:text-rose-400 rounded-full border border-rose-200 dark:border-rose-900">
              MCP / AI Indexed
            </span>
          </Link>
        </div>

        <nav className="flex items-center gap-3">
          <div className="hidden md:flex items-center gap-4 text-sm font-medium text-neutral-600 dark:text-neutral-300">
            <Link href={`/${lang}`} className="hover:text-rose-600 transition-colors">
              {dict.allCategories}
            </Link>
            <Link href={`/${lang}/convenience-food`} className="hover:text-rose-600 transition-colors">
              {dict.convenienceFood}
            </Link>
            <Link href={`/${lang}/k-beauty`} className="hover:text-rose-600 transition-colors">
              {dict.kBeauty}
            </Link>
            <Link href={`/${lang}/k-fashion`} className="hover:text-rose-600 transition-colors">
              {dict.kFashion}
            </Link>
          </div>

          <LanguageSwitcher currentLang={lang} />
        </nav>
      </div>
    </header>
  );
}
