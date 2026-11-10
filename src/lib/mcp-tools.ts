import { PRODUCTS, getProductBySlug, searchProducts, Product } from './products';
import { Locale, LOCALES } from './i18n';

export const SERVER_INFO = {
  name: 'k-trend-box-mcp-server',
  version: '1.0.0',
};

export const PROTOCOL_VERSION = '2024-11-05';

export const MCP_TOOLS = [
  {
    name: 'list_latest_products',
    description: 'Retrieve latest curated Korean convenience store food, K-Beauty, and K-Fashion new releases with multilingual summaries.',
    inputSchema: {
      type: 'object',
      properties: {
        category: {
          type: 'string',
          enum: ['all', 'convenience-food', 'k-beauty', 'k-fashion'],
          description: 'Filter by category. Defaults to all.',
        },
        lang: {
          type: 'string',
          enum: ['ko', 'en', 'ja', 'zh'],
          description: 'Output language (ko=Korean, en=English, ja=Japanese, zh=Chinese). Defaults to en.',
        },
        limit: {
          type: 'number',
          description: 'Max number of items to return. Defaults to 10.',
        },
      },
    },
    annotations: { readOnlyHint: true, openWorldHint: true },
  },
  {
    name: 'get_product_detail',
    description: 'Get in-depth review, pricing, store availability, and local tasting/styling tips for a specific Korean trend product by slug.',
    inputSchema: {
      type: 'object',
      properties: {
        slug: {
          type: 'string',
          description: 'The product slug (e.g. cu-strawberry-choco-whip-castella-sand).',
        },
        lang: {
          type: 'string',
          enum: ['ko', 'en', 'ja', 'zh'],
          description: 'Output language (ko, en, ja, zh). Defaults to en.',
        },
      },
      required: ['slug'],
    },
    annotations: { readOnlyHint: true },
  },
  {
    name: 'search_k_trends',
    description: 'Search Korean trend items, convenience store food, and fashion releases by keyword.',
    inputSchema: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'Keywords to search (e.g., strawberry, hooppang, cashmere, ramen).',
        },
        lang: {
          type: 'string',
          enum: ['ko', 'en', 'ja', 'zh'],
          description: 'Language code. Defaults to en.',
        },
      },
      required: ['query'],
    },
    annotations: { readOnlyHint: true },
  },
];

export async function executeMcpTool(name: string, args: Record<string, any>) {
  const lang = (args.lang && LOCALES.includes(args.lang) ? args.lang : 'en') as Locale;

  if (name === 'list_latest_products') {
    const category = args.category || 'all';
    const limit = args.limit || 10;
    const filtered = category === 'all' 
      ? PRODUCTS 
      : PRODUCTS.filter((p) => p.category === category);

    const items = filtered.slice(0, limit).map((p) => {
      const loc = p.i18n[lang] || p.i18n.en;
      return {
        id: p.id,
        slug: p.slug,
        category: p.category,
        store: p.store,
        priceKrw: p.priceKrw,
        releaseDate: p.releaseDate,
        rating: p.rating,
        title: loc.title,
        summary: loc.summary,
        url: `https://k-trendbox.com/${lang}/post/${p.slug}`,
      };
    });

    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify({ count: items.length, products: items }, null, 2),
        },
      ],
    };
  }

  if (name === 'get_product_detail') {
    const product = getProductBySlug(args.slug);
    if (!product) {
      return {
        isError: true,
        content: [{ type: 'text', text: `Product with slug '${args.slug}' not found.` }],
      };
    }

    const loc = product.i18n[lang] || product.i18n.en;
    const detail = {
      id: product.id,
      slug: product.slug,
      category: product.category,
      store: product.store,
      priceKrw: product.priceKrw,
      releaseDate: product.releaseDate,
      rating: product.rating,
      title: loc.title,
      summary: loc.summary,
      description: loc.description,
      tasteReview: loc.tasteReview,
      tips: loc.tips,
      affiliateUrl: product.affiliateUrl,
      canonicalUrl: `https://k-trendbox.com/${lang}/post/${product.slug}`,
    };

    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify(detail, null, 2),
        },
      ],
    };
  }

  if (name === 'search_k_trends') {
    const results = searchProducts(args.query, lang).map((p) => {
      const loc = p.i18n[lang] || p.i18n.en;
      return {
        slug: p.slug,
        title: loc.title,
        store: p.store,
        priceKrw: p.priceKrw,
        url: `https://k-trendbox.com/${lang}/post/${p.slug}`,
      };
    });

    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify({ query: args.query, matches: results.length, results }, null, 2),
        },
      ],
    };
  }

  throw new Error(`Unknown MCP tool: ${name}`);
}
