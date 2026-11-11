#!/usr/bin/env python3
"""
Upload 4 High-Density SEO Curation Posts to Supabase k-blog
Topics:
1. CU 모찌 파베 초콜릿 말차맛 (편의점 떡 디저트 1위)
2. GS25 x 설빙 피자설기 (11월 5일 전국 출시 냉동 떡 디저트)
3. 올리브영 토리든 다이브인 저분자 히알루론산 세럼 리필 기획 (올영 세럼 1위)
4. 무신사 스탠다드 MTR 오버사이즈 발마칸 코트 (겨울 싱글 코트 랭킹 1위)
"""

import json
import urllib.request
import urllib.error

SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptdXFtdnh1YnV3aG9vY3Vrbm50Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDMwODA3NywiZXhwIjoyMTA5ODg0MDc3fQ.ELyAmyRJrWdQoIHRu4thMGvjAnjJfVZ4S8Cfpb9MiDY"
REVALIDATE_URL = "https://www.k-trand.store/api/revalidate?secret=kblog2026"

seo_products = [
  {
    "id": "cu-matcha-pave-mochi-202611",
    "slug": "cu-matcha-pave-chocolate-mochi-review",
    "category": "convenience-food",
    "store": "CU",
    "priceKrw": 4500,
    "releaseDate": "2026-10-22",
    "rating": 4.9,
    "imageUrl": "/images/products/cu-matcha-pave-mochi.jpg",
    "affiliateUrl": "https://link.coupang.com/example-cu-mochi",
    "affiliatePlatform": "ConvenienceStore",
    "i18n": {
      "ko": {
        "title": "CU 신상 디저트 \"모찌 파베 초콜릿 말차맛\" 솔직 후기 · 가격 · 칼로리",
        "summary": "SNS 누적 200만 뷰 '생초코 모찌' 40만 개 완판 돌풍을 잇는 후속작! 쫀득한 모찌와 꾸덕한 말차 파베 초콜릿의 2중 식감",
        "description": "편의점 디저트 시장에서 '떡지순례' 신드롬을 일으킨 CU의 최고 기대작입니다. 출시 한 달 만에 40만 개를 돌파한 생초코 모찌의 후속 제품으로, 얇고 차진 모찌 피 속에 쌉싸름한 제주 말차 가루와 진한 화이트 파베 초콜릿을 황금 비율로 배합했습니다. 한 입 베어 물면 치아 자국이 선명하게 남을 정도로 묵직하고 꾸덕한 파베 초콜릿의 밀도감과 모찌 특유의 차진 탄력이 입안 가득 감돕니다. 전문 쇼콜라티에 카페 수준의 농후한 맛을 4,500원이라는 합리적인 가격에 구현했습니다.",
        "tasteReview": [
          "단맛만 앞서는 저가 초콜릿과 달리 첫맛은 쌉싸래한 말차 향이 치고 올라오며 끝맛은 고소한 유크림 풍미로 마무리",
          "포크가 묵직하게 들어갈 만큼 밀도 높은 생초콜릿과 얇고 투명한 모찌 피의 극대화된 대비감",
          "아메리카노나 무가당 말차 라떼와 페어링 시 텁텁함 없이 고급스러운 애프터눈 티 디저트로 완성"
        ],
        "tips": "냉장 보관 직후 차가운 상태에서 드셔야 파베 초콜릿 본연의 꾸덕한 식감이 극대화됩니다. 포켓CU 앱에서 '모찌 파베'를 검색해 재고를 미리 확인 후 방문하는 것을 권장합니다."
      },
      "en": {
        "title": "CU Korea Viral Dessert \"Matcha Pave Chocolate Mochi\" Review & Taste Test",
        "summary": "The smash-hit follow-up to Korea's 400,000-unit sold Raw Choco Mochi! Chewy rice cake shell meets decadent Jeju matcha ganache.",
        "description": "Following the viral phenomenon of CU's raw chocolate mochi series which racked up over 2 million views on TikTok and Instagram, Korea's top convenience chain officially introduced the 'Matcha Pave Chocolate Mochi'. Encased in an ultra-thin, translucent glutinous rice cake layer, the filling consists of velvety dense pave ganache infused with authentic bittersweet Jeju green tea. The texture is so rich that teeth leave distinct marks, delivering a high-end patisserie experience at an accessible 4,500 KRW ($3.20 USD).",
        "tasteReview": [
          "Authentic earthy matcha bitterness balances the sweet rich cocoa butter base without artificial coloring",
          "Noticeable textural contrast between the elastic mochi skin and thick, fudge-like ganache",
          "Perfect pairing with iced Americano or hot roasted green tea"
        ],
        "tips": "Best enjoyed immediately out of the refrigerated section for maximum ganache firmness. Available exclusively at CU convenience stores across South Korea."
      },
      "ja": {
        "title": "韓国CU最新スイーツ「抹茶生チョコ餅」実食レビュー・カロリー・価格情報",
        "summary": "発売1ヶ月で40万個突破の「生チョコ餅」後継作！極薄もちもち求肥と濃厚な宇治風抹茶生チョコの絶妙な2層ハーモニー",
        "description": "韓国SNSで総再生数200万回を超え、コンビニ和洋折衷スイーツブームを牽引するCUの最新作です。大ヒットした生チョコ餅シリーズに続き、ほろ苦い特選抹茶とホワイト生チョコを凝縮した贅沢仕立て。歯形がくっきり残るほど密度の高い生チョコレートと、薄く柔らかいお餅の弾力が一口で口いっぱいに広がります。専門店クオリティの贅沢な味わいを4,500ウォンで手軽に楽しめます。",
        "tasteReview": [
          "甘すぎず、抹茶本来のほろ苦い香りと生クリームの深いコクがしっかりと香る大人向けの味わい",
          "フォークが沈み込むほど濃厚なパヴェチョコレートと弾力ある薄皮もちのコントラスト",
          "ブラックコーヒーや無糖茶と相性抜群で、お土産・旅行中の夜食スイーツとしても大人気"
        ],
        "tips": "常温に置かず、冷蔵庫から取り出して冷たい状態で食べると生チョコのねっとり濃厚な食感が際立ちます。Pocket CUアプリで在庫検索が可能です。"
      },
      "zh": {
        "title": "韩国CU便利店爆款甜品“抹茶生巧麻薯”真实测评·价格·口感",
        "summary": "全网爆卖40万个的生巧大福升级版！Q弹糯米薄皮包裹浓郁微苦抹茶生巧克力，口感层次极佳",
        "description": "引领韩国便利店“糯米糕巡礼”热潮的CU最新力作。在创下单月狂销40万个纪录的生巧大福基础上，全新推出这款“抹茶生巧麻薯”。外层采用晶莹剔透、韧性十足的传统糯米薄皮，内馅则是厚实绵密的济州岛抹茶风味生巧克力。咬下一口能清晰留下齿印，生巧的微苦茶香与浓醇乳脂在舌尖慢慢融化，定价仅4,500韩元（约合人民币23元）。",
        "tasteReview": [
          "纯正抹茶茶香扑鼻，微苦回甘，彻底摆脱廉价代可可脂的甜腻感",
          "叉子戳入时能明显感受到生巧的高密度质地与Q弹外皮的韧劲反差",
          "搭配无糖美式咖啡堪称完美的韩式下午茶体验"
        ],
        "tips": "建议在冷藏温度下直接品尝，切勿微波加热，冰凉紧实的生巧口感最为正宗。赴韩旅游者可在任意CU便利店冷藏甜点区找到。"
      }
    }
  },
  {
    "id": "gs25-sulbing-pizzaseolgi-202611",
    "slug": "gs25-sulbing-pizza-ricecake-review",
    "category": "convenience-food",
    "store": "GS25",
    "priceKrw": 3900,
    "releaseDate": "2026-11-05",
    "rating": 4.8,
    "imageUrl": "/images/products/gs25-sulbing-pizzaseolgi.jpg",
    "affiliateUrl": "https://link.coupang.com/example-gs25-pizza",
    "affiliatePlatform": "ConvenienceStore",
    "i18n": {
      "ko": {
        "title": "GS25 x 설빙 신상 \"피자설기\" 전국 출시 실구매 후기 · 조리법 · 맛 분석",
        "summary": "11월 5일 전국 점포 전격 출시! 설빙과의 이색 콜라보로 사전예약 5,000개 완판을 기록한 냉동 백설기 피자 토핑 디저트",
        "description": "전통 백설기와 이탈리안 피자 토핑이 만난 GS25의 11월 공식 신상품입니다. 디저트 전문 브랜드 '설빙'과 협업하여 개발되었으며, 떡이 냉장 보관 시 딱딱해지는 전분 노화 현상을 막기 위해 영하 18도 급속 냉동 방식을 채택했습니다. 뽀얀 쌀 백설기 베이스 위에 상큼한 토마토 피자 소스, 자연산 모짜렐라 피자치즈, 짭조름한 페퍼로니 슬라이스, 톡톡 터지는 스위트콘을 얹었습니다. 전자레인지에 데우면 백설기의 은은한 단맛과 치즈의 짭짤한 풍미가 단짠 조합을 이룹니다. 총 130g(65g 2개입)에 3,900원입니다.",
        "tasteReview": [
          "밀가루 피자 도우 대신 쫄깃하고 폭신한 백설기가 소스를 머금어 색다른 떡피자 식감 선사",
          "모짜렐라 치즈가 길게 늘어나며 옥수수 콘과 페퍼로니가 씹히는 정통 콤비네이션 피자의 맛",
          "개별 포장 2개입 구성으로 간단한 간식이나 아이들 영양 간식, 가벼운 맥주 안주로 제격"
        ],
        "tips": "포장지를 살짝 뜯은 후 전자레인지(700W) 기준 1분~1분 20초 데운 뒤 30초간 뜸을 들이면 치즈가 골고루 녹아 가장 쫀득합니다."
      },
      "en": {
        "title": "GS25 x Sulbing Korea \"Pizza Seolgi\" Viral Rice Cake Snack Review",
        "summary": "Officially launched nationwide Nov 5! 5,000 pre-orders sold out in days. Traditional Korean Baekseolgi topped with pepperoni, mozzarella & sweet corn.",
        "description": "An innovative crossover between Korean dessert giant Sulbing and GS25 convenience chain, hitting stores nationwide on November 5, 2026. Replacing traditional wheat dough with chewy Korean steamed white rice cake (Baekseolgi), it features rich marinara sauce, stretchable mozzarella cheese, savory pepperoni, and sweet corn. Flash-frozen to preserve moisture, it reheats into a piping hot sweet-and-savory comfort snack in just 70 seconds. Priced at 3,900 KRW for a pack of two (130g total).",
        "tasteReview": [
          "Unique contrast of subtle sweetness from steamed rice cake combined with savory melted cheese and tomato sauce",
          "Bouncy, chewy texture that offers a surprisingly satisfying alternative to conventional pizza pockets",
          "Convenient twin-pack portioning makes it an ideal late-night snack with craft beer"
        ],
        "tips": "Microwave for 1 minute 15 seconds at 700W. Let it rest for 30 seconds before eating to allow the cheese to fully melt over the rice cake."
      },
      "ja": {
        "title": "韓国GS25×ソルビン「ピザソルギ」全国発売レビュー・電子レンジ調理法",
        "summary": "11月5日全国発売！有名カフェ「ソルビン」監修、予約販売5000個即完売の冷凍ピザ風伝統白餅スイーツ",
        "description": "韓国の有名かき氷・伝統デザートカフェ「ソルビン」とコンビニ大手GS25がタッグを組んだ話題作です。通常の小麦ピザ生地の代わりに伝統的な蒸し米餅「ペクソルギ」を使用。トマトピザソース、とろけるモッツァレラチーズ、ペパロニ、スイートコーンをトッピングし急速冷凍しました。電子レンジで温めるだけで、ふっくらモチモチしたお米の自然な甘みと、濃厚チーズの塩気が絶妙な「甘じょっぱ（タンッチャン）」を演出します。2個入り（130g）3,900ウォン。",
        "tasteReview": [
          "小麦粉ピザとはひと味違う、韓国伝統餅ならではのムチムチ・ふわふわな噛みごたえ",
          "しっかり伸びるチーズとペパロニの香ばしさがマッチした本格ピザの風味",
          "個包装で2個入りのため、旅行中のホテルでの手軽な夜食にも最適"
        ],
        "tips": "袋の端を少し切り、電子レンジ（700W）で約1分10秒加熱。加熱後30秒置くと余熱でチーズがとろりと馴染みます。"
      },
      "zh": {
        "title": "韩国GS25联名雪冰“披萨雪糕白条糕”测评·微波炉加热指南·口感分析",
        "summary": "11月5日全韩上市！预售5000份秒空的冷冻创新米糕，传统白条糕与意式披萨芝士火腿的完美跨界",
        "description": "韩国GS25便利店携手甜品巨头“雪冰（Sulbing）”于2026年11月5日正式推出的冷冻跨界美食。突破性地用韩国传统蒸米糕“白条糕（Baekseolgi）”替代传统面粉饼底，表面铺满浓郁番茄披萨酱、拉丝马苏里拉芝士、意式辣香肠片和甜玉米粒。采用速冻工艺锁住米香软糯，微波炉叮1分钟即可享受到外拉丝、内香甜的绝妙咸甜风味。一盒2袋共130g，售价3,900韩元（约合人民币20元）。",
        "tasteReview": [
          "软糯微甜的传统米香与咸香浓郁的马苏里拉芝士融合，咸甜交织极具辨识度",
          "芝士拉丝效果出众，玉米粒与香肠增添了丰富的咀嚼层次",
          "独立双份包装，非常适合作为深夜追剧小吃或简易早餐"
        ],
        "tips": "包装撕开小口后放入微波炉，700W高火加热1分10秒，取出静置半分钟让芝士均匀融化拉丝效果最佳。"
      }
    }
  },
  {
    "id": "oliveyoung-torriden-divein-serum-202611",
    "slug": "oliveyoung-torriden-divein-serum-refill-set",
    "category": "k-beauty",
    "store": "Olive Young",
    "priceKrw": 27000,
    "releaseDate": "2026-11-01",
    "rating": 4.9,
    "imageUrl": "/images/products/oliveyoung-torriden-divein-serum.jpg",
    "affiliateUrl": "https://link.coupang.com/example-torriden",
    "affiliatePlatform": "OliveYoung",
    "i18n": {
      "ko": {
        "title": "올리브영 1위 \"토리든 다이브인 저분자 히알루론산 세럼 리필 기획\" 성분 및 속보습 효과",
        "summary": "5년 연속 올리브영 어워즈 에센스/세럼 1위! 본품 50ml + 친환경 리필팩 50ml 구성의 겨울철 속건조 구원템",
        "description": "한국 올리브영 스킨케어 랭킹에서 독보적인 판매량을 유지하는 수분 세럼의 정석입니다. 크기가 다른 5가지 복합 저분자 히알루론산(5D Hyaluronic Acid)이 각질층 깊숙이 수분을 층층이 채워 속당김을 근본적으로 개선합니다. 판테놀, 알란토인, 마데카소사이드 진정 성분이 배합되어 있으며, 천연 말라카이트 추출물로 은은한 파스텔 블루빛을 띱니다. 끈적임이나 밀림 없이 산뜻하게 스며들어 메이크업 전후 사계절 데일리 에센스로 최적화되었습니다. 본품 50ml에 에코 리필 파우치 50ml가 결합된 11월 올리브영 한정 기획 세트입니다.",
        "tasteReview": [
          "물처럼 가볍게 퍼지면서 바르는 즉시 속당김이 잡히는 오일 프리 고수분 포뮬러",
          "파운데이션이나 선크림 전에 2~3회 덧발라도 밀림이나 들뜸 없는 완벽한 메이크업 밀착력",
          "무향, 무자극, 화해 20가지 유해성분 0개로 여드름성·극민감성 피부도 안심 사용"
        ],
        "tips": "세안 직후 토너 전 퍼스트 에센스로 손바닥에 2~3방울 떨어뜨려 흡수시키면 부스팅 효과가 탁월합니다. 올리브영 오프라인 매장에서 즉시 텍스처 테스트가 가능합니다."
      },
      "en": {
        "title": "Olive Young No.1 Hydration Serum \"Torriden DIVE-IN Low Molecular Hyaluronic Acid\" Review",
        "summary": "5-year consecutive Olive Young Awards winner! Value duo set including 50ml serum bottle plus 50ml eco-refill pouch for severe winter dryness.",
        "description": "Regarded as the undisputed holy grail of Korean hydrating serums, Torriden DIVE-IN Low Molecular Hyaluronic Acid Serum consistently tops the sales charts across all Olive Young stores nationwide. Formulated with a proprietary 5D complex of multi-weight hyaluronic acid molecules, it penetrates deeply into the dermis rather than sitting slick on the surface. Infused with D-panthenol, allantoin, and madecassoside, its natural pastel-blue hue originates from malachite extract. Oil-free, fragrance-free, and thoroughly non-comedogenic, it preps skin with an instant glass-skin glow without stickiness.",
        "tasteReview": [
          "Weightless watery gel texture absorbs in seconds without greasy residue or heaviness",
          "Layerable formula that layers seamlessly under makeup without pilling or silicone slipping",
          "Clinically proven 48-hour moisture retention with EWG green grade clean beauty certification"
        ],
        "tips": "Apply 2-3 drops onto damp skin immediately after cleansing for optimal moisture trapping. Tourists can claim an instant tax refund at airport kiosks or major Olive Young flagship counters."
      },
      "ja": {
        "title": "オリーブヤング1位「トリデン(Torriden) ダイブイン低分子ヒアルロン酸セラム」保湿成分レビュー",
        "summary": "5年連続オリーブヤングアワード受賞の殿堂入り美容液！本品50ml＋詰替え用50mlの限定ダブル企画セット",
        "description": "韓国コスメを代表する水分チャージ美容液の代名詞。分子量の異なる5重低分子ヒアルロン酸が角質層の奥深くまで浸透し、インナードライや冬の乾燥肌を根本からケアします。パンテノール、アラントイン、ツボクサエキス配合で肌荒れを穏やかに鎮静。天然マラカイト抽出物による爽やかなスカイブルーのテクスチャーが特徴です。ベタつきゼロのサラッとした浸透感で、朝のメイク前スキンケアにも最適です。",
        "tasteReview": [
          "水のようにみずみずしく広がり、肌にぐんぐん吸い込まれるような抜群の浸透スピード",
          "ファンデーションの前に重ね塗りしてもポロポロとヨレない高密着モイスチャー処方",
          "無香料・弱酸性・20種の注意成分フリーで敏感肌やニキビ肌でも安心して使える低刺激性"
        ],
        "tips": "洗顔後すぐのブースター美容液として2〜3滴ハンドプレスするのが最も効果的。オリーブヤング明洞・江南店で免税（即時Tax Free）適用可能です。"
      },
      "zh": {
        "title": "Olive Young断货王“Torriden低分子玻尿酸深层补水精华”成分与使用效果",
        "summary": "连续5年斩获Olive Young大赏第一名！正装50ml加赠50ml环保替换装，秋冬换季深层锁水必备神物",
        "description": "长期占据韩国Olive Young全店护肤榜榜首的“国民补水精华”。核心采用5D多重复合微分子玻尿酸体系，分子量逐级渗透直达角质层深处，有效缓解外油内干及脱皮紧绷。配合泛醇（B5）、尿囊素及积雪草活性精粹，淡淡的浅天蓝色来自天然孔雀石提取物。质地水润清透，零油脂、零香精，吸收迅速且完全不黏腻，能瞬间抚平干纹，为后续底妆提供服帖平滑的肌底状态。",
        "tasteReview": [
          "仿若纯净水滴的轻盈水凝质感，拍开后几秒内迅速被肌肤吃透",
          "妆前连涂2层也不会出现任何搓泥现象，显著提升粉底服帖度与光泽感",
          "全绿无添加配方，温和弱酸性，敏感肌及医美术后修护均可放心使用"
        ],
        "tips": "洁面后趁皮肤微湿时取2-3滴轻按全脸，补水抓水效果翻倍。在韩国大型Olive Young专卖店购买可享即时免税退税。"
      }
    }
  },
  {
    "id": "musinsa-mtr-balmacaan-coat-202611",
    "slug": "musinsa-standard-mtr-oversized-balmacaan-coat-review",
    "category": "k-fashion",
    "store": "Musinsa Standard",
    "priceKrw": 269890,
    "releaseDate": "2026-10-15",
    "rating": 4.9,
    "imageUrl": "/images/products/musinsa-mtr-balmacaan-coat.jpg",
    "affiliateUrl": "https://musinsa.com/products/2682035",
    "affiliatePlatform": "Musinsa",
    "i18n": {
      "ko": {
        "title": "무신사 코트 랭킹 1위 \"무신사 스탠다드 MTR 오버사이즈 발마칸 코트\" 실측 핏 · 울 혼용률 후기",
        "summary": "겨울 싱글 코트 부문 평점 4.9점 1위! 이탈리아 명품 패브릭 MTR사 프리미엄 울 75% 원단의 A라인 실루엣 발마칸",
        "description": "무신사 스탠다드의 프리미엄 라인을 대표하는 겨울 시즌 시그니처 코트입니다. 막스마라, 산드로 등 글로벌 컨템포러리 브랜드가 애용하는 이탈리아 명문 방직사 'MTR'의 24온스 헤비 울 패브릭(울 75%, 폴리아미드 20%, 캐시미어 5%)을 아낌없이 사용했습니다. 부드러운 터치감과 유려한 드레이프성이 돋보이며, 여유로운 레글런 슬리브와 유려하게 떨어지는 세미 오버핏 A라인 실루엣이 클래식하면서도 트렌디한 감성을 연출합니다. 소매 비죠 버클과 히든 버튼 플래킷 디테일로 완성도를 높였으며, 정가 299,900원에서 시즌 쿠폰 적용 시 26만 원대 구매 가능합니다.",
        "tasteReview": [
          "MTR 원단 특유의 은은한 윤기와 묵직하게 떨어지는 유려한 무게감이 저가 울 코트와 확연히 차별화",
          "레글런 어깨 라인 설계로 체형에 구애받지 않고 두터운 니트나 수트 재킷 위에 레이어드해도 자연스러운 실루엣",
          "발목 위까지 단정하게 떨어지는 롱 기장과 든든한 방풍 보온성으로 한겨울까지 착용 가능"
        ],
        "tips": "정사이즈 선택 시 자연스러운 세미 오버핏이 연출됩니다. 깃을 세워 목 비죠 단추를 채우면 트렌디한 하이넥 스탠드 칼라 스타일로 연출할 수 있습니다."
      },
      "en": {
        "title": "Musinsa Korea Winter Best \"MTR Oversized Balmacaan Coat\" Review & Fabric Sizing",
        "summary": "Ranked #1 with a 4.9/5 rating! Crafted from premium 24oz Italian MTR wool blend with a relaxed A-line raglan drape.",
        "description": "The flagship luxury piece from Musinsa Standard's upscale winter collection, dominating the men's outerwear category across South Korea. Made with authentic 24oz luxury coating fabric sourced directly from Italy's renowned Manifattura Tessile Risorti (MTR) mill—a blend of 75% virgin wool, 20% polyamide, and 5% cashmere. Featuring a flowing raglan sleeve shoulder, concealed horn button placket, and adjustable cuff tabs, it offers an effortlessly chic silhouette that complements both tailored suits and streetwear. Retails for 269,890 KRW (~$195 USD) after seasonal discounts.",
        "tasteReview": [
          "Subtle cashmere-like sheen and substantial structural drape that holds its tailored shape in windy weather",
          "Generously cut raglan shoulders provide comfortable layering over chunky knitwear without shoulder bunching",
          "Contemporary below-the-knee length creates a sleek, elongated profile"
        ],
        "tips": "True to size for a relaxed contemporary fit. Turn up the collar and fasten the throat latch for a sharp military-inspired high-neck look."
      },
      "ja": {
        "title": "韓国ムシンサ1位「MTRオーバーサイズバルマカーンコート」実測サイズ感・ウール質感解説",
        "summary": "冬のシングルコート部門レビュー4.9点堂々1位！イタリア名門MTR社製プレミアムウールを使用した極上Aラインコート",
        "description": "韓国最大のファッショントレンドを牽引するムシンサ・スタンダードのプレミアムライン代表作です。マックスマーラなど高級メゾンが採用するイタリア名門織物メーカー「MTR社」の24オンス上質ウール混紡生地（ウール75％、ポリアミド20％、カシミヤ5％）を贅沢に使用。ラグランスリーブによる滑らかな肩の落ち感と、歩くたびに美しく揺れるセミオーバーサイズのAラインシルエットが魅力です。袖口のアジャスターベルトや比翼仕立ての隠しボタンなど細部までこだわり抜かれています。セール時約26万ウォン台で購入可能。",
        "tasteReview": [
          "MTR社ファブリックならではの品のある艶感と、型崩れしない適度な重厚感が安価なコートと一線を画す高級感",
          "肩幅を選ばないラグランスリーブ構造で、厚手ニットやジャケットの上から羽織っても窮屈感ゼロ",
          "膝下まで届くエレガントなロング丈で、真冬でも風を通さず抜群の保温性を発揮"
        ],
        "tips": "普段着用サイズを選ぶだけで綺麗なオーバーサイズシルエットが完成します。襟を立ててチンストラップを留めるとモードなスタンドカラーに変身します。"
      },
      "zh": {
        "title": "Musinsa韩国男装销量榜首“MTR落肩巴尔马肯大衣”版型实测与面料细节",
        "summary": "冬季单排扣大衣评分4.9分断层第一！采用意大利顶级MTR毛纺厂75%重磅羊毛，展现流畅A字廓形",
        "description": "韩国潮流平台Musinsa自营高端线“Musinsa Standard”的冬季门面之作。精选意大利百年名厂MTR出品的24盎司重磅羊毛呢料（含75%初剪羊毛、20%聚酰胺、5%羊绒），触感温润柔滑，兼具极佳的悬垂垂坠感与挺括保暖度。采用经典的落肩插肩袖剪裁与隐形暗门襟设计，下摆自然舒展呈优雅微A字型，无论是内搭正装西装还是连帽卫衣均能轻松驾驭。活动到手价约26.9万韩元（约合人民币1,420元）。",
        "tasteReview": [
          "MTR面料自带微光泽感与扎实的分量，垂坠飘逸且不易起球起皱",
          "插肩袖版型完美修饰肩线，内搭厚毛衣也不会显得臃肿笨拙",
          "过膝长款设计兼顾防风保暖与拉长身形的视觉比例"
        ],
        "tips": "建议按日常正码选购即可呈现松弛有度的韩系廓形感；领口配有防风领袢，扣上即可切换利落帅气的高领立领造型。"
      }
    }
  }
]

def main():
    print(f"[*] Uploading {len(seo_products)} High-Density SEO posts to Supabase...")
    
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }

    inserted_count = 0
    for product in seo_products:
        slug = product["slug"]
        
        # Check if already exists
        check_url = f"{SUPABASE_URL}/rest/v1/posts?slug=eq.{slug}&select=id"
        req = urllib.request.Request(check_url, headers=headers)
        try:
            with urllib.request.urlopen(req) as resp:
                existing = json.loads(resp.read().decode("utf-8"))
                if existing:
                    print(f"[-] Slug '{slug}' already exists (ID: {existing[0]['id']}). Updating...")
                    update_url = f"{SUPABASE_URL}/rest/v1/posts?id=eq.{existing[0]['id']}"
                    update_payload = json.dumps({"data": product}).encode("utf-8")
                    up_req = urllib.request.Request(update_url, data=update_payload, headers=headers, method="PATCH")
                    with urllib.request.urlopen(up_req) as up_resp:
                        print(f"    [+] Updated post {existing[0]['id']}: {slug}")
                    inserted_count += 1
                    continue
        except Exception as e:
            print(f"[-] Check error for {slug}: {e}")

        # Insert new
        post_url = f"{SUPABASE_URL}/rest/v1/posts"
        payload = json.dumps({
            "slug": slug,
            "data": product
        }).encode("utf-8")
        
        req = urllib.request.Request(post_url, data=payload, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
                new_id = res_data[0]["id"] if res_data else "unknown"
                print(f"[+] Inserted post ID {new_id}: {slug}")
                inserted_count += 1
        except urllib.error.HTTPError as e:
            print(f"[-] Failed inserting {slug}: {e.code} {e.read().decode('utf-8')}")
        except Exception as e:
            print(f"[-] Failed inserting {slug}: {e}")

    print(f"\n[*] Total {inserted_count} SEO posts successfully processed in Supabase.")

    # Revalidate Next.js cache
    print(f"[*] Triggering Vercel on-demand ISR revalidation: {REVALIDATE_URL}")
    try:
        rev_req = urllib.request.Request(REVALIDATE_URL)
        with urllib.request.urlopen(rev_req, timeout=10) as resp:
            print("[+] Revalidation response:", json.loads(resp.read().decode("utf-8")))
    except Exception as e:
        print(f"[-] Revalidation failed: {e}")

if __name__ == "__main__":
    main()
