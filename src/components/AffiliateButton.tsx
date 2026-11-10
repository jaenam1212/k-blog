import { Locale, DICTIONARY } from '@/lib/i18n';

interface AffiliateButtonProps {
  url: string;
  platform: 'Coupang' | 'Musinsa' | 'OliveYoung' | 'ConvenienceStore';
  priceKrw: number;
  lang: Locale;
}

export function AffiliateButton({
  url,
  platform,
  priceKrw,
  lang,
}: AffiliateButtonProps) {
  const dict = DICTIONARY[lang] || DICTIONARY.en;

  const platformBadge: Record<string, { name: string; color: string }> = {
    Coupang: { name: 'Coupang Rocket', color: 'bg-rose-600 hover:bg-rose-700' },
    Musinsa: { name: 'Musinsa Store', color: 'bg-neutral-900 hover:bg-black' },
    OliveYoung: { name: 'Olive Young', color: 'bg-emerald-600 hover:bg-emerald-700' },
    ConvenienceStore: { name: 'Official Store', color: 'bg-blue-600 hover:bg-blue-700' },
  };

  const badge = platformBadge[platform] || platformBadge.ConvenienceStore;

  return (
    <div className="my-6 p-5 bg-gradient-to-r from-rose-50 to-amber-50 dark:from-neutral-900 dark:to-neutral-800 rounded-2xl border border-rose-200 dark:border-neutral-700 flex flex-col sm:flex-row items-center justify-between gap-4 shadow-sm">
      <div>
        <p className="text-xs uppercase font-bold tracking-wider text-rose-600 dark:text-rose-400">
          Official Deal / Stock Check
        </p>
        <p className="text-lg font-black text-neutral-900 dark:text-neutral-100">
          ₩{priceKrw.toLocaleString('ko-KR')}
        </p>
      </div>

      <a
        href={url}
        target="_blank"
        rel="noopener noreferrer sponsored"
        className={`w-full sm:w-auto px-6 py-3 rounded-xl text-white font-bold text-sm shadow-md transition-all text-center flex items-center justify-center gap-2 ${badge.color}`}
      >
        <span>{dict.shoppingLink}</span>
        <span className="text-xs opacity-80 font-normal">({badge.name})</span>
      </a>
    </div>
  );
}
