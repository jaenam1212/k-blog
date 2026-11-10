import { Locale } from './i18n';

export interface LocalizedContent {
  title: string;
  summary: string;
  description: string;
  tasteReview: string[];
  tips: string;
}

export interface Product {
  id: string;
  slug: string;
  category: 'convenience-food' | 'k-beauty' | 'k-fashion';
  store: string;
  priceKrw: number;
  releaseDate: string;
  rating: number; // out of 5
  imageUrl: string;
  affiliateUrl: string;
  affiliatePlatform: 'Coupang' | 'Musinsa' | 'OliveYoung' | 'ConvenienceStore';
  i18n: Record<Locale, LocalizedContent>;
}

export const FALLBACK_PRODUCTS: Product[] = [
  {
    id: 'cu-strawberry-choco-sand-202611',
    slug: 'cu-strawberry-choco-whip-castella-sand',
    category: 'convenience-food',
    store: 'CU',
    priceKrw: 5500,
    releaseDate: '2026-11-06',
    rating: 4.8,
    imageUrl: 'https://images.unsplash.com/photo-1509440159596-0249088772ff?w=800&auto=format&fit=crop',
    affiliateUrl: 'https://link.coupang.com/example-cu-strawberry',
    affiliatePlatform: 'Coupang',
    i18n: {
      ko: {
        title: 'CU 신상 "딸기 초코 휩 카스텔라 샌드" 실구매 후기 및 칼로리 총정리',
        summary: '겨울 한정 생딸기와 진한 초코 휩크림, 초코칩이 씹히는 부드러운 카스텔라 디저트 샌드위치',
        description: 'CU가 겨울 생딸기 시즌을 맞아 선보인 스스스 샌드위치 시리즈의 최신 역작입니다. 폭신한 초코 카스텔라 빵 사이에 고당도 국내산 생딸기와 진한 가나슈 초코 휩크림을 가득 채웠습니다.',
        tasteReview: [
          '첫 입에 씹히는 생딸기 과즙과 달콤 쌉싸름한 초코칩의 조화가 완벽함',
          '크림이 과하게 미끌거리지 않고 동물성 생크림 특유의 깔끔한 단맛',
          '포켓CU 앱에서 사전예약 후 픽업하면 품절 걱정 없이 획득 가능',
        ],
        tips: '냉장고에서 꺼낸 직후보다 실온에 5분 정도 두어 크림이 살짝 녹았을 때 먹으면 카스텔라의 촉촉함이 극대화됩니다.',
      },
      en: {
        title: 'Korean CU Convenience Store Viral "Fresh Strawberry Choco Castella Sand" Review',
        summary: 'Winter limited edition with whole fresh Korean strawberries, rich chocolate whipped cream, and chocolate chips.',
        description: 'CU Convenience Store has officially kicked off its 2026 winter strawberry dessert lineup. Sandwiched inside ultra-soft chocolate sponge castella, sweet whole strawberries meet silky chocolate cream and crunchy chips.',
        tasteReview: [
          'Crisp fresh strawberry acidity cuts through the deep chocolate cream richness',
          'Soft bakery-level castella bread that never feels dry or rubbery',
          'Extremely viral in Seoul; best reserved on the PocketCU app to beat the morning sellout',
        ],
        tips: 'Pair with unsweetened black coffee or iced Americano for the ultimate Seoul cafe vibe.',
      },
      ja: {
        title: '韓国CUコンビニ新作「生イチゴチョコホイップカステラサンド」実食レビュー＆価格',
        summary: '冬限定！みずみずしい韓国産生イチゴと濃厚チョコホイップ、チョコチップが贅沢に詰まった話題の新作サンド。',
        description: '韓国のコンビニ大手CUが贈る冬のイチゴシリーズ最新作。しっとりしたチョコカステラ生地の間に、ジューシーな大粒イチゴとふわふわのチョコ生クリームを贅沢にサンドしています。',
        tasteReview: [
          'イチゴのフレッシュな酸味とビターチョコチップの食感が絶妙にマッチ',
          'コンビニスイーツの域を超えた本格パティスリー級のクリームの軽さ',
          '現地の若者に大人気で午前中に完売する店舗続出中',
        ],
        tips: '冷たい牛乳やアメリカーノと一緒に味わうと甘さが引き立ち最高のおやつになります。',
      },
      zh: {
        title: '韩国CU便利店冬季王炸新品“草莓巧克力奶油蛋糕三明治”测评与打卡指南',
        summary: '冬日限定整颗鲜草莓搭配浓郁巧克力夹心奶油与香脆巧克力豆，口感松软香甜。',
        description: '韩国CU便利店2026年冬季草莓甜品季的断货王！在松软的巧克力长崎蛋糕中，裹入了甜脆多汁的韩国当季鲜草莓和香醇不腻的生巧奶油。',
        tasteReview: [
          '咬下去先是草莓果汁爆浆，紧接着是巧克力豆的酥脆口感，层级丰富',
          '奶油清甜不腻，蛋糕体松软湿润，完全不输首尔精品甜品店',
          '首尔主要商圈店铺每日限量发售，建议早晨进店或通过CU App提前预约',
        ],
        tips: '从冷藏柜取出后静置5分钟再食用，奶油口感会更加绵密顺滑。',
      },
    },
  },
  {
    id: 'seven-redhot-steamed-bun-202611',
    slug: '7-eleven-red-hot-veggie-pizza-steamed-bun',
    category: 'convenience-food',
    store: '7-Eleven',
    priceKrw: 1800,
    releaseDate: '2026-11-06',
    rating: 4.6,
    imageUrl: 'https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?w=800&auto=format&fit=crop',
    affiliateUrl: 'https://link.coupang.com/example-7eleven-bun',
    affiliatePlatform: 'Coupang',
    i18n: {
      ko: {
        title: '세븐일레븐 동절기 신상 "레드핫 야채호빵 & 피자호빵" 매운맛 솔직 리뷰',
        summary: '칼칼한 매운맛 소스와 푸짐한 고기·치즈가 들어간 세븐일레븐 단독 겨울 호빵 신작',
        description: '기온이 급강하하며 출시된 세븐일레븐의 2026 겨울 간식 라인업. 레드핫야채호빵은 돼지고기와 채소에 매콤 소스를 버무렸고, 레드핫피자호빵은 라구 소스와 치즈로 스파이시 피자 풍미를 냅니다.',
        tasteReview: [
          '신라면보다 살짝 매콤한 칼칼함으로 겨울철 찬바람 불 때 해장 간식으로 제격',
          '피자호빵은 치즈 함량이 높아 전자레인지 30초 돌렸을 때 치즈가 길게 늘어남',
          '개당 1,800원으로 가성비 훌륭',
        ],
        tips: '찜기에서 바로 꺼낸 것을 사거나, 포장지 귀퉁이를 조금 찢고 전자레인지에 딱 30초 데워 드세요.',
      },
      en: {
        title: '7-Eleven Korea Winter Viral "Red Hot Spicy Steamed Buns" (Hoppang) Review',
        summary: 'Warm, fluffy Korean steamed buns with a fiery kick—available in Spicy Veggie-Pork and Spicy Pizza Cheese.',
        description: 'Hoppang is Korea’s quintessential winter street snack. 7-Eleven introduced spicy upgrades featuring juicy pork, melted cheese, and Korean chili seasoning to beat the freezing weather.',
        tasteReview: [
          'Spicy kick reminiscent of spicy ramen, perfect warming snack on a chilly Seoul evening',
          'The pizza version has stretchy cheese with tomato ragu and corn sweetness',
          'Only 1,800 KRW (~$1.30 USD), unmatched street food value',
        ],
        tips: 'Ask the clerk for one directly from the glass steamer warmer at the counter.',
      },
      ja: {
        title: '韓国セブンイレブン冬の風物詩「レッドホット旨辛野菜・ピザ中華まん（ホッパン）」レビュー',
        summary: '冬の韓国コンビニ名物ホッパンにスパイシーな新作登場！ピリ辛野菜豚肉味＆とろけるピザチーズ味。',
        description: '寒波が訪れた韓国で飛ぶように売れているセブンイレブン限定の旨辛ホッパン（中華まん）。具だくさんの豚肉と野菜に唐辛子ソースを利かせた野菜まんと、濃厚チーズのピザまんの2種展開です。',
        tasteReview: [
          'しっかりとした辛さがあり、日本のピザまんより刺激的で病みつきになる味わい',
          '生地がもちもちで温かいまま頬張ると体がポカポカ温まります',
          '1個1,800ウォンとお手頃価格で夜食にぴったり',
        ],
        tips: '店頭の専用スチーマー（蒸し器）から熱々を購入するのが一番美味しい食べ方です。',
      },
      zh: {
        title: '韩国7-Eleven冬季限定“Red Hot香辣蔬菜包 & 辣味披萨包”实拍测评',
        summary: '冬日韩国街头便利店必吃暖冬热食包子（Hoppang），香辣猪肉与拉丝披萨芝士的双重诱惑。',
        description: '韩国便利店秋冬最具代表性的保温箱热食！7-Eleven推出的Red Hot香辣系列，外皮软糯香甜，内馅包含了香辣调味猪肉碎、蔬菜以及浓郁拉丝芝士。',
        tasteReview: [
          '辣度适中带有一丝甜香，特别适合寒风中咬上一口暖胃',
          '披萨款拉丝效果惊艳，番茄肉酱与玉米粒搭配香气扑鼻',
          '单价仅1,800韩元（约合9元人民币），性价比极高',
        ],
        tips: '收银台旁边的玻璃蒸包机里现取最佳，或带回酒店用微波炉加热30秒。',
      },
    },
  },
  {
    id: 'musinsa-cashmere-coat-202611',
    slug: 'musinsa-standard-cashmere-balmacaan-robe-coat',
    category: 'k-fashion',
    store: 'Musinsa Standard',
    priceKrw: 189000,
    releaseDate: '2026-11-09',
    rating: 4.9,
    imageUrl: 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=800&auto=format&fit=crop',
    affiliateUrl: 'https://musinsa.com/example-cashmere-coat',
    affiliatePlatform: 'Musinsa',
    i18n: {
      ko: {
        title: '무신사 스탠다드 2026 겨울 신상 "캐시미어 블렌드 발마칸 로브 코트" 핏·소재 분석',
        summary: '한일 동시 발매된 미니멀 감성의 캐시미어 혼방 발마칸 코트. 높은 보온성과 우아한 실루엣.',
        description: '무신사 스탠다드가 일본 유명 패션 인플루언서와 손잡고 글로벌 동시 출시한 2026 동절기 플래그십 코트입니다. 캐시미어 특유의 부드러운 윤기와 발마칸 특유의 자연스러운 어깨 라인이 특징입니다.',
        tasteReview: [
          '울 80% + 캐시미어 20% 황금 비율로 가벼우면서도 바람을 완벽 차단',
          '허리 로브 벨트를 묶거나 자연스럽게 풀었을 때 전혀 다른 무드 연출 가능',
          '20만 원 이하 가격대에서 찾아보기 힘든 고급스러운 텍스처',
        ],
        tips: '정사이즈를 입으면 단정한 출근룩, 한 사이즈 업하면 세련된 오버핏 스트리트 룩이 연출됩니다.',
      },
      en: {
        title: 'Musinsa Standard FW26 "Cashmere Blend Balmacaan Robe Coat" Style Guide',
        summary: 'The minimalist Seoul aesthetic perfected: premium cashmere blend with versatile robe belt styling.',
        description: 'Korea’s largest fashion platform Musinsa released its flagship winter coat. Featuring a classic balmacaan collar and flowing silhouette, it delivers quiet luxury at an accessible Korean price point.',
        tasteReview: [
          'Lightweight yet remarkably wind-resistant thanks to premium cashmere-wool weave',
          'Neutral charcoal and black tones that pair seamlessly with sneakers or leather boots',
          'Worldwide shipping available through Musinsa Global store',
        ],
        tips: 'Size up by one if you plan to layer thick knit sweaters or tailored blazers underneath.',
      },
      ja: {
        title: '韓国MUSINSA新作「カシミヤブレンドバルマカーンローブコート」着こなし＆サイズ感',
        summary: '日韓同時展開の注目アウター！上質なカシミヤ混素材とミニマルなソウルストリート의 洗練シルエット。',
        description: '韓国最大のファッション通販ムシンサ（MUSINSA）のオリジナルブランドが発表した冬の本命コート。加藤順子氏とのコラボキャンペーンでも話題を呼び、上質な光沢感と美しい落ち感が魅力です。',
        tasteReview: [
          'カシミヤ混ならではの軽やかさと保温性、チクチク感のない極上の肌触り',
          'ウエストベルトを縛るとシックに、外すとリラックスした韓国風オーバーサイズに',
          '2万円を切る圧倒的コストパフォーマンス',
        ],
        tips: '日本のMUSINSA GLOBALサイトから関税フリーで直接自宅配送が可能です。',
      },
      zh: {
        title: '韩国MUSINSA Standard秋冬重磅“羊绒混纺巴尔玛肯浴袍大衣”版型与穿搭测评',
        summary: '首尔极简风天花板！羊绒羊毛混纺保暖面料，自带随性腰带，打造高级韩系冬日穿搭。',
        description: '韩国本土最受欢迎的国民时尚品牌MUSINSA推出的2026冬季王牌大衣。巴尔玛肯插肩袖设计修饰肩线，羊绒混纺带来高级光泽感，中性版型男女皆宜。',
        tasteReview: [
          '羊绒质感细腻柔糯，保暖抗风性出众且自重极轻',
          '既可系带勾勒腰线打造优雅通勤风，也可敞开穿营造慵懒松弛感',
          '性价比无敌，质感媲美万元级轻奢大牌',
        ],
        tips: '建议选择比平时大一码，内搭厚针织衫或西装叠穿层次感更丰富。',
      },
    },
  },
];

const SUPABASE_URL = process.env.NEXT_PUBLIC_SUPABASE_URL || 'https://jmuqmvxubuwhoocuknnt.supabase.co';
const SUPABASE_KEY = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptdXFtdnh1YnV3aG9vY3Vrbm50Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTQzMDgwNzcsImV4cCI6MjEwOTg4NDA3N30.wgl1-ohyWwTlg2rishdaqXA8jBeFgjQ3qyfINY5sc5A';

export const PRODUCTS = FALLBACK_PRODUCTS;

export async function fetchProductsFromDb(): Promise<Product[]> {
  try {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/posts?select=slug,data&order=id.desc`, {
      headers: {
        apikey: SUPABASE_KEY,
        Authorization: `Bearer ${SUPABASE_KEY}`,
      },
      next: { revalidate: 60, tags: ['posts'] },
    });
    if (!res.ok) throw new Error(`Supabase returned status ${res.status}`);
    const rows = await res.json();
    if (Array.isArray(rows) && rows.length > 0) {
      return rows.map((r: any) => r.data as Product);
    }
  } catch (err) {
    console.error('Supabase fetch failed, falling back to static list:', err);
  }
  return FALLBACK_PRODUCTS;
}

export async function getProductBySlugAsync(slug: string): Promise<Product | undefined> {
  const all = await fetchProductsFromDb();
  return all.find((p) => p.slug === slug);
}

export async function getProductsByCategoryAsync(category?: string): Promise<Product[]> {
  const all = await fetchProductsFromDb();
  if (!category || category === 'all') return all;
  return all.filter((p) => p.category === category);
}

export async function searchProductsAsync(query: string, lang: Locale = 'en'): Promise<Product[]> {
  const all = await fetchProductsFromDb();
  const q = query.toLowerCase();
  return all.filter((p) => {
    const loc = p.i18n[lang] || p.i18n.en;
    return (
      loc.title.toLowerCase().includes(q) ||
      loc.summary.toLowerCase().includes(q) ||
      p.store.toLowerCase().includes(q)
    );
  });
}

export function getProductBySlug(slug: string): Product | undefined {
  return FALLBACK_PRODUCTS.find((p) => p.slug === slug);
}

export function getProductsByCategory(category?: string): Product[] {
  if (!category || category === 'all') return FALLBACK_PRODUCTS;
  return FALLBACK_PRODUCTS.filter((p) => p.category === category);
}

export function searchProducts(query: string, lang: Locale = 'en'): Product[] {
  const q = query.toLowerCase();
  return FALLBACK_PRODUCTS.filter((p) => {
    const loc = p.i18n[lang] || p.i18n.en;
    return (
      loc.title.toLowerCase().includes(q) ||
      loc.summary.toLowerCase().includes(q) ||
      p.store.toLowerCase().includes(q)
    );
  });
}
