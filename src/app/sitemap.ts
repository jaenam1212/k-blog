import { MetadataRoute } from 'next';
import { fetchProductsFromDb } from '@/lib/products';
import { LOCALES } from '@/lib/i18n';

export const revalidate = 3600; // revalidate every hour

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const baseUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://www.k-trand.store';
  const products = await fetchProductsFromDb();

  const entries: MetadataRoute.Sitemap = [];

  // Home & category pages for all supported languages
  for (const lang of LOCALES) {
    entries.push({
      url: `${baseUrl}/${lang}`,
      lastModified: new Date(),
      changeFrequency: 'daily',
      priority: 1.0,
    });

    for (const cat of ['convenience-food', 'k-beauty', 'k-fashion']) {
      entries.push({
        url: `${baseUrl}/${lang}/${cat}`,
        lastModified: new Date(),
        changeFrequency: 'daily',
        priority: 0.8,
      });
    }

    // Individual product post pages
    for (const product of products) {
      entries.push({
        url: `${baseUrl}/${lang}/post/${product.slug}`,
        lastModified: new Date(product.releaseDate || new Date()),
        changeFrequency: 'weekly',
        priority: 0.9,
      });
    }
  }

  return entries;
}
