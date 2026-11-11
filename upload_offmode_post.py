#!/usr/bin/env python3
"""
Update offmode color matching post with strong hooking title and original clean lookbook images
"""

import json
import urllib.request

SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptdXFtdnh1YnV3aG9vY3Vrbm50Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDMwODA3NywiZXhwIjoyMTA5ODg0MDc3fQ.ELyAmyRJrWdQoIHRu4thMGvjAnjJfVZ4S8Cfpb9MiDY"
REVALIDATE_URL = "https://www.k-trand.store/api/revalidate?secret=kblog2026"

post = {
  "id": "color-match-cheatsheet-8-rules-2026",
  "slug": "fail-proof-8-color-matching-rules-for-men",
  "category": "k-fashion",
  "store": "개똥마요 x 무신사",
  "priceKrw": 129000,
  "releaseDate": "2026-11-11",
  "rating": 5.0,
  "imageUrl": "/images/products/lookbook-cover.png",
  "images": [
    "/images/products/lookbook-cover.png",
    "/images/products/lookbook-brown-grey.png",
    "/images/products/lookbook-green-navy.png",
    "/images/products/lookbook-charcoal-blue.png",
    "/images/products/lookbook-burgundy-black.png"
  ],
  "affiliateUrl": "https://www.musinsa.com/curator/s/jaenam1212",
  "affiliatePlatform": "Musinsa",
  "i18n": {
    "ko": {
      "title": "옷 못 입는 사람 특징: 옷장에 검정·회색만 있음 (실패 없는 8가지 색 조합 치트키)",
      "summary": "옷장 열면 검정 롱패딩에 회색 후드티뿐인 놈들 필독. 비싼 명품 살 돈 없어도 색깔만 제대로 섞으면 '저 새끼 옷 좀 입네?' 소리 듣는다.",
      "description": "옷 못 입는 애들 특징이 뭔지 아냐?\n옷장 열어보면 검정 롱패딩, 검정 슬랙스, 회색 후드티, 검정 패딩 조끼가 전부다.\n본인은 '무난하고 깔끔하다'고 생각하겠지만 남들이 볼 땐 그냥 무채색 그림자 1이다. 솔직히 인상도 칙칙해 보이고 아무 매력이 없다.\n\n그렇다고 갑자기 빨간 바지나 형광색 입으면 어디 행사 뛰러 온 광대 소리 듣기 십상이다.\n인스타 패션 매거진 보다가 실전에서 바로 써먹기 좋은 '무채색 탈출 8가지 실패 없는 컬러 매치'가 있길래, 남들한테 '너 오늘 옷 좀 입었다?' 소리 들을 수 있게 내 식대로 핵심만 요약해준다.\n\n옷 새로 살 필요도 없다. 평소 입던 검정·회색 기본 템에 단품 하나만 색깔 섞어줘도 바로 가오 산다.\n\n1. 브라운 + 그레이\n브라운만 입으면 아저씨 같고, 회색만 입으면 추워 보이는데 둘이 섞이면 단점을 알아서 깎아 먹는다. 캐시미어 니트에 울 코트 걸칠 때 가장 만만한 고급 조합.\n\n2. 그린 + 네이비\n네이비 슬랙스나 자켓에 묵직한 포레스트 그린 니트 하나 쓱 걸쳐주면 끝. 튀지 않으면서도 안정감 있고 자연스럽게 세련돼 보임.\n\n3. 차콜 + 블루\n검정 대신 묵직한 쥐색(차콜) 슬랙스에 스카이블루나 딥블루 이너 하나 얹는 거다. 출근할 때 가오 살리기 제일 좋은 댄디 룩.\n\n4. 그린 + 핑크\n카키색 야상이나 올리브 패딩에 연핑크 이너 조합. 군대 깔깔이 느낌 날 뻔한 걸 연분홍이 멱살 잡고 건져 올려준다. 남들이 보면 센스 터짐.\n\n5. 옐로우 + 블루\n네이비 아우터에 버터나 머스타드 옐로우 이너. 색 대비가 확실해서 생동감 돌고 훨씬 어려 보인다. 주말 데이트룩 치트키.\n\n6. 브라운 + 레드\n브라운 코트나 자켓에 쨍한 빨간 목도리나 비니, 가디건 얹기. 연말 모임 갈 때 가오 챙기기 직빵인 프렌치 스타일.\n\n7. 퍼플 + 그레이\n회색 바지나 가디건에 은은한 연보라(라벤더) 이너. 과하지 않으면서도 신비롭고 감도 있어 보이는 사기 조합.\n\n8. 버건디 + 블랙\n올블랙 셋업에 버건디 가죽 자켓이나 니트 하나 툭. 가볍지 않고 묵직하면서 성숙한 분위기 내기 끝판왕.\n\n결론:\n비싼 명품 살 돈 없으면 색깔 조합이나 제대로 맞춰 입어라.\n아침에 뇌 빼고 입어도 남들 보여주기 가오가 좀 산다.",
      "tasteReview": [
        "맨날 입던 검정·회색 기본 템에 포인트 컬러 하나만 얹어서 룩 심폐소생",
        "보색이나 촌스러운 형광 배제하고 무채색과 자연스럽게 섞이는 현실적인 8대 조합",
        "무신사나 SPA에서 가디건·목도리 단품 하나만 사서 바로 써먹기 가능"
      ],
      "tips": "비율은 베이스 70%에 포인트 컬러 30%가 국룰이다. 1:1로 반반 섞으면 펩시콜라 되니까 조심해라."
    },
    "en": {
      "title": "Why Your Style Looks Boring: You Only Wear Black & Grey (8 Cheatsheets to Fix It)",
      "summary": "Tired of looking like a walking shadow? You don't need designer logos—master these 8 fail-proof color formulas to instantly look sharp.",
      "description": "Open your closet. If you only see black puffers, black slacks, and grey hoodies, you're not 'minimalist'—you're just blending into the background.\nHere are 8 fail-proof color equations tested by fashion editors that rescue you from boring monochrome without making you look like a clown:\n\n1. Brown + Grey: Earthy cocoa softens cold grey. Effortless quiet luxury.\n2. Green + Navy: Forest green against crisp navy. Calm, reliable, and sharp.\n3. Charcoal + Blue: Heavy charcoal paired with vibrant sky blue. The ideal modern commuter look.\n4. Green + Pink: Rugged military olive neutralized by muted dusty pink. Peak subtle contrast.\n5. Yellow + Blue: Butter yellow beneath a navy coat. Energetic and youthful.\n6. Brown + Red: Rich chocolate brown accented with cherry red. Classic retro charm.\n7. Purple + Grey: Heather grey elevated with soft lavender. Minimalist sophistication.\n8. Burgundy + Black: Jet black anchored with deep wine leather. Heavyweight elegance.\n\nBottom Line:\nKeep your base at 70% and accent at 30%. Easy upgrade with zero guesswork.",
      "tasteReview": [
        "Instantly revives boring monochrome staples with zero guesswork",
        "Avoids gaudy neons in favor of muted tones that blend seamlessly with black and grey",
        "Executable immediately by swapping a single scarf or inner sweater"
      ],
      "tips": "Stick to the 70/30 golden ratio. Never split colors 50/50 unless you want to look like a sports flag."
    },
    "ja": {
      "title": "ダサく見える人の特徴：全身黒とグレーしか着ていない（垢抜け確実な8つの配色チート）",
      "summary": "クローゼットが黒ダウンとグレーパーカーばかりの人必見。高い服を買わなくても「なんか今日お洒落」と言わせる8つの配色ルール。",
      "description": "服に気を使っていない人の共通点：クローゼットを開けると黒ダウン、黒パンツ、グレーのパーカーしかない。\n「無難でシンプル」だと思っているのは本人だけで、周りから見るとただの地味な影です。\n派手な蛍光色に逃げる必要はありません。手持ちの黒・グレーの基本アイテムに、たった1色足すだけで一気に垢抜ける8つの配色公式を伝授します。\n\n1. ブラウン ＋ グレー：都会的な洗練と温もりの共存。\n2. グリーン ＋ ネイビー：深いフォレストグリーンがネイビーの知性を引き立てる。\n3. チャコール ＋ ブルー：重厚なチャコールに爽やかなブルーを差す通勤スタイル。\n4. グリーン ＋ ピンク：武骨なミリタリーオリーブを淡いピンクで柔らかく中和。\n5. イエロー ＋ ブルー：ネイビーアウターにバターイエローの遊び心を。\n6. ブラウン ＋ レッド：深みのある茶色に赤をピリッと効かせるレトロシック。\n7. パープル ＋ グレー：グレーを背景にラベンダーを品よく魅せる上級者テク。\n8. バーガンディ ＋ ブラック：黒で引き締める大人のワインレッド。\n\n結論：\n高いブランド服を買うより、色の組み合わせを覚える方が圧倒的にコスパが良いです。",
      "tasteReview": [
        "手持ちの定番黒・グレー服に差し色1点を足すだけで印象が劇的に変わる",
        "派手すぎない大人向けの配色で、通勤から休日まで幅広く対応",
        "マフラーやインナーニット1枚を変えるだけで即実践可能"
      ],
      "tips": "ベースカラー70％、差し色30％の黄金比率を守ること。半々にするとまとまりがなくなります。"
    },
    "zh": {
      "title": "穿搭土气的原因只有一个：衣柜里只有黑白灰（拯救直男的8套神仙撞色作弊码）",
      "summary": "打开衣柜全是黑羽绒服和灰卫衣？不用花大钱买大牌，掌握这8套神级撞色公式，秒变行走的穿搭教科书。",
      "description": "很多男生觉得自己穿得‘低调干净’，实际上走在街上就像一团移动的黑灰色影子，毫无辨识度。\n不用突然去穿红裤子或荧光绿，教你8套在黑灰基础上稍作点缀就能瞬间高级的配色公式：\n\n1. 棕色 + 灰色：克制温暖，最不易出错的高智感知识分子风。\n2. 绿色 + 藏青：深森林绿打破藏青的沉闷，干净又帅气。\n3. 炭灰 + 蓝色：沉稳的深炭灰与爽朗天蓝撞色，职场型男首选。\n4. 军绿 + 浅粉：硬朗工装绿用低饱和婴儿粉中和，反差感拉满。\n5. 姜黄 + 宝蓝：大面积藏青内搭一抹明黄，减龄又吸睛。\n6. 棕色 + 正红：浓郁巧克力大衣搭配复古红围巾，法式复古拉满。\n7. 浅紫 + 浅灰：中性灰底色衬托香芋紫的清冷高雅。\n8. 酒红 + 纯黑：全黑造型叠加一件酒红皮衣，成熟贵气。\n\n结论：\n把颜色配明白了，普通的衣服也能穿出几千块的质感。",
      "tasteReview": [
        "彻底拯救无聊的黑灰打底，用局部点睛色给整套穿搭做心肺复苏",
        "摈弃俗气荧光色，精选与大地色系完美交融的8大多元组合",
        "实操成本极低，一条围巾或一件内搭针织即可轻松复刻"
      ],
      "tips": "主色70%、点睛色30%是铁律，切忌五五开平分。"
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
            print(f"[+] Updated post with hooking title & original lookbook: {slug}")
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
