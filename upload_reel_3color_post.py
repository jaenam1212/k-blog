#!/usr/bin/env python3
"""
Upload Reel 3-Color Layering Guide in Jae-nam's hooking authentic tone with original lookbook images
"""

import json
import urllib.request

SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptdXFtdnh1YnV3aG9vY3Vrbm50Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDMwODA3NywiZXhwIjoyMTA5ODg0MDc3fQ.ELyAmyRJrWdQoIHRu4thMGvjAnjJfVZ4S8Cfpb9MiDY"
REVALIDATE_URL = "https://www.k-trand.store/api/revalidate?secret=kblog2026"

post = {
  "id": "pinterest-3-color-layering-rules-2026",
  "slug": "pinterest-3-color-layering-rules-2026",
  "category": "k-fashion",
  "store": "개똥마요 x 무신사",
  "priceKrw": 149000,
  "releaseDate": "2026-11-11",
  "rating": 5.0,
  "imageUrl": "/images/products/lookbook-3color-cover.png",
  "images": [
    "/images/products/lookbook-3color-cover.png",
    "/images/products/lookbook-navy-white-beige.png",
    "/images/products/lookbook-brown-black-navy.png",
    "/images/products/lookbook-darkbrown-white-gold.png",
    "/images/products/lookbook-burgundy-blue-grey.png"
  ],
  "affiliateUrl": "https://www.musinsa.com/curator/s/jaenam1212",
  "affiliatePlatform": "Musinsa",
  "i18n": {
    "ko": {
      "title": "‘너 오늘 분위기 미쳤다’ 소리 듣는 법: 핀터레스트 3컬러 레이어링 치트키 5",
      "summary": "색깔 2개는 심심하고 4개는 조잡하다. 인스타에서 저장 폭발한 실패 없는 '3색 삼위일체' 레이어링 공식 5가지 총정리.",
      "description": "옷 입을 때 색깔 2개만 쓰면 뭔가 심심하고, 욕심내서 4개 이상 섞으면 어디 서커스단 광대 같아진다.\n옷잘알들이 핀터레스트에서 사진 건질 때 쓰는 절대 법칙이 바로 '3컬러 법칙(Three-Color Rule)'이다.\n단단한 베이스 2개에 포인트 컬러 딱 1개만 스치듯 얹는 건데, 인스타에서 반응 폭발한 가을/겨울 실패 없는 5가지 삼위일체 조합을 내 식대로 딱 정리해준다.\n\n1. 그레이 & 화이트 + 옐로우 (Grey & White + Yellow)\n깔끔한 차콜이나 멜란지 그레이 아우터에 화이트 셔츠를 받쳐 입고, 버터 옐로우 니트나 머플러 하나 얹기. 차분하고 지적인 톤 속에 화사한 센스가 확 돋보이는 사기 조합이다.\n\n2. 화이트 & 네이비 + 베이지 (White & Navy + Beige)\n네이비 자켓이나 울 코트에 화이트 이너, 그리고 바지나 머플러로 베이지 툭 얹기. 단정하고 지적이면서도 부드러운 '핀터레스트 느좋(느낌 좋은)' 미니멀 룩이 완성된다.\n\n3. 브라운 & 블랙 + 네이비 (Brown & Black + Navy)\n묵직한 다크 브라운 코트에 블랙 터틀넥, 그리고 네이비 슬랙스나 머플러 한 스푼 레이어드. 톤 다운된 컬러끼리 묵직하게 맞물려 절제된 시크함이 철철 흐른다.\n\n4. 다크 브라운 & 화이트 + 골드 (Dark Brown & White + Gold)\n에스프레소 브라운 코트에 깨끗한 아이보리 니트, 그리고 벨트 버클이나 시계의 은은한 골드 포인트. 소위 말하는 '올드머니 룩' 감성 낼 때 가오 살리기 직빵이다.\n\n5. 버건디 & 블루 + 그레이 (Burgundy & Blue + Grey)\n딥한 와인 버건디 아우터에 생지 데님(블루), 그리고 이너로 멜란지 그레이 받치기. 분위기 있으면서도 힙해서 연말 모임 나갈 때 남들 시선 끌기 최고다.\n\n결론:\n옷은 비싼 걸 사 입는 게 아니라 색깔 비율을 아는 놈이 이긴다.\n베이스 2개(70%) + 포인트 1개(30%), 이 삼위일체만 기억해라.",
      "tasteReview": [
        "2색의 밋밋함과 4색의 난잡함을 동시에 해결하는 황금비 3컬러 룩",
        "인스타 릴스 및 핀터레스트에서 가장 반응 좋은 현실적인 5대 무드",
        "기존 베이직 아이템에 포인트 컬러 소품 하나만 추가해 즉시 연출 가능"
      ],
      "tips": "포인트 컬러는 면적이 크면 촌스러워진다. 이너 넥라인 살짝 보이게 입거나 머플러, 비니 등 소품으로 면적을 조절하는 게 핵심이다."
    },
    "en": {
      "title": "How to Get 'Your Vibe Is Unreal' Today: 5 Pinterest 3-Color Layering Cheatsheets",
      "summary": "Two colors feel boring, four look chaotic. Master these 5 viral three-color formulas to achieve effortless quiet luxury.",
      "description": "Two colors often look too plain, while mixing four turns you into a circus clown.\nThe secret weapon stylish creators use on Pinterest is the 'Three-Color Rule'—two grounded neutrals combined with one intentional accent pop.\nHere are 5 foolproof autumn/winter three-color formulas curated for effortless confidence:\n\n1. Grey & White + Yellow: Crisp charcoal and white elevated with a butter yellow knit or scarf. Intellectual yet vibrant.\n2. White & Navy + Beige: Tailored navy coat over clean white, grounded with soft beige wide trousers. The quintessential minimal aesthetic.\n3. Brown & Black + Navy: Deep chocolate wool over black turtleneck, layered with a navy accent. Disciplined, brooding chic.\n4. Dark Brown & White + Gold: Espresso coat with ivory knit and subtle brushed gold hardware. Instant old-money sophistication.\n5. Burgundy & Blue + Grey: Rich wine leather over raw indigo denim, buffered with heather grey. Moody, charismatic, and stylish.\n\nBottom Line:\nStyle isn't about expensive logos—it's about mastering the 70/30 color balance.",
      "tasteReview": [
        "Resolves the dilemma between boring 2-tone outfits and messy 4-color clashes",
        "Directly replicates the highest-engagement Pinterest & Instagram fashion aesthetics",
        "Executes effortlessly with existing wardrobe staples plus one accent accessory"
      ],
      "tips": "Never let the accent color dominate over 30% of your silhouette. Keep it confined to an inner collar, knit vest, or scarf."
    },
    "ja": {
      "title": "「今日の雰囲気ヤバいね」と言わせる技術：ピンタレスト流3色レイヤード公式5選",
      "summary": "2色だと地味、4色だとごちゃつく。SNSで保存数急増中の「3色黄金比」垢抜けテクニックを徹底解説。",
      "description": "コーディネートで2色だけ使うとどこか物足りず、4色以上混ぜるとガチャガチャして見えます。\nお洒落な人が実践している鉄則が、ベース2色＋差し色1色でまとめる「3カラーの法則」です。\nこの秋冬に失敗しない、保存必須の5大カラー方程式をまとめました：\n\n1. グレー ＆ ホワイト ＋ イエロー：知的なモノトーンにバターイエローの温もりをプラス。\n2. ホワイト ＆ ネイビー ＋ ベージュ：洗練されたネイビー×白に、柔らかいベージュを添えた王道クワイエットラグジュアリー。\n3. ブラウン ＆ ブラック ＋ ネイビー：重厚なダークブラウンと黒に、ネイビーを重ねた都会派シック。\n4. ダークブラウン ＆ ホワイト ＋ ゴールド：エスプレッソブラウンにアイボリー、金具のゴールドを効かせたオールドマネースタイル。\n5. バーガンディ ＆ ブルー ＋ グレー：深みのあるワインレッドとデニムブルーを、グレーで大人っぽく調和。\n\n結論：\n高い服を着るのではなく、色の黄金比（70：30）を知っている人が勝ちます。",
      "tasteReview": [
        "地味な2色コーデと散らかる多色コーデの悩みを一発で解消",
        "ピンタレストで最も支持されているリアルで真似しやすい5大スタイル",
        "手持ちの定番服にマフラーや小物を1点足すだけで即実践可能"
      ],
      "tips": "差し色の面積が広すぎると悪目立ちします。インナーの襟元から覗かせるか、小物で取り入れるのが洗練のコツです。"
    },
    "zh": {
      "title": "让人忍不住夸‘你今天太有氛围感了’：小红书推爆的3色叠穿作弊码5套",
      "summary": "2种颜色太单调，4种颜色像马戏团。手把手教你掌握两门底色+一抹点睛的‘三色黄金法则’。",
      "description": "穿搭时只用2种颜色容易显得呆板，超过4种又容易像行走的调色盘。\n穿搭博主私藏的高级感秘诀，就是‘三色法则’：2种沉稳中性色打底，叠加1种点睛色。\n为你梳理出今年秋冬最不容易出错、质感拉满的5套神仙组合：\n\n1. 灰色 ＆ 白色 ＋ 姜黄：利落的炭灰与白衬衫，内叠一件黄油黄针织，清冷克制中透出高级活力。\n2. 白色 ＆ 藏青 ＋ 燕麦米：深蓝大衣搭配干净白内搭，用燕麦色阔腿裤调和，松弛智性风天花板。\n3. 棕色 ＆ 纯黑 ＋ 藏青：浓郁巧克力大衣叠穿黑色高领，搭配藏青围巾，克制沉稳的都市冷都风。\n4. 深棕 ＆ 纯白 ＋ 浅金：浓缩咖啡色配米白针织，点缀细致金色表扣，纯正老钱风名仕感。\n5. 酒红 ＆ 丹宁蓝 ＋ 浅灰：浓郁复古酒红皮衣碰撞原色牛仔蓝，用浅灰卫衣打底中和，时髦度拉满。\n\n结论：\n高级感从来不靠大牌堆砌，搞懂70%主色+30%点睛的三色比例你就赢了。",
      "tasteReview": [
        "完美解决黑灰太单调、彩色又太扎眼的直男穿搭死穴",
        "对标小红书与Pinterest高赞图鉴，复刻成本极低",
        "利用衣柜现有基础款，加一件点睛配饰即可脱胎换骨"
      ],
      "tips": "点睛色千万不要大面积铺陈，露出一截领口、一条围巾或帽子即可，克制才是高级。"
    }
  }
}

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
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
