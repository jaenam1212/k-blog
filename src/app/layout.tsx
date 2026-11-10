import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  metadataBase: new URL('https://k-trendbox.com'),
  title: 'K-Trend Archive | Korean Trend Guide',
  description: 'Curated editorial guide to latest Korean convenience food, beauty, and fashion releases in 4 languages.',
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
      <body className="min-h-screen bg-white dark:bg-zinc-950 text-zinc-900 dark:text-zinc-100 antialiased selection:bg-zinc-200 dark:selection:bg-zinc-800">
        {children}
      </body>
    </html>
  );
}
