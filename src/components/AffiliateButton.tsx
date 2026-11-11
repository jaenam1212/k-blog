import { Locale, DICTIONARY } from '@/lib/i18n';

interface AffiliateButtonProps {
  url: string;
  platform: 'Coupang' | 'Musinsa' | 'OliveYoung' | 'ConvenienceStore' | 'Zara' | 'Uniqlo' | string;
  priceKrw: number;
  lang: Locale;
  productTitle?: string;
  category?: string;
}

export function AffiliateButton({
  url,
  platform,
  priceKrw,
  lang,
  productTitle = '',
  category = '',
}: AffiliateButtonProps) {
  const dict = DICTIONARY[lang] || DICTIONARY.en;

  const platformNames: Record<string, string> = {
    Coupang: '쿠팡 로켓배송',
    Musinsa: '무신사 스토어',
    OliveYoung: '올리브영 공식몰',
    Zara: 'ZARA 공식 스토어',
    Uniqlo: '유니클로 공식 스토어',
    ConvenienceStore: '공식 판매처',
  };

  const storeName = platformNames[platform] || '공식 판매처';

  const COUPANG_AF_ID = process.env.NEXT_PUBLIC_COUPANG_AF_ID || 'AF9412775';
  const coupangSearchUrl = `https://www.coupang.com/np/search?component=&q=${encodeURIComponent(productTitle)}&lptag=${COUPANG_AF_ID}`;
  const musinsaSearchUrl = `https://www.musinsa.com/search/goods?keyword=${encodeURIComponent(productTitle)}`;

  return (
    <div className="my-8 p-6 border border-zinc-200 dark:border-zinc-800 rounded-xl bg-zinc-50/70 dark:bg-zinc-900/40">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-zinc-200/60 dark:border-zinc-800/60">
        <div>
          <div className="text-[11px] font-mono uppercase tracking-wider text-zinc-400">
            {storeName}
          </div>
          <div className="text-xl font-bold text-zinc-900 dark:text-zinc-100 font-mono mt-0.5">
            ₩{priceKrw.toLocaleString('ko-KR')}
          </div>
        </div>

        <div className="flex flex-wrap items-center gap-2">
          <a
            href={url}
            target="_blank"
            rel="noopener noreferrer sponsored"
            className="inline-flex items-center justify-center gap-1.5 px-5 py-2.5 rounded-lg bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-900 hover:bg-zinc-800 dark:hover:bg-white text-xs font-medium transition-colors"
          >
            <span>{dict.shoppingLink}</span>
            <span>→</span>
          </a>

          {platform !== 'Coupang' && (category === 'convenience-food' || category === 'k-beauty') && (
            <a
              href={coupangSearchUrl}
              target="_blank"
              rel="noopener noreferrer sponsored"
              className="inline-flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-lg border border-zinc-300 dark:border-zinc-700 text-zinc-700 dark:text-zinc-200 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-xs font-medium transition-colors"
            >
              <span>쿠팡 최저가 검색</span>
              <span>↗</span>
            </a>
          )}

          {platform !== 'Musinsa' && category === 'k-fashion' && (
            <a
              href={musinsaSearchUrl}
              target="_blank"
              rel="noopener noreferrer sponsored"
              className="inline-flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-lg border border-zinc-300 dark:border-zinc-700 text-zinc-700 dark:text-zinc-200 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-xs font-medium transition-colors"
            >
              <span>무신사 연관 상품</span>
              <span>↗</span>
            </a>
          )}
        </div>
      </div>

      <div className="mt-3 text-[11px] text-zinc-400 dark:text-zinc-500 font-mono leading-relaxed">
        * 본 콘텐츠는 제휴 마케팅 활동의 일환으로, 구매 발생 시 일정액의 수수료를 제공받을 수 있습니다.
      </div>
    </div>
  );
}
