import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Privacy Policy | K-Trend Archive',
  description: 'Privacy Policy for K-Trend Archive regarding cookies, analytics, and advertising.',
};

export default function PrivacyPage() {
  return (
    <main className="max-w-3xl mx-auto px-4 sm:px-6 py-12">
      <h1 className="text-3xl font-bold tracking-tight text-zinc-900 dark:text-zinc-100">
        Privacy Policy
      </h1>
      <p className="mt-2 text-sm text-zinc-500 font-mono">
        Effective date: November 11, 2026
      </p>

      <div className="mt-8 space-y-6 text-sm leading-relaxed text-zinc-700 dark:text-zinc-300">
        <section>
          <h2 className="text-lg font-semibold text-zinc-900 dark:text-zinc-100 mb-2">
            1. Information We Collect
          </h2>
          <p>
            At K-Trend Archive (accessible from https://www.k-trand.store), one of our main priorities is the privacy of our visitors. This Privacy Policy document contains types of information that is collected and recorded by K-Trend Archive and how we use it.
          </p>
          <p className="mt-2">
            Like many other websites, K-Trend Archive makes use of log files and privacy-focused analytics. The information inside the log files includes internet protocol (IP) addresses, browser type, Internet Service Provider (ISP), date/time stamp, referring/exit pages, and number of clicks to analyze trends, administer the site, and gather broad demographic information.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-zinc-900 dark:text-zinc-100 mb-2">
            2. Cookies and Web Beacons
          </h2>
          <p>
            K-Trend Archive uses cookies to store information about visitors' preferences, to record user-specific information on which pages the site visitor accesses or visits, and to personalize or customize our web page content based upon visitors' browser type or other information that the visitor sends via their browser.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-zinc-900 dark:text-zinc-100 mb-2">
            3. Google DoubleClick DART Cookies & Google AdSense
          </h2>
          <p>
            Google is one of the third-party vendors on our site. It also uses cookies, known as DART cookies, to serve ads to our site visitors based upon their visit to www.k-trand.store and other sites on the internet. However, visitors may choose to decline the use of DART cookies by visiting the Google ad and content network Privacy Policy at the following URL:{' '}
            <a
              href="https://policies.google.com/technologies/ads"
              target="_blank"
              rel="noopener noreferrer"
              className="text-zinc-900 dark:text-zinc-100 underline hover:no-underline font-mono"
            >
              https://policies.google.com/technologies/ads
            </a>
          </p>
          <p className="mt-2">
            Some of our advertising partners may use cookies and web beacons on our site. Our advertising partners include Google AdSense and affiliate networks. Third-party ad servers or ad networks use technologies like cookies, JavaScript, or Web Beacons that are used in their respective advertisements and links that appear on K-Trend Archive.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-zinc-900 dark:text-zinc-100 mb-2">
            4. Affiliate Disclosure
          </h2>
          <p>
            K-Trend Archive participates in various affiliate marketing programs, which means we may get paid commissions on editorially chosen products purchased through our links to retailer sites. This disclosure is provided in accordance with the Federal Trade Commission (FTC) guidelines and the Korea Fair Trade Commission.
          </p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-zinc-900 dark:text-zinc-100 mb-2">
            5. Consent
          </h2>
          <p>
            By using our website, you hereby consent to our Privacy Policy and agree to its terms.
          </p>
        </section>
      </div>
    </main>
  );
}
