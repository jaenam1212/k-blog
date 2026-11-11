#!/usr/bin/env python3
"""
Upload Instagram-Inspired Brown Outfit 4 Color Combinations Styling Posts to Supabase
Based on viral Reel (@hamalog_):
1. Brown + Grey + Butter Yellow
2. Brown + Beige + Red
3. Brown + Sky Blue + Cream
4. Brown + Olive + Light Pink
"""

import json
import urllib.request
import urllib.error

SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptdXFtdnh1YnV3aG9vY3Vrbm50Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDMwODA3NywiZXhwIjoyMTA5ODg0MDc3fQ.ELyAmyRJrWdQoIHRu4thMGvjAnjJfVZ4S8Cfpb9MiDY"
REVALIDATE_URL = "https://www.k-trand.store/api/revalidate?secret=kblog2026"

brown_styling_posts = [
  {
    "id": "fw-brown-styling-4-color-guide-2026",
    "slug": "fall-winter-brown-outfit-color-combination-guide",
    "category": "k-fashion",
    "store": "Musinsa & K-Lookbook",
    "priceKrw": 189000,
    "releaseDate": "2026-11-11",
    "rating": 5.0,
    "imageUrl": "/images/products/musinsa-mtr-balmacaan-coat.jpg",
    "images": [
      "/images/products/musinsa-mtr-balmacaan-coat.jpg",
      "/images/products/musinsa-butter-yellow-knit.jpg",
      "/images/products/musinsa-red-cardigan.jpg",
      "/images/products/musinsa-pastel-blue-knit.jpg",
      "/images/products/musinsa-light-pink-cardigan.jpg"
    ],
    "affiliateUrl": "https://www.musinsa.com/curator/s/jaenam1212",
    "affiliatePlatform": "Musinsa",
    "i18n": {
      "ko": {
        "title": "2026 가을·겨울 실패 없는 '브라운 코디' 4대 컬러 조합 실전 룩북",
        "summary": "SNS 조회수 70만 돌파 팬톤 19-1223 다운타운 브라운 기준! 버터옐로우·레드·스카이블루·라이트핑크 실전 매칭 가이드",
        "description": "가을과 겨울 시즌 옷장에 한 벌쯤 있지만 색 맞추기가 은근히 까다로운 '브라운(Downtown Brown)'. 인스타그램 인기 패션 크리에이터가 제안한 실패 없는 4대 핵심 컬러 매칭을 바탕으로, 무신사 실물 신상 아이템과 조합한 실전 룩북을 공개합니다.\n\n1️⃣ [브라운 + 그레이 + 버터옐로우]\n차분한 멜란지 그레이 슬랙스나 스커트에 부드러운 버터 옐로우 니트([빅토리아 울] 우먼즈 크루 넥 50,310원)를 이너로 매치하고 딥 브라운 MTR 코트를 걸치는 조합입니다. 칙칙해지기 쉬운 무채색 겨울 착장에 따뜻한 햇살 같은 생기를 불어넣어 피부 톤을 화사하게 밝혀줍니다.\n\n2️⃣ [브라운 + 베이지 + 레드]\n톤온톤 베이지 하의와 딥 브라운 아우터의 클래식한 베이스에 강렬한 레드 가디건([우먼즈 에센셜 라운드 넥] 38,990원)을 포인트로 얹는 프렌치 시크 룩입니다. 단추를 한두 개 풀어 이너 레이어드로 연출하거나 어깨에 살짝 둘러주면 과하지 않은 세련된 연말 무드를 완성합니다.\n\n3️⃣ [브라운 + 스카이블루 + 크림]\n따뜻한 브라운과 청량한 쿨톤 스카이블루 니트([우먼즈 퍼지 크루 넥] 42,210원), 그리고 화사한 크림 팬츠를 믹스한 댄디 룩입니다. 웜톤과 쿨톤의 절묘한 온도차 대비가 주는 감각적인 분위기로, 올해 해외 스트리트 패션에서 가장 뜨겁게 떠오르는 컬러 플레이입니다.\n\n4️⃣ [브라운 + 올리브 + 라이트핑크]\n빈티지한 올리브 카키 아우터와 초콜릿 브라운 하의에 여리여리한 라이트 핑크 가디건([우먼즈 케이블 라운드 넥] 42,390원)을 더한 믹스매치입니다. 투박한 워크웨어 감성을 사랑스럽고 은은한 페미닌 톤으로 부드럽게 중화시켜 유니크한 스트리트 룩을 연출합니다.",
        "tasteReview": [
          "단순한 톤온톤을 넘어 버터옐로우·레드·파스텔블루·라이트핑크 포인트로 세련된 대비감 극대화",
          "무신사 스탠다드 실구매 랭킹 상위권의 실제 울·캐시미어 신상 단품으로 구성되어 실착 접근성 우수",
          "아우터(브라운) 중심의 기본 옷장 아이템에 소장 중인 이너 및 머플러로 즉시 응용 가능한 실용 가이드"
        ],
        "tips": "브라운 아우터가 어둡고 묵직할수록 이너는 버터옐로우나 라이트핑크처럼 채도가 낮고 부드러운 파스텔 톤을 선택하면 얼굴이 화사해 보입니다."
      },
      "en": {
        "title": "2026 Fall/Winter Brown Styling Guide: 4 Fail-Proof Color Combinations & Lookbook",
        "summary": "Based on Pantone 19-1223 Downtown Brown! How to style brown coats with Butter Yellow, Red, Sky Blue, and Light Pink.",
        "description": "Brown is an indispensable staple of Fall/Winter wardrobes, yet styling it beyond basic monotone can be tricky. Inspired by Korea's viral fashion creator tips, we curating 4 fail-proof color equations matched with real Musinsa outerwear and knitwear.\n\n1️⃣ [Brown + Grey + Butter Yellow]\nLayer a deep brown MTR coat over melange grey trousers and an ultra-soft Butter Yellow crewneck sweater (Victoria Wool, $36 USD). The creamy yellow illuminates dull winter skin tones while maintaining quiet-luxury sophistication.\n\n2️⃣ [Brown + Beige + Red]\nGround a tone-on-tone oatmeal beige and deep brown silhouette with an electric Cherry Red knit cardigan ($28 USD). Drape it over shoulders or show a sliver at the neckline for an effortless French-chic accent.\n\n3️⃣ [Brown + Sky Blue + Cream]\nA masterful interplay of warm chocolate brown against crisp, cool pastel Sky Blue fuzzy knit ($30 USD) and cream corduroy trousers. The contrasting color temperatures produce the sharpest contemporary dandy aesthetics seen on Seoul streets.\n\n4️⃣ [Brown + Olive + Light Pink]\nPair an olive-green field jacket or trousers with rich dark brown, then soften the utilitarian edge with an airy Baby Pink cable cardigan ($30 USD). It blends rugged street casual with subtle feminine charm.",
        "tasteReview": [
          "Breaks free from boring all-brown looks by infusing curated pastel and vivid primary accent hues",
          "Fully mapped to real high-rating wool and cashmere knitwear readily available on Musinsa",
          "Universal formula that flatters both warm and cool undertones with minimal effort"
        ],
        "tips": "For darker cocoa browns, select desaturated muted pastels like butter yellow and baby pink for the inner layer to brighten the complexion."
      },
      "ja": {
        "title": "2026秋冬 失敗しない「ブラウンコーデ」4大カラー配色＆実戦ルックブック",
        "summary": "韓国SNSで大バズりのパントン19-1223基準！バターイエロー・レッド・スカイブルー・ライトピンクを効かせた最旬着こなし術",
        "description": "秋冬の定番でありながら、合わせ方次第で地味に見えがちな「ブラウン（Downtown Brown）」。韓国の人気ファッションクリエイターが提案した失敗知らずの4大配色ルールをベースに、MUSINSAのリアルな新作アイテムを組み合わせた実戦ルックブックを公開します。\n\n1️⃣ [ブラウン + グレー + バターイエロー]\n落ち着いた杢グレースラックスに優しいバターイエローのウールニットをインナーとして差し、濃いブラウンコートを羽織る上品コーデ。重くなりがちな冬の装いに柔らかな明るさをプラスします。\n\n2️⃣ [ブラウン + ベージュ + レッド]\n同系色のベージュとブラウンの安心感あるベースに、鮮やかなレッドカーディガンを差し色として投入するフレンチシックな着こなし。肩掛けや首元のチラ見せでこなれ感が劇的にアップします。\n\n3️⃣ [ブラウン + スカイブルー + クリーム]\n温かみのあるブラウンに清涼感あるパステルスカイブルーニットとクリーム色のパンツを合わせた上級者コーデ。暖色と寒色の絶妙な温度差が洗練されたモダンな雰囲気を演出します。\n\n4️⃣ [ブラウン + オリーブ + ライトピンク]\nミリタリーテイストのオリーブカーキにダークブラウンを合わせ、甘いライトピンクのケーブル編みニットで中和する甘辛ミックス。人と被らない洗練されたストリートスタイルが完成します。",
        "tasteReview": [
          "単調になりがちなワントーンコーデを打破し、差し色を効果的に効かせた洗練スタイル",
          "MUSINSAで実際に高評価を獲得している人気ウール・カシミヤアイテムで構成",
          "手持ちのブラウンアウターにインナーや小物を買い足すだけで即実践できる実用性"
        ],
        "tips": "ダークブラウンのアウターには、彩度を抑えたバターイエローやライトピンクなどの柔らかいパステルトーンを合わせると顔周りがパッと明るく見えます。"
      },
      "zh": {
        "title": "2026秋冬绝不出错的“棕色系穿搭”4大配色公式与实战单品推荐",
        "summary": "基于Pantone 19-1223下城棕！黄油黄、复古红、天水蓝、樱花粉4大多元配色方案实战解析",
        "description": "秋冬衣橱里不可或缺却又最容易穿得沉闷老气的“棕色（Downtown Brown）”。借鉴韩国爆款穿搭博主的核心穿搭灵感，结合Musinsa真实在售人气单品，总结出以下4套绝不出错的高阶撞色实战方案：\n\n1️⃣ [棕色 + 浅灰 + 黄油黄]\n沉稳的花灰色阔腿西裤，内搭一抹软糯温柔的黄油黄圆领羊毛衫（Victoria Wool，约260元），外披深棕色大衣。一秒打破冬日暗沉，自带提亮面部肤色的天然反光板效果。\n\n2️⃣ [棕色 + 燕麦米 + 复古红]\n深棕与燕麦米的同色系大地色打底，叠加一件吸睛亮眼的樱桃红针织开衫（约200元）。无论是披在肩头还是解开领口露出层次，都能瞬间营造松弛随性的法式复古名伶风。\n\n3️⃣ [棕色 + 天水蓝 + 奶油白]\n温暖厚重的巧克力棕，碰撞清冷爽朗的浅天蓝毛圈针织衫（约220元）与奶油白灯芯绒长裤。冷暖色调的极致对撞，是今年首尔街头最受欢迎的时髦雅痞Clean Fit风格。\n\n4️⃣ [棕色 + 军绿橄榄 + 浅樱粉]\n粗犷复古的橄榄绿外套搭配深棕色下装，内搭一件淡雅的浅粉色麻花针织衫（约220元）。刚柔并济的工装甜美混搭，将中性机能风与温柔少女感平衡得恰到好处。",
        "tasteReview": [
          "跳脱单一枯燥的大地色同色系限制，融入黄油黄、复古红等高阶点睛色",
          "严选韩国Musinsa官方热卖榜高质感单品，版型与材质均经真实买家好评验证",
          "实操性极强，无需更换主外套即可通过内搭与配饰实现多套风格切换"
        ],
        "tips": "棕色外套颜色越深，内搭越建议选用黄油黄或浅粉等低饱和柔和色，能有效中和厚重感并提亮气色。"
      }
    }
  },
  {
    "id": "look-brown-butter-yellow-2026",
    "slug": "brown-mtr-coat-butter-yellow-knit-outfit",
    "category": "k-fashion",
    "store": "Musinsa Standard",
    "priceKrw": 50310,
    "releaseDate": "2026-11-11",
    "rating": 4.9,
    "imageUrl": "/images/products/musinsa-butter-yellow-knit.jpg",
    "images": [
      "/images/products/musinsa-butter-yellow-knit.jpg",
      "/images/products/musinsa-mtr-balmacaan-coat.jpg"
    ],
    "affiliateUrl": "https://www.musinsa.com/products/6704410",
    "affiliatePlatform": "Musinsa",
    "i18n": {
      "ko": {
        "title": "무신사 꿀조합: 딥 브라운 코트 x 버터 옐로우 빅토리아 울 니트 코디",
        "summary": "브라운의 묵직함에 버터 한 스푼! 피부 톤을 화사하게 살려주는 포근한 데일리 웜톤 룩북",
        "description": "SNS 화제의 '브라운 + 그레이 + 버터옐로우' 공식을 완성하는 핵심 아이템입니다. 호주산 프리미엄 빅토리아 울 100% 원사로 편직된 부드러운 버터 옐로우 니트는 단독으로 입어도 까슬거림이 전혀 없으며, 딥 브라운 MTR 발마칸 코트 안에 레이어드했을 때 목선과 가슴 라인에서 은은한 버터 컬러가 포근하게 드러납니다. 하의로는 차콜이나 멜란지 그레이 슬랙스를 매치해 단정하면서도 따뜻한 인상을 완성할 수 있습니다.",
        "tasteReview": [
          "호주산 빅토리아 엑스트라파인 울 100% 특유의 부드럽고 가벼운 보온 착용감",
          "과하게 튀지 않는 파스텔 버터 크림 색감으로 브라운 아우터와 자연스러운 톤 조화",
          "정가 5만 원대 합리적인 가격 대비 탄탄한 시보리와 필링 방지 마감"
        ],
        "tips": "이너로 흰색 티셔츠를 레이어드해 목과 밑단에 1cm 정도 살짝 흰색 라인을 빼주면 더욱 입체적인 캐주얼 룩이 연출됩니다."
      },
      "en": {
        "title": "Musinsa Outfit Match: Deep Brown Coat x Butter Yellow Victoria Wool Knit",
        "summary": "Add a dollop of butter to winter brown! Warm and brightening daily quiet-luxury knit styling.",
        "description": "The quintessential centerpiece for the viral 'Brown + Grey + Butter Yellow' formula. Knitted from 100% premium Australian Victoria wool, this sweater delivers supreme softness without itchiness. When layered under a deep cocoa brown balmacaan coat, the delicate butter tone peeks through, instantly banishing winter dullness. Pair with charcoal grey wide-leg trousers for a balanced, polished look.",
        "tasteReview": [
          "100% extra-fine Australian wool guarantees plush warmth without bulky weight",
          "Subtle butter cream shade that harmonizes effortlessly with all shades of brown and camel",
          "Exceptional rib knit cuffs that retain shape after repeated daily wear"
        ],
        "tips": "Layer a white crewneck tee underneath with a 1cm hem peeking out to add crisp depth to the outfit."
      },
      "ja": {
        "title": "MUSINSAおすすめコーデ：濃いブラウンコート×バターイエローウールニット",
        "summary": "ブラウンの重厚感にバターを一さじ！肌トーンをパッと明るく見せる温もりデイリールック",
        "description": "SNSで話題の「ブラウン＋グレー＋バターイエロー」の黄金ルールを再現する主役アイテム。オーストラリア産最高級ビクトリアウール100％で仕立てられ、チクチク感のない極上の肌触りを実現。ダークブラウンのバルマカーンコートのインナーに仕込むことで、首元から柔らかなイエローが覗き、重たい冬コーデを一気に華やかに格上げします。",
        "tasteReview": [
          "オーストラリア産エクストラファインウール100%ならではの軽やかで贅沢な保温性",
          "派手すぎないまろやかなバタークリームカラーがブラウンと抜群の相性",
          "5,000円前後の手頃なプライスながら、伸びにくいリブ編み仕上げで高耐久"
        ],
        "tips": "白のクルーネックTシャツをインナーに重ねて裾や首元から少し見せると、立体的なこなれ感がアップします。"
      },
      "zh": {
        "title": "Musinsa搭配推荐：深棕大衣 x 黄油黄维多利亚纯羊毛针织衫",
        "summary": "给厚重棕色加一抹黄油！自带柔焦反光板的秋冬日常治愈系温暖穿搭",
        "description": "完美复刻爆款“棕色+浅灰+黄油黄”穿搭公式的核心内搭。采用100%澳洲优质维多利亚纯羊毛纺织而成，亲肤软糯无刺痒感。套在深浓的巧克力棕大衣内部，领口与胸前不经意露出柔润的黄油暖调，瞬间化解冬日暗沉。下半身搭配深灰或炭灰色高腰阔腿裤，干练知性又充满亲和力。",
        "tasteReview": [
          "100%超细澳洲羊毛，轻盈贴肤且锁温保暖效果显著",
          "饱和度适中的温润黄油奶油色调，包容各种冷暖肤色",
          "百元级亲民定价，领口与下摆螺纹紧密不易松懈变形"
        ],
        "tips": "内里叠穿一件基础白T，下摆微露1厘米白色边缘，层次感立刻提升一个档次。"
      }
    }
  },
  {
    "id": "look-brown-red-vintage-cardigan-2026",
    "slug": "brown-outfit-red-essential-cardigan-look",
    "category": "k-fashion",
    "store": "Musinsa Standard",
    "priceKrw": 38990,
    "releaseDate": "2026-11-11",
    "rating": 4.8,
    "imageUrl": "/images/products/musinsa-red-cardigan.jpg",
    "images": [
      "/images/products/musinsa-red-cardigan.jpg",
      "/images/products/musinsa-mtr-balmacaan-coat.jpg"
    ],
    "affiliateUrl": "https://www.musinsa.com/products/4251251",
    "affiliatePlatform": "Musinsa",
    "i18n": {
      "ko": {
        "title": "무신사 꿀조합: 딥 브라운 x 체리 레드 에센셜 라운드 넥 가디건 코디",
        "summary": "베이지·브라운 톤온톤에 강렬한 레드 한 방울! 감각적인 프렌치 레트로 무드 연출",
        "description": "'브라운 + 베이지 + 레드' 공식을 가장 세련되게 완성하는 레드 니트 가디건입니다. 텁텁하지 않은 맑은 체리 레드 컬러로, 브라운 레더 자켓이나 울 코트 안에 포인트 이너로 착용하거나 브라운 코트 어깨 위에 숄처럼 가볍게 둘러주는 것만으로도 패션 피플 분위기를 자아냅니다. 오트밀 베이지 와이드 팬츠나 브라운 플리츠 스커트와 함께 매치하면 연말 모임 룩으로도 손색없습니다.",
        "tasteReview": [
          "얼굴을 생기 있게 살려주는 선명하고 고급스러운 톤의 체리 레드 색감",
          "이너 단독 착용부터 가벼운 아우터, 어깨 숄 레이어드까지 다채로운 활용도",
          "부드러운 비스코스 혼방 원사로 맨살에 닿아도 편안한 촉감"
        ],
        "tips": "가디건의 맨 위와 맨 아래 단추를 풀어 허리선을 살짝 드러내면 다리가 길어 보이고 답답하지 않은 실루엣이 연출됩니다."
      },
      "en": {
        "title": "Musinsa Outfit Match: Deep Brown x Cherry Red Essential Round Neck Cardigan",
        "summary": "A splash of crimson over earthy brown and beige! Channel effortless French-retro winter allure.",
        "description": "The ultimate statement piece for the viral 'Brown + Beige + Red' styling formula. Dyed in a clean, vibrant cherry red that cuts through earth tones like chocolate and camel. Wear it buttoned as a standalone top, peeking beneath a heavy wool coat, or loosely draped over the shoulders as a preppy knit scarf. Pairs flawlessly with oatmeal pleated trousers and vintage loafers.",
        "tasteReview": [
          "Rich crimson red hue that instantly energizes muted winter color schemes",
          "Versatile 3-way styling: knit sweater, cardigan layer, or shoulder wrap scarf",
          "Silky smooth viscose blend with non-itch gentle drape on bare skin"
        ],
        "tips": "Unbutton the top and bottom buttons to create a flattering hourglass silhouette that elongates the leg line."
      },
      "ja": {
        "title": "MUSINSAおすすめコーデ：濃いブラウン×チェリーレッド定番ラウンドネックカーディガン",
        "summary": "ベージュ＆ブラウンのアースカラーに鮮烈な赤をひとさじ！洗練されたフレンチレトロコーデ",
        "description": "話題の「ブラウン＋ベージュ＋レッド」の配色を叶えるチェリーレッドのラウンドネックカーディガン。深みのあるブラウンアウターやベージュのボトムスに合わせるだけで、パリジェンヌのような小粋なアクセントが完成。肩にショールのように巻いたり、前を留めてトップス風に着たりと、真冬から春先まで着回し力抜群の1着です。",
        "tasteReview": [
          "顔映りをパッと明るく見せてくれる上品で鮮やかなチェリーレッド",
          "トップス使い・羽織り・肩掛けと1着で3役こなす高い汎用性",
          "なめらかな肌触りのレーヨン混紡で素肌に着てもストレスフリー"
        ],
        "tips": "上下のボタンを1つずつ外して抜け感を作ると、ウエスト位置が高く見えてスタイルアップ効果抜群です。"
      },
      "zh": {
        "title": "Musinsa搭配推荐：浓郁深棕 x 樱桃红圆领基础针织开衫",
        "summary": "大地色系里的一抹惊艳红！高级感满满的法式复古名伶冬日搭配",
        "description": "轻松拿捏“棕色+燕麦米+复古红”配色的灵魂单品。正气清透的樱桃红色泽，既能作为深棕色大衣内部的视觉重心，也能随性地披在肩膀充当披肩配饰。搭配一条燕麦米色的高腰西装阔腿裤和一双复古乐福鞋，优雅知性又充满节日氛围，轻松胜任通勤与年末聚会场合。",
        "tasteReview": [
          "极其显白提气色的浓郁樱桃正红色，彻底打破冬日灰暗沉闷",
          "一件多穿：单穿做打底衫、开衫叠穿、肩部随意披搭皆有型",
          "细腻黏胶混纺面料，贴肤穿着柔顺无刺激"
        ],
        "tips": "开衫最上方和最下方各解开一颗纽扣，自然形成X形下摆，视觉上拉长下半身比例且更加灵动不呆板。"
      }
    }
  }
]

def main():
    print(f"[*] Uploading {len(brown_styling_posts)} Instagram Brown Styling posts to Supabase...")
    
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }

    for post in brown_styling_posts:
        slug = post["slug"]
        
        # Check existing
        check_url = f"{SUPABASE_URL}/rest/v1/posts?slug=eq.{slug}&select=id"
        req = urllib.request.Request(check_url, headers=headers)
        try:
            with urllib.request.urlopen(req) as resp:
                existing = json.loads(resp.read().decode("utf-8"))
                if existing:
                    print(f"[-] Updating existing post {existing[0]['id']}: {slug}")
                    update_url = f"{SUPABASE_URL}/rest/v1/posts?id=eq.{existing[0]['id']}"
                    update_payload = json.dumps({"data": post}).encode("utf-8")
                    up_req = urllib.request.Request(update_url, data=update_payload, headers=headers, method="PATCH")
                    with urllib.request.urlopen(up_req) as up_resp:
                        print(f"    [+] Updated {slug}")
                    continue
        except Exception as e:
            print(f"[-] Check error: {e}")

        # Insert new
        post_url = f"{SUPABASE_URL}/rest/v1/posts"
        payload = json.dumps({
            "slug": slug,
            "data": post
        }).encode("utf-8")
        
        req = urllib.request.Request(post_url, data=payload, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
                new_id = res_data[0]["id"] if res_data else "unknown"
                print(f"[+] Inserted post ID {new_id}: {slug}")
        except Exception as e:
            print(f"[-] Failed inserting {slug}: {e}")

    # Trigger revalidation
    print(f"[*] Triggering Vercel ISR revalidation...")
    try:
        rev_req = urllib.request.Request(REVALIDATE_URL)
        with urllib.request.urlopen(rev_req, timeout=10) as resp:
            print("[+] Revalidation response:", json.loads(resp.read().decode("utf-8")))
    except Exception as e:
        print(f"[-] Revalidation failed: {e}")

if __name__ == "__main__":
    main()
