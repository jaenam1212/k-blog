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

  const platformNames: Record<string, string> = {
    Coupang: '쿠팡',
    Musinsa: '무신사 스토어',
    OliveYoung: '올리브영',
    ConvenienceStore: '공식 판매처',
  };

  const storeName = platformNames[platform] || '공식 판매처';

  return (
    <div className="my-8 p-5 border border-zinc-200 dark:border-zinc-800 rounded-xl bg-zinc-50/70 dark:bg-zinc-900/40 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
      <div>
        <div className="text-[11px] font-mono uppercase tracking-wider text-zinc-400">
          {storeName}
        </div>
        <div className="text-xl font-bold text-zinc-900 dark:text-zinc-100 font-mono mt-0.5">
          ₩{priceKrw.toLocaleString('ko-KR')}
        </div>
      </div>

      <a
        href={url}
        target="_blank"
        rel="noopener noreferrer sponsored"
        className="inline-flex items-center justify-center gap-1.5 px-5 py-2.5 rounded-lg bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900 hover:bg-zinc-800 dark:hover:bg-white text-xs font-medium transition-colors"
      >
        <span>{dict.shoppingLink}</span>
        <span>→</span>
      </a>
    </div>
  );
}
