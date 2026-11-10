import json
import urllib.request

SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptdXFtdnh1YnV3aG9vY3Vrbm50Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDMwODA3NywiZXhwIjoyMTA5ODg0MDc3fQ.ELyAmyRJrWdQoIHRu4thMGvjAnjJfVZ4S8Cfpb9MiDY"

real_products = [
  {
    "id": "cu-rescene-kimchi-pork-lunchbox-202611",
    "slug": "cu-rescene-kimchi-pork-lunchbox",
    "category": "convenience-food",
    "store": "CU",
    "priceKrw": 5900,
    "releaseDate": "2026-11-10",
    "rating": 4.9,
    "imageUrl": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800&auto=format&fit=crop",
    "affiliateUrl": "https://link.coupang.com/example-cu-rescene",
    "affiliatePlatform": "ConvenienceStore",
    "i18n": {
      "ko": {
        "title": "CU 신상 도시락 \"리센느 덕연이 딸 김치제육\" 실구매 후기",
        "summary": "2026년 11월 10일 전국 출시! 걸그룹 리센느 원이 어머니의 손맛 레시피를 담은 정통 집밥 제육 도시락",
        "description": "걸그룹 리센느(RESCENE)와 협업해 11월 10일 정식 출시된 CU의 화제작입니다. 멤버 원이 어머니의 가정식 손맛 레시피를 그대로 살려 매콤달콤한 김치제육볶음과 비엔나소시지 야채볶음, 달콤 짭조름한 감자조림, 부드러운 계란말이를 정갈하게 담았습니다. 한정판 원이 포토카드 15종 중 1종이 랜덤 동봉되어 출시 당일 점심시간부터 품절 대란을 빚고 있습니다.",
        "tasteReview": [
          "김치와 돼지고기 앞다리살이 큼직하게 볶아져 인스턴트 특유의 텁텁함 없이 깔끔한 칼칼함",
          "밥 위에 올려진 계란지단과 소시지, 감자조림까지 집에서 챙겨준 도시락 같은 푸짐한 반찬 구성",
          "5,900원 가격에 퀄리티 높은 포토카드까지 포함되어 가성비·팬심 모두 만족"
        ],
        "tips": "포켓CU 앱의 '재고 조회' 및 '픽업 예약' 기능을 이용하면 헛걸음하지 않고 당일 픽업할 수 있습니다. 뚜껑을 벗기고 전자레인지에 2분간 데우면 갓 지은 밥맛이 납니다."
      },
      "en": {
        "title": "CU Convenience Store Korea Viral \"RESCENE Kimchi Pork Lunchbox\" Review",
        "summary": "Released Nov 10, 2026! Homestyle Korean Kimchi Pork Stir-fry Bento made with K-pop girl group RESCENE Woni's mother recipe.",
        "description": "A viral collaboration between K-pop rookie sensations RESCENE and Korea's top convenience chain CU, officially hitting shelves nationwide on November 10, 2026. Inspired by the homestyle cooking of member Woni's mother, this hearty dosirak features tender spicy stir-fried pork with aged kimchi, sweet braised baby potatoes, sausage veggies, and rolled egg omelet. Each lunchbox includes 1 of 15 exclusive collectible photo cards.",
        "tasteReview": [
          "Real aged kimchi tartness balances the savory glazed pork shoulder without artificial aftertaste",
          "Generous side dishes evoke the authentic feel of a warm home-cooked meal in Seoul",
          "Outstanding value at 5,900 KRW ($4.20 USD) for a full meal plus limited K-pop merch"
        ],
        "tips": "Check the PocketCU mobile app for real-time inventory at neighborhood stores. Microwave for 2 minutes at 700W without the clear lid."
      },
      "ja": {
        "title": "韓国CU新作「RESCENE ウォニ母の家庭料理 キムチ豚炒め弁当」実食レポート",
        "summary": "2026年11月10日全国発売！人気ガールズグループRESCENEコラボ、母の手作り味を再現した本格お弁当。",
        "description": "韓国コンビニ大手CUが2026年11月10日に発売した注目の最新弁当。第5世代ガールズグループRESCENEのメンバー・ウォニの実母の特製家庭料理レシピをそのままお弁当に仕立てました。熟成キムチと豚肉のピリ辛炒め（チェユクポックム）をメインに、ウィンナー炒め、じゃがいもの甘辛煮、卵焼きがぎっしり詰まっています。ウォニの限定フォトカード（全15種からランダム1枚）入りです。",
        "tasteReview": [
          "酸味の効いた古漬けキムチと柔らかい豚肉が絶品で、白ご飯が進む本格的な辛旨テイスト",
          "コンビニ弁当とは思えないほど手作り感あふれる温かみのあるおかずの数々",
          "5,900ウォンとお手頃ながらフォトカード付きで現地ファンにも大人気"
        ],
        "tips": "韓国旅行中に購入する際は、公式アプリ「PocketCU」で最寄り店舗の在庫をチェックするのがおすすめです。"
      },
      "zh": {
        "title": "韩国CU便利店11月重磅新品“RESCENE女团妈妈风味 泡菜炒猪肉便当”实吃测评",
        "summary": "2026年11月10日全韩上市！人气五代女团RESCENE合作款，复刻妈妈牌温情家常便当。",
        "description": "韩国CU便利店于2026年11月10日正式推出的顶流联名便当！以新晋女团RESCENE成员Woni母亲的私房家常菜谱为灵感，主打香辣浓郁的老泡菜炒猪五花肉，搭配香肠、韩式土豆小菜和厚蛋烧，营养丰盛。每份便当随机附赠Woni限定小卡1张（全套15款），上市首日便在首尔各大高校商圈引发抢购热潮。",
        "tasteReview": [
          "酸甜适口的正宗老泡菜完美中和肉香，微辣爽口，超级下饭",
          "配菜种类丰富，口感温润，真正还原了首尔家庭手作便当的温度",
          "5,900韩元（约合31元人民币）兼顾美味饱腹与正版爱豆周边收集"
        ],
        "tips": "建议使用PocketCU App提前查询附近门店库存并预约自提；微波炉揭盖中火加热2分钟口感最佳。"
      }
    }
  },
  {
    "id": "gs25-lalasweet-real-greek-apple-bar-202611",
    "slug": "gs25-lalasweet-real-greek-apple-bar",
    "category": "convenience-food",
    "store": "GS25",
    "priceKrw": 3000,
    "releaseDate": "2026-11-02",
    "rating": 4.8,
    "imageUrl": "https://images.unsplash.com/photo-1501443762994-82bd5dace89a?w=800&auto=format&fit=crop",
    "affiliateUrl": "https://link.coupang.com/example-gs25-lalasweet",
    "affiliatePlatform": "ConvenienceStore",
    "i18n": {
      "ko": {
        "title": "GS25 저당 아이스크림 신상 \"라라스윗 리얼그릭 사과 쫀득바\" 솔직 후기",
        "summary": "75kcal, 당류 단 3g! 청송 사과 과즙과 그릭요거트의 쫀득한 만남 (11월 한 달간 1+1)",
        "description": "국내 저당 디저트 1위 브랜드 라라스윗이 GS25 단독으로 11월 첫 주 출시한 과일 그릭요거트 쫀득바입니다. 제철 청송 사과의 싱그러운 과즙에 고단백 그릭요거트를 더해 젤라또처럼 쫀득한 식감을 완성했습니다. 개당 75kcal, 당류 3g에 불과해 겨울철 다이어트 간식이나 식후 디저트로 압도적인 인기를 얻고 있습니다.",
        "tasteReview": [
          "한 입 베어 물면 셔벗이 아니라 쫀득하게 씹히는 밀도 높은 그릭요거트 식감",
          "인공적인 사과향이 아닌 새콤달콤한 생사과 퓨레의 깔끔한 단맛",
          "개당 3,000원이지만 11월 한 달간 1+1 행사로 개당 1,500원 가성비"
        ],
        "tips": "냉동실에서 갓 꺼내 바로 먹으면 단단하므로 상온에 1~2분 정도 두었다가 먹으면 쫀득바 특유의 젤라또 질감이 한층 살아납니다."
      },
      "en": {
        "title": "GS25 Korea New Low-Sugar \"Lalasweet Chewy Greek Apple Ice Bar\" Review",
        "summary": "Only 75 calories & 3g sugar! Tangy Cheongsong apples meet rich chewy Greek yogurt (1+1 promotion all November).",
        "description": "Korea's leading healthy dessert brand Lalasweet launched its latest viral guilt-free treat exclusively at GS25 convenience stores in November 2026. Blending premium Korean Cheongsong apple juice with strained Greek yogurt, it achieves a dense, stretchy gelato-like texture without refined sugar. Packing just 75 kcal and 3g of sugar, it is currently dominating Seoul fitness communities.",
        "tasteReview": [
          "Satisfyingly chewy texture that feels like premium gelato rather than icy popsicles",
          "Natural apple puree delivers crisp tart sweetness without chemical sweetener aftertaste",
          "Exceptional value with the nationwide Buy-1-Get-1-Free event running through November"
        ],
        "tips": "Let sit at room temperature for 90 seconds before taking your first bite for the signature stretchy chew."
      },
      "ja": {
        "title": "韓国GS25新作 低糖アイス「ララスウィート リアルグリークアップルもちもちバー」実食レポ",
        "summary": "わずか75kcal・糖類3g！青松リンゴの果汁と濃厚グリークヨーグルトのもちもち食感アイス（11月中1+1実施）。",
        "description": "韓国のヘルシースイーツ界を牽引するLalasweet（ララスウィート）がGS25限定で発売した2026年11月の新作アイスバー。名産地・青松（チョンソン）の旬のリンゴ果汁と濃厚な水切りギリシャヨーグルトを贅沢に使用。ジェラートのようにもちっと伸びる食感でありながら、1本あたり75kcal・糖類3gと驚異のヘルシーさを実現しています。",
        "tasteReview": [
          "氷っぽさが一切なく、もっちりと濃密なヨーグルトの口当たりが贅沢",
          "もぎたてリンゴのフレッシュな甘酸っぱさが口いっぱいに広がる上品な味",
          "通常3,000ウォンですが11月中は1本買うともう1本無料（1+1）でお得感満点"
        ],
        "tips": "冷凍庫から出して常温で1分ほど待ってから食べると、よりもちもちした食感が楽しめます。"
      },
      "zh": {
        "title": "韩国GS25便利店爆款低卡冰淇淋“Lalasweet苹果希腊酸奶生巧棒”测评",
        "summary": "仅75大卡、糖分仅3g！青松苹果原汁搭配希腊酸奶的绝妙Q弹口感（11月整月享买一送一）。",
        "description": "韩国减脂控糖甜品第一品牌Lalasweet于2026年11月在GS25独家上线的全新水果酸奶棒。精选韩国著名产地青松苹果鲜榨果汁，融入高蛋白浓缩希腊酸奶，咬下去像意式吉拉托一般软糯拉丝。每支热量仅75kcal，糖分低至3g，迅速成为首尔白领与健身爱好者的秋冬最爱低卡甜点。",
        "tasteReview": [
          "完全不是普通冰棍的冰渣感，而是类似浓厚酸奶软糖的独特软糯回弹感",
          "纯正苹果清香伴随酸奶的微酸乳香，甜而不腻，没有廉价代糖味",
          "单支原价3,000韩元，11月全韩国GS25支持1+1活动，折合仅8元人民币一支"
        ],
        "tips": "从冰柜取出后在常温下静置1-2分钟再品尝，Q弹拉丝的口感最佳。"
      }
    }
  },
  {
    "id": "oliveyoung-aestura-atobarrier365-cream-202611",
    "slug": "oliveyoung-aestura-atobarrier365-cream-double-set",
    "category": "k-beauty",
    "store": "Olive Young",
    "priceKrw": 44500,
    "releaseDate": "2026-11-01",
    "rating": 4.9,
    "imageUrl": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=800&auto=format&fit=crop",
    "affiliateUrl": "https://link.coupang.com/example-aestura",
    "affiliatePlatform": "OliveYoung",
    "i18n": {
      "ko": {
        "title": "올리브영 11월 랭킹 1위 \"에스트라 아토베리어365 크림 더블 기획\" 분석",
        "summary": "환절기 속건조 구원템! 세라마이드 캡슐 100시간 보습 장벽 크림 80ml 2개 + 앰플 15ml 증정",
        "description": "2026년 11월 올리브영 어워즈 및 데일리 랭킹 크림 부문 1위를 굳건히 지키고 있는 피부 장벽 전문 브랜드 에스트라의 플래그십 기획 세트입니다. 미세 세라마이드 보습 캡슐이 체온에 부드럽게 녹아들며 피부 지질 장벽을 100시간 동안 빈틈없이 지켜줍니다. 찬바람으로 당기고 각질이 일어나는 민감성 피부의 속건조를 즉각 개선하며, 올리브영 단독으로 80ml 본품 2개와 세라-히알 앰플 15ml를 묶어 44,500원 역대급 혜택가에 판매 중입니다.",
        "tasteReview": [
          "육안으로 보이는 세라마이드 알갱이가 롤링 시 자극 없이 부드럽게 스며들어 속광 형성",
          "끈적이거나 겉도는 유분감 없이 벨벳처럼 밀착되어 메이크업 전 발라도 밀리지 않음",
          "화해 및 올리브영 실사용자 평점 4.9점 기록, 피부과 시술 후 진정용으로도 최적"
        ],
        "tips": "저녁 스킨케어 마지막 단계에서 평소보다 두껍게 레이어링해 수면팩처럼 사용하면 다음 날 아침 세안 후에도 속당김이 전혀 없습니다."
      },
      "en": {
        "title": "Olive Young Korea #1 Skincare: Aestura Atobarrier 365 Cream Double Value Set",
        "summary": "Seoul's holy-grail barrier cream: 100-hour moisture capsules, includes 80ml x 2 + 15ml Cera-Hyal Ampoule.",
        "description": "Ranked #1 in Olive Young Korea's moisturizing cream category for November 2026, Aestura Atobarrier 365 Cream is the undisputed gold standard for skin barrier recovery. Powered by patented micro-ceramide DermaOn capsules that melt upon skin contact, it repairs compromised barriers and provides continuous 100-hour deep hydration. This exclusive Olive Young November holiday set offers two 80ml full-size tubes plus a 15ml serum at 44,500 KRW ($32 USD).",
        "tasteReview": [
          "Visible white ceramide beads dissolve smoothly without friction, leaving a hydrated non-greasy glow",
          "Absorbs into a velvet matte finish that never pills under sunscreen or foundation",
          "Hypoallergenic formula verified safe for acne-prone, post-laser, and eczema-sensitive skin"
        ],
        "tips": "Layer generously as an overnight sleeping mask during dry, freezing winter nights for glass-smooth morning skin."
      },
      "ja": {
        "title": "韓国オリーブヤング1位「エストラ アトバリア365クリーム ダブル企画セット」徹底解説",
        "summary": "乾燥肌の救世主！セラミドカプセルが100時間潤いを守る名品クリーム（80ml×2本＋アンプル15ml付き）。",
        "description": "2026年11月の韓国オリーブヤング（OLIVE YOUNG）ランキングで圧倒的1位に君臨するドクターズコスメ・エストラ（AESTURA）の限定ダブルセット。目に見える高密度セラミドカプセルがお肌の上でとろけるように馴染み、肌バリアを強化して100時間保湿を持続させます。秋冬の寒風による乾燥や肌荒れ、インナードライを劇的にケア。現地の免税店や明洞店舗でも即完売する大人気アイテムです。",
        "tasteReview": [
          "小さな粒状セラミドが体温でスッと溶け込み、ベタつかずもっちりした潤いヴェールを形成",
          "メイク前に塗ってもヨレたり浮いたりせず、翌朝までしっとり感が持続",
          "皮膚科テスト済み・低刺激処方で、ピーリングやレーザー施術後の敏感肌にも安心"
        ],
        "tips": "夜のスキンケアの最後に少し厚めに塗り広げると、スリーピングパックのような集中保湿効果が得られます。"
      },
      "zh": {
        "title": "韩国Olive Young断货王：Aestura瑷丝特兰365屏障面霜双支超值套盒深度测评",
        "summary": "拯救秋冬换季干痒泛红！专利神经酰胺微胶囊100小时锁水，内含80ml*2正装+15ml安瓶赠品。",
        "description": "2026年11月稳坐韩国Olive Young面霜销量榜榜首的医研护肤天花板！爱茉莉旗下医美级品牌Aestura的核心单品。肉眼可见的微型神经酰胺胶囊触肤即溶，重构受损皮脂膜，临床验证长达100小时强效锁水保湿。针对秋冬寒风造成的干痒起皮、换季泛红及医美术后修复效果显著，11月专享双支大容量礼盒仅售44,500韩元（约合235元人民币）。",
        "tasteReview": [
          "白色微小神经酰胺颗粒推开瞬间化水吸收，形成一层透气锁水膜，哑光丝绒质感不搓泥",
          "完全不假滑、不闷痘，干皮敏皮以及刷酸后修护的安心本命面霜",
          "全网好评率高达4.9分，明洞旗舰店每人限购的韩国旅游必囤护肤品"
        ],
        "tips": "秋冬睡前可厚涂一层当作急救睡眠面膜使用，次日清晨洗脸后皮肤依旧软嫩水润。"
      }
    }
  },
  {
    "id": "musinsa-standard-cashmere-blend-coat-202611",
    "slug": "musinsa-standard-cashmere-blend-oversized-single-coat",
    "category": "k-fashion",
    "store": "Musinsa Standard",
    "priceKrw": 169900,
    "releaseDate": "2026-11-04",
    "rating": 4.9,
    "imageUrl": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=800&auto=format&fit=crop",
    "affiliateUrl": "https://musinsa.com/example-cashmere-coat-2026",
    "affiliatePlatform": "Musinsa",
    "i18n": {
      "ko": {
        "title": "무신사 스탠다드 2026 FW \"캐시미어 블렌드 오버사이즈 싱글 코트\" 실착 핏 가이드",
        "summary": "무신사 11월 아우터 페스티벌 랭킹 1위! 호주산 울 70% + 캐시미어 30% 혼방의 미니멀 데일리 코트",
        "description": "국내 최대 패션 플랫폼 무신사의 자체 브랜드(PB) 무신사 스탠다드가 11월 선보인 2026 겨울 주력 롱코트입니다. 최고급 호주산 메리노 울 70%에 몽골산 캐시미어 30%를 황금 비율로 블렌딩하여 묵직함 없이 가볍고 부드러운 드레이프성을 자랑합니다. 자연스럽게 떨어지는 드롭 숄더 오버사이즈 실루엣으로 정갈한 미니멀룩부터 캐주얼 스트리트까지 폭넓게 소화 가능하며, 169,900원의 믿기 힘든 가성비로 전 사이즈 초도 물량이 품절 임박 상태입니다.",
        "tasteReview": [
          "캐시미어 30% 함유로 은은한 결광과 실크 같은 터치감, 장시간 착용해도 피로감 없는 경량성",
          "무릎 아래까지 우아하게 내려오는 맥시 기장감으로 체형 커버 및 방한력 우수",
          "클래식 블랙, 딥 차콜, 오트밀 베이지 3가지 기본 컬러로 실패 없는 겨울 데일리 아우터"
        ],
        "tips": "이너로 두터운 헤비 니트나 오버핏 후드티를 레이어드하려면 정사이즈를, 깔끔한 수트 출근룩을 원하면 한 치수 다운을 권장합니다."
      },
      "en": {
        "title": "Musinsa Standard FW26 \"Cashmere Blend Oversized Single Coat\" Buying Guide",
        "summary": "Ranked #1 in Musinsa Korea Winter Festival: 70% Australian Merino Wool + 30% Cashmere minimal long coat.",
        "description": "The flagship winter outerwear from Musinsa Standard, the house label of Korea's biggest fashion destination Musinsa, released in November 2026. Crafted from a luxurious blend of 70% premium Australian wool and 30% Mongolian cashmere, this single-breasted coat offers an exquisite natural drape and featherlight warmth. Featuring relaxed drop shoulders and an understated modern silhouette, it epitomizes the iconic Seoul minimalist aesthetic at an unbeatable price of 169,900 KRW (~$122 USD).",
        "tasteReview": [
          "High cashmere content provides a subtle sheen and buttery softness without the bulkiness of cheap coats",
          "Elegant maxi length falling just below the knee offers great wind chill protection",
          "Versatile enough to style with tailored trousers for office wear or sweatpants for casual street vibes"
        ],
        "tips": "True-to-size fit leaves ample room for layering chunky sweaters or lightweight down vests."
      },
      "ja": {
        "title": "韓国MUSINSA新作「カシミヤブレンド オーバーサイズシングルコート」サイズ感＆コーデ",
        "summary": "ムシンサ冬のアウターフェス1位！上質ウール70％×カシミヤ30％混紡の洗練ソウルミニマルコート。",
        "description": "韓国最大のファッションプラットフォーム「MUSINSA（ムシンサ）」のオリジナルブランドが2026年11月に放つ冬の本命アウター。オーストラリア産メリノウール70%とモンゴル産カシミヤ30%を贅沢にブレンドし、驚くほど軽やかで上品な艶感を実現しました。ドロップショルダーのリラックスしたオーバーサイズ設計で、羽織るだけで今っぽい韓国ストリート＆ミニマルシックが完成します。169,900ウォンという破格のコスパも魅力です。",
        "tasteReview": [
          "カシミヤ30%ならではのしっとり柔らかな肌触りと、肩がこらない軽量な着心地",
          "膝下まで美しく落ちるロング丈で、スタイルアップ効果と防寒性を両立",
          "MUSINSA GLOBALサイトから日本への直接配送も可能で関税手続きもスムーズ"
        ],
        "tips": "厚手のタートルネックニットやパーカーと合わせるなら普段の日本サイズと同等を選ぶのがベストです。"
      },
      "zh": {
        "title": "韩国MUSINSA Standard秋冬断货王“羊绒混纺宽松单排扣大衣”版型实穿测评",
        "summary": "稳居全韩男装/女装冬装榜第一！70%澳洲美丽诺羊毛+30%羊绒黄金配比，首尔极简风本命大衣。",
        "description": "韩国第一潮流平台MUSINSA旗下品牌MUSINSA Standard于2026年11月震撼推出的冬季旗舰单品。采用70%澳洲精纺羊毛与30%蒙古山羊绒黄金配比混纺，手感如糯米般细腻软滑，自重轻盈且垂坠感极佳。经典的微落肩宽松单排扣版型，无论日常通勤搭配衬衫还是街头叠穿卫衣都能轻松驾驭，169,900韩元（约合890元人民币）的价格重新定义了性价比天花板。",
        "tasteReview": [
          "30%高羊绒含量带来自然高级的丝光质感，抗风保暖性出色",
          "过膝及小腿中部的黄金长款剪裁，包容各种身材，拉长全身比例",
          "百搭纯黑、深炭灰与燕麦奶茶三色可选，实穿度极高"
        ],
        "tips": "版型偏微宽松，内搭厚毛衣选平时正码即可穿出随性慵懒的高级松弛感。"
      }
    }
  }
]

rows = []
for p in real_products:
    rows.append({
        "slug": p["slug"],
        "data": p
    })

url = f"{SUPABASE_URL}/rest/v1/posts"
data_bytes = json.dumps(rows).encode("utf-8")

req = urllib.request.Request(
    url,
    data=data_bytes,
    headers={
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print(f"Successfully inserted {len(res)} REAL trending posts into Supabase!")
        for r in res:
            print(f"- id: {r['id']}, slug: {r['slug']}")
except Exception as e:
    print(f"Error: {e}")
