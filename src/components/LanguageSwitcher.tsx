'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Locale, LOCALES, LOCALE_NAMES } from '@/lib/i18n';

export function LanguageSwitcher({ currentLang }: { currentLang: Locale }) {
  const pathname = usePathname() || '/';

  // Replace existing language segment in url
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
    <div className="flex items-center gap-1 bg-neutral-100 dark:bg-neutral-800 p-1 rounded-lg text-xs font-medium">
      {LOCALES.map((loc) => {
        const isActive = loc === currentLang;
        return (
          <Link
            key={loc}
            href={getUrlForLocale(loc)}
            className={`px-2 py-1 rounded transition-colors ${
              isActive
                ? 'bg-white dark:bg-neutral-900 text-rose-600 dark:text-rose-400 font-bold shadow-sm'
                : 'text-neutral-600 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white'
            }`}
          >
            {LOCALE_NAMES[loc]}
          </Link>
        );
      })}
    </div>
  );
}
