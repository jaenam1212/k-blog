import { Metadata } from 'next';
import { Locale, LOCALES } from '@/lib/i18n';

export async function generateStaticParams() {
  return LOCALES.map((lang) => ({ lang }));
}

export const metadata: Metadata = {
  title: 'Terms of Service | K-Trend Archive',
  description: 'Terms and Conditions for using K-Trend Archive.',
};

export default function TermsPage({ params }: { params: { lang: Locale } }) {
  return (
    <main className="max-w-3xl mx-auto px-4 sm:px-6 py-12">
      <h1 className="text-3xl font-bold tracking-tight text-zinc-900 dark:text-zinc-100">
        Terms of Service
      </h1>
      <p className="mt-2 text-sm text-zinc-500 font-mono">
        Effective date: November 11, 2026
      </p>

      <div className="mt-8 space-y-6 text-sm leading-relaxed text-zinc-700 dark:text-zinc-300">
        <section>
          <h2 className="text-lg font-semibold text-zinc-900 dark:text-zinc-100 mb-2">
            1. Terms
          </h2>
          <p>
            By accessing the website at https://www.k-trand.store, you agree to be bound by these terms of service, all applicable laws and regulations, and agree that you are responsible for compliance with any applicable local laws.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-zinc-900 dark:text-zinc-100 mb-2">
            2. Content & Disclaimer
          </h2>
          <p>
            The materials on K-Trend Archive are provided on an 'as is' basis for informational and editorial purposes. Product prices, availability, and retail specifications are subject to change without notice by respective retailers and brands.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-zinc-900 dark:text-zinc-100 mb-2">
            3. Intellectual Property
          </h2>
          <p>
            All original editorial content, curation analysis, and site layout are the property of K-Trend Archive. Brand names, logos, and product photographs belong to their respective trademark and copyright holders and are cited under fair use for commentary and identification.
          </p>
        </section>
      </div>
    </main>
  );
}
