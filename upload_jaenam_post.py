#!/usr/bin/env python3
"""
Upload a post written in Jae-nam's authentic personal tone:
- Honest, direct, developer-centric pragmatism
- '완성됫다', '되시겟다', '가오가 좀 살고', '이색기', no fluff
"""

import json
import urllib.request
import os

def _env_local(name):
    """Read a value from the .env.local next to this script (never hardcode secrets)."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env.local")
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith(name + "="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    except OSError:
        pass
    return ""


def _require_env(name):
    """Environment variable (or .env.local) only: the repository holds no secrets."""
    value = os.environ.get(name) or _env_local(name)
    if not value:
        raise SystemExit(
            f"{name} is not set. Set it in the environment or in .env.local "
            f"(see .env.example). Secrets are never stored in the repository."
        )
    return value


def _bearer_header(key):
    """Legacy JWT keys ride on Authorization; new sb_ keys must not (Invalid JWT)."""
    return {"Authorization": f"Bearer {key}"} if key.startswith("eyJ") else {}




SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = _require_env("SUPABASE_SERVICE_ROLE_KEY")
REVALIDATE_URL = ("https://www.k-trand.store/api/revalidate?secret="
                  + _require_env("REVALIDATE_SECRET"))

post = {
  "id": "jaenam-brown-outfit-curation-2026",
  "slug": "jaenam-style-brown-outfit-guide",
  "category": "k-fashion",
  "store": "개똥마요 x Musinsa",
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
      "title": "가을 겨울 브라운 코디 실패 없는 4개 조합 정리 — 가오 살리는 실전 룩북",
      "summary": "가을 겨울에 브라운 잘못 입으면 낙타 아저씨 된다. 인스타에서 핫한 4개 조합 무신사 실물로 딱 정리해줌.",
      "description": "가을 겨울 되면 옷장에 코트나 패딩 하나씩 사는데 다들 브라운 많이 산다.\n근데 솔직히 브라운 색 잘못 입으면 칙칙한 낙타 아저씨 되기 십상이다.\n인스타 릴스 뒤지다가 팬톤 다운타운 브라운 기준으로 꽤 그럴듯한 색 조합 4개가 있어서 무신사 실물 옷으로 맞춰봤다.\n남들 보여주기도 가오가 좀 살고, 아침에 옷 고를 때 뇌 빼고 입기 좋은 조합들 되시겠다.\n\n1. 브라운 + 그레이 + 버터옐로우\n어두운 브라운 코트에 무난한 그레이 슬랙스 입고 이너로 버터 옐로우 니트 하나 쓱 넣어주는 거다.\n모니터만 보느라 누렇게 뜬 개발자 낯빛도 이거 하나 입으면 사람 얼굴빛이 좀 산다.\n\n2. 브라운 + 베이지 + 레드\n베이지랑 브라운만 입으면 심심해 뒤지는데, 여기에 쨍한 빨간 가디건이나 목도리 하나 얹어주면 끝난다.\n대충 걸쳤는데 왠지 옷 잘 입는 척하기 딱 좋다. 연말 모임 갈 때 가오 챙기기 최고.\n\n3. 브라운 + 스카이블루 + 크림\n따뜻한 브라운에 차가운 하늘색 니트 조합이다. 바지는 크림색 치노.\n색 대비가 확실해서 제일 세련돼 보인다. 요즘 성수동이나 홍대 가면 애들이 제일 많이 입는 스타일.\n\n4. 브라운 + 올리브 + 라이트핑크\n카키 야상이나 패딩에 브라운 바지 입고, 안에 연핑크 이너를 슬쩍 받쳐 입는 조합.\n군대 깔깔이 느낌 날 뻔한 걸 핑크가 멱살 잡고 건져 올려준다. 남들이 보면 센스 있어 보임.",
      "tasteReview": [
        "지루한 브라운 톤온톤 벗어나서 버터·레드·스카이블루 포인트로 한 방에 해결",
        "무신사 상위 랭킹 울·캐시미어 실제 신상 기준이라 핏이랑 재질 검증 끝남",
        "비싼 옷 다 새로 살 필요 없이 집에 있는 브라운 아우터에 이너만 갈아 끼우면 됨"
      ],
      "tips": "브라운 아우터 어두울수록 이너는 버터옐로우나 라이트핑크처럼 부드러운 파스텔로 가라. 그래야 얼굴 안 죽는다."
    },
    "en": {
      "title": "4 Fail-Proof Brown Outfit Formulas for Men — Look Sharp Without Trying Hard",
      "summary": "Wear brown wrong and you look like a tired camel. Here are 4 viral color equations mapped to real K-fashion items.",
      "description": "Everyone buys a brown coat in autumn and winter, but style it wrong and you end up looking like a dreary camel.\nWe took 4 viral styling formulas from Korean fashion feeds and mapped them directly to top-rated Musinsa items.\nSimple, no-nonsense combos that keep you looking sharp with zero morning mental load.\n\n1. Brown + Grey + Butter Yellow\nDeep brown coat + grey trousers + soft butter yellow knit. Instantly revives tired developer complexion.\n\n2. Brown + Beige + Red\nEarth tone base spiced with an electric cherry red cardigan. Effortless French retro swagger.\n\n3. Brown + Sky Blue + Cream\nWarm cocoa meets cool pastel blue knit and cream pants. The sharpest clean-fit trend on Seoul streets.\n\n4. Brown + Olive + Light Pink\nMilitary olive jacket + brown slacks + baby pink knit. Softens rugged workwear with effortless cool.",
      "tasteReview": [
        "Cuts through muddy brown monotony with instant high-contrast accents",
        "Built strictly with verified high-grade Australian wool knitwear on Musinsa",
        "Zero need to buy whole new outfits—just swap out the inner layer"
      ],
      "tips": "The darker your brown outerwear, the softer and paler your inner sweater should be. Keeps your face bright."
    },
    "ja": {
      "title": "失敗しない「ブラウンコーデ」4大配色ルール — 誰でも即こなれる実戦ルックブック",
      "summary": "茶色を間違えて着ると地味なおじさんになる。韓国SNSで話題の4大配色をMUSINSA人気作で完全再現。",
      "description": "秋冬の定番ブラウンコート。一歩間違えるとラクダのような野暮ったい印象になりがちです。韓国トレンドフィードでバズった4大配色ルールをベースに、MUSINSAの実在アイテムでリアルな組み合わせを作りました。\n\n1. ブラウン ＋ グレー ＋ バターイエロー\nダークブラウンのコートにグレースラックス、インナーにまろやかなバターイエローのニット。顔色がパッと明るく見えます。\n\n2. ブラウン ＋ ベージュ ＋ レッド\n同系色ベースに鮮やかな赤カーディガンを差し色投入。大人のこなれ感を演出します。\n\n3. ブラウン ＋ スカイブルー ＋ クリーム\n温かみのあるブラウンに清涼感あるパステルブルーをぶつける上級者スタイル。\n\n4. ブラウン ＋ オリーブ ＋ ライトピンク\nミリタリーなオリーブに淡いピンクを差して柔らかく中和する甘辛ミックス。",
      "tasteReview": [
        "単調な茶色コーデを抜け出し、差し色で一気に今っぽく垢抜ける",
        "MUSINSA高評価のリアルなウール・カシミヤ新作で構成",
        "手持ちのブラウンアウターにインナーを変えるだけで即応用可能"
      ],
      "tips": "アウターが暗いブラウンなら、インナーはバターイエローなど淡いパステルを選ぶと顔周りが明るくなります。"
    },
    "zh": {
      "title": "秋冬棕色穿搭绝不出错的4大配色法则 — 告别老气的高级感实战手册",
      "summary": "棕色穿不好秒变老气驼色大叔。精选韩国SNS爆款4套配色公式，搭配Musinsa真实现货单品。",
      "description": "秋冬大家都在买深棕色大衣，但搭配不当极易显得沉闷老气。参考首尔街头爆火的配色灵感，用Musinsa在售高分单品整合成4套拿来即用的实战穿搭：\n\n1. 棕色 + 浅灰 + 黄油黄\n深棕大衣搭配灰色西裤，内搭一件软糯黄油黄毛衣。瞬间提亮打工人疲惫气色。\n\n2. 棕色 + 燕麦米 + 樱桃红\n大地色基底中加入一抹吸睛正红开衫，不费力的复古名伶随性感拉满。\n\n3. 棕色 + 天水蓝 + 奶油白\n暖咖色与冷水蓝的温度碰撞，干净利落的时髦雅痞Clean Fit风格。\n\n4. 棕色 + 橄榄绿 + 浅樱粉\n工装绿外套配深棕裤，用一件浅粉色麻花毛衣化解硬朗，刚柔并济十分高级。",
      "tasteReview": [
        "彻底摆脱大地色沉闷感，用黄油黄、复古红等点睛色一秒提气色",
        "精选Musinsa官方高好评澳洲羊毛单品，版型质感经得起考验",
        "实操门槛低，无需全套换新，仅换内搭即可穿出高级感"
      ],
      "tips": "深棕外套颜色越厚重，内搭越建议选浅黄、淡粉等低饱和色调，显白不压肤色。"
    }
  }
}

headers = {
    "apikey": SUPABASE_KEY,
    **_bearer_header(SUPABASE_KEY),
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
