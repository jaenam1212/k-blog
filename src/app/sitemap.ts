import { MetadataRoute } from 'next';
import { fetchProductsFromDb } from '@/lib/products';
import { LOCALES } from '@/lib/i18n';
import { SITE_URL } from '@/lib/site';

export const revalidate = 3600; // revalidate every hour

const CATEGORIES = ['convenience-food', 'k-beauty', 'k-fashion', 'tech'];

/** hreflang map for one logical page path, e.g. "/{lang}" style template. */
function languageAlternates(pathFor: (lang: string) => string) {
  const languages: Record<string, string> = {};
  for (const lang of LOCALES) {
    languages[lang] = `${SITE_URL}${pathFor(lang)}`;
  }
  languages['x-default'] = `${SITE_URL}${pathFor('ko')}`;
  return { languages };
}

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const baseUrl = SITE_URL;
  const products = await fetchProductsFromDb();

  const entries: MetadataRoute.Sitemap = [];

  // Home & category pages for all supported languages
  for (const lang of LOCALES) {
    entries.push({
      url: `${baseUrl}/${lang}`,
      lastModified: new Date(),
      changeFrequency: 'daily',
      priority: 1.0,
      alternates: languageAlternates((l) => `/${l}`),
    });

    for (const cat of CATEGORIES) {
      entries.push({
        url: `${baseUrl}/${lang}/${cat}`,
        lastModified: new Date(),
        changeFrequency: 'daily',
        priority: 0.8,
        alternates: languageAlternates((l) => `/${l}/${cat}`),
      });
    }

    // Individual product post pages
    for (const product of products) {
      entries.push({
        url: `${baseUrl}/${lang}/post/${product.slug}`,
        lastModified: new Date(product.releaseDate || new Date()),
        changeFrequency: 'weekly',
        priority: 0.9,
        alternates: languageAlternates((l) => `/${l}/post/${product.slug}`),
      });
    }
  }

  return entries;
}
