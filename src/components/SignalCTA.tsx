import { Locale, DICTIONARY } from '@/lib/i18n';

export const SIGNAL_URL = 'https://signal.k-trand.store';

/**
 * Funnel from k-trand.store editorial traffic to K-Signal (K-Trend Radar).
 * External link, opened in a new tab, no tracking parameters.
 */
export function SignalCTA({ lang, compact = false }: { lang: Locale; compact?: boolean }) {
  const dict = DICTIONARY[lang] || DICTIONARY.en;

  if (compact) {
    return (
      <a
        href={SIGNAL_URL}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-flex items-center gap-1.5 text-[11px] font-mono text-zinc-500 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100 transition-colors"
      >
        <span>{dict.signalEyebrow}</span>
        <span className="text-zinc-300 dark:text-zinc-700">·</span>
        <span>{dict.signalNav}</span>
        <span aria-hidden="true">↗</span>
      </a>
    );
  }

  return (
    <section className="my-10 rounded-xl border border-zinc-200/80 dark:border-zinc-800 bg-zinc-50/60 dark:bg-zinc-900/40 p-6">
      <p className="text-[10px] font-mono uppercase tracking-[0.18em] text-zinc-400 dark:text-zinc-500">
        {dict.signalEyebrow}
      </p>
      <h2 className="mt-2 text-base sm:text-lg font-bold tracking-tight text-zinc-900 dark:text-zinc-100 leading-snug">
        {dict.signalTitle}
      </h2>
      <p className="mt-2.5 text-xs sm:text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed">
        {dict.signalDesc}
      </p>
      <a
        href={SIGNAL_URL}
        target="_blank"
        rel="noopener noreferrer"
        className="mt-4 inline-flex items-center gap-1.5 rounded-lg bg-zinc-900 dark:bg-zinc-100 px-3.5 py-2 text-xs font-semibold text-white dark:text-zinc-900 hover:opacity-85 transition-opacity"
      >
        <span>{dict.signalCta}</span>
        <span aria-hidden="true">↗</span>
      </a>
      <p className="mt-3 text-[10px] font-mono text-zinc-400 dark:text-zinc-500">
        signal.k-trand.store
      </p>
    </section>
  );
}
