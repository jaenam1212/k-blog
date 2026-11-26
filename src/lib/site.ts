/**
 * Single source of truth for the public site origin.
 *
 * The canonical origin is https://www.k-trand.store:
 * - the apex domain (k-trand.store) answers with a 308 redirect to the www host,
 *   so a canonical/sitemap URL on the apex would point at a redirect target.
 * - preview/legacy deployment hosts (*.vercel.app, e.g. k-blog-ten.vercel.app)
 *   must never leak into canonical, hreflang, sitemap, robots or OG URLs.
 *
 * NEXT_PUBLIC_SITE_URL may be provided by the environment, but any value that is
 * not the apex/www k-trand.store host is ignored in favour of CANONICAL_ORIGIN.
 */
export const CANONICAL_ORIGIN = 'https://www.k-trand.store';

function resolveSiteUrl(raw: string | undefined): string {
  if (!raw) return CANONICAL_ORIGIN;
  const trimmed = raw.trim().replace(/\/+$/, '');
  if (!/^https?:\/\//i.test(trimmed)) return CANONICAL_ORIGIN;
  try {
    const { hostname } = new URL(trimmed);
    if (hostname === 'k-trand.store' || hostname === 'www.k-trand.store') {
      return CANONICAL_ORIGIN;
    }
  } catch {
    return CANONICAL_ORIGIN;
  }
  return CANONICAL_ORIGIN;
}

export const SITE_URL = resolveSiteUrl(process.env.NEXT_PUBLIC_SITE_URL);

/** Absolute URL for a path that starts with "/". */
export function siteUrl(path = '/'): string {
  return `${SITE_URL}${path.startsWith('/') ? path : `/${path}`}`;
}
