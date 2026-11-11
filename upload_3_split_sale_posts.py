#!/usr/bin/env python3
"""
Upload 3 separate, highly targeted mega-sale posts:
1) Coupang WOW Mega Sale & Goldbox Steals
2) 11.11 Guanggunjie (Singles' Day) Tech & Gadgets Must-Buys
3) 2026 Musinsa Black Friday Winter Outerwear Top 6
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

# ==========================================
# Post 1: Coupang WOW Mega Sale & Goldbox
# ==========================================
post1_desc_ko = """11월을 맞아 쿠팡이 와우 회원을 대상으로 연중 최대 규모의 '와우 메가세일'에 돌입했습니다.
특히 매일 아침 7시 한정 수량으로 풀리는 '골드박스 단 하루 특가'와 로켓프레시 신선식품 대전은 지금 시점에 장바구니에 담아두지 않으면 손해인 대표 이벤트입니다.

정가 대비 최대 40~50% 저렴하게 건질 수 있는 핵심 카테고리별 실전 알짜 추천 품목을 정리해 드립니다.

1. 로켓프레시 신선식품 & 겨울 밀키트
• 1등급 한우 구이용/국거리: 오프라인 마트 대비 30~45% 저렴한 가격에 새벽배송으로 도착.
• 겨울 찌개 및 샤브샤브 밀키트: 주말 가족 식사용 밀키트 묶음 할인 진행 중.
• 생필품 번들: 햇반, 생수, 대용량 세제 등 무거운 장보기 품목 무료 새벽 반값 혜택.

2. 겨울 가전 & 생활 방한용품
• 대용량 초음파 가습기: 건조한 환절기 필수 가전으로 와우 회원 전용 즉시할인 쿠폰 적용.
• 온열 탄소매트 & 전기요: 주요 카드사 10% 추가 청구할인 적용 가능.

3. 쿠팡 쇼핑 실전 팁
• 오전 7시 골드박스 오픈 직후 인기 신선식품과 가전 품목이 빠르게 소진되므로, 미리 찜해둔 상품은 아침 출근길에 결제하는 것이 안전합니다.
• 쿠팡 최저가 검색 버튼을 통해 실시간 변동 가격과 카드 즉시할인 적용 여부를 확인해 보세요."""

post1 = {
  "id": "coupang-wow-mega-sale-goldbox-top-deals-2026",
  "slug": "coupang-wow-mega-sale-goldbox-top-deals-2026",
  "category": "convenience-food",
  "store": "쿠팡 와우 메가세일 큐레이션",
  "priceKrw": 23900,
  "releaseDate": "2026-11-11",
  "rating": 5.0,
  "imageUrl": "/images/products/coupang-sale-cover.png",
  "images": [
    "/images/products/coupang-sale-cover.png",
    "/images/products/item-hanwoo-beef.png",
    "/images/products/item-humidifier.png",
    "/images/products/sale-dessert-treats.png"
  ],
  "exampleItems": [
    {
      "name": "로켓프레시 1등급 한우 등심 구이용 500g",
      "brand": "쿠팡 로켓프레시",
      "priceKrw": 23900,
      "imageUrl": "/images/products/item-hanwoo-beef.png",
      "url": "https://www.k-trand.store"
    },
    {
      "name": "홈플래닛 상부급수 대용량 초음파 가습기 4.5L",
      "brand": "홈플래닛 가전",
      "priceKrw": 24900,
      "imageUrl": "/images/products/item-humidifier.png",
      "url": "https://www.k-trand.store"
    },
    {
      "name": "곰곰 무라벨 천연 암반수 생수 2L x 12병",
      "brand": "곰곰 (gomgom)",
      "priceKrw": 7990,
      "imageUrl": "/images/products/coupang-sale-cover.png",
      "url": "https://www.k-trand.store"
    },
    {
      "name": "CJ 햇반 백미 210g x 24개입 대용량 박스",
      "brand": "CJ제일제당",
      "priceKrw": 19800,
      "imageUrl": "/images/products/sale-dessert-treats.png",
      "url": "https://www.k-trand.store"
    }
  ],
  "affiliateUrl": "https://www.k-trand.store",
  "affiliatePlatform": "Coupang",
  "i18n": {
    "ko": {
      "title": "쿠팡 와우 메가세일 추천템 총정리: 골드박스 반값 특가 & 신선식품 BEST 4",
      "summary": "매일 아침 7시 열리는 골드박스 단 하루 특가부터 로켓프레시 1등급 한우, 겨울 난방 가전까지 지금 안 사면 손해인 쿠팡 알짜 쇼핑 리스트.",
      "description": post1_desc_ko,
      "tasteReview": [
        "로켓프레시 한우·신선식품 및 대용량 생필품 반값 골드박스 특가 완벽 큐레이션",
        "건조한 계절 필수템 가습기 등 겨울 생활가전 카드사 추가 10% 혜택",
        "쿠팡 고유 트래킹 링크로 실시간 최저가 및 로켓 새벽배송 즉시 확인"
      ],
      "tips": "골드박스는 매일 아침 7시에 오픈되며 인기 신선식품은 오전 중 조기 품절됩니다. 장바구니에 담아둔 품목의 가격 변동 알림을 켜두세요."
    },
    "en": {
      "title": "Coupang WOW Mega Sale 2026: Top Goldbox Steals & Rocket Fresh Grocery Guide",
      "summary": "From 7:00 AM daily Goldbox deals to premium Hanwoo beef and winter humidifiers—the best Coupang steals right now.",
      "description": "Coupang has launched its massive November WOW Mega Sale for subscribers. Here are the top vetted deals across groceries, winter living, and essentials.",
      "tasteReview": [
        "Curated top grocery and lifestyle steals with up to 45% Goldbox discounts",
        "Winter season essentials including large humidifiers and fresh dinner sets",
        "Direct real-time price lookup with Rocket dawn delivery access"
      ],
      "tips": "Goldbox resets at 7 AM daily. Popular grocery items sell out by noon."
    },
    "ja": {
      "title": "クーパン（Coupang）WOWメガセール完全攻略：ゴールドボックス特価＆生鮮食品まとめ",
      "summary": "毎朝7時更新のゴールドボックス半額特価から韓牛（ハヌ）、冬の生活家電まで今買うべきリアルなお得アイテムリスト。",
      "description": "韓国最大手ECクーパンが11月最大のWOWメガセールを開催中。生鮮食品から冬家電まで、本当にお得なアイテムだけを厳選しました。",
      "tasteReview": [
        "Rocket Freshの韓牛・生鮮食品や大容量日用品の半額特価を厳選",
        "乾燥する季節に必須の大容量加湿器など冬家電のカード追加割引",
        "リアルタイム最安値検索ボタン搭載"
      ],
      "tips": "ゴールドボックスは毎朝7時更新。人気食品は午前中に完売します。"
    },
    "zh": {
      "title": "韩国Coupang酷澎WOW会员超级周：金盒半价闪购与生鲜好物清单",
      "summary": "每日早7点准时开抢的金盒半价，到Rocket Fresh顶级韩牛和冬季加湿器，避坑高性价比抄底指南。",
      "description": "韩国Coupang全面开启11月WOW超级特价周。为你精选生鲜食品与秋冬生活家电最值得囤货的高性价比好物。",
      "tasteReview": [
        "精准覆盖Rocket Fresh韩牛、大容量生活消耗品金盒闪购",
        "秋冬必备大容量加湿器享信用卡专属折上折",
        "直连Coupang最安值比价入口"
      ],
      "tips": "金盒闪购每日早7点更新，热门生鲜通常上午售罄。"
    }
  }
}

# ==========================================
# Post 2: 11.11 Guanggunjie Tech & Gadgets
# ==========================================
post2_desc_ko = """11월 11일 광군제는 가성비 전자기기, 데스크 테크 소품, 고속 충전 기기를 가장 저렴하게 직구할 수 있는 연중 최대 쇼핑 축제입니다.
국내 오픈마켓의 11절 행사와 알리익스프레스 광군제가 동시에 맞물리면서 관부가세 면제 한도 내에서 주워 담을 수 있는 알짜 가성비 테크 템들이 쏟아져 나오고 있습니다.

IT/개발자와 테크 유저들이 이번 광군제에 무조건 챙겨야 할 실전 가성비 기기 BEST 4를 정리해 드립니다.

1. GaN 초소형 65W 고속 멀티 충전기 (Baseus / UGREEN)
노트북, 스마트폰, 태블릿을 벽돌 충전기 하나 없이 동시에 초고속 충전할 수 있는 필수 데스크 아이템입니다. 광군제 쿠폰 적용 시 1만 원대 후반에 진입합니다.

2. 3-in-1 마그네틱 무선 충전 스탠드
아이폰, 애플워치, 에어팟을 깔끔하게 하나의 스탠드에 거치할 수 있는 미니멀 데스크테리어 종결템입니다.

3. 액티브 노이즈 캔슬링(ANC) 무선 헤드폰
출퇴근길이나 카페 작업 시 외부 소음을 완벽히 차단해 주는 가성비 끝판왕 헤드폰입니다.

4. 광군제 직구 결제 팁
• 카카오페이, 토스페이, 네이버페이 등 국내 간편결제사 선착순 즉시 할인(30달러 이상 구매 시 4~6달러 할인)을 반드시 적용하세요.
• 결제 통화는 '달러(USD)'로 설정해야 이중 환전 수수료를 아낄 수 있습니다."""

post2 = {
  "id": "guanggunjie-1111-tech-gadgets-must-buy-list",
  "slug": "guanggunjie-1111-tech-gadgets-must-buy-list",
  "category": "k-fashion",
  "store": "11.11 광군제 테크 큐레이션",
  "priceKrw": 19800,
  "releaseDate": "2026-11-11",
  "rating": 5.0,
  "imageUrl": "/images/products/tech-gadgets-cover.png",
  "images": [
    "/images/products/tech-gadgets-cover.png",
    "/images/products/item-gan-charger.png",
    "/images/products/item-magsafe-stand.png",
    "/images/products/item-anc-headphones.png"
  ],
  "exampleItems": [
    {
      "name": "65W GaN 고속 3포트 초소형 멀티 충전기",
      "brand": "베이스어스 (Baseus)",
      "priceKrw": 19800,
      "imageUrl": "/images/products/item-gan-charger.png",
      "url": "https://www.musinsa.com/curator/s/jaenam1212"
    },
    {
      "name": "3-in-1 마그네틱 맥세이프 무선 충전 스탠드",
      "brand": "유그린 (UGREEN)",
      "priceKrw": 29900,
      "imageUrl": "/images/products/item-magsafe-stand.png",
      "url": "https://www.musinsa.com/curator/s/jaenam1212"
    },
    {
      "name": "하이브리드 ANC 무선 노이즈캔슬링 오버이어 헤드폰",
      "brand": "베이스어스 테크",
      "priceKrw": 34900,
      "imageUrl": "/images/products/item-anc-headphones.png",
      "url": "https://www.musinsa.com/curator/s/jaenam1212"
    },
    {
      "name": "미니멀 알루미늄 마그네틱 보조배터리 10000mAh",
      "brand": "테크 기어스",
      "priceKrw": 18900,
      "imageUrl": "/images/products/tech-gadgets-cover.png",
      "url": "https://www.musinsa.com/curator/s/jaenam1212"
    }
  ],
  "affiliateUrl": "https://www.musinsa.com/curator/s/jaenam1212",
  "affiliatePlatform": "Musinsa",
  "i18n": {
    "ko": {
      "title": "11.11 광군제 직구 추천템 BEST 4: 가성비 전자기기 & 테크 잡화 종결 가이드",
      "summary": "광군제 시즌에 무조건 담아야 할 GaN 65W 초소형 고속충전기, 맥세이프 3-in-1 스탠드, ANC 노이즈캔슬링 헤드폰 완벽 큐레이션.",
      "description": post2_desc_ko,
      "tasteReview": [
        "11.11 광군제 시즌 역대 최저가 갱신 가성비 테크 기기 엄선",
        "GaN 초고속 충전기부터 맥세이프 무선 거치대까지 실전 데스크테리어 필수템",
        "이중 환전 수수료 방지 및 국내 간편결제 즉시할인 꿀팁 수록"
      ],
      "tips": "결제 시 원화(KRW) 대신 달러(USD)로 설정해야 이중 환전 수수료 3~8%를 아낄 수 있습니다. 국내 간편결제 선착순 쿠폰을 꼭 적용하세요."
    },
    "en": {
      "title": "11.11 Singles' Day Tech Steals: Top 4 GaN Chargers & Smart Desk Gadgets",
      "summary": "The ultimate November 11 shopping festival guide for high-efficiency GaN chargers, MagSafe stands, and ANC headphones.",
      "description": "Singles' Day (11.11) offers the deepest global tech discounts of the year. Curated top picks for compact high-speed chargers and desk accessories.",
      "tasteReview": [
        "Lowest historical prices on verified EDC and desk technology",
        "Compact GaN chargers and 3-in-1 magnetic wireless charging docks",
        "Essential currency conversion and wallet checkout discounts included"
      ],
      "tips": "Always check out in USD to eliminate double currency conversion fees."
    },
    "ja": {
      "title": "11.11独身の日（光棍節）ガジェット特集：GaN急速充電器＆デスク小物おすすめ4選",
      "summary": "11月最大のグローバルセールで今すぐ買うべきGaN 65W充電器、MagSafeスタンド、ANCヘッドホンの決定版。",
      "description": "独身の日セールで最もコスパが高いコンパクト充電器やデスク周りの便利ガジェットを厳選して解説します。",
      "tasteReview": [
        "年間最安値を更新する高コスパガジェットを厳選",
        "ミニマルなデスク環境を構築するGaN充電器とMagSafeスタンド",
        "為替手数料を抑える決済テクニック掲載"
      ],
      "tips": "決済通貨をUSDに設定することで二重為替手数料を防げます。"
    },
    "zh": {
      "title": "双11数码狂欢节闭眼入清单：GaN氮化镓快充与桌面好物TOP4",
      "summary": "双十一全球购物节必囤的高性价比GaN 65W多口充电头、三合一磁吸无线充与降噪耳机保姆级指南。",
      "description": "双十一是一年中华强北与高性价比数码配件最值得抄底的时刻。为你精选高效桌面与移动办公必备好物。",
      "tasteReview": [
        "年度破盘价硬核数码配件精选",
        "桌面极简收纳与高速充电必备利器",
        "包含支付立减与免双重汇率手续费实操建议"
      ],
      "tips": "跨境结算时记得勾选以USD美元结算，避免双重货币转换费。"
    }
  }
}

# ==========================================
# Post 3: 2026 Musinsa Black Friday Outerwear
# ==========================================
post3_desc_ko = """겨울 아우터 쇼핑의 절대 골든타임은 12월 한파가 닥치기 직전인 '11월 무신사 블랙프라이데이(무진장 겨울 세일)' 기간입니다.
정가 20~30만 원대 프리미엄 MTR 코트와 헤비 다운 패딩이 선착순 특가로 10만 원대 중후반까지 떨어지는 시기이기 때문입니다.

12월이 되면 인기 컬러와 황금 사이즈(L, XL)가 모두 품절되므로, 지금 오픈 시점에 무조건 선점해야 할 대표 아우터 BEST 4를 정리해 드립니다.

1. 무신사 스탠다드 MTR 오버사이즈 발마칸 코트 [딥 브라운]
이탈리아 최고급 MTR 울 원사를 사용해 각이 무너지지 않고 보온성이 뛰어난 무신사 랭킹 1위 코트입니다. 블프 특가로 18만 원대에 진입합니다.

2. 시티 레저 푸퍼 다운 자켓 [블랙]
미니멀한 실루엣에 가벼운 경량성과 뛰어난 덕다운 충전재를 갖춘 도심형 숏패딩입니다. 5만 원대 파격 특가로 출퇴근 데일리용으로 최적입니다.

3. 탑필 헤비 캐시미어 크루넥 니트 [포레스트 그린]
코트 안에 받쳐 입기 가장 좋은 고밀도 캐시미어 니트로, 부드러운 촉감과 은은한 고급 컬러감이 돋보입니다.

4. 오버핏 비건 레더 싱글 자켓 [딥 버건디]
칙칙한 겨울 착장에 묵직하고 성숙한 분위기를 단숨에 더해주는 트렌디한 레더 블루종입니다.

블랙프라이데이 실전 팁:
• 무신사는 매일 밤 12시 선착순 랜덤 쿠폰과 브랜드 데이 쿠폰이 리셋됩니다. 마음에 드는 아우터는 미리 장바구니에 담아두고 자정 정각에 쿠폰을 먹여 결제하세요."""

post3 = {
  "id": "musinsa-black-friday-2026-outerwear-best-picks",
  "slug": "musinsa-black-friday-2026-outerwear-best-picks",
  "category": "k-fashion",
  "store": "무신사 블랙프라이데이 큐레이션",
  "priceKrw": 59900,
  "releaseDate": "2026-11-11",
  "rating": 5.0,
  "imageUrl": "/images/products/musinsa-bf-cover.png",
  "images": [
    "/images/products/musinsa-bf-cover.png",
    "/images/products/musinsa-bf-puffer.png",
    "/images/products/musinsa-mtr-balmacaan-coat.jpg",
    "/images/products/item-black-puffer.png"
  ],
  "exampleItems": [
    {
      "name": "MTR 오버사이즈 발마칸 코트 [딥 브라운]",
      "brand": "무신사 스탠다드",
      "priceKrw": 189900,
      "imageUrl": "/images/products/musinsa-mtr-balmacaan-coat.jpg",
      "url": "https://www.musinsa.com/curator/s/jaenam1212"
    },
    {
      "name": "시티 레저 푸퍼 다운 자켓 [블랙]",
      "brand": "무신사 스탠다드",
      "priceKrw": 59900,
      "imageUrl": "/images/products/item-black-puffer.png",
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
      "name": "오버핏 비건 레더 싱글 자켓 [딥 버건디]",
      "brand": "도프제이슨",
      "priceKrw": 89000,
      "imageUrl": "/images/products/item-burgundy-jacket.png",
      "url": "https://www.musinsa.com/curator/s/jaenam1212"
    }
  ],
  "affiliateUrl": "https://www.musinsa.com/curator/s/jaenam1212",
  "affiliatePlatform": "Musinsa",
  "i18n": {
    "ko": {
      "title": "2026 무신사 블랙프라이데이 아우터 추천템: 코트·패딩 역대급 세일 BEST 4",
      "summary": "12월 한파 오기 전 11월 블프 선착순 특가로 끝내는 겨울 아우터 쇼핑. 무신사 스탠다드 MTR 코트부터 헤비 푸퍼 패딩, 레더 자켓까지 사이즈 품절 전 픽.",
      "description": post3_desc_ko,
      "tasteReview": [
        "11월 무신사 블랙프라이데이 시즌 랭킹 1위 발마칸 코트와 숏패딩 특가 엄선",
        "한파 전 황금 사이즈 선점을 위한 실전 선착순 구매 가이드",
        "무신사 큐레이터 공식 링크 탑재로 최대 10% 추가 혜택 연동"
      ],
      "tips": "자정 12시에 선착순 랜덤 쿠폰이 리셋됩니다. 인기 아우터는 미리 장바구니에 담아두고 자정에 바로 결제해야 품절을 피할 수 있습니다."
    },
    "en": {
      "title": "Musinsa Black Friday 2026: Top 4 Korean Winter Outerwear & Puffer Jacket Steals",
      "summary": "Beat the December chill with Musinsa's biggest Black Friday outerwear drop—MTR cashmere coats, city puffers, and leather jackets.",
      "description": "Korea's leading fashion platform Musinsa is running its peak winter Black Friday event. Here are the 4 essential coats and puffers to grab before sizes run out.",
      "tasteReview": [
        "Vetted top coats and down puffers from Korea's #1 fashion marketplace",
        "Critical sizing advice before December sellouts hit popular L/XL inventory",
        "Direct Musinsa Curator link attached for exclusive member pricing"
      ],
      "tips": "Midnight coupon resets offer the deepest stackable discounts. Pre-load your cart before 12 AM."
    },
    "ja": {
      "title": "2026ムシンサ（MUSINSA）ブラックフライデー：本命アウター＆ダウンBEST 4",
      "summary": "本格的な寒波が来る前に手に入れるべきムシンサ黒金セール特集。名作MTRバルマカーンコートからショートダウンまで徹底解説。",
      "description": "韓国No.1ファッションEC「ムシンサ」の冬のメガブラックフライデー。完売前に抑えるべきおすすめアウター4選をまとめました。",
      "tasteReview": [
        "ムシンサランキング1位のMTRウールコートと軽量ダウンを厳選",
        "本格的な冬を迎える前のゴールデンサイズ先取りガイド",
        "ムシンサ公式キュレーターリンク搭載"
      ],
      "tips": "深夜0時に限定クーポンがリセットされます。お気に入りは事前にカートへ。"
    },
    "zh": {
      "title": "2026韩国Musinsa黑五大促终极战报：必抢羊毛大衣与羽绒服TOP4",
      "summary": "赶在寒潮前锁定Musinsa黑五王牌外套：MTR羊毛插肩大衣、极简短款羽绒服与复古皮衣折扣首发。",
      "description": "韩国第一潮牌平台Musinsa黑五大促正式打响。为你盘点断码前必须加购的四大镇店之宝冬装外套。",
      "tasteReview": [
        "韩国本土断货王MTR羊毛大衣与白鸭绒短羽绒服精选",
        "避开12月大断码，提前锁定黄金尺码实操建议",
        "内置Musinsa官方分销通道，一键直达折扣页面"
      ],
      "tips": "韩国时间零点刷新大额随机折扣券，提前加购是抢到黄金码的关键。"
    }
  }
}

target_posts = [post1, post2, post3]

for p in target_posts:
    slug = p["slug"]
    check_url = f"{SUPABASE_URL}/rest/v1/posts?slug=eq.{slug}&select=id"
    req = urllib.request.Request(check_url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            existing = json.loads(resp.read().decode("utf-8"))
            if existing:
                up_url = f"{SUPABASE_URL}/rest/v1/posts?id=eq.{existing[0]['id']}"
                payload = json.dumps({"data": p}).encode("utf-8")
                urllib.request.urlopen(urllib.request.Request(up_url, data=payload, headers=headers, method="PATCH"))
                print(f"[+] Updated dedicated post: {slug}")
            else:
                p_url = f"{SUPABASE_URL}/rest/v1/posts"
                payload = json.dumps({"slug": slug, "data": p}).encode("utf-8")
                urllib.request.urlopen(urllib.request.Request(p_url, data=payload, headers=headers, method="POST"))
                print(f"[+] Inserted dedicated post: {slug}")
    except Exception as e:
        print(f"[-] Error with {slug}: {e}")

try:
    urllib.request.urlopen(urllib.request.Request(REVALIDATE_URL))
    print("[+] Revalidated Vercel cache successfully!")
except Exception as e:
    print(f"[-] Revalidate error: {e}")
