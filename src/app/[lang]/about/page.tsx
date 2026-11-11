import { Metadata } from 'next';
import { Locale, LOCALES } from '@/lib/i18n';

export async function generateStaticParams() {
  return LOCALES.map((lang) => ({ lang }));
}

export const metadata: Metadata = {
  title: 'About Us | K-Trend Archive',
  description: 'Learn about K-Trend Archive, our editorial curation methodology, and mission.',
};

export default function AboutPage({ params }: { params: { lang: Locale } }) {
  const { lang } = params;

  return (
    <main className="max-w-3xl mx-auto px-4 sm:px-6 py-12">
      <h1 className="text-3xl font-bold tracking-tight text-zinc-900 dark:text-zinc-100">
        About K-Trend Archive
      </h1>
      <p className="mt-2 text-sm text-zinc-500 font-mono">
        Last updated: November 2026
      </p>

      <div className="mt-8 space-y-6 text-sm leading-relaxed text-zinc-700 dark:text-zinc-300">
        <section>
          <h2 className="text-lg font-semibold text-zinc-900 dark:text-zinc-100 mb-2">
            Our Mission
          </h2>
          <p>
            K-Trend Archive is an independent digital publication dedicated to chronicling and curating the fast-moving trends in South Korea. We cover convenience store culinary innovations, K-beauty skincare breakthroughs, and seasonal contemporary Seoul street fashion in four languages (Korean, English, Japanese, and Simplified Chinese).
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-zinc-900 dark:text-zinc-100 mb-2">
            Editorial Integrity & Fact-Checking
          </h2>
          <p>
            Every product profiled on K-Trend Archive undergoes rigorous verification. We verify retail pricing, official ingredient breakdowns, fabric compositions, and release dates directly from manufacturers, press releases, and authorized Korean retail distributors.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-zinc-900 dark:text-zinc-100 mb-2">
            Global Accessibility & AI Readiness
          </h2>
          <p>
            We believe cultural trends should be universally accessible. In addition to multilingual human-readable guides, our archive provides machine-readable structured feeds (Model Context Protocol / MCP and llms.txt) to assist global researchers and automated retrieval systems.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-zinc-900 dark:text-zinc-100 mb-2">
            Contact & Inquiries
          </h2>
          <p>
            For editorial inquiries, partnership proposals, or corrections, contact our editorial team at{' '}
            <span className="font-mono text-zinc-900 dark:text-zinc-100">contact@k-trand.store</span>.
          </p>
        </section>
      </div>
    </main>
  );
}
