#!/usr/bin/env python3
"""쿠팡 쿠블프(로켓직구) 2026 실측 5종 → Supabase posts + ISR revalidate (4개국어).

근거
 - 행사: 연합뉴스 2026-11-23 — 로켓직구 '쿠블프' 11/23~12/1(9일), 미국·일본·유럽·중국·홍콩 약 3만 개,
   선착순 메가딜·하루특가·990원 오픈런 990딜, 행사 상품 2개 이상 10% 할인 쿠폰, 일본 직구 7,000원 쿠폰
 - 가격·리뷰·배송: 쿠팡 검색 화면 2026-11-25 11:40~12:05 KST 직접 확인
 - 비교가: 롯데ON(바샤커피 42,000원), 하카타몰(이치란 34,500원+배송 5,900원), 29CM(어그 298,000원)
 - 사진: 쿠팡·롯데ON·WAFUU·29CM 실제 상품 이미지 4장 (AI 생성 0장)
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
SLUG = "coupang-kubleop-rocket-direct-2026"

K = "https://www.coupang.com/np/search?q="
TAG = "&lptag=AF9412775"


def q(s):
    return K + quote(s) + TAG


C = "/images/products/bf-coupang-osmall-immun.jpg"
G1 = "/images/products/bf-coupang-bacha-dripbag.jpg"
G2 = "/images/products/bf-coupang-ichiran-ramen.jpg"
G3 = "/images/products/bf-coupang-ugg-classic-short.jpg"

KO_DESC = """쿠팡 로켓직구 행사 '쿠블프'가 11월 23일 시작해 12월 1일에 끝난다. 9일짜리 행사다. 미국·일본·유럽·중국·홍콩에서 들어오는 상품 약 3만 개가 걸려 있고, 선착순 메가딜과 하루특가, 990원부터 시작하는 오픈런 '990딜'이 매일 붙는다. 행사 상품을 2개 이상 담으면 10% 할인 쿠폰이 적용되고, 일본 직구용으로는 7,000원 쿠폰이 따로 나온다.
문제는 '직구 = 싸다'가 올해는 절반만 맞다는 것이다. 같은 브랜드라도 국내 재고와 해외 발송 상품의 가격이 뒤집히는 경우가 흔하고, 도착일이 12월로 넘어가면 연말 선물로는 쓸 수 없다. 그래서 11월 25일 오전 쿠팡 화면에서 실제로 확인한 다섯 개만 골라 직구가와 국내가를 나란히 놓았다.

1. 오쏘몰 이뮨 — 직구 이득이 가장 작은 품목
오쏘몰 이뮨 멀티비타민 30회분은 로켓직구로 96,480원 정가에 17% 할인한 80,070원이다. 독일에서 발송돼 11월 28일(토) 도착 예정이고, 리뷰 7,187개에 별점 5.0이다. 7회분짜리는 29,800원에서 10% 할인한 26,820원이다.
같은 제품을 국내 로켓배송으로 사면 30회분 83,700원, 동아제약 정품 표기 상품은 87,900원이다. 직구(80,070원)와 국내(83,700원) 차이는 3,630원, 4.3%다. 배송을 사흘 더 기다려서 아끼는 돈이 커피 한 잔 값이라는 뜻이다. 오쏘몰은 '직구로 사면 무조건 이득'인 품목이 아니다. 다만 2개 이상 10% 쿠폰이 붙으면 30회분 두 통이 144,126원까지 내려가 국내가(167,400원)보다 13.9% 싸진다. 쿠폰을 못 받으면 국내 재고가 낫다.

2. 바샤커피 — 이번 행사에서 가장 확실한 차이
바샤커피 밀라노 모닝 드립백 12개입은 로켓직구로 46,680원 정가에 34% 할인한 30,580원이다. 홍콩에서 발송되고 11월 28일 도착 예정이다. 리뷰 1,685개, 별점 5.0.
같은 상품을 롯데백화점 공식 판매처(롯데ON)에서는 42,000원에 판다. 11,420원, 27.2% 차이다. 바샤커피는 국내 정식 수입가가 높게 잡혀 있는 브랜드라 직구 이득이 큰 편이다. 12개입 두 통을 10% 쿠폰으로 묶으면 55,044원, 통당 27,522원까지 내려간다. 선물용으로 여러 통 살 계획이라면 이 조합이 이번 주 가장 계산이 좋다.

3. 이치란 라멘 — 직구가 더 비싼 반례
이치란 하카타 얇은 면 스트레이트 2개입은 21,480원에서 15% 할인한 18,250원, 일본에서 11월 28일 도착이다. 그런데 5인분 645g 돈코츠는 로켓직구 37,400원(23% 할인)에 도착일이 12월 11일이다.
같은 5인분을 국내 로켓배송으로 사면 31,900원이고 내일 도착한다. 일본 현지 배송대행인 하카타몰에서는 34,500원에 배송비 5,900원이 붙어 40,400원이다. 즉 이치란 5인분은 쿠팡 국내 재고가 가장 싸고 가장 빠르다. 라멘처럼 중량이 나가고 마진이 얇은 식품은 직구 라인업에 있어도 직구가 답이 아니다.

4. 어그 클래식 쇼트 — 가격 차이가 정품 차이인지부터 봐야
어그 클래식 쇼트 II 체스트넛(1016223)은 쿠팡에서 100,000원, 12월 5일 도착 예정인 해외 발송 상품이 최저가로 올라와 있다. 같은 모델을 29CM 공식 수입 정품으로 사면 298,000원이다(현재 품절). 3배 차이다. 이 차이는 할인이 아니라 판본 차이다. 병행수입·구시즌·재고 처리 상품일 수 있으므로 정품 보증과 교환 조건을 확인해야 한다.
로켓직구 라인업에는 오즈웨어어그 클래식 울트라 미니(139,900원 → 66,490원, 52% 할인)가 홍콩 발송 11월 28일 도착으로 올라와 있다. 오즈웨어는 어그와 다른 호주 브랜드다. 이름이 비슷하다고 같은 신발로 읽으면 안 된다.

5. 샥즈 오픈런 프로 2 — 이번 행사 최대 할인폭
샥즈 오픈런 프로 2(S820)는 로켓직구로 249,000원 정가에 44% 할인한 139,000원이다. 중국에서 발송돼 12월 1일 도착 예정이다. 국내 정품은 최저 185,000원(25% 할인, 내일 도착), 브랜드샵 단독세트는 2년 AS가 붙어 236,550원이다. 직구가 국내 최저가보다 46,000원, 24.9% 싸다.
대신 조건이 다르다. 직구 상품에는 국내 2년 무상 AS가 붙지 않고, 하자 발생 시 반품·교환 절차가 해외 발송 상품 기준으로 돌아간다. 12월 1일 도착 예정이라는 점도 연말 일정에는 늦다. 운동용으로 매일 쓰고 AS를 중요하게 본다면 185,000원 국내 정품이, 가격이 우선이고 AS를 포기할 수 있다면 139,000원 직구가 맞다.

6. 쿠폰 두 장 겹치는 계산
쿠블프의 쿠폰은 두 종류다. 행사 상품 2개 이상 구매 시 10% 할인 쿠폰, 일본 직구용 7,000원 쿠폰이다. 실제 결제액으로 계산해 보면 이렇다.
샥즈 오픈런 프로 2 두 개를 10% 쿠폰으로 묶으면 278,000원이 250,200원, 개당 125,100원이다.
바샤커피 12개입 두 통은 61,160원이 55,044원이다.
이치란 하카타 2개입 두 세트는 36,500원이 32,850원이다.
일본 직구 7,000원 쿠폰은 일본 발송 상품에만 붙으므로 이치란·바샤커피 같은 일본·홍콩 발송 상품에 쓰는 게 자연스럽다. 다만 쿠폰마다 최소 구매금액과 할인 한도가 따로 걸릴 수 있으므로, 결제 화면에서 최종 금액을 확인한 뒤 주문하는 게 순서다. 쿠폰은 선착순으로 소진되는 경우가 있어 오전에 담아두는 편이 안전하다.

7. 결제 전 확인할 세 가지
첫째, 도착일이다. 이번에 확인한 직구 상품은 대부분 11월 28일~12월 11일 도착이다. 12월 1일 이후 도착하는 상품은 연말 선물용으로 쓰기 어렵다.
둘째, AS와 반품 창구다. 로켓직구는 해외 발송 상품이라 국내 재고와 반품 절차가 다르다. 무상 AS 기간이 붙는지 상품 페이지에서 확인해야 한다.
셋째, 관부가세다. 미국에서 오는 특송 목록통관 물품은 200달러(약 26만~27만 원, 환율에 따라 변동) 이하까지 관세와 부가세가 면제된다. 다만 의약품·건강기능식품·식품류는 미국발이어도 150달러 기준이 적용되고, 한도를 넘으면 넘은 금액만이 아니라 물품가격 전체에 세금이 붙는다. 이번 5종 중 오쏘몰(건강기능식품)은 150달러 기준, 나머지 잡화는 200달러 기준으로 봐야 한다.

한 줄 정리
쿠블프는 12월 1일까지 9일이다. 이번에 실제로 이득이 큰 품목은 바샤커피(27.2% 저렴)와 샥즈 오픈런 프로 2(24.9% 저렴)였고, 오쏘몰(4.3%)과 이치란(-17.2%, 국내가 더 쌈)은 직구가 답이 아니었다. 어그처럼 3배 차이가 나는 상품은 할인이 아니라 판본 차이일 수 있으니 정품 보증부터 확인해야 한다. 쿠폰은 2개 이상 10%가 핵심이고, 결제 화면에서 도착일과 최종 금액을 함께 확인하는 것이 이번 주에 돈을 지키는 방법이다."""

EN_DESC = """Coupang's Rocket Direct Purchase event, "Kubleop," runs nine days from November 23 to December 1. About 30,000 items ship in from the US, Japan, Europe, China and Hong Kong, with first-come mega deals, daily deals and an "open run" 990-won tier added every day. Two or more event items trigger a 10% coupon, and Japanese direct purchases get a separate 7,000-won coupon.
The catch: "direct purchase means cheaper" is only half true this year. The same brand regularly flips between domestic stock and overseas shipping, and an arrival date that slips into December rules out a year-end gift. So we checked five products on Coupang on the morning of November 25 and put the direct-purchase price next to the domestic one.

1. Orthomol Immun — the smallest gain
A 30-day box of Orthomol Immun is 80,070 won, 17% off the 96,480-won list, shipped from Germany and due Saturday, November 28. It carries 7,187 reviews at 5.0. The 7-day box is 26,820 won, 10% off 29,800 won.
Buy the same 30-day box from domestic Rocket Delivery and it is 83,700 won, or 87,900 won for the Dong-A Pharmaceutical import. The gap is 3,630 won, or 4.3% — three extra days of waiting for the price of a coffee. With the two-item 10% coupon, two boxes fall to 144,126 won against 167,400 won domestically, a 13.9% saving. Without the coupon, domestic stock wins.

2. Bacha Coffee — the clearest gap in the event
Bacha Coffee's Milano Morning drip bags, 12 per box, are 30,580 won, 34% off 46,680 won, shipped from Hong Kong and due November 28, with 1,685 reviews at 5.0.
Lotte Department Store's official seller lists the same box at 42,000 won. That is 11,420 won, or 27.2%. Bacha's official import price is set high here, so the direct route pays off. Two boxes with the 10% coupon come to 55,044 won, 27,522 won each — the best arithmetic in this week's event if you are buying gifts.

3. Ichiran ramen — the counter-example
Ichiran Hakata thin straight noodles, two servings, are 18,250 won, 15% off 21,480 won, arriving November 28 from Japan. But the 5-serving 645g tonkotsu pack is 37,400 won (23% off) with a December 11 arrival.
Domestic Rocket Delivery sells the same 5 servings for 31,900 won, arriving tomorrow. Hakata Mall in Japan lists it at 34,500 won plus 5,900 won shipping, 40,400 won in total. For Ichiran, domestic stock is both cheapest and fastest. Heavy, thin-margin food is on direct-purchase shelves without being a direct-purchase win.

4. UGG Classic Short — check whether the gap is price or product
The UGG Classic Short II in chestnut (1016223) shows 100,000 won on Coupang as the lowest listing, shipped overseas and due December 5. The same model from 29CM as an official import is 298,000 won, currently sold out. That is a threefold gap, and it is a difference in goods, not a discount: parallel imports, older seasons and stock clearance look identical in a search result. Verify the authenticity guarantee and the exchange terms first.
The direct line-up also carries Ozwear UGG Classic Ultra Mini at 66,490 won, 52% off 139,900 won, shipped from Hong Kong and due November 28. Ozwear is an Australian brand, not UGG. A similar name is not the same boot.

5. Shokz OpenRun Pro 2 — the biggest discount in the event
Shokz OpenRun Pro 2 (S820) is 139,000 won, 44% off the 249,000-won list, shipped from China and due December 1. Domestic genuine stock starts at 185,000 won (25% off, arriving tomorrow), and the brand-store set with two years of warranty is 236,550 won. The direct route is 46,000 won, or 24.9%, below the domestic floor.
The terms differ. The direct unit does not carry the domestic two-year free repair service, and defects go through the overseas-shipping return process. A December 1 arrival is also late for year-end plans. Daily training with warranty cover points to the 185,000-won domestic unit; price first and warranty dispensable points to 139,000 won.

6. Stacking the two coupons
Kubleop has two coupons: 10% off two or more event items, and 7,000 won for Japanese direct purchases. In real money: two OpenRun Pro 2 at 278,000 won become 250,200 won, 125,100 won each. Two Bacha boxes go from 61,160 won to 55,044 won. Two Ichiran two-serving sets go from 36,500 won to 32,850 won. The 7,000-won coupon applies only to Japanese shipments, so it fits Ichiran and other Japan-shipped items. Minimum spend and discount caps are set per coupon, so confirm the final amount at checkout; coupons can run out, so filling the cart in the morning is safer.

7. Three checks before paying
First, the arrival date: most direct items here land between November 28 and December 11, and anything after December 1 is a poor year-end gift.
Second, the warranty and return channel: Rocket Direct items are overseas shipments with a different return process, so check whether free repair applies.
Third, duty. US express shipments under the list-clearance rule are duty- and VAT-free up to $200 (roughly 260,000-270,000 won, moving with the exchange rate). Medicines, health supplements and foods fall back to the $150 limit even from the US, and crossing the line taxes the entire value, not just the excess. Of the five items here, Orthomol is a health supplement ($150) while the rest are general goods ($200).

Bottom line
Kubleop ends December 1. The real winners were Bacha Coffee (27.2% cheaper) and Shokz OpenRun Pro 2 (24.9% cheaper); Orthomol (4.3%) and Ichiran (17.2% more expensive than domestic) were not. A threefold gap like UGG's may be a different product rather than a discount, so start with the authenticity guarantee. The two-item 10% coupon is the one that matters, and checking arrival date and final amount together at checkout is how you keep your money this week."""

JA_DESC = """クーパンのロケット直球イベント「クブルフ」は11月23日から12月1日までの9日間です。米国・日本・欧州・中国・香港から約3万点が並び、先着メガディール、日替わり特価、990ウォンからのオープンラン「990ディール」が毎日付きます。対象商品を2点以上買うと10％割引クーポン、日本直球には7,000ウォンクーポンが別に用意されています。
ただし「直球＝安い」は今年は半分しか当たりません。同じブランドでも国内在庫と海外発送で価格が逆転することが多く、到着が12月にずれ込むと年末の贈り物には使えません。そこで11月25日午前のクーパン画面で実際に確認した5点だけを選び、直球価格と国内価格を並べました。

1. オルソモル・イムン — 差が最も小さい商品
オルソモル・イムン30日分はロケット直球で定価96,480ウォンの17％引き、80,070ウォン。ドイツ発送で11月28日（土）到着予定、レビュー7,187件で星5.0です。7日分は29,800ウォンから10％引きの26,820ウォン。
同じ30日分を国内ロケット配送で買うと83,700ウォン、東亜製薬の国内正規品は87,900ウォン。差は3,630ウォン、4.3％です。3日余計に待ってコーヒー1杯分の節約にしかなりません。2点以上10％クーポンを使えば2箱144,126ウォンとなり国内（167,400ウォン）より13.9％安くなりますが、クーポンなしなら国内在庫が勝ちです。

2. バチャコーヒー — 今回最も確実な差
バチャコーヒーのミラノモーニング ドリップバッグ12袋入りは、定価46,680ウォンの34％引きで30,580ウォン。香港発送、11月28日到着予定、レビュー1,685件で星5.0です。
同じ商品をロッテ百貨店の公式販売（ロッテON）では42,000ウォンで売っています。11,420ウォン、27.2％の差です。国内正規輸入価格が高めのブランドなので直球の利得が大きい。2箱を10％クーポンでまとめると55,044ウォン、1箱27,522ウォンまで下がります。

3. 一蘭ラーメン — 直球のほうが高い反例
一蘭の博多細麺ストレート2食入りは21,480ウォンから15％引きの18,250ウォン、日本発送で11月28日到着。ところが5食入り645gの豚骨はロケット直球で37,400ウォン（23％引き）、到着は12月11日です。
同じ5食入りを国内ロケット配送で買うと31,900ウォンで翌日到着。日本の博多モールでは34,500ウォンに送料5,900ウォンで40,400ウォンです。一蘭は国内在庫が最も安く最も速い。重くて利益率の薄い食品は、直球の棚に並んでいても直球が正解ではありません。

4. UGGクラシックショート — 価格差が「商品差」でないか先に見る
UGGクラシックショートII チェスナット（1016223）はクーパン最安が100,000ウォン、海外発送で12月5日到着予定。同じ型番を29CMの公式輸入正規品で買うと298,000ウォン（現在品切れ）。3倍の差です。これは割引ではなく版の違いで、並行輸入・旧シーズン・在庫処分が検索結果では同じに見えます。正規保証と交換条件を先に確認してください。
直球のラインナップにはオズウェアUGGクラシックウルトラミニ（139,900ウォン→66,490ウォン、52％引き、香港発送11月28日到着）もあります。オズウェアはUGGとは別のオーストラリアブランドです。名前が似ていても同じ靴ではありません。

5. Shokzオープンラン プロ2 — 今回最大の割引
Shokzオープンラン プロ2（S820）は定価249,000ウォンの44％引き、139,000ウォン。中国発送で12月1日到着予定です。国内正規品は最安185,000ウォン（25％引き、翌日到着）、ブランドストアの2年保証セットは236,550ウォン。直球は国内最安より46,000ウォン、24.9％安い。
条件は違います。直球品に国内2年無償修理は付かず、不具合は海外発送の返品手続きになります。12月1日到着も年末には遅い。毎日使って保証を重視するなら185,000ウォン、価格優先で保証を諦められるなら139,000ウォンです。

6. クーポン2枚の重ね方
クブルフのクーポンは2種類。2点以上で10％と、日本直球用7,000ウォンです。実際の金額で見ると、オープンラン プロ22台は278,000ウォン→250,200ウォン（1台125,100ウォン）。バチャコーヒー2箱は61,160ウォン→55,044ウォン。一蘭2食×2セットは36,500ウォン→32,850ウォン。7,000ウォンクーポンは日本発送品のみなので一蘭などに向きます。クーポンごとに最低購入額と割引上限があるので、決済画面で最終金額を確認してから注文してください。先着でなくなりやすいため午前にカートへ入れておくのが安全です。

7. 支払い前の確認3点
第一に到着日。今回の直球品は11月28日〜12月11日到着が中心で、12月1日以降は年末の贈り物に使いにくい。
第二に保証と返品窓口。ロケット直球は海外発送で国内在庫と手続きが違うため、無償修理の有無を商品ページで確認します。
第三に関税。米国発の特送リスト通関品は200ドル（約26〜27万ウォン、為替で変動）以下なら関税と付加価値税が免除。ただし医薬品・健康機能食品・食品は米国発でも150ドル基準で、超えると超過分ではなく全額に課税されます。今回の5点ではオルソモルが健康機能食品（150ドル）、残りは一般用品（200ドル）です。

まとめ
クブルフは12月1日まで。実際に得だったのはバチャコーヒー（27.2％安）とShokzオープンラン プロ2（24.9％安）で、オルソモル（4.3％）と一蘭（国内より17.2％高い）は直球が答えではありませんでした。UGGのように3倍差がつく商品は割引ではなく別商品の可能性があるので、正規保証から確認を。2点以上10％クーポンが要点で、決済画面で到着日と最終金額を一緒に見ることが今週のお金の守り方です。"""

ZH_DESC = """Coupang的火箭直购活动「Kubleop」从11月23日持续到12月1日，共9天。来自美国、日本、欧洲、中国和香港的约3万件商品参加，每天还有先到先得的超级特价、每日特价和990韩元起的「990抢购」。购买两件以上活动商品可享10%优惠券，日本直购另有7,000韩元优惠券。
问题是「直购一定便宜」今年只对了一半。同一品牌在国内库存与海外发货之间经常价格倒挂，到货日推到12月就无法当作年末礼物。因此本文只挑出11月25日上午在Coupang页面上实际确认的五件商品，把直购价与国内价并排比较。

1. Orthomol Immun — 差价最小的商品
Orthomol Immun 30日份在火箭直购为80,070韩元，比定价96,480韩元低17%，德国发货，预计11月28日（周六）到达，评论7,187条、评分5.0。7日份从29,800韩元降到26,820韩元（10%）。
同样的30日份在国内火箭配送是83,700韩元，东亚制药国内正品为87,900韩元。差距3,630韩元，仅4.3%，多等三天只省一杯咖啡的钱。若使用两件以上10%优惠券，两盒降到144,126韩元，比国内167,400韩元便宜13.9%；拿不到券则国内库存更划算。

2. Bacha Coffee — 本次活动最确定的差价
Bacha Coffee米兰早晨挂耳咖啡12袋装，直购价30,580韩元，比定价46,680韩元低34%，香港发货，11月28日到达，评论1,685条、评分5.0。
同一商品在乐天百货官方渠道（乐天ON）售价42,000韩元，相差11,420韩元、27.2%。该品牌国内正式进口价偏高，直购收益明显。两盒叠加10%券后为55,044韩元，每盒27,522韩元，是本周送礼最划算的组合。

3. 一兰拉面 — 直购更贵的反例
一兰博多细直面2人份为18,250韩元，比21,480韩元低15%，日本发货11月28日到达。但5人份645g豚骨在火箭直购是37,400韩元（低23%），到货日为12月11日。
同样的5人份在国内火箭配送为31,900韩元，次日到达；日本博多商城为34,500韩元加5,900韩元运费，合计40,400韩元。一兰是国内库存最便宜也最快。厚重、利润薄的食品即使上了直购货架，也不代表直购划算。

4. UGG经典短靴 — 先确认三倍差是价格还是商品
UGG Classic Short II 栗色（1016223）在Coupang最低标价100,000韩元，为海外发货、12月5日到达。同一型号在29CM官方进口正品为298,000韩元（目前售罄）。三倍差距不是折扣而是版本差异，平行进口、旧季、清库存商品在搜索结果里看起来一样。应先确认正品保证与换货条件。
直购专区还有Ozwear UGG经典Ultra Mini（139,900韩元→66,490韩元，52%折扣，香港发货11月28日到达）。Ozwear是与UGG不同的澳大利亚品牌，名字相似不等于同一双靴。

5. Shokz OpenRun Pro 2 — 本次活动最大折扣
Shokz OpenRun Pro 2（S820）定价249,000韩元，直购139,000韩元（-44%），中国发货12月1日到达。国内正品最低185,000韩元（-25%，明日到达），品牌店两年保修套装236,550韩元。直购比国内最低价便宜46,000韩元、24.9%。
但条件不同：直购不附带国内两年免费维修，故障按海外发货退货流程处理，12月1日到达对年末计划也偏晚。每天运动且重视保修选185,000韩元，价格优先且可放弃保修选139,000韩元。

6. 两张优惠券的叠加
Kubleop有两种券：两件以上10%，日本直购7,000韩元。按实付算：OpenRun Pro 2两台 278,000→250,200韩元（每台125,100）；Bacha两盒 61,160→55,044韩元；一兰两套 36,500→32,850韩元。7,000韩元券只适用于日本发货商品，因此一兰等更合适。每张券都有最低消费与折扣上限，请在结算页确认最终金额；优惠券常被抢空，上午先放入购物车更稳妥。

7. 付款前的三项确认
第一，到货日：本次直购商品集中在11月28日至12月11日到达，12月1日以后不适合年末送礼。
第二，保修与退货窗口：火箭直购为海外发货，退货流程与国内库存不同，需在商品页确认是否含免费维修。
第三，关税：美国发特快清单通关商品在200美元（约26万~27万韩元，随汇率变动）以内免关税与增值税；但药品、健康功能食品、食品即使来自美国也适用150美元标准，超额时对全额而非超额部分征税。本文五件中Orthomol属健康功能食品（150美元），其余为一般商品（200美元）。

一句话总结
Kubleop到12月1日。真正划算的是Bacha Coffee（便宜27.2%）与Shokz OpenRun Pro 2（便宜24.9%）；Orthomol（4.3%）和一兰（比国内贵17.2%）并不适合直购。像UGG这样三倍差价可能不是折扣而是不同商品，先看正品保证。两件以上10%券是关键，在结算页同时确认到货日与最终金额，才是本周守住钱包的方法。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "store": "쿠팡",
    "priceKrw": 139000,
    "releaseDate": "2026-11-25",
    "rating": 4.8,
    "imageUrl": C,
    "images": [G1, G2, G3],
    "affiliateUrl": q("쿠팡 쿠블프 로켓직구"),
    "affiliatePlatform": "Coupang",
    "exampleItems": [
        {
            "name": "오쏘몰 이뮨 멀티비타민 30회분",
            "brand": "오쏘몰",
            "priceKrw": 80070,
            "imageUrl": "/images/products/bf-coupang-osmall-immun.jpg",
            "url": q("오쏘몰 이뮨 30회분"),
            "category": "건강기능식품",
        },
        {
            "name": "바샤커피 밀라노 모닝 드립백 12개입",
            "brand": "BACHA COFFEE",
            "priceKrw": 30580,
            "imageUrl": "/images/products/bf-coupang-bacha-dripbag.jpg",
            "url": q("바샤커피 밀라노 모닝 드립백"),
            "category": "커피",
        },
        {
            "name": "이치란 하카타 돈코츠 라멘 5인분 645g",
            "brand": "이치란",
            "priceKrw": 31900,
            "imageUrl": "/images/products/bf-coupang-ichiran-ramen.jpg",
            "url": q("이치란 돈코츠 라멘 5인분"),
            "category": "라면",
        },
        {
            "name": "어그 클래식 쇼트 II 체스트넛 1016223",
            "brand": "UGG",
            "priceKrw": 100000,
            "imageUrl": "/images/products/bf-coupang-ugg-classic-short.jpg",
            "url": q("어그 클래식 쇼트 1016223"),
            "category": "부츠",
        },
    ],
    "i18n": {
        "ko": {
            "title": "쿠블프 로켓직구 12월 1일 마감 — 국내가보다 싼 5종과 10% 쿠폰 겹치는 법",
            "summary": "쿠팡 로켓직구 '쿠블프'는 12월 1일에 끝납니다. 11월 25일 오전 쿠팡에서 직접 확인한 5종을 국내가와 나란히 놓았습니다. 바샤커피는 27.2%, 샥즈 오픈런 프로 2는 24.9% 쌌고, 오쏘몰은 4.3%, 이치란은 국내가가 더 쌌습니다. 2개 이상 10% 쿠폰 조합 계산까지.",
            "description": KO_DESC,
            "tasteReview": [
                "쿠블프 11/23~12/1(9일), 미국·일본·유럽·중국·홍콩 약 3만 개, 990원 오픈런·하루특가",
                "실측: 바샤커피 30,580원(34%↓) / 샥즈 오픈런 프로2 139,000원(44%↓) / 오쏘몰 30회분 80,070원(17%↓)",
                "이치란 5인분은 직구 37,400원·12/11 도착 vs 국내 31,900원·내일 도착 — 직구가 손해",
                "어그 3배 차이는 할인이 아니라 판본 차이 — 정품 보증과 교환 조건 먼저 확인",
                "2개 이상 10% 쿠폰: 샥즈 2대 250,200원, 바샤커피 2통 55,044원",
            ],
            "tips": "가격은 2026-11-25 11:40~12:05 KST 쿠팡 노출가이며 쿠폰·와우할인·카드할인에 따라 달라집니다. 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있습니다.",
        },
        "en": {
            "title": "Coupang Kubleop Ends December 1: 5 Direct-Purchase Items Checked Against Korean Prices",
            "summary": "Coupang's Rocket Direct Purchase event Kubleop ends December 1. Five products were checked on the morning of November 25 against their domestic prices: Bacha Coffee came out 27.2% cheaper and Shokz OpenRun Pro 2 24.9% cheaper, while Orthomol saved only 4.3% and Ichiran was cheaper domestically. The two-item 10% coupon maths is included.",
            "description": EN_DESC,
            "tasteReview": [
                "Kubleop November 23 to December 1, about 30,000 items from the US, Japan, Europe, China and Hong Kong",
                "Checked: Bacha Coffee 30,580 won (34% off), Shokz OpenRun Pro 2 139,000 won (44% off), Orthomol 30-day 80,070 won (17% off)",
                "Ichiran 5 servings: 37,400 won direct arriving Dec 11 vs 31,900 won domestic arriving tomorrow",
                "A threefold UGG gap is a different product, not a discount — check the authenticity guarantee first",
                "Two-item 10% coupon: two Shokz 250,200 won, two Bacha boxes 55,044 won",
            ],
            "tips": "Prices are Coupang listings at 11:40-12:05 KST on 25 November 2026 and move with coupons and card discounts. This post contains affiliate links and may earn a commission.",
        },
        "ja": {
            "title": "クブルフは12月1日まで——国内価格より安い5点と10％クーポンの重ね方",
            "summary": "クーパンのロケット直球「クブルフ」は12月1日終了。11月25日午前に確認した5点を国内価格と並べました。バチャコーヒーは27.2％、Shokzオープンラン プロ2は24.9％安く、オルソモルは4.3％、一蘭は国内のほうが安いという結果です。2点以上10％クーポンの計算も掲載。",
            "description": JA_DESC,
            "tasteReview": [
                "クブルフ11/23〜12/1（9日間）、米・日・欧・中・香港から約3万点、990ウォンオープンラン",
                "実測: バチャコーヒー30,580ウォン（34％↓）、Shokzオープンラン プロ2 139,000ウォン（44％↓）、オルソモル30日分80,070ウォン（17％↓）",
                "一蘭5食は直球37,400ウォン・12/11着 vs 国内31,900ウォン・翌日着で直球が損",
                "UGGの3倍差は割引ではなく版の違い——正規保証と交換条件を先に確認",
                "2点以上10％クーポン: Shokz 2台250,200ウォン、バチャ2箱55,044ウォン",
            ],
            "tips": "価格は2026-11-25 11:40〜12:05 KSTのクーパン表示価格で、クーポンやカード割引により変わります。本記事はアフィリエイトリンクを含み、手数料を受け取る場合があります。",
        },
        "zh": {
            "title": "Coupang火箭直购「Kubleop」12月1日截止——比国内便宜的5件与10%优惠券叠加",
            "summary": "Coupang火箭直购「Kubleop」12月1日结束。本文把11月25日上午实际确认的5件商品与国内价格并排比较：Bacha咖啡便宜27.2%、Shokz OpenRun Pro 2便宜24.9%，Orthomol仅4.3%，一兰反而国内更便宜。附两件以上10%优惠券计算。",
            "description": ZH_DESC,
            "tasteReview": [
                "Kubleop 11/23~12/1（9天），美日欧中港约3万件，990韩元抢购、每日特价",
                "实测：Bacha咖啡30,580韩元（-34%）、Shokz OpenRun Pro 2 139,000韩元（-44%）、Orthomol 30日80,070韩元（-17%）",
                "一兰5人份：直购37,400韩元·12/11到达 vs 国内31,900韩元·次日到达，直购反而更贵",
                "UGG三倍差价不是折扣而是版本差异——先确认正品保证与换货条件",
                "两件以上10%券：Shokz两台250,200韩元，Bacha两盒55,044韩元",
            ],
            "tips": "价格为2026-11-25 11:40~12:05 KST Coupang显示价，随优惠券和银行卡折扣变化。本文含联盟链接，可能获得佣金。",
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
    urllib.request.urlopen(urllib.request.Request(REVALIDATE_URL), timeout=120)
    print("[+] Revalidated")
except Exception as e:
    print(f"[-] Revalidate error: {e}")
