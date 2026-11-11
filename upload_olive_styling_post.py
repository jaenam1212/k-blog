#!/usr/bin/env python3
"""
Upload Olive Two-Tone Color Matching Guide with 3:4 High-Res Lookbook & Studio Product Cards
"""

import json
import urllib.request
import urllib.error

SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptdXFtdnh1YnV3aG9vY3Vrbm50Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDMwODA3NywiZXhwIjoyMTA5ODg0MDc3fQ.ELyAmyRJrWdQoIHRu4thMGvjAnjJfVZ4S8Cfpb9MiDY"
REVALIDATE_URL = "https://www.k-trand.store/api/revalidate?secret=kblog2026"

example_items = [
    {
        "name": "M-65 오버사이즈 필드 자켓 [올리브]",
        "brand": "무신사 스탠다드",
        "priceKrw": 99900,
        "imageUrl": "/images/products/item-olive-m65.png",
        "url": "https://www.musinsa.com/search/goods?keyword=M65+%EC%98%AC%EB%A6%AC%EB%B8%8C+%EC%9E%90%EC%BC%93&gf=A",
        "category": "Outer"
    },
    {
        "name": "탑필 헤비 캐시미어 크루넥 니트 [딥 버건디]",
        "brand": "쿠어 (COOOR)",
        "priceKrw": 108000,
        "imageUrl": "/images/products/item-wine-knit.png",
        "url": "https://www.musinsa.com/search/goods?keyword=%EC%BF%A0%EC%96%B4+%EB%B2%84%EA%B1%B4%EB%94%94+%EB%8B%88%ED%8A%B8&gf=A",
        "category": "Knitwear"
    },
    {
        "name": "2-Tone 헤비웨이트 크루넥 스웨트셔츠 [오트밀 그레이]",
        "brand": "예일 (YALE)",
        "priceKrw": 49000,
        "imageUrl": "/images/products/item-grey-sweat.png",
        "url": "https://www.musinsa.com/search/goods?keyword=%EC%98%88%EC%9D%BC+%EA%B7%B8%EB%A0%88%EC%9D%B4+%EB%A7%A8%ED%88%AC%EB%A7%A8&gf=A",
        "category": "Sweatshirt"
    },
    {
        "name": "13.5oz 와이드 스트레이트 셀비지 데님 [딥 인디고]",
        "brand": "모드나인 (MODNINE)",
        "priceKrw": 118000,
        "imageUrl": "/images/products/item-raw-denim.png",
        "url": "https://www.musinsa.com/search/goods?keyword=%EB%AA%A8%EB%93%9C%EB%82%98%EC%9D%B8+%EC%85%80%EB%B9%84%EC%A7%80+%EC%83%9D%EC%A7%80&gf=A",
        "category": "Pants"
    },
    {
        "name": "유틸리티 와이드 카고 퍼티그 팬츠 [올리브]",
        "brand": "브라운야드 (BROWNYARD)",
        "priceKrw": 148000,
        "imageUrl": "/images/products/item-olive-cargo.png",
        "url": "https://www.musinsa.com/search/goods?keyword=%EC%99%80%EC%9D%B4%EB%93%9C+%EC%B9%B4%EA%B3%A0+%EC%98%AC%EB%A6%AC%EB%B8%8C+%ED%8C%AC%EC%8 advocates&gf=A",
        "category": "Pants"
    }
]

post = {
    "id": "fall-olive-two-tone-color-styling-rules-2026",
    "slug": "fall-olive-two-tone-color-styling-rules-2026",
    "category": "k-fashion",
    "store": "무신사 스토어",
    "priceKrw": 99900,
    "releaseDate": "2026-11-11",
    "rating": 5.0,
    "imageUrl": "/images/products/lookbook-olive-cover.png",
    "images": [
        "/images/products/lookbook-olive-cover.png",
        "/images/products/lookbook-olive-burgundy.png",
        "/images/products/lookbook-olive-grey.png",
        "/images/products/lookbook-olive-black.png",
        "/images/products/lookbook-olive-white.png",
        "/images/products/lookbook-olive-indigo.png"
    ],
    "exampleItems": example_items,
    "affiliateUrl": "https://www.musinsa.com/search/goods?keyword=%EC%98%AC%EB%A6%AC%EB%B8%8C+%EC%BD%94%EB%94%94&gf=A",
    "affiliatePlatform": "Musinsa",
    "i18n": {
        "ko": {
            "title": "‘국방색’ 소리 듣던 올리브의 반전: 실패 없는 가을 투톤 배색 치트키 5",
            "summary": "올리브(Olive)는 가을 웜톤 뉴트럴의 최고봉이지만 배색을 모르면 군대 군복이 됩니다. SNS에서 폭발적 반응을 얻은 투톤 컬러 매치 5대 공식을 공개합니다.",
            "description": "가을과 겨울이 되면 자연스럽게 옷장에서 꺼내게 되는 컬러가 바로 '올리브(Olive)'입니다. 하지만 채도와 명도를 잘못 맞추면 자칫 칙칙한 '국방색 군복'처럼 보이기 십상입니다.\n\n올리브 컬러의 본질은 차분하고 자연스러운 어스 톤(Earth Tone)에 있습니다. 올리브가 가진 특유의 빈티지함과 묵직한 무게감을 가장 세련되게 살려주는 핵심은 '명확한 대비를 주는 파트너 컬러의 선택'입니다.\n\n최근 패션 에디터들과 인스타그램 크리에이터들 사이에서 검증된, 실패 없는 올리브 투톤 배색 5대 공식을 소개합니다.\n\n1. 올리브 + 버건디 (Olive + Burgundy): 빈티지 클래식의 정석\n채도가 낮은 차분한 올리브 와이드 팬츠에 깊은 와인빛 버건디 오버핏 캐시미어 니트를 매치하는 조합입니다. 붉은 계열의 따뜻함과 녹색 계열의 차분함이 만나 보색 대비 효과를 내면서도 톤 다운되어 있어 우아하고 고급스러운 클래식 무드를 자아냅니다. 다크 브라운 로퍼로 마무리하면 감도가 배가됩니다.\n\n2. 올리브 + 멜란지 그레이 (Olive + Melange Grey): 실패 없는 데일리 꾸안꾸\n가장 쉽고 편안하게 시도할 수 있는 스트릿 캐주얼의 정석입니다. 멜란지 그레이 스웨트셔츠나 후디 밑단에 화이트 이너를 살짝 레이어드하고, 넉넉한 올리브 와이드 카고 팬츠를 매치합니다. 회색의 차분한 도시적 분위기가 올리브의 투박함을 중화시켜 자연스러운 '시티보이 룩'을 완성합니다.\n\n3. 올리브 + 블랙 (Olive + Black): 단단하고 시크한 밀리터리 & 고프코어\nM-65 필드 자켓이나 피쉬테일 파카 등 올리브 컬러 아우터에 올블랙 이너와 블랙 비니를 매치하는 조합입니다. 군더더기 없는 블랙이 중심을 잡아주어 국방색 특유의 촌스러움은 사라지고, 남성적이고 단단한 어반 밀리터리 감성이 극대화됩니다.\n\n4. 올리브 + 퓨어 화이트 (Olive + Pure White): 미니멀하고 청량한 대비\n깨끗한 화이트 롱슬리브 티셔츠를 올리브 와이드 투턱 치노 팬츠 안에 단정하게 넣어 입는 미니멀 룩입니다. 맑은 화이트가 올리브 컬러에 청량한 활력을 불어넣어 주어, 초가을부터 늦가을까지 산뜻하면서도 센스 있는 남친룩을 연출할 수 있습니다.\n\n5. 올리브 + 딥 인디고 (Olive + Deep Indigo): 아메카지 & 워크웨어 치트키\n올리브 트윌 워크자켓이나 MA-1 아우터에 빳빳한 생지 셀비지 데님을 롤업해 매치하는 정통 조합입니다. 두 컬러 모두 시간이 지날수록 자연스러운 에이징(Aging)의 멋을 자랑하며, 투박하지만 깊이 있는 워크웨어 무드를 가장 확실하게 증명합니다.\n\n올리브 컬러는 단독으로 튀게 입기보다, 신뢰감 있는 1개의 베이직 컬러와 1:1로 짝지을 때 가장 완벽한 균형을 이룹니다.",
            "tasteReview": [
                "국방색 오명을 벗고 도시적인 하이엔드 감도를 완성하는 5대 투톤 공식",
                "출근룩부터 주말 캐주얼, 스트릿 고프코어까지 모든 TPO를 커버하는 범용성",
                "기존에 가지고 있는 베이직 단품(그레이 맨투맨, 생지 데님 등)과 즉시 호환 가능"
            ],
            "tips": "올리브는 광택감이 없는 매트한 코튼이나 울, 캔버스 소재를 선택해야 고급스러워 보입니다. 버건디나 화이트와 매치할 때는 가죽 벨트나 슈즈를 딥 브라운으로 통일하면 완성도가 훨씬 높아집니다."
        },
        "en": {
            "title": "Beyond Military Khaki: 5 Fail-Proof Two-Tone Color Combinations with Olive for Fall",
            "summary": "Olive is the quintessential autumn neutral, but poor pairing makes it look like military camouflage. Discover 5 viral two-tone styling formulas curated by fashion editors.",
            "description": "As autumn sets in, olive green naturally becomes a wardrobe essential. However, getting the tone wrong can quickly make you look like you are wearing vintage military surplus.\n\nThe secret to mastering olive lies in deliberate color contrast. Here are 5 fail-proof two-tone formulas that elevate olive into modern quiet luxury:\n\n1. Olive + Burgundy: The Vintage Classic\nA deep wine knit sweater paired with relaxed olive trousers. The toned-down complementary contrast creates sophisticated old-money depth.\n\n2. Olive + Melange Grey: Effortless City Boy Casual\nA classic heather grey sweatshirt layered over olive fatigue cargo pants. The neutral grey softens olive's ruggedness for a daily streetwear aesthetic.\n\n3. Olive + Black: Modern Urban Military & Gorpcore\nAn M-65 field jacket layered over an all-black hoodie and knitted beanie. Sharp, brooding, and masculine.\n\n4. Olive + Pure White: Clean Minimal Contrast\nA crisp heavy-cotton white longsleeve tucked into wide two-tuck olive chinos. Brings fresh clarity to earthy tones.\n\n5. Olive + Deep Indigo: The Authentic Workwear Formula\nOlive canvas work jacket paired with rigid raw selvedge denim. Rich in heritage textures and timeless durability.\n\nElevate your seasonal palette by anchoring olive with one confident foundational neutral.",
            "tasteReview": [
                "Transforms rugged olive into high-end editorial streetwear and quiet luxury",
                "Covers every context from casual office days to weekend getaways",
                "Seamlessly pairs with staples you already own like grey crewnecks and raw denim"
            ],
            "tips": "Opt for matte cotton, twill, or wool textures rather than shiny synthetics. Finish burgundy or white pairings with dark brown leather accessories."
        },
        "ja": {
            "title": "野暮ったいカーキを卒業：失敗しないオリーブ秋の2トーン配色黄金ルール5選",
            "summary": "オリーブ（カーキ）は秋冬の大本命カラーですが、合わせ方を間違えると作業着や軍服に見えがちです。SNSで大反響を呼んだ2トーン配色黄金律を徹底解説。",
            "description": "秋冬の定番色であるオリーブですが、配色バランスを間違えると野暮ったい軍服感が出てしまいがちです。\nオリーブの魅力を最大限に引き出す鍵は、「清潔感のあるコントラスト」にあります。\n\n今季即実践できる、失敗知らずのオリーブ2トーン配色5大公式をご紹介します：\n\n1. オリーブ ＋ バーガンディ：上品なヴィンテージクラシック\n深みのあるワインレッドのニットに、オリーブのワイドパンツを合わせた大人の補色コーデ。\n\n2. オリーブ ＋ 杢グレー：失敗しないデイリーシティボーイ\nヘザーグレーのスウェットにオリーブのカーゴパンツを合わせた王道の抜け感スタイル。\n\n3. オリーブ ＋ ブラック：武骨で洗練されたミリタリー＆ゴープコア\nM-65フィールドジャケットにオールブラックのインナーを合わせた引き締めコーデ。\n\n4. オリーブ ＋ ピュアホワイト：清潔感あふれるミニマルカジュアル\n上質な白ロンTをオリーブのチノパンにタックインした爽やかな好印象スタイル。\n\n5. オリーブ ＋ 濃紺インディゴ：本格派アメカジ＆ワークウェア\nオリーブのカバーオールに生デニム（セルビッジ）をロールアップして合わせた至高の組み合わせ。\n\nオリーブは余計な色を足さず、頼れる基本色と1:1で組むのが一番スマートです。",
            "tasteReview": [
                "軍服感を払拭し都会的なセンスを醸し出す洗練の5大配色",
                "休日のお出かけから通勤まで幅広く着回せる高い実用性",
                "手持ちの定番アイテム（グレースウェット、生デニム等）で今すぐ再現可能"
            ],
            "tips": "テカリのないマットなコットンやウール素材を選ぶのが高級感の秘訣です。足元はダークブラウンのレザーシューズで引き締めると完璧です。"
        },
        "zh": {
            "title": "告别军绿土气：秋冬绝不出错的橄榄绿（Olive）双色叠搭黄金法则 5 选",
            "summary": "橄榄绿是秋冬最高级的暖调中性色，但搭配不当极易沦为军大衣既视感。盘点博主都在用的 5 个双色王炸搭配公式。",
            "description": "一到秋冬季，橄榄绿（Olive）就是不可或缺的经典色彩。但如果明度和色彩比例没选对，很容易穿出土气的军大衣感。\n\n橄榄绿的精髓在于质感与对比。掌握以下 5 个经过验证的双色搭配公式，轻松进阶穿搭高手：\n\n1. 橄榄绿 ＋ 酒红（Burgundy）：复古优雅的高级撞色\n深酒红针织衫搭配垂坠感橄榄绿阔腿裤，微撞色却沉稳克制，尽显老钱风范。\n\n2. 橄榄绿 ＋ 花灰（Melange Grey）：松弛感十足的 City Boy\n灰色连帽卫衣露出白边下摆，下搭宽松橄榄绿工装裤，毫不费力的高级日常感。\n\n3. 橄榄绿 ＋ 纯黑（Black）：利落硬朗的机能工装风\nM-65 军风外套内搭全黑高领与冷帽，黑色压住军绿的粗犷，气场全开。\n\n4. 橄榄绿 ＋ 纯白（Pure White）：清爽干净的极简少年感\n高克重白色长袖 T 恤塞入橄榄绿双褶奇诺裤，清新明亮，视觉舒适度拉满。\n\n5. 橄榄绿 ＋ 原色深蓝（Deep Indigo）：复古阿美咔叽工装王炸\n橄榄绿工装夹克搭配深蓝赤耳丹宁牛仔裤，两款经年耐磨的质感面料碰撞出极致经典。\n\n穿好橄榄绿的关键在于：不要多色堆砌，专注 1:1 的双色高级对比。",
            "tasteReview": [
                "摆脱土味军绿标签，进阶高阶杂志级街头穿搭",
                "覆盖日常通勤、周末约会、户外机能全场景",
                "完美盘活衣柜已有基础款（灰色卫衣、原色牛仔等）"
            ],
            "tips": "尽量挑选无光泽感的哑光重磅棉、羊毛或帆布材质。搭配酒红或白色时，皮具与鞋履首选深棕色系。"
        }
    }
}

def upload_post():
    req = urllib.request.Request(
        f"{SUPABASE_URL}/rest/v1/posts",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates"
        },
        data=json.dumps({"slug": post["slug"], "data": post}).encode("utf-8")
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            print(f"[+] Post upserted successfully! Status: {r.status}")
    except urllib.error.HTTPError as e:
        print(f"[-] HTTP Error: {e.code} {e.read().decode('utf-8')}")
        return False
    except Exception as e:
        print(f"[-] Error: {e}")
        return False

    # Trigger revalidation
    try:
        with urllib.request.urlopen(REVALIDATE_URL, timeout=10) as r:
            print(f"[+] Revalidation triggered! Status: {r.status}, response: {r.read().decode('utf-8')}")
    except Exception as e:
        print(f"[-] Revalidation warning: {e}")

    return True

if __name__ == "__main__":
    upload_post()
