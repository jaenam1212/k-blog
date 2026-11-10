'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Locale, LOCALES } from '@/lib/i18n';

const SHORT_LABELS: Record<Locale, string> = {
  ko: 'KO',
  en: 'EN',
  ja: 'JA',
  zh: 'ZH',
};

export function LanguageSwitcher({ currentLang }: { currentLang: Locale }) {
  const pathname = usePathname() || '/';

  const getUrlForLocale = (loc: Locale) => {
    const segments = pathname.split('/').filter(Boolean);
    if (segments.length === 0) return `/${loc}`;
    if (LOCALES.includes(segments[0] as Locale)) {
      segments[0] = loc;
      return `/${segments.join('/')}`;
    }
    return `/${loc}/${segments.join('/')}`;
  };

  return (
    <div className="flex items-center gap-1.5 text-[11px] font-mono">
      {LOCALES.map((loc, idx) => {
        const isActive = loc === currentLang;
        return (
          <span key={loc} className="flex items-center gap-1.5">
            <Link
              href={getUrlForLocale(loc)}
              className={`transition-colors ${
                isActive
                  ? 'font-bold text-zinc-950 dark:text-zinc-100 underline underline-offset-4 decoration-1'
                  : 'text-zinc-400 hover:text-zinc-700 dark:hover:text-zinc-300'
              }`}
            >
              {SHORT_LABELS[loc]}
            </Link>
            {idx < LOCALES.length - 1 && (
              <span className="text-zinc-300 dark:text-zinc-700 select-none">/</span>
            )}
          </span>
        );
      })}
    </div>
  );
}
