# 🍱 K-Trend Box (Korea Trend & Convenience Store Blog)

A next-generation multilingual (Korean, English, Japanese, Chinese) trend blog built with **Next.js 15 App Router**, **Tailwind CSS**, and native **Model Context Protocol (MCP)** server integration for AI search engines (Perplexity, ChatGPT, Claude) and Google SEO.

---

## ⚡ Core Features

1. **Multilingual Architecture (i18n)**
   - 4 Languages: `ko` (한국어), `en` (English), `ja` (日本語), `zh` (简体中文).
   - Dynamic localized routing (`/[lang]/[category]/...`).
   - SEO Canonical & `hreflang` alternate links pre-configured for global indexation.

2. **Native MCP Server (`/api/mcp`)**
   - Built-in JSON-RPC 2.0 Streamable HTTP endpoint conforming to Model Context Protocol standards.
   - Tools exposed to AI agents:
     - `list_latest_products`: Filter new releases by category and language.
     - `get_product_detail`: In-depth taste/style reviews, store availability, pricing.
     - `search_k_trends`: Multi-language keyword search.
   - Discovery endpoints at `/.well-known/mcp.json` and HTTP `Link` response headers.

3. **GEO (Generative Engine Optimization) & llms.txt**
   - `/llms.txt`: Standard site manifest for LLM crawlers (Anthropic, OpenAI, Perplexity).
   - `/llms-full.txt`: Full raw markdown stream for AI RAG indexers.
   - Schema.org JSON-LD structured data (`Product`, `Review`, `AggregateRating`, `Offer`) on every post.

4. **Dual Monetization Pipeline**
   - **Google AdSense**: Responsive `AdSenseSlot` banners (in-feed and in-article).
   - **Affiliate Marketing**: High-converting CTAs for Coupang Rocket, Musinsa Store, and Olive Young (3~5% purchase commission).

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
npm install

# 2. Run local development server
npm run dev

# 3. Open in browser
open http://localhost:3000
```

### Endpoints
- Web App: `http://localhost:3000/ko`
- English Version: `http://localhost:3000/en`
- Japanese Version: `http://localhost:3000/ja`
- Chinese Version: `http://localhost:3000/zh`
- MCP Server: `http://localhost:3000/api/mcp`
- AI Discovery: `http://localhost:3000/llms.txt`
- REST API: `http://localhost:3000/api/products`

---

## 📦 Deployment (100% Free Hosting)

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "feat: initial k-trend-box with mcp server and i18n"
   git branch -M main
   git remote add origin <your-github-repo>
   git push -u origin main
   ```
2. **Deploy on Cloudflare Pages or Vercel**:
   - Connect repository.
   - Framework preset: `Next.js`.
   - Build command: `npm run build`.
   - Output directory: `.next`.
   - Monthly hosting cost: **₩0 (Free forever)**.
