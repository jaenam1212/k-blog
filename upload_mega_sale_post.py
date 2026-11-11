#!/usr/bin/env python3
"""
Upload November Mega Sale Curation Post covering Black Friday, Guanggunjie, Coupang, CVS & Food
"""

import json
import urllib.request

SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptdXFtdnh1YnV3aG9vY3Vrbm50Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDMwODA3NywiZXhwIjoyMTA5ODg0MDc3fQ.ELyAmyRJrWdQoIHRu4thMGvjAnjJfVZ4S8Cfpb9MiDY"
REVALIDATE_URL = "https://www.k-trand.store/api/revalidate?secret=kblog2026"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

desc_ko = """1년 중 쇼핑하기 가장 좋은 11월 할인 시즌이 본격적으로 시작되었습니다.
11.11 광군제를 기점으로 무신사 블랙프라이데이, 쿠팡 와우 빅세일, 편의점 11월 정기 1+1 행사까지 전 커머스 채널이 연중 최대 할인 공세에 들어갔습니다.

하지만 수만 개의 세일 상품 중에서 '진짜 살 만한 품목'을 골라내지 못하면 불필요한 지출만 늘어나기 십상입니다.
의류 패션부터 편의점 간식, 신선 식품까지 지금 시점에 장바구니에 담아야 마진이 남는 핵심 특가 정보만 엄선해 정리해 드립니다.

1. 쿠팡 11월 와우 메가세일 & 골드박스 특가
로켓배송과 로켓프레시를 이용 중인 와우 회원이라면 지금이 생필품과 겨울 방한용품을 쟁여둘 최적기입니다.
• 식품/생필품: 로켓프레시 한우·삼겹살 등 육류 및 겨울 밀키트 최대 45% 즉시할인, 햇반·생수 등 대용량 묶음상품 단독 최저가
• 디지털/가전: 에어팟, 온열매트, 가습기 등 겨울 시즌 필수 가전 카드사 추가 10% 쿠폰 할인
• 팁: 매일 아침 7시 갱신되는 '골드박스 단 하루 특가' 탭을 노리면 정가 대비 50% 이상 저렴하게 득템 가능합니다.

2. 11.11 광군제 & 글로벌 쇼핑 페스타
알리익스프레스와 국내 주요 오픈마켓이 총출동하는 광군제 시즌은 가성비 전자기기와 생활 잡화를 쓸어 담는 날입니다.
• 추천 품목: 스마트워치 스트랩, 고속 충전기(GaN), 차량용 거치대, 캠핑·레저 용품
• 결제 혜택: 카카오페이, 토스페이, 네이버페이 결제 시 선착순 즉시 할인 쿠폰 중복 적용 필수

3. 무신사 & SPA 겨울 블랙프라이데이 (패션 의류)
겨울 아우터는 12월 한파가 오기 전, 11월 블프 선착순 특가로 장만하는 것이 가장 저렴합니다.
• 무신사 스탠다드: MTR 코트 및 시티 레저 다운 패딩 최대 40~60% 선착순 특가
• 유니클로 감사제: 겨울 필수템 히트텍 울트라웜 및 플리스 풀짚 재킷 기간 한정 특가(2만 원대)
• 인기 도메스틱: 쿠어, 인사일런스, 도프제이슨 등 대표 브랜드의 캐시미어 니트와 레더 자켓 시즌오프 진입

4. 편의점 11월 1+1 기획전 & 배달앱 특가 (CU / GS25 / 배민)
빼빼로데이와 수능 시즌이 겹친 11월 편의점은 과자, 초콜릿뿐만 아니라 즉석 간편식과 주류 혜택이 역대급입니다.
• CU & GS25: 헤이루/유어스 즉석밥 및 컵라면 번들 1+1, 프리미엄 캔맥주·하이볼 4캔 1만 원 골라담기
• 배달/포장: 주요 치킨·피자 프랜차이즈 배달앱 11월 릴레이 할인 쿠폰(방문포장 시 최대 45% 할인)

결론 및 실전 쇼핑 팁:
• 패션 아우터는 11월 중순 블프 티징 시점이 사이즈 재고가 가장 넉넉합니다.
• 편의점 1+1 상품은 앱의 보관함 기능(포켓CU 키핑, GS25 나만의 냉장고)을 활용해 미리 쟁여두면 유통기한 걱정 없이 소비할 수 있습니다.
• 쿠팡 장바구니에 담아둔 상품은 자정 및 오전 7시 골드박스 편성 여부를 한 번 더 확인 후 결제하는 것을 추천합니다."""

desc_en = """November marks the single biggest shopping and discount season of the year in Korea and globally.
Kicking off with 11.11 Singles' Day (Guanggunjie), Korean fashion giant Musinsa's Black Friday, Coupang's WOW Mega Sale, and nationwide CVS 1+1 events are offering peak year-end discounts.

Here is your essential, hype-free curated shopping cheatsheet covering winter fashion, convenience store staples, and fresh grocery deals:

1. Coupang WOW Mega Sale & Goldbox Steals
- Fresh Food: Up to 45% off premium Korean beef (Hanwoo), pork belly, and winter dinner meal kits via Rocket Fresh.
- Tech & Life: Heavy discounts on AirPods, humidifiers, and heated blankets with additional 10% credit card checkout perks.
- Pro Tip: Check Coupang Goldbox at 7:00 AM daily for flash 24-hour steals up to 50% off.

2. 11.11 Global Shopping Festival (Singles' Day)
- Key Picks: High-speed GaN chargers, smartwatch bands, EDC tech gear, and outdoor essentials with stacked digital wallet coupons (KakaoPay, TossPay).

3. Musinsa & SPA Winter Black Friday
- Outerwear Essentials: Musinsa Standard MTR wool coats and city leisure down puffers at 40-60% off before the December cold snap.
- Uniqlo Winter Thank-You Days: Heattech Ultra Warm thermal layers and fleece full-zip jackets under $25.
- Top Korean Designer Brands: Coor, In Silence, and Doff Jason cashmere sweaters and vegan leather jackets.

4. Convenience Store 1+1 & Food Delivery Promotions
- CU & GS25: Massive 1+1 deals on instant rice, ramen multipacks, and 4-can craft beer bundles for 10,000 KRW.
- Delivery Apps: Up to 45% off takeaway orders on top fried chicken and pizza franchises throughout November."""

desc_ja = """1年で最もお得な11月のメガセールシーズンが本格開幕しました。
11.11独身の日（光棍節）を皮切りに、韓国最大のファッションプラットフォーム「MUSINSA（ムシンサ）」のブラックフライデー、クーパン（Coupang）のWOWメガセール、大手コンビニ（CU・GS25）の1+1キャンペーンが一斉にスタート。

冬物アウターからコンビニスイーツ、生鮮食品まで、今カートに入れるべき本命アイテムだけを厳選してまとめました：

1. クーパン WOWメガセール ＆ ゴールドボックス特価
- 生鮮食品：Rocket Freshの韓牛（ハヌ）・サムギョプサル、冬用ミールキットが最大45%OFF。
- 家電・日用品：AirPodsや加湿器、電熱マットなどの冬家電がカード決済でさらに10%OFF。
- 攻略法：毎朝7時に更新される「ゴールドボックス1日限定特価」が最大の狙い目。

2. 11.11 独身の日（光棍節）グローバルフェスタ
- ガジェット小物、スマートウォッチ用ストラップ、急速充電器などのコスパ神アイテムが最安値を更新。

3. MUSINSA ＆ SPA 冬のブラックフライデー
- 韓国人気ブランドのアウター：ムシンサスタンダードのMTRウールコートやダウンジャケットが40〜60%OFF。
- ユニクロ感謝祭：ヒートテックウルトラウォームやフリースジャケットの期間限定特価。

4. 韓国コンビニ 1+1 キャンペーン ＆ フードデリバリー
- CU・GS25：即席ご飯、カップ麺、プレミアム缶ビール・ハイボール4缶1万ウォンのメガキャンペーン。
- フード：人気チキン・ピザチェーンのテイクアウトで最大45%OFFのクーポン配布中。"""

desc_zh = """一年一度最大力度的11月购物狂欢节正式打响！
以双11双十一狂欢节为起点，韩国时尚巨头Musinsa黑五大促、Coupang酷澎WOW超级特价，以及韩国各大便利店（CU/GS25）买一送一活动全面引爆。

帮你避开套路，精选韩国服装、便利店美食和生鲜数码最值得入手的硬核折扣清单：

1. Coupang 酷澎WOW会员超级周 ＆ 金盒闪购
- 生鲜食品：Rocket Fresh 1级韩牛、精品五花肉及秋冬暖锅料理包低至5.5折。
- 数码家电：AirPods、电热毯、加湿器等秋冬必备好物享信用卡专属额外9折优惠。
- 技巧：每天早上7点更新的‘金盒单日闪购’是抢半价硬通货的最佳时机。

2. 双11全球购物狂欢季
- 推荐囤货：高功率GaN快充头、智能手表表带、车载支架、轻户外数码小物件。

3. Musinsa 韩国潮牌黑五 ＆ 品牌换季大促
- 冬季重头戏：Musinsa Standard MTR羊毛大衣、极简羽绒服享4-6折首发抢购。
- 优衣库感谢祭：超保暖Heattech内衣、摇粒绒拉链开衫限时破盘价。
- 设计师品牌：Coor羊绒毛衣、Doff Jason皮衣等韩国热门高阶品牌全面换季折价。

4. 韩国便利店11月买一送一 ＆ 外卖特惠
- CU ＆ GS25：即食米饭、泡面套组1+1，精酿啤酒与Highball威士忌苏打4罐1万韩元任意搭。
- 炸鸡外卖：BBQ、BHC等韩国头部炸鸡及披萨品牌自提专享最高5.5折折扣券。"""

example_items = [
  {
    "name": "시티 레저 푸퍼 다운 자켓 [블랙]",
    "brand": "무신사 스탠다드",
    "priceKrw": 59900,
    "imageUrl": "/images/products/item-black-puffer.png",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "MTR 오버사이즈 발마칸 코트 [딥 브라운]",
    "brand": "무신사 스탠다드",
    "priceKrw": 189900,
    "imageUrl": "/images/products/musinsa-mtr-balmacaan-coat.jpg",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "탑필 헤비 캐시미어 크루넥 니트 [포레스트 그린]",
    "brand": "쿠어 (COOOR)",
    "priceKrw": 79000,
    "imageUrl": "/images/products/item-green-knit.png",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "후리스 풀짚 스탠드넥 재킷 [그레이]",
    "brand": "유니클로 (UNIQLO)",
    "priceKrw": 29900,
    "imageUrl": "/images/products/uniqlo-mens-winter-wool-blend-balmacaan-coat-look-2.jpg",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "모찌 파베 초콜릿 말차맛 기획 세트",
    "brand": "CU 디저트",
    "priceKrw": 9900,
    "imageUrl": "/images/products/sale-dessert-treats.png",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "오버핏 비건 레더 싱글 블루종 [버건디]",
    "brand": "도프제이슨",
    "priceKrw": 89000,
    "imageUrl": "/images/products/item-burgundy-jacket.png",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  }
]

post = {
  "id": "november-2026-mega-sale-cheatsheet",
  "slug": "november-2026-mega-sale-cheatsheet-black-friday-coupang",
  "category": "convenience-food",
  "store": "11월 메가 쇼핑 페스타 큐레이션",
  "priceKrw": 29900,
  "releaseDate": "2026-11-11",
  "rating": 5.0,
  "imageUrl": "/images/products/sale-guide-cover.png",
  "images": [
    "/images/products/sale-guide-cover.png",
    "/images/products/sale-puffer-jacket.png",
    "/images/products/sale-dessert-treats.png",
    "/images/products/item-black-puffer.png"
  ],
  "exampleItems": example_items,
  "affiliateUrl": "https://www.musinsa.com/curator/s/jaenam1212",
  "affiliatePlatform": "Musinsa",
  "i18n": {
    "ko": {
      "title": "놓치면 무조건 손해: 11월 광군제·블랙프라이데이·쿠팡 대형 세일 총정리 (실시간 특가 치트키)",
      "summary": "11.11 광군제부터 무신사 블프, 쿠팡 와우 빅세일, 편의점 1+1까지. 지금 당장 장바구니에 담아야 할 패션·식품·생필품 알짜 할인 품목 완벽 가이드.",
      "description": desc_ko,
      "tasteReview": [
        "11.11 광군제부터 쿠팡 메가세일, 무신사 블프, 편의점 1+1까지 핵심 4대 쇼핑 축제 완벽 정리",
        "가격 거품을 뺀 패션 아우터, 신선식품, 디지털 소품 중심의 실전 알짜 품목 큐레이션",
        "무신사 큐레이터 및 쿠팡 최저가 검색 연동으로 즉시 최저가 비교 및 구매 가능"
      ],
      "tips": "인기 브랜드의 한정 수량 블프 특가 상품은 오픈 직후 황금 사이즈(L, XL)부터 품절됩니다. 마음에 드는 상품은 미리 장바구니에 담아두고 자정 쿠폰 리셋 시점에 결제하는 것이 안전합니다."
    },
    "en": {
      "title": "Korea's Biggest November Mega Sales: Black Friday, Singles' Day, & Coupang Steals Guide",
      "summary": "From 11.11 Singles' Day and Musinsa Black Friday to Coupang WOW Mega Sale and CVS 1+1s—here are the must-buy deals right now.",
      "description": desc_en,
      "tasteReview": [
        "Complete overview of Korea's 4 major shopping festivals happening right now in November",
        "Hype-free curation focusing on winter outerwear, fresh foods, and convenience store steals",
        "Direct real-time price comparison and affiliate links attached for seamless checkout"
      ],
      "tips": "Popular outerwear sizes (L/XL) sell out within hours of Black Friday launch. Pre-load your cart before midnight coupon drops."
    },
    "ja": {
      "title": "見逃すと損！韓国11月メガセール完全攻略：独身の日・ブラックフライデー・クーパン特価まとめ",
      "summary": "11.11独身の日からムシンサ黒金セール、クーパンWOWビッグセール、コンビニ1+1まで。今すぐ買うべき本命アイテム徹底ガイド。",
      "description": desc_ja,
      "tasteReview": [
        "韓国で今開催中の4大ショッピングフェスティバルを1本の記事で網羅",
        "冬物アウター、韓国コンビニスイーツ、生鮮食品までリアルなお得品だけを厳選",
        "ムシンサおよびクーパンの最安値検索ボタン搭載で即座にショッピング可能"
      ],
      "tips": "アウターの人気サイズはセール開始直後に完売します。気になる商品は事前にカートへ入れて日付変更の瞬間に決済するのが鉄則です。"
    },
    "zh": {
      "title": "双11与黑五神级抄底攻略：韩国Coupang、潮牌Musinsa、便利店大促全汇总",
      "summary": "从双11全球购物节、Musinsa黑五破盘价，到Coupang生鲜特价和韩国便利店1+1，今年最值得冲的折扣好物一次讲透。",
      "description": desc_zh,
      "tasteReview": [
        "全面覆盖11月四大主力购物节：双十一、黑五、Coupang酷澎与便利店1+1",
        "去粗取精，专攻高性价比冬季外套、便利店零食与高频生活消耗品",
        "搭载Musinsa与Coupang即时比价入口，无缝完成一站式采购"
      ],
      "tips": "热门潮牌外套的黄金尺码（L/XL）通常在开抢数小时内售罄，建议提前加购并在零点折扣券刷新时秒付。"
    }
  }
}

slug = post["slug"]
check_url = f"{SUPABASE_URL}/rest/v1/posts?slug=eq.{slug}&select=id"
req = urllib.request.Request(check_url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        existing = json.loads(resp.read().decode("utf-8"))
        if existing:
            update_url = f"{SUPABASE_URL}/rest/v1/posts?id=eq.{existing[0]['id']}"
            payload = json.dumps({"data": post}).encode("utf-8")
            urllib.request.urlopen(urllib.request.Request(update_url, data=payload, headers=headers, method="PATCH"))
            print(f"[+] Updated post: {slug}")
        else:
            post_url = f"{SUPABASE_URL}/rest/v1/posts"
            payload = json.dumps({"slug": slug, "data": post}).encode("utf-8")
            urllib.request.urlopen(urllib.request.Request(post_url, data=payload, headers=headers, method="POST"))
            print(f"[+] Inserted post: {slug}")
except Exception as e:
    print(f"[-] Error: {e}")

try:
    urllib.request.urlopen(urllib.request.Request(REVALIDATE_URL))
    print("[+] Revalidated Vercel cache successfully!")
except Exception as e:
    print(f"[-] Revalidate error: {e}")
