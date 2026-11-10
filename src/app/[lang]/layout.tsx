import { Header } from '@/components/Header';
import { Footer } from '@/components/Footer';
import { Locale, LOCALES } from '@/lib/i18n';
import { notFound } from 'next/navigation';

export async function generateStaticParams() {
  return LOCALES.map((lang) => ({ lang }));
}

export default async function LocaleLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ lang: string }>;
}) {
  const { lang } = await params;

  if (!LOCALES.includes(lang as Locale)) {
    notFound();
  }

  return (
    <div className="flex flex-col min-h-screen">
      <Header lang={lang as Locale} />
      <main className="flex-1 max-w-5xl w-full mx-auto px-4 py-8">
        {children}
      </main>
      <Footer lang={lang as Locale} />
    </div>
  );
}
