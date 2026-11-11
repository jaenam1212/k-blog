#!/usr/bin/env python3
"""
Upload Instagram @offmode_mag color matching guide written in Jae-nam's authentic tone:
- Title: 맨날 검정·회색만 쳐입는 사람들을 위한 8가지 색 조합 치트키 — 가오 살리는 법
- 8 Combos: Brown+Grey, Green+Navy, Charcoal+Blue, Green+Pink, Yellow+Blue, Brown+Red, Purple+Grey, Burgundy+Black
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
  "store": "개똥마요 매거진 x 무신사",
  "priceKrw": 129000,
  "releaseDate": "2026-11-11",
  "rating": 5.0,
  "imageUrl": "/images/products/color-matching-cover.png",
  "images": [
    "/images/products/color-matching-cover.png",
    "/images/products/color-matching-brown-grey.png",
    "/images/products/color-matching-green-navy.png",
    "/images/products/color-matching-charcoal-blue.png",
    "/images/products/color-matching-brown-red.png"
  ],
  "affiliateUrl": "https://www.musinsa.com/curator/s/jaenam1212",
  "affiliatePlatform": "Musinsa",
  "i18n": {
    "ko": {
      "title": "맨날 검정·회색만 쳐입는 사람들을 위한 8가지 색 조합 치트키 — 가오 살리는 법",
      "summary": "옷장에 검정 롱패딩이랑 회색 후드티밖에 없는 놈들 필독. 인스타에서 핫한 8가지 실패 없는 컬러 매치 내 식대로 딱 정리해줌.",
      "description": "맨날 검정 롱패딩에 회색 후드티, 칙칙한 검정 슬랙스만 쳐입고 다니면 솔직히 사람 인상도 칙칙해 보이고 멋도 없다.\n그렇다고 형광색 같은 거 입으면 어디 광대 같아 보이고.\n인스타 매거진(@offmode_mag) 보다가 '무채색만 입는 사람들을 위한 8가지 실패 없는 컬러 매치' 정리해둔 게 있길래 내용이 꽤 실전적이라 내 식대로 요약해본다.\n옷은 평소 입던 거 그대로 입고 색깔만 살짝 섞어도 '저 새끼 왠지 옷 좀 입네?' 소리 듣기 딱 좋은 치트키들 되시겠다.\n\n1. 브라운 + 그레이\n브라운만 입으면 늙어 보이고, 회색만 입으면 춥고 차가워 보이는데 둘이 섞으면 알아서 단점을 깎아 먹는다. 니트나 울 코트 입을 때 가장 만만한 어른 조합.\n\n2. 그린 + 네이비\n네이비 바지나 자켓에 딥그린(포레스트 그린) 니트 하나 쓱 걸쳐주면 끝난다. 튀지 않으면서도 안정감 있고 자연스럽게 세련돼 보임.\n\n3. 차콜 + 블루\n검정 대신 묵직한 쥐색(차콜) 슬랙스에 스카이블루나 딥블루 이너 하나 얹는 거다. 출근할 때 가오 살리기 제일 좋은 댄디 룩.\n\n4. 그린 + 핑크\n카키색 야상이나 올리브 패딩에 연핑크 이너 조합. 군대 깔깔이 느낌 날 뻔한 걸 연분홍이 멱살 잡고 건져 올려준다. 남들이 보면 센스 터짐.\n\n5. 옐로우 + 블루\n네이비 아우터에 버터나 머스타드 옐로우 이너. 색 대비가 확실해서 생동감 돌고 어려 보인다. 주말 캐주얼 룩으로 제격.\n\n6. 브라운 + 레드\n브라운 코트나 자켓에 쨍한 빨간 목도리나 비니, 가디건 얹기. 연말 모임 갈 때 가오 챙기기 직빵인 프렌치 스타일.\n\n7. 퍼플 + 그레이\n회색 바지나 가디건에 은은한 연보라(라벤더) 이너. 과하지 않으면서도 신비롭고 감도 있어 보이는 사기 조합.\n\n8. 버건디 + 블랙\n올블랙 셋업에 버건디 가죽 자켓이나 니트 하나 툭. 가볍지 않고 묵직하면서 성숙한 분위기 내기 끝판왕.\n\n결론:\n비싼 명품 살 돈 없으면 색깔 조합이나 제대로 맞춰 입어라.\n아침에 뇌 빼고 입어도 남들 보여주기 가오가 좀 산다.",
      "tasteReview": [
        "맨날 입던 검정·회색 기본 템에 포인트 컬러 하나만 얹어서 룩 심폐소생",
        "보색이나 촌스러운 형광 배제하고 무채색과 자연스럽게 섞이는 현실적인 8대 조합",
        "무신사나 SPA에서 가디건·목도리 단품 하나만 사서 바로 써먹기 가능"
      ],
      "tips": "비율은 베이스 70%에 포인트 컬러 30%가 국룰이다. 1:1로 반반 섞으면 펩시콜라 되니까 조심해라."
    },
    "en": {
      "title": "8 Fail-Proof Color Combinations for Men Sick of All-Black & Grey — Easy Style Upgrade",
      "summary": "Tired of looking like a walking shadow in black and grey? Here are 8 proven color cheatsheets from viral fashion feeds.",
      "description": "If your winter wardrobe consists entirely of black down parkas and grey hoodies, you inevitably blend into the dreary background.\nInspired by @offmode_mag's viral curation, here are 8 foolproof color equations that make you look effortlessly stylish without buying an entire new wardrobe.\n\n1. Brown + Grey: Earthy warmth neutralizes cold grey. The ultimate understated luxury formula.\n2. Green + Navy: Deep forest green against structured navy. Calm, reliable, and sharp.\n3. Charcoal + Blue: Heavy charcoal grounded with crisp sky or cobalt blue. Perfect modern commuter dandy look.\n4. Green + Pink: Rugged military olive softened with muted baby pink. Subtle high-end contrast.\n5. Yellow + Blue: Butter yellow peeking beneath navy outerwear. Energetic and youthful.\n6. Brown + Red: Cocoa brown coats spiced with electric cherry red accents. French retro swagger.\n7. Purple + Grey: Heather grey elevated with soft lavender or dusty plum. Sensual, tasteful minimalism.\n8. Burgundy + Black: Jet black anchored with deep wine burgundy. Heavyweight, mature elegance.\n\nBottom line:\nYou don't need luxury logos—just nail the color ratios to stand out.",
      "tasteReview": [
        "Breathes instant life into boring monochrome essentials with zero guesswork",
        "Avoids gaudy neons in favor of muted tones that blend seamlessly with black and grey",
        "Can be executed immediately by swapping a single scarf or inner sweater"
      ],
      "tips": "Keep base colors at 70% and accent pops at 30%. Never split 50/50 unless you want to look like a sports flag."
    },
    "ja": {
      "title": "黒とグレーばかり着る人のための「失敗しない8大カラー配色ルール」— こなれ感の極意",
      "summary": "黒ダウンとグレーパーカーから抜け出したい人必見。韓国SNSで話題の8つの垢抜け配色を完全攻略。",
      "description": "冬になると全身黒やグレーばかりで地味になりがちな人へ。韓国人気ファッションメディア(@offmode_mag)のバズ投稿をベースに、手持ちの服に少し色を足すだけで「なんかお洒落」と言わせる8つの配色ルールをまとめました。\n\n1. ブラウン ＋ グレー：温かみと都会的な冷たさの絶妙なバランス。\n2. グリーン ＋ ネイビー：深いフォレストグリーンがネイビーの知性を引き立てる。\n3. チャコール ＋ ブルー：重厚なチャコールに爽やかなブルーを差す洗練スタイル。\n4. グリーン ＋ ピンク：ミリタリーなオリーブを淡いピンクで柔らかく中和。\n5. イエロー ＋ ブルー：ネイビーアウターにバターイエローの遊び心。\n6. ブラウン ＋ レッド：深みのある茶色に鮮やかな赤を効かせたレトロシック。\n7. パープル ＋ グレー：グレーを背景にラベンダーを品よく魅せる。\n8. バーガンディ ＋ ブラック：黒で引き締める大人のワインレッド。\n\n結論：\n高い服を買わなくても、色の組み合わせを覚えるだけで劇的に垢抜けます。",
      "tasteReview": [
        "手持ちの定番黒・グレー服に差し色1点を足すだけで印象が劇的に変わる",
        "派手すぎない大人向けの配色で、通勤から休日まで幅広く対応",
        "マフラーやインナーニット1枚を変えるだけで即実践可能"
      ],
      "tips": "ベースカラー70％、差し色30％の黄金比率を守ること。1対1で半々にするとまとまりがなくなります。"
    },
    "zh": {
      "title": "给只会穿黑白灰直男的8套绝不出错配色作弊码 — 轻松穿出高级感",
      "summary": "衣柜里只有黑色羽绒服和灰色卫衣？韩国穿搭杂志推爆的8套保姆级撞色公式一次讲透。",
      "description": "冬天满大街都是黑羽绒和灰卫衣，单调又容易显得没精打采。参考韩国时尚杂志(@offmode_mag)爆款内容，用最通俗实用的方式整理出8套拿来即用的配色指南。无需大换血，仅靠内搭或配饰换个颜色，就能让人觉得你很有衣品：\n\n1. 棕色 + 灰色：温暖克制，最不易出错的职场知识分子风。\n2. 绿色 + 藏青：深森林绿打破藏青的刻板，沉稳中透出活力。\n3. 炭灰 + 蓝色：厚重的深炭灰与清爽天蓝色碰撞，利落干净。\n4. 军绿 + 浅粉：硬朗工装绿搭配低饱和婴儿粉，刚柔并济极具辨识度。\n5. 姜黄 + 宝蓝：大面积藏青内搭一抹明黄，减龄又吸睛。\n6. 棕色 + 正红：浓郁巧克力大衣叠加复古红围巾，法式氛围拉满。\n7. 浅紫 + 浅灰：中性灰底色衬托香芋紫的清冷高级。\n8. 酒红 + 纯黑：全黑造型用一件酒红皮衣或毛衣点睛，成熟贵气。\n\n结论：\n没钱买大牌不要紧，把颜色配明白了，站在人群里照样支棱起来。",
      "tasteReview": [
        "彻底拯救无聊的黑灰打底，用局部点睛色给整套穿搭做心肺复苏",
        "摈弃俗气荧光色，精选与大地色系完美交融的8大多元组合",
        "实操成本极低，一条围巾或一件内搭针织即可轻松复刻"
      ],
      "tips": "主色70%、点睛色30%是铁律，千万别五五开平分，否则秒变行走的指示牌。"
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

# Revalidate
try:
    urllib.request.urlopen(urllib.request.Request(REVALIDATE_URL))
    print("[+] Revalidated Vercel cache successfully!")
except Exception as e:
    print(f"[-] Revalidate error: {e}")
