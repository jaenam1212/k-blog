#!/usr/bin/env python3
"""겨울 난방기 4종 비교 + 전기요금 계산 글 (4개국어) → Supabase posts + ISR revalidate.

근거
 - 전기요금: 한국전력 주택용 전력(저압) 요금표(2023-11-09 시행, 2026년 4분기 연료비조정단가 5.0원/kWh).
   1단계 200kWh 이하 120.0원/kWh·기본 910원 / 2단계 201~400kWh 214.6원·1,600원 /
   3단계 400kWh 초과 307.3원·7,300원, 기후환경요금 9.0원/kWh, 부가가치세 10%, 전력산업기반기금 2.7%.
 - 제품 가격·리뷰: 쿠팡 검색 결과 2026-11-24 08:50 KST 노출가(직접 확인).
 - 제품 사진: 쿠팡 상품 썸네일 원본(실물). AI 생성 0장.
"""

import json
import os
import urllib.request
from urllib.parse import quote


def _env_local(name):
    try:
        for line in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env.local"), encoding="utf-8"):
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip()
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
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or _env_local("SUPABASE_SERVICE_ROLE_KEY")
REVALIDATE_URL = ("https://www.k-trand.store/api/revalidate?secret="
                  + _require_env("REVALIDATE_SECRET"))
SLUG = "winter-heating-cost-comparison-2026"

K = "https://www.coupang.com/np/search?q="
TAG = "&lptag=AF9412775"


def q(s):
    return K + quote(s) + TAG


C = "/images/products/heater-hanil-radiator.jpg"
G1 = "/images/products/heater-shinil-ceramic.jpg"
G2 = "/images/products/heater-shinil-ptc-bathroom.jpg"
G3 = "/images/products/heater-shinil-carbon.jpg"

KO_DESC = """전기 난방기의 전기요금은 광고 문구가 아니라 숫자로 정해진다. 소비전력(W)에 사용시간을 곱하면 kWh가 나오고, 여기에 주택용 전기요금 단가를 곱하면 끝이다. 2026년 4분기 한국전력 주택용 전력(저압) 요금표는 이렇다. 200kWh 이하 1단계 120.0원/kWh(기본요금 910원), 201~400kWh 2단계 214.6원(1,600원), 400kWh 초과 3단계 307.3원(7,300원). 여기에 기후환경요금 9.0원/kWh와 4분기 연료비조정요금 5.0원이 붙고, 마지막에 부가가치세 10%와 전력산업기반기금 2.7%가 더해진다. 12월~2월에 1,000kWh를 넘기면 넘는 부분은 슈퍼유저 요금 736.2원/kWh가 적용된다.
중요한 것은 누진제다. 난방기 하나를 하루 6시간, 한 달 쓰면 180시간이다. 2,000W 제품은 360kWh, 1,000W 제품은 180kWh를 더 쓴다. 이미 200kWh를 쓰고 있는 집이라면 2,000W 난방기는 사용량을 곧바로 3단계(307.3원)로 밀어 올린다. 같은 360kWh라도 2단계 단가로 계산한 8만2,296원이 아니라 3단계 단가로 계산하면 11만5,668원이 된다(전력량+기후환경+연료비조정 기준, 부가세·기금 제외). "전기요금 폭탄"의 정체는 대개 이 계단이다.
반대로 600W 이하 제품은 같은 180시간을 써도 108kWh다. 2만4,689원 수준이다. 난방기의 전기요금을 결정하는 것은 "발열 기술"이 아니라 소비전력과 사용시간, 그리고 그 집의 누진 위치다.

1. 방식별로 무엇이 다른가
라디에이터(오일식)는 내부 오일을 데워 금속 핀으로 열을 퍼뜨린다. 팬이 없어 무소음이고, 데워지는 데 10~20분 걸리지만 한 번 데워지면 열이 오래 간다. 11핀 제품이 흔하고 소비전력은 2,000W 안팎이다. 거실·침실처럼 넓은 공간을 오래 켜두는 용도에 맞는다.
세라믹 히터는 세라믹 발열체에 팬을 붙여 뜨거운 바람을 보낸다. 전원을 켜면 수 초 안에 따뜻한 바람이 나오고, 몸에 바로 닿아 "빨리 따뜻해지는" 느낌이 강하다. 대신 팬 소리가 있고, 바람이 닿는 곳만 따뜻하다. 소비전력은 1,000~2,000W대가 많다.
PTC 온풍기는 세라믹 히터의 개량형이다. PTC 소자는 온도가 올라가면 저항이 커져 스스로 출력을 줄이는 특성이 있어 과열 위험이 낮고, 최근 제품은 리모컨·타이머·온도조절이 붙는다. 욕실처럼 습하고 좁은 공간에는 방수(IPX4) 등급 제품이 따로 있다.
카본 히터는 탄소 발열체의 원적외선 복사열을 쓴다. 바람이 없어 조용하고, 복사열이라 사람 몸에 직접 닿는 거리(1~2m)에서 효율이 좋다. 넓은 방 전체를 데우는 용도보다는 책상 아래, 소파 옆처럼 국소 난방에 맞는다.
전기요는 발열선이 들어간 매트로, 소비전력이 200W 안팎으로 가장 낮다. 방 전체를 데우지는 못하지만 "발이 시려서 못 견디는" 상황을 가장 싸게 해결한다.

2. 오늘 쿠팡에서 실제로 팔리는 제품 4종 (2026-11-24 08:50 KST 기준)
한일전기 타이머 라디에이터 11핀 HOR-H11 — 189,000원 → 119,000원(37% 할인). 동파방지·타이머가 붙은 이동식 11핀. 리뷰 51개, 평점 4.5.
신일 세라믹 히터 SEH-GD200CR — 110,000원 → 52,510원(52% 할인). 스탠드형 세라믹 히터, 리뷰 796개에 평점 4.5로 이번 비교에서 가장 리뷰가 많다. 좁은 방이나 출근 직후 30분처럼 "짧게 데울 때" 가격 대비 만족도가 높은 구간이다.
신일 PTC 욕실 온풍기 SEH-2W180T — 159,000원 → 79,000원(50% 할인). 제품명에 2,000W·IPX4 방수 등급이 표기된 벽걸이 겸용 모델이다. 화장실·현관처럼 짧게 쓰는 공간에 맞는다. 2,000W를 하루 1시간만 써도 한 달 60kWh, 2단계 기준 1만3,716원이다.
신일 카본 히터 히트타워 — 118,000원. 카본 발열 히트타워형으로 리뷰 154개 평점 5. 바람이 없는 복사열이라 책상 옆·소파 옆 국소 난방에 어울린다.
가격은 2026년 11월 24일 오전 쿠팡 검색 화면에 노출된 값이고, 쿠폰·와우할인·카드할인에 따라 달라진다.

3. 전기요금을 줄이는 다섯 가지 (효과 큰 순서)
첫째, 국소 난방으로 바꾸는 것. 2,000W 라디에이터 한 대를 6시간씩 켜는 대신, 200W 전기요 하나와 600W 히터를 조합하면 같은 시간에 108kWh 수준으로 떨어진다. 거실 전체를 데우는 대신 앉아 있는 자리만 데우는 방식이다.
둘째, 타이머와 온도조절. 22도에 맞추고 자동으로 꺼지게 하면 실제 가동 시간이 30~40% 줄어든다. 요금은 가동 시간에 정비례한다.
셋째, 누진 구간을 넘지 않는 것. 400kWh를 넘는 순간 kWh당 단가가 214.6원에서 307.3원으로 뛴다. 난방기를 켜는 달에는 다른 전기 사용(건조기·식기세척기)을 낮에 몰아 쓰거나 주 1회 줄이는 편이 낫다.
넷째, 문풍지·커튼·단열. 창문으로 빠지는 열을 막으면 같은 소비전력으로 체감 온도가 올라간다. 난방기 출력을 낮출 수 있는 가장 싼 방법이다.
다섯째, 대기전력 차단. 멀티탭 스위치를 끄는 것만으로 대기전력 1~3W가 사라진다. 한 달 2kWh 수준이지만, 겨울철 3~4개월이면 무시할 숫자는 아니다.

4. 겨울 데스크 셋업과 함께 보면
재택 근무 자리라면 발밑 200W 전기요와 600W 세라믹 히터, 손목용 소형 히터 조합이 라디에이터 한 대보다 요금이 낮다. 네이버 크리에이터샵(재남픽)의 '겨울 재택 데스크 셋업' 컬렉션에 모니터암·버티컬마우스·충전기와 함께 이런 소형 난방 아이템을 모아두었다. 데스크 주변 8종을 한 번에 비교하고 싶다면 cshop.naver.com/jaenam에서 볼 수 있다.

한 줄 정리
난방기 선택의 기준은 "빨리 따뜻해지는가"가 아니라 "몇 W를 몇 시간 쓰는가"다. 2,000W는 하루 6시간이면 한 달 8만원대, 600W는 2만원대, 200W는 1만원 아래다. 여기에 누진 구간이 붙으면 3만원 이상 차이가 더 벌어진다. 방 전체를 데워야 한다면 라디에이터, 짧게 한 곳만 데운다면 세라믹·PTC·카본, 발이 문제라면 전기요가 답이다."""

EN_DESC = """The electricity bill from a space heater is arithmetic, not marketing. Multiply the rated wattage by the hours you run it, divide by 1,000 to get kWh, then apply Korea's residential tariff. As of the fourth quarter of 2026, KEPCO's residential low-voltage tariff runs 120.0 won/kWh for the first 200 kWh (base fee 910 won), 214.6 won for 201-400 kWh (1,600 won), and 307.3 won above 400 kWh (7,300 won). On top of that come a 9.0 won/kWh climate levy and a 5.0 won fuel adjustment, then 10% VAT and a 2.7% industry fund. From December to February, any use above 1,000 kWh is charged the 736.2 won/kWh "super user" rate.

The tier structure is what actually stings. A heater running six hours a day for 30 days is 180 hours: 360 kWh for a 2,000W unit, 180 kWh for a 1,000W unit. A household already using 200 kWh a month is pushed straight into the third tier at 307.3 won. The same 360 kWh costs about 82,300 won calculated at the second-tier rate and about 115,700 won at the third-tier rate (energy, climate and fuel charges only, before VAT). That step is what people mean by a winter bill shock.

A 600W unit uses 108 kWh over the same 180 hours, roughly 24,700 won. What decides the bill is wattage, hours, and where the household sits on the tier ladder — not the heating technology on the box.

1. How the four types differ
Oil-filled radiators heat oil inside metal fins and radiate and convect the warmth. They are silent, take 10-20 minutes to warm up and hold heat for a long time; 11-fin models are common and draw about 2,000W. Good for living rooms and bedrooms that stay on for hours.
Ceramic heaters push air across a ceramic element with a fan. They feel warm within seconds and are pleasant when the air reaches you, but the fan is audible and the warmth is local. Most draw 1,000-2,000W.
PTC fan heaters are an improved ceramic design: the PTC element raises its resistance as it heats, limiting output and reducing overheating risk, and current models add remotes, timers and thermostats. Bathroom models carry an IPX4 water-resistance rating.
Carbon heaters use far-infrared radiation from a carbon element. There is no fan and no noise, and radiation works best within one to two metres, so they suit a spot under a desk or beside a sofa rather than a whole room.
Electric blankets and mats use a heating wire and draw around 200W — the cheapest way to fix cold feet without heating the room.

2. Four heaters actually on sale today (Coupang, 24 Nov 2026, 08:50 KST)
Hanil Electric 11-fin timer radiator HOR-H11 — 189,000 won, now 119,000 won (37% off). Portable, anti-freeze and timer functions, 4.5 stars from 51 reviews.
Shinil ceramic heater SEH-GD200CR — 110,000 won, now 52,510 won (52% off). A stand ceramic heater with 796 reviews at 4.5 stars, the most-reviewed model here; strong value for heating a small room for short bursts.
Shinil PTC bathroom fan heater SEH-2W180T — 159,000 won, now 79,000 won (50% off). The listing specifies 2,000W and IPX4 water resistance, and it works wall-mounted or freestanding for bathrooms and entryways. Even one hour a day at 2,000W is 60 kWh a month, about 13,700 won at the second tier.
Shinil carbon heat tower — 118,000 won, 154 reviews at five stars. Fanless radiant heat for a desk or sofa.
Prices are what appeared on Coupang's search page on the morning of 24 November 2026 and move with coupons and card discounts.

3. Five ways to cut the bill (in order of effect)
First, heat a spot, not a room. Swap six hours of a 2,000W radiator for a 200W electric mat plus a 600W heater and the same hours come to about 108 kWh.
Second, use timers and thermostats. Setting 22°C with auto shut-off typically cuts run time by 30-40%, and the bill scales with run time.
Third, stay out of the top tier. Once monthly use passes 400 kWh the marginal rate jumps from 214.6 to 307.3 won. In heating months, shift or reduce other heavy loads such as dryers and dishwashers.
Fourth, stop the leaks: window sealing, thicker curtains and door draught strips raise perceived warmth at the same wattage — the cheapest way to lower output.
Fifth, kill standby power. Switching off a multi-tap removes 1-3W per device, a couple of kWh a month that adds up over a winter.

4. For a winter desk setup
If you work from home, a 200W foot mat, a 600W ceramic heater and a small wrist heater usually cost less to run than one radiator. The winter desk collection in the Naver Creator Shop (JAENAM PICK) gathers these small heaters alongside monitor arms, a vertical mouse and chargers; all eight items are at cshop.naver.com/jaenam.

Bottom line
Choose a heater by how many watts it draws for how many hours, not by how fast it feels warm. At six hours a day, 2,000W is about 82,000 won a month, 600W about 25,000 won and 200W under 10,000 won — and the tier ladder can add 30,000 won or more on top."""

JA_DESC = """電気ストーブの電気代は宣伝文句ではなく計算で決まる。消費電力(W)を使用時間に掛けて1,000で割ればkWhになり、そこに住宅用電気料金の単価を掛ければ終わりだ。2026年第4四半期の韓国電力・住宅用電力(低圧)の料金表は、200kWh以下が1段階120.0ウォン/kWh(基本料金910ウォン)、201〜400kWhが2段階214.6ウォン(1,600ウォン)、400kWh超が3段階307.3ウォン(7,300ウォン)。これに気候環境料金9.0ウォン/kWhと第4四半期の燃料費調整単価5.0ウォンが加わり、最後に付加価値税10%と電力産業基盤基金2.7%が付く。12月〜2月に1,000kWhを超えた分には「スーパーユーザー」料金736.2ウォン/kWhが適用される。

効いてくるのは累進構造だ。暖房機器を1日6時間、30日使うと180時間。2,000Wなら360kWh、1,000Wなら180kWhを余分に使う。すでに月200kWhを使っている家庭では、2,000Wの暖房器は使用量を一気に3段階(307.3ウォン)へ押し上げる。同じ360kWhでも2段階単価なら約8万2,300ウォン、3段階単価なら約11万5,700ウォン(電力量+気候環境+燃料費調整、付加価値税別)。「電気代爆弾」の正体はたいていこの段差だ。

一方600W以下の製品なら、同じ180時間で108kWh、約2万4,700ウォン。電気代を決めるのは「発熱技術」ではなく、消費電力と使用時間、そしてその家庭の累進位置である。

1. 方式ごとの違い
オイルラジエーターは内部のオイルを温めて金属フィンで熱を広げる。ファンがなく静かで、温まるまで10〜20分かかるが熱が長持ちする。11フィン型が一般的で消費電力は約2,000W。リビングや寝室で長時間つける用途に向く。
セラミックヒーターはセラミック発熱体にファンで風を送る。電源を入れると数秒で温風が出て、体に当たると「すぐ暖かい」。ただしファン音があり、風が当たる場所だけが暖かい。1,000〜2,000W級が多い。
PTC暖房機はセラミックの改良型で、温度が上がると抵抗が増えて出力を抑えるため過熱リスクが低い。最近のモデルはリモコン・タイマー・温度調節付き。浴室向けにはIPX4の防水モデルがある。
カーボンヒーターは炭素発熱体の遠赤外線放射熱を使う。風がなく静かで、放射熱は1〜2mの距離で効率的。部屋全体より机の下やソファ横の局所暖房に向く。
電気毛布・ホットマットは発熱線入りで消費電力は約200W。部屋は暖まらないが「足が冷たい」問題を最も安く解決する。

2. 今日クーポン(クーパン)で実際に売られている4製品(2026-11-24 08:50 KST)
ハニル電機 タイマーラジエーター11フィン HOR-H11 — 189,000ウォン→119,000ウォン(37%割引)。凍結防止・タイマー付き移動式。レビュー51件、4.5。
シンイル セラミックヒーター SEH-GD200CR — 110,000ウォン→52,510ウォン(52%割引)。レビュー796件・4.5で今回最多。狭い部屋を短時間で暖める用途に価格対効果が高い。
シンイル PTC浴室暖房機 SEH-2W180T — 159,000ウォン→79,000ウォン(50%割引)。商品名に2,000W・IPX4と明記された壁掛け兼用モデル。1日1時間でも月60kWh、2段階単価で約1万3,700ウォン。
シンイル カーボンヒートタワー — 118,000ウォン、レビュー154件・5。風のない放射熱で机やソファ横の局所暖房に。
価格は2026年11月24日午前のクーパン検索画面の表示価格で、クーポンやカード割引により変わる。

3. 電気代を下げる5つ(効果が大きい順)
第一に、部屋ではなく一点を暖める。2,000Wラジエーターを6時間つける代わりに、200Wホットマットと600Wヒーターの組み合わせなら同じ時間で約108kWh。
第二に、タイマーと温度調節。22度で自動オフにすると稼働時間が30〜40%減る。料金は稼働時間に比例する。
第三に、累進段階を越えないこと。月400kWhを超えると単価が214.6ウォンから307.3ウォンに跳ね上がる。暖房を使う月は乾燥機や食器洗浄機の使用をずらす。
第四に、隙間と断熱。窓の隙間テープ、厚手のカーテン、ドアの風除けで体感温度が上がり、同じ消費電力で出力を下げられる。
第五に、待機電力の遮断。電源タップのスイッチを切るだけで1〜3Wが消える。

4. 冬のデスクセットアップと一緒に
在宅勤務なら、200Wの足元マット、600Wのセラミックヒーター、小型の手元ヒーターの組み合わせがラジエーター1台より安い。NAVERクリエイターショップ「ジェナムピック」の冬の在宅デスクコレクションに、モニターアーム・縦型マウス・充電器と一緒にまとめてある(cshop.naver.com/jaenam)。

まとめ
暖房器は「どれだけ早く暖かく感じるか」ではなく「何Wを何時間使うか」で選ぶ。1日6時間なら2,000Wは月約8万2,000ウォン、600Wは約2万5,000ウォン、200Wは1万ウォン未満。累進段階が加われば差はさらに3万ウォン以上広がる。"""

ZH_DESC = """电暖器的电费是算出来的，不是广告写出来的。把额定功率(W)乘以每天使用小时数，再除以1,000得到kWh，然后乘以韩国的住宅用电单价即可。2026年第四季度韩国电力住宅用（低压）电价为：200kWh以下第一档120.0韩元/kWh（基本费910韩元），201~400kWh第二档214.6韩元（1,600韩元），400kWh以上第三档307.3韩元（7,300韩元）；再加上气候环境费9.0韩元/kWh与第四季度燃料费调整单价5.0韩元，最后加10%增值税和2.7%电力产业基础基金。12月至2月用电超过1,000kWh的部分适用736.2韩元/kWh的"超级用户"电价。

真正扎手的是阶梯结构。取暖器每天开6小时、一个月就是180小时：2,000W机型多用360kWh，1,000W机型多用180kWh。本来每月已用200kWh的家庭，一台2,000W取暖器会直接把用电量推入第三档（307.3韩元）。同样是360kWh，按第二档单价约8.23万韩元，按第三档单价则约11.57万韩元（仅含电力量、气候环境与燃料费调整，不含增值税）。所谓"电费炸弹"，多半就是这一级台阶。

而600W以下的机型，同样180小时只用108kWh，约2.47万韩元。决定电费的不是"发热技术"，而是功率、使用时长，以及这个家庭所处的阶梯位置。

1. 四类取暖方式的差别
油汀（充油式散热器）加热内部导热油，通过金属散热片扩散热量。没有风扇，安静；升温需要10~20分钟，但保温持久。常见11片机型，功率约2,000W，适合客厅、卧室长时间开启。
陶瓷暖风机用风扇把热风吹过陶瓷发热体，开机数秒即有热风，直接吹到身上"马上变暖"。缺点是风扇声，且只有被吹到的位置暖。多为1,000~2,000W。
PTC暖风机是陶瓷式的改良版：PTC元件升温后电阻增大、自动降低输出，过热风险更低，近期机型多配遥控、定时与温控。浴室款式具备IPX4防水等级。
碳素取暖器利用碳发热体的远红外辐射热，无风、安静，辐射热在1~2米距离最有效，适合桌下、沙发旁的局部取暖，而非整间房。
电热毯与电热垫靠发热线，功率约200W，是最便宜地解决"脚冷"的方案。

2. 今天实际在售的四款（Coupang，2026-11-24 08:50 KST）
Hanil电机 11片定时油汀 HOR-H11 — 189,000韩元→119,000韩元（37%折扣），防冻与定时功能，51条评价4.5分。
Shinil 陶瓷取暖器 SEH-GD200CR — 110,000韩元→52,510韩元（52%折扣），796条评价4.5分，本次评价最多，适合小房间短时取暖，性价比突出。
Shinil PTC浴室暖风机 SEH-2W180T — 159,000韩元→79,000韩元（50%折扣），商品页标注2,000W与IPX4防水，壁挂/落地两用；每天1小时即每月60kWh，第二档约1.37万韩元。
Shinil 碳素取暖塔 — 118,000韩元，154条评价5分，无风辐射热，适合桌旁、沙发旁。
价格为2026年11月24日上午Coupang搜索页显示价，会随优惠券与银行卡折扣变化。

3. 降低电费的五个方法（按效果排序）
第一，暖"点"不暖"面"。把2,000W油汀开6小时，换成200W电热垫加600W取暖器，同样时长约108kWh。
第二，用定时和温控。设定22度并自动关机，运行时间通常减少30~40%，而电费与运行时间成正比。
第三，不要跨过阶梯。月用电超过400kWh，边际单价从214.6韩元跳到307.3韩元；取暖月份应错开或减少烘干机、洗碗机等大功率用电。
第四，堵住漏风。窗户密封、厚窗帘、门底挡风条可以在同样功率下提高体感温度，是最便宜的降功率办法。
第五，切断待机功耗。关掉插排开关，每台设备可省1~3W，一个冬天累积起来并不小。

4. 与冬季桌面搭配
居家办公时，200W脚下电热垫、600W陶瓷取暖器加小型手部取暖器的组合，通常比一台油汀更省。NAVER创作者店铺"JAENAM PICK"的冬季居家桌面合辑里，把这些小型取暖件与显示器支架、垂直鼠标、充电器放在一起，8件商品可在 cshop.naver.com/jaenam 查看。

一句话总结
选取暖器看的是"多少瓦用多少小时"，而不是"多快觉得暖"。每天6小时计算，2,000W约每月8.2万韩元，600W约2.5万韩元，200W不到1万韩元；若叠加阶梯电价，差距还会扩大到3万韩元以上。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "store": "쿠팡",
    "priceKrw": 119000,
    "releaseDate": "2026-11-24",
    "rating": 4.5,
    "imageUrl": C,
    "images": [G1, G2, G3],
    "affiliateUrl": q("겨울 난방기"),
    "affiliatePlatform": "Coupang",
    "exampleItems": [
        {
            "name": "한일전기 타이머 라디에이터 11핀 HOR-H11",
            "brand": "한일전기",
            "priceKrw": 119000,
            "imageUrl": "/images/products/heater-hanil-radiator.jpg",
            "url": q("한일전기 라디에이터 11핀 HOR-H11"),
            "category": "라디에이터",
        },
        {
            "name": "신일 세라믹 히터 SEH-GD200CR",
            "brand": "신일",
            "priceKrw": 52510,
            "imageUrl": "/images/products/heater-shinil-ceramic.jpg",
            "url": q("신일 세라믹 히터 SEH-GD200CR"),
            "category": "세라믹 히터",
        },
        {
            "name": "신일 PTC 욕실 온풍기 SEH-2W180T (2,000W·IPX4)",
            "brand": "신일",
            "priceKrw": 79000,
            "imageUrl": "/images/products/heater-shinil-ptc-bathroom.jpg",
            "url": q("신일 PTC 욕실 온풍기 SEH-2W180T"),
            "category": "PTC 온풍기",
        },
        {
            "name": "신일 카본 히터 히트타워",
            "brand": "신일",
            "priceKrw": 118000,
            "imageUrl": "/images/products/heater-shinil-carbon.jpg",
            "url": q("신일 카본 히터 히트타워"),
            "category": "카본 히터",
        },
    ],
    "i18n": {
        "ko": {
            "title": "겨울 난방비, 온풍기와 라디에이터 중 뭐가 덜 나올까? 소비전력으로 계산해봤다",
            "summary": "2,000W 난방기를 하루 6시간 한 달 켜면 360kWh. 2026년 4분기 한전 주택용 요금표와 누진 구간으로 계산하면 8만2천원에서 11만5천원까지 벌어집니다. 방식별 차이와 실제 판매 제품 4종 가격까지 정리했습니다.",
            "description": KO_DESC,
            "tasteReview": [
                "2,000W·하루 6시간·30일 = 360kWh → 2단계 단가 8만2,296원, 3단계 단가 11만5,668원(부가세 제외)",
                "600W는 같은 시간 108kWh로 2만4,689원, 200W 전기요는 36kWh로 8,230원",
                "실제 판매 4종: 한일 11핀 라디에이터 119,000원(37%↓), 신일 세라믹 히터 52,510원(52%↓)",
                "결론은 '발열 기술'이 아니라 '몇 W를 몇 시간' — 누진 구간이 요금을 가른다",
            ],
            "tips": "가격은 2026-11-24 08:50 KST 쿠팡 노출가이며, 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있습니다.",
        },
        "en": {
            "title": "Radiator, Ceramic or PTC: What Winter Heating Actually Costs in Korea",
            "summary": "A 2,000W heater running six hours a day for a month uses 360 kWh. With Korea's Q4 2026 residential tariff and the tier ladder, that is anywhere from 82,000 to 116,000 won. The four heater types, the maths, and four models on sale today.",
            "description": EN_DESC,
            "tasteReview": [
                "2,000W × 6h × 30d = 360 kWh: 82,296 won at the second-tier rate, 115,668 won at the third (before VAT)",
                "600W uses 108 kWh over the same hours (24,689 won); a 200W electric mat uses 36 kWh (8,230 won)",
                "On sale today: Hanil 11-fin radiator 119,000 won (37% off), Shinil ceramic heater 52,510 won (52% off)",
                "The bill is set by watts, hours and the tier you land in — not by the heating element",
            ],
            "tips": "Prices are Coupang listings at 08:50 KST on 24 Nov 2026; this post contains affiliate links and may earn a commission.",
        },
        "ja": {
            "title": "冬の暖房費、セラミックヒーターとラジエーターはどちらが安い？消費電力で計算した",
            "summary": "2,000Wの暖房器を1日6時間・30日使うと360kWh。2026年第4四半期の韓国電力住宅用料金と累進段階で計算すると8万2千ウォンから11万5千ウォンまで開きます。方式別の違いと実際に売られている4製品の価格まで整理しました。",
            "description": JA_DESC,
            "tasteReview": [
                "2,000W・1日6時間・30日＝360kWh → 2段階単価で8万2,296ウォン、3段階単価で11万5,668ウォン(付加価値税別)",
                "600Wは同じ時間で108kWh・2万4,689ウォン、200Wのホットマットは36kWh・8,230ウォン",
                "実際の販売4製品: ハニル11フィンラジエーター119,000ウォン(37%↓)、シンイル セラミック52,510ウォン(52%↓)",
                "結論は「発熱技術」ではなく「何Wを何時間」 — 累進段階が料金を分ける",
            ],
            "tips": "価格は2026-11-24 08:50 KSTのクーパン表示価格です。本記事はアフィリエイトリンクを含み、手数料を受け取る場合があります。",
        },
        "zh": {
            "title": "油汀、陶瓷暖风机还是PTC？韩国冬季取暖费按功率算给你看",
            "summary": "2,000W取暖器每天6小时、一个月即360kWh。按2026年第四季度韩国电力住宅电价和阶梯结构计算，费用从8.23万韩元到11.57万韩元不等。四种类型的差别与今天在售的四款机型价格一并整理。",
            "description": ZH_DESC,
            "tasteReview": [
                "2,000W×6小时×30天=360kWh：第二档单价8.23万韩元，第三档单价11.57万韩元（不含增值税）",
                "600W同样时长108kWh（2.47万韩元），200W电热垫36kWh（8,230韩元）",
                "今日在售：Hanil 11片油汀11.9万韩元（37%折扣）、Shinil陶瓷取暖器52,510韩元（52%折扣）",
                "结论不是“发热技术”，而是“多少瓦用多少小时”——阶梯电价决定差价",
            ],
            "tips": "价格为2026-11-24 08:50 KST Coupang显示价；本文含联盟链接，可能获得佣金。",
        },
    },
}

headers = {
    "apikey": SUPABASE_KEY,
    **_bearer_header(SUPABASE_KEY),
    "Content-Type": "application/json",
    "Prefer": "return=representation",
}

check_url = f"{SUPABASE_URL}/rest/v1/posts?slug=eq.{SLUG}&select=id"
req = urllib.request.Request(check_url, headers=headers)
with urllib.request.urlopen(req) as resp:
    existing = json.loads(resp.read().decode("utf-8"))

if existing:
    upd = f"{SUPABASE_URL}/rest/v1/posts?id=eq.{existing[0]['id']}"
    payload = json.dumps({"data": POST}).encode("utf-8")
    urllib.request.urlopen(urllib.request.Request(upd, data=payload, headers=headers, method="PATCH"))
    print(f"[+] Updated: {SLUG}")
else:
    payload = json.dumps({"slug": SLUG, "data": POST}).encode("utf-8")
    r = urllib.request.urlopen(urllib.request.Request(f"{SUPABASE_URL}/rest/v1/posts", data=payload, headers=headers, method="POST"))
    print(f"[+] Inserted: {SLUG} ({r.status})")

try:
    urllib.request.urlopen(urllib.request.Request(REVALIDATE_URL), timeout=90)
    print("[+] Revalidated")
except Exception as e:
    print(f"[-] Revalidate error: {e}")
