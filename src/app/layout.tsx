import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  metadataBase: new URL('https://k-trendbox.com'),
  title: 'K-Trend Box | Korean Convenience Food & K-Beauty Multilingual Guide',
  description: 'Real-time Korean convenience store food (CU, GS25, 7-Eleven) new snacks, K-Beauty, and K-Fashion guides in Korean, English, Japanese, and Chinese. MCP & AI-search ready.',
  alternates: {
    types: {
      'text/markdown': '/llms.txt',
    },
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <link rel="describedby" href="/llms.txt" />
        <link rel="service-desc" href="/api/mcp" />
      </head>
      <body className="min-h-screen bg-neutral-50 dark:bg-neutral-950 text-neutral-900 dark:text-neutral-100 antialiased selection:bg-rose-500 selection:text-white">
        {children}
      </body>
    </html>
  );
}
