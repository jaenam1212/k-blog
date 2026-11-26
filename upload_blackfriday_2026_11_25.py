#!/usr/bin/env python3
"""블랙프라이데이 2026 국내 일정 + 실측 4종 (4개국어) → Supabase posts + ISR revalidate.

근거
 - 일정: 연합뉴스 2026-11-15(쿠팡 가전·디지털 블프 11/16~29, 블프페스타 라이브 11/23~27),
   2026-11-23(로켓직구 '쿠블프' 11/23~12/01, 약 3만 개 상품·10% 쿠폰·일본직구 7,000원 쿠폰),
   일정 집계(2026-11-23 확인): 블랙프라이데이 11/27(금)·사이버먼데이 11/30(월), 무신사 무진장 11/22~12/02, 오늘의집 11/16~11/30, 아마존 11/19~11/30
 - 카테고리 데이터: 닐슨아이큐(NIQ) '2026년 상반기 가전시장 트렌드 리포트'(전자신문 2026-11-08 보도)
 - 가격·리뷰·사진: 쿠팡 검색 결과 2026-11-25 08:40~08:50 KST 직접 확인. 상품 썸네일 원본 사용(AI 생성 0장)
 - 환율: 야후 파이낸스 USD/KRW 1,340.93(2026-11-24)
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
SLUG = "black-friday-2026-korea-deals-4picks"

K = "https://www.coupang.com/np/search?q="
TAG = "&lptag=AF9412775"


def q(s):
    return K + quote(s) + TAG


C = "/images/products/bf-headphone-sony-ch720n.jpg"
G1 = "/images/products/bf-steamiron-philips-dst1040.jpg"
G2 = "/images/products/bf-airfryer-philips-na220.jpg"
G3 = "/images/products/bf-smartwatch-galaxy-watch8.jpg"

KO_DESC = """블랙프라이데이가 11월 27일(금)이라는 건 미국 달력의 이야기다. 국내 이커머스는 이미 절반 넘게 지나갔고, 행사마다 마감일이 다르다. 2026년 국내 일정을 먼저 정리하면 이렇다.
쿠팡은 '가전·디지털 블랙프라이데이'를 11월 16일부터 29일까지 진행한다. 삼성전자·LG전자·인텔·HP·쿠첸·TCL 등이 참여하고, 11월 23~27일에는 '블프페스타 라이브'로 방송 중에만 받을 수 있는 혜택을 더한다. 같은 기간 로켓직구 행사 '쿠블프'는 11월 23일부터 12월 1일까지 9일간 열린다. 미국·일본·유럽·중국·홍콩 상품 약 3만 개로, 지난해(2만7,000여 개)보다 규모를 키웠다. 선착순 메가딜, 하루특가, 990원부터 시작하는 오픈런 990딜이 붙고, 행사 상품 2개 이상 구매 시 10% 할인 쿠폰과 일본 직구용 7,000원 쿠폰이 제공된다.
패션은 무신사 '무진장 26 겨울'이 11월 20일 사전 행사, 22일부터 12월 2일까지 온라인 본행사를 연다. 오늘의집 '집요한세일'은 11월 16~30일, 아마존은 11월 19~30일이다. 사이버먼데이는 11월 30일(월).
정리하면 이렇다. 11월 27일은 '블랙프라이데이 당일'일 뿐, 시작일도 마감일도 아니다. 쿠팡 가전·디지털은 11월 29일, 쿠블프는 12월 1일, 무신사는 12월 2일에 끝난다. 반대로 이미 끝났거나 곧 끝나는 행사도 있다. "27일까지 기다린다"는 전략은 절반의 경우에 손해다.

1. 올해 실제로 팔린 품목 — 무엇이 싸게 나오는가
닐슨아이큐(NIQ)의 2026년 상반기 국내 가전·IT 시장 리포트를 보면, 36개 품목 시장 규모가 11조2,273억 원으로 전년 동기보다 9.5% 커졌다. 그 안에서 가장 빠르게 큰 품목이 이번 시즌 할인 폭이 큰 곳이다.
헤드폰 매출이 92.4% 늘어 36개 품목 중 1위였다. 스팀다리미가 92.0%, 웨어러블이 52.6%, 에어프라이어가 37.1%, 미니오븐이 20.5%, 데스크톱PC가 37.6%, 노트북이 11.8% 늘었다. 반대로 건조기는 12.9%, 헤어스타일러는 11.9%, 전기면도기는 5.9%, 공기청정기는 2.4% 줄었다. 유통 채널에서는 온라인 마켓플레이스 매출이 24.8% 늘어 오프라인 대형마트(−14.6%)와 TV홈쇼핑(−28.5%)을 압도했다.
즉 이번 시즌 재고를 가장 세게 털어내는 카테고리는 오디오·생활가전·주방가전이고, 수요가 꺾인 건조기·공기청정기·면도기는 '싸다고 사면 안 되는' 쪽에 가깝다. 사지 않아도 되는 물건을 싸게 사는 건 할인이 아니다.

2. 11월 25일 쿠팡에서 실제로 확인한 4종
소니 노이즈 캔슬링 헤드폰 WH-CH720N — 정가 199,000원, 판매가 143,000원(28% 할인). 50시간 재생, 멀티포인트, 무게 192g. 별점 5.0에 리뷰 2,664개. 오늘 도착 보장. 헤드폰 카테고리가 가장 뜨거운 만큼 대체 모델도 많다. 같은 검색에서 앤커 사운드코어 스페이스2가 131,600원, QCY H3 ANC가 40,820원이었다.
필립스 스팀 다리미 1000시리즈 DST1040/30 — 정가 47,500원, 판매가 22,100원(53% 할인). 별점 4.5에 리뷰 9,114개로 이번 4종 중 리뷰가 가장 많다. 여기서 중요한 게 하나 있다. 같은 모델을 다른 판매자가 40,600~45,340원에 올려두고 있다. 로켓배송 재고가 떨어지면 두 배 가까운 값에 사게 된다는 뜻이다. 블랙프라이데이에 '최저가'를 확인해야 하는 이유가 이 한 줄에 있다.
필립스 에어프라이어 2000시리즈 4.2L NA220/00 — 정가 199,300원, 판매가 68,810원(65% 할인). 별점 5.0, 리뷰 1,141개. 바스켓 안이 보이는 '보이는 에어프라이어' 계열이고, 4일 남은 쿠폰 할인이다. 같은 브랜드 1000시리즈 6.2L(NA130/00)가 73,110원, 쿠첸 5L(COV-D050G)가 63,580원으로 용량과 가격이 붙어 있어, 필요한 용량부터 정하는 게 순서다.
삼성 갤럭시워치8 40mm 블루투스 SM-L320N — 정가 419,000원, 판매가 358,050원(14% 할인). 별점 5.0, 리뷰 9,129개. 쿠폰 할인이 붙어야 이 가격이고, 44mm는 440,070원, 클래식 46mm는 436,750원이다. 웨어러블은 신제품 사이클이 짧아 '직전 세대'를 노리는 게 정석이다. 같은 검색에 갤럭시워치9가 499,590원으로 나왔다.
가격은 2026년 11월 25일 오전 쿠팡 검색 화면에 노출된 값이고, 쿠폰·와우할인·카드할인에 따라 달라진다.

3. 직구가 싸다고 다 싸지 않다 — 같은 모델 비교
소니 WH-CH720N은 로켓직구로도 판매된다. 204,600원 정가에 37% 할인한 127,630원, 국내 로켓배송(143,000원)보다 15,370원(10.7%) 싸다. 대신 조건이 다르다. 직구는 중국에서 발송돼 12월 1일 도착 예정이고, 중고·새 상품이 섞여 있으며, 최저가는 122,900원까지 내려간다. 반대로 국내 재고는 '오늘 도착 보장'이다.
환율은 2026년 11월 24일 기준 달러당 1,340원대다. 여기에 미국발 추가 관세가 얹힐 수 있다. 미 무역대표부(USTR)가 한국·EU·일본·중국 등 16개 경제주체의 '과잉생산'에 대한 301조 조사 결과를 곧 발표하고, 기존 관세에 더하는 새 관세를 제안할 예정이다. 한·미 무역합의의 15% 상한이 유지될 전망이지만, 관세율이 올라가면 직구 체감가가 그만큼 뛴다. 12월 1일까지 기다리는 직구는 배송 지연과 관세 변동을 동시에 떠안는 셈이다.
정리하면 이렇다. 차액이 1만5,000원 안팎이면 AS와 반품이 쉬운 국내 재고를, 차액이 3만원을 넘고 도착일이 상관없다면 직구를 고른다. 이번 사례는 전자에 가깝다.

4. 결제 전에 확인할 세 가지
첫째, 정가가 아니라 최근 3개월 최저가와 비교한다. '37% 할인' 같은 문구는 정가를 얼마로 잡느냐에 따라 숫자가 달라진다. 쿠팡 상품 페이지의 최저가 표기와 다른 판매자 가격을 함께 봐야 한다(앞의 스팀다리미 사례).
둘째, 쿠폰이 겹치는지 본다. 이번 쿠블프는 행사 상품 2개 이상 구매 시 10% 쿠폰을 준다. 와우회원 할인, 카드 할인, 쿠팡캐시 적립이 각각 붙는지에 따라 최종 결제액이 달라진다. 라이브 방송 혜택은 방송 중에만 적용된다.
셋째, 도착일과 반품 조건을 확인한다. 로켓직구는 해외 발송이라 반품·교환이 국내 재고보다 번거롭고, 도착일이 12월로 넘어간다. 연말 선물용이라면 이 조건이 가격 차이보다 중요할 수 있다.

한 줄 정리
블랙프라이데이는 하루가 아니라 두 주다. 쿠팡 가전·디지털은 11월 29일, 쿠블프는 12월 1일, 무신사는 12월 2일에 끝나고, 사이버먼데이는 11월 30일이다. 올해 가장 세게 할인되는 곳은 헤드폰·스팀다리미·웨어러블·에어프라이어(매출 증가율 상위)이고, 가장 조심할 곳은 수요가 꺾인 건조기·공기청정기다. 정가 대비 할인율이 아니라 같은 모델의 다른 판매자 가격을 먼저 확인하는 것이 이번 주에 돈을 아끼는 가장 확실한 방법이다."""

EN_DESC = """Black Friday falling on Friday, November 27 is the American calendar. Korean e-commerce is already more than halfway through its season, and every store closes at a different time. Here is the 2026 schedule.
Coupang runs its home-appliance and digital Black Friday from November 16 to 29, with Samsung, LG, Intel, HP, Cuchen and TCL among the participants, and adds live-stream-only offers from November 23 to 27. Its Rocket Direct Purchase event, "Kubleop," runs nine days from November 23 to December 1 with about 30,000 imported products across the US, Japan, Europe, China and Hong Kong — up from 27,000 last year — alongside first-come mega deals, daily deals and "open run" 990-won deals, plus a 10% coupon for buying two or more items and a 7,000-won coupon for Japanese direct purchases.
Musinsa's winter "Mujinjang 26" started offline on November 20 and runs online from November 22 to December 2. Today's House's sale runs November 16-30 and Amazon's November 19-30. Cyber Monday is November 30.
The conclusion: November 27 is a date, not a deadline. Coupang's appliance sale ends November 29, Kubleop December 1 and Musinsa December 2. Waiting for the 27th is a losing strategy about half the time.

1. What actually sold this year
NielsenIQ's first-half 2026 report puts Korea's consumer tech and durables market at 11.23 trillion won, up 9.5% year on year across 36 categories. The fastest growers are where the discounts are deepest this season.
Headphone revenue rose 92.4%, the highest of all 36 categories. Steam irons rose 92.0%, wearables 52.6%, air fryers 37.1%, mini ovens 20.5%, desktops 37.6% and laptops 11.8%. Dryers fell 12.9%, hair stylers 11.9%, electric shavers 5.9% and air purifiers 2.4%. Online marketplaces grew 24.8% while hypermarkets fell 14.6% and TV home shopping 28.5%.
So the categories being cleared hardest are audio, small appliances and kitchen appliances, while dryers, air purifiers and shavers are the ones to leave — a discount on something you do not need is not a discount.

2. Four products checked on Coupang on November 25
Sony WH-CH720N noise-cancelling headphones — 199,000 won list, 143,000 won (28% off), 50-hour playback, multipoint, 192g, 5.0 stars from 2,664 reviews, same-day delivery. Alternatives in the same search: Anker Soundcore Space 2 at 131,600 won and QCY H3 ANC at 40,820 won.
Philips Steam Iron 1000 Series DST1040/30 — 47,500 won list, 22,100 won (53% off), 4.5 stars from 9,114 reviews, the most-reviewed of the four. Note this: other sellers list the same model at 40,600-45,340 won. If Rocket stock runs out you pay nearly double, which is the whole case for checking the lowest price rather than the discount badge.
Philips Airfryer 2000 Series 4.2L NA220/00 — 199,300 won list, 68,810 won (65% off), 5.0 stars, 1,141 reviews, a see-through basket model on a coupon that runs four more days. The same brand's 1000 Series 6.2L (NA130/00) is 73,110 won and Cuchen's 5L (COV-D050G) 63,580 won, so decide capacity first.
Samsung Galaxy Watch8 40mm Bluetooth SM-L320N — 419,000 won list, 358,050 won (14% off) with a coupon, 5.0 stars from 9,129 reviews. The 44mm is 440,070 won and the Classic 46mm 436,750 won; the Watch9 showed at 499,590 won. Wearables cycle fast, so the previous generation is usually the value play.
Prices are what appeared on Coupang's search page on the morning of November 25, 2026 and move with coupons and card discounts.

3. Direct purchase is not automatically cheaper
The same Sony WH-CH720N is sold through Rocket Direct Purchase at 127,630 won (37% off a 204,600 won list), 15,370 won (10.7%) below the domestic 143,000 won. The conditions differ: it ships from China and arrives around December 1, listings mix new and used stock, and the lowest price seen was 122,900 won. The domestic listing arrives today.
The won trades near 1,340 per dollar as of November 24. On top of that, new US tariffs may stack. The U.S. Trade Representative is poised to release a Section 301 probe into excess capacity in 16 partners including Korea, the EU, Japan and China and propose duties on top of existing ones. The 15% cap from the Korea-US deal is expected to hold, but higher rates raise the effective cost of direct purchases. Waiting until December 1 means taking both shipping delay and tariff risk.
The rule of thumb: if the gap is around 15,000 won, take domestic stock with easy returns; if it is over 30,000 won and the arrival date does not matter, buy direct. In this case the gap points to domestic.

4. Three checks before paying
First, compare with the recent three-month low, not the list price. A "37% off" badge depends on the list price chosen, so read the lowest-price marker on the page and other sellers' prices (see the iron).
Second, check stacking coupons. Kubleop gives 10% off two or more items; Wow membership, card discounts and Coupang Cash each change the final amount, and live-stream offers apply only during the broadcast.
Third, check the arrival date and returns. Direct purchases are harder to return than domestic stock and can land in December, which may matter more than the price difference for a gift.

Bottom line
Black Friday is two weeks, not a day. Coupang's appliance sale ends November 29, Kubleop December 1, Musinsa December 2, and Cyber Monday is November 30. The deepest discounts are in headphones, steam irons, wearables and air fryers; the ones to avoid are dryers and air purifiers, where demand has fallen. Checking other sellers' prices for the same model, rather than the discount percentage, is the surest way to save money this week."""

JA_DESC = """ブラックフライデーが11月27日（金）というのはアメリカの暦の話だ。韓国のECはすでにシーズンの半分を過ぎており、締切は店ごとに違う。2026年の日程を先に整理する。
クーパン（Coupang）は「家電・デジタル・ブラックフライデー」を11月16日から29日まで開催する。サムスン、LG、インテル、HP、クチェン、TCLなどが参加し、11月23〜27日にはライブ配信限定の特典「ブルフフェスタライブ」を追加する。同じ期間、ロケット直球購入のイベント「クブルフ」は11月23日から12月1日までの9日間。米国・日本・欧州・中国・香港の商品約3万点で、昨年（約2万7,000点）より規模を広げた。先着メガディール、デイリー特価、990ウォンからの「オープンラン990ディール」に加え、対象商品2点以上の購入で10%割引クーポン、日本直球用7,000ウォンクーポンが付く。
ファッションはムシンサ「無尽蔵26 冬」が11月20日に先行、22日から12月2日までオンライン本番。オヌルイジプは11月16〜30日、アマゾンは11月19〜30日。サイバーマンデーは11月30日。
つまり11月27日は「当日」にすぎず、開始日でも締切でもない。クーパンの家電は11月29日、クブルフは12月1日、ムシンサは12月2日に終わる。「27日まで待つ」戦略は半分のケースで損をする。

1. 今年実際に売れたもの
ニールセンIQ（NIQ）の2026年上期レポートによると、韓国の家電・IT市場は36品目で11兆2,273億ウォン、前年同期比9.5%増えた。伸びが速い品目が、今季もっとも大きく値引きされる場所だ。
ヘッドホンの売上は92.4%増で36品目中1位。スチームアイロン92.0%、ウェアラブル52.6%、エアフライヤー37.1%、ミニオーブン20.5%、デスクトップPC37.6%、ノートPC11.8%増。逆に乾燥機は12.9%、ヘアスタイラーは11.9%、電気シェーバーは5.9%、空気清浄機は2.4%減った。チャネル別ではオンラインマーケットプレイスが24.8%伸び、オフライン大型スーパー（−14.6%）とテレビ通販（−28.5%）を圧倒した。
つまり在庫を最も強く処分しているのはオーディオ・生活家電・キッチン家電で、需要が落ちた乾燥機・空気清浄機・シェーバーは「安いから買う」べきではない側だ。必要のない物を安く買うのは割引ではない。

2. 11月25日にクーパンで確認した4点
ソニー WH-CH720N — 定価199,000ウォン、販売価格143,000ウォン（28%引き）。50時間再生、マルチポイント、192g、5.0（レビュー2,664件）、当日配送。同じ検索でAnker Soundcore Space 2が131,600ウォン、QCY H3 ANCが40,820ウォンだった。
フィリップス スチームアイロン1000シリーズ DST1040/30 — 定価47,500ウォン、22,100ウォン（53%引き）、4.5（9,114件）で4点中最もレビューが多い。ここが重要だ。同じ型番を別の販売者が40,600〜45,340ウォンで出している。ロケット在庫が切れるとほぼ2倍の値段になるということで、「割引率」ではなく「最安値」を見る理由がここにある。
フィリップス エアフライヤー2000シリーズ 4.2L NA220/00 — 定価199,300ウォン、68,810ウォン（65%引き）、5.0（1,141件）。中が見えるバスケット型で、残り4日のクーポン割引。同ブランド1000シリーズ6.2L（NA130/00）は73,110ウォン、クチェン5L（COV-D050G）は63,580ウォンなので、容量から決めるのが順序だ。
サムスン ギャラクシーウォッチ8 40mm Bluetooth SM-L320N — 定価419,000ウォン、358,050ウォン（14%引き、クーポン適用）。5.0（9,129件）。44mmは440,070ウォン、クラシック46mmは436,750ウォン、ギャラクシーウォッチ9は499,590ウォンだった。ウェアラブルは世代交代が速く、1つ前の世代を狙うのが定石だ。
価格は2026年11月25日午前のクーパン検索画面の表示価格で、クーポンやカード割引により変わる。

3. 直球購入が常に安いわけではない
同じソニーWH-CH720Nはロケット直球でも売られている。定価204,600ウォンの37%引きで127,630ウォン、国内ロケット便（143,000ウォン）より15,370ウォン（10.7%）安い。条件は違う。中国から発送され12月1日到着予定、新古品が混在し、最安値は122,900ウォンまで下がる。国内在庫は「当日到着保証」だ。
為替は11月24日時点で1ドル1,340ウォン台。さらに米国の追加関税が上乗せされる可能性がある。USTRは韓国・EU・日本・中国など16の経済主体の「過剰生産」に関する301条調査の結果を近く公表し、既存関税に上乗せする新関税を提案する見通しだ。韓米合意の15%上限は維持される見込みだが、税率が上がれば直球の実質コストは上がる。12月1日まで待つ直球は、配送遅延と関税変動を同時に負うことになる。
目安はこうだ。差額が1万5,000ウォン程度なら返品しやすい国内在庫、3万ウォンを超え到着日を問わなければ直球。今回のケースは前者に近い。

4. 支払い前に確認する3点
第一に、定価ではなく直近3か月の最安値と比べる。「37%引き」は定価の取り方で数字が変わる。商品ページの最安値表示と別販売者の価格を併せて見る（前述のアイロン）。
第二に、クーポンの重複を確認する。クブルフは2点以上で10%クーポン。Wow会員割引、カード割引、クーパンキャッシュ還元の有無で最終金額が変わり、ライブ特典は配信中のみ適用される。
第三に、到着日と返品条件。直球は海外発送で返品・交換が国内在庫より面倒で、到着が12月にずれる。贈り物なら価格差よりこの条件が効く。

まとめ
ブラックフライデーは1日ではなく2週間だ。クーパンの家電は11月29日、クブルフは12月1日、ムシンサは12月2日、サイバーマンデーは11月30日。最も深く値引きされるのはヘッドホン・スチームアイロン・ウェアラブル・エアフライヤーで、避けるべきは需要が落ちた乾燥機・空気清浄機。割引率ではなく同じ型番の別販売者の価格を見ることが、今週いちばん確実な節約になる。"""

ZH_DESC = """黑色星期五是11月27日（周五），那是美国的日历。韩国电商的促销季已经过半，而且各平台的截止日都不同。先梳理2026年的日程。
Coupang的"家电·数码黑色星期五"从11月16日进行到29日，三星、LG、英特尔、HP、酷晨、TCL等参与，11月23~27日还有仅限直播的"黑五庆典直播"加码。同期，火箭直购活动"Kubleop"从11月23日到12月1日共9天，涵盖美国、日本、欧洲、中国、香港约3万件商品，比去年的2.7万件扩大规模，并设先到先得的超级特价、每日特价、990韩元起的"开跑990特价"，以及购买2件以上打10%的优惠券和日本直购7,000韩元优惠券。
时尚方面，Musinsa"无尽藏26 冬季"20日先行、22日至12月2日线上正式开跑；今日之家11月16~30日，亚马逊11月19~30日。网络星期一为11月30日。
结论是：11月27日只是"当天"，既不是开始日也不是截止日。Coupang家电11月29日结束，Kubleop 12月1日，Musinsa 12月2日。"等到27日"的策略在一半情况下是亏的。

1. 今年真正卖得动的品类
尼尔森IQ（NIQ）2026年上半年报告显示，韩国家电与IT市场36个品类规模为11.23万亿韩元，同比增长9.5%。增长最快的品类，就是本季折扣最狠的地方。
耳机销售额增长92.4%，在36个品类中排第一；蒸汽熨斗92.0%、可穿戴52.6%、空气炸锅37.1%、迷你烤箱20.5%、台式机37.6%、笔记本11.8%。相反，烘干机下降12.9%、美发造型器11.9%、电动剃须刀5.9%、空气净化器2.4%。渠道上，线上市场增长24.8%，远超线下大型超市（−14.6%）与电视购物（−28.5%）。
也就是说，正在大力清库存的是音频、生活家电与厨房家电；需求下滑的烘干机、空气净化器、剃须刀属于"不该因为便宜就买"的一侧。不需要的东西打折，不是优惠。

2. 11月25日在Coupang实际确认的四款
索尼 WH-CH720N 降噪耳机 — 原价199,000韩元，售价143,000韩元（28%折扣），50小时续航、多点连接、192g，5.0分（2,664条评价），当日送达。同一搜索中Anker Soundcore Space 2为131,600韩元，QCY H3 ANC为40,820韩元。
飞利浦 蒸汽熨斗1000系列 DST1040/30 — 原价47,500韩元，售价22,100韩元（53%折扣），4.5分、9,114条评价，是四款中评价最多。关键在这里：同一型号其他卖家标价40,600~45,340韩元。火箭库存售罄就要付近两倍价格——这正是要看"最低价"而不是"折扣率"的理由。
飞利浦 空气炸锅2000系列 4.2L NA220/00 — 原价199,300韩元，售价68,810韩元（65%折扣），5.0分、1,141条评价，可视篮款，优惠券还剩4天。同品牌1000系列6.2L（NA130/00）73,110韩元，酷晨5L（COV-D050G）63,580韩元，先定容量再选型号。
三星 Galaxy Watch8 40mm 蓝牙 SM-L320N — 原价419,000韩元，售价358,050韩元（14%折扣，需用券），5.0分、9,129条评价。44mm为440,070韩元，Classic 46mm为436,750韩元，Watch9显示499,590韩元。可穿戴换代快，买上一代通常最划算。
价格为2026年11月25日上午Coupang搜索页显示价，会随优惠券与银行卡折扣变化。

3. 直购不一定更便宜
同款索尼WH-CH720N也有火箭直购：原价204,600韩元、37%折扣后127,630韩元，比国内火箭配送（143,000韩元）便宜15,370韩元（10.7%）。但条件不同：从中国发货、预计12月1日到达，新旧货混售，最低价曾到122,900韩元；国内库存则是"当日送达保证"。
汇率方面，11月24日美元兑韩元约1,340。此外还可能叠加美国新增关税：美国贸易代表办公室即将公布对韩国、欧盟、日本、中国等16个经济体"产能过剩"的301条款调查结果，并拟在现有关税上叠加新税。韩美协议15%的上限预计维持，但税率上调会推高直购的实际成本。等到12月1日的直购，同时承担物流延迟与关税变动。
经验规则：差价约1.5万韩元以内选退换方便的国内库存；超过3万韩元且不在意到货日再选直购。本例更接近前者。

4. 付款前的三项检查
第一，不比原价，比最近三个月最低价。"37%折扣"取决于原价怎么定，要同时看商品页的最低价标记与其他卖家价格（见上面的熨斗）。
第二，确认优惠券能否叠加。Kubleop购买2件以上给10%券；会员折扣、银行卡折扣、Coupang Cash返现是否同时适用会改变最终金额，直播福利只在直播期间有效。
第三，确认到货日与退货条件。直购为海外发货，退换比国内库存麻烦，到货会推到12月。若是年尾礼物，这一条件可能比差价更重要。

一句话总结
黑色星期五不是一天而是两周：Coupang家电到11月29日、Kubleop到12月1日、Musinsa到12月2日、网络星期一为11月30日。折扣最深的是耳机、蒸汽熨斗、可穿戴与空气炸锅；要避开的是需求下滑的烘干机与空气净化器。本周最可靠的省钱方式，是看同款其他卖家的价格，而不是折扣百分比。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "store": "쿠팡",
    "priceKrw": 143000,
    "releaseDate": "2026-11-25",
    "rating": 4.8,
    "imageUrl": C,
    "images": [G1, G2, G3],
    "affiliateUrl": q("블랙프라이데이 가전"),
    "affiliatePlatform": "Coupang",
    "exampleItems": [
        {
            "name": "소니 노이즈 캔슬링 헤드폰 WH-CH720N (50시간·192g)",
            "brand": "소니",
            "priceKrw": 143000,
            "imageUrl": "/images/products/bf-headphone-sony-ch720n.jpg",
            "url": q("소니 WH-CH720N"),
            "category": "헤드폰",
        },
        {
            "name": "필립스 스팀 다리미 1000시리즈 DST1040/30",
            "brand": "필립스",
            "priceKrw": 22100,
            "imageUrl": "/images/products/bf-steamiron-philips-dst1040.jpg",
            "url": q("필립스 스팀다리미 DST1040/30"),
            "category": "스팀다리미",
        },
        {
            "name": "필립스 에어프라이어 2000시리즈 4.2L NA220/00",
            "brand": "필립스",
            "priceKrw": 68810,
            "imageUrl": "/images/products/bf-airfryer-philips-na220.jpg",
            "url": q("필립스 에어프라이어 NA220/00"),
            "category": "에어프라이어",
        },
        {
            "name": "삼성 갤럭시워치8 40mm 블루투스 SM-L320N",
            "brand": "삼성전자",
            "priceKrw": 358050,
            "imageUrl": "/images/products/bf-smartwatch-galaxy-watch8.jpg",
            "url": q("갤럭시워치8 40mm SM-L320N"),
            "category": "스마트워치",
        },
    ],
    "i18n": {
        "ko": {
            "title": "블랙프라이데이 2026, 27일까지 기다리면 손해다 — 국내 마감일 총정리와 실측 4종",
            "summary": "쿠팡 가전·디지털은 11/29, 로켓직구 '쿠블프'는 12/1, 무신사는 12/2에 끝납니다. 올해 매출이 가장 많이 늘어난 헤드폰·스팀다리미·웨어러블·에어프라이어 4종을 11월 25일 쿠팡에서 직접 확인했습니다. 같은 모델이 판매자에 따라 두 배 차이 나는 사례까지 정리했습니다.",
            "description": KO_DESC,
            "tasteReview": [
                "쿠팡 가전·디지털 블프 11/16~29, 로켓직구 '쿠블프' 11/23~12/1(약 3만 개), 무신사 무진장 11/22~12/2, 사이버먼데이 11/30",
                "2026 상반기 매출 증가율: 헤드폰 +92.4%, 스팀다리미 +92.0%, 웨어러블 +52.6%, 에어프라이어 +37.1% (건조기 −12.9%)",
                "실측: 소니 WH-CH720N 143,000원(28%↓)·필립스 DST1040/30 22,100원(53%↓)·필립스 NA220 68,810원(65%↓)·갤럭시워치8 358,050원(14%↓)",
                "같은 스팀다리미 다른 판매자 40,600~45,340원 — 할인율보다 '최저가' 확인이 먼저",
            ],
            "tips": "가격은 2026-11-25 08:40~08:50 KST 쿠팡 노출가이며, 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있습니다.",
        },
        "en": {
            "title": "Black Friday 2026 in Korea: Waiting for Nov 27 Costs You — Deadlines and 4 Verified Deals",
            "summary": "Coupang's appliance sale ends November 29, Rocket Direct Purchase December 1 and Musinsa December 2. Here are four products checked on Coupang on November 25 in the categories that actually grew this year — headphones, steam irons, wearables and air fryers — plus the case where the same model costs twice as much from another seller.",
            "description": EN_DESC,
            "tasteReview": [
                "Coupang appliances Nov 16-29, Kubleop Nov 23-Dec 1 (about 30,000 items), Musinsa Nov 22-Dec 2, Cyber Monday Nov 30",
                "H1 2026 revenue growth: headphones +92.4%, steam irons +92.0%, wearables +52.6%, air fryers +37.1% (dryers -12.9%)",
                "Checked: Sony WH-CH720N 143,000 won (28% off), Philips DST1040/30 22,100 won (53% off), Philips NA220 68,810 won (65% off), Galaxy Watch8 358,050 won (14% off)",
                "The same iron lists at 40,600-45,340 won from other sellers — check the lowest price, not the discount badge",
            ],
            "tips": "Prices are Coupang listings at 08:40-08:50 KST on 25 Nov 2026; this post contains affiliate links and may earn a commission.",
        },
        "ja": {
            "title": "2026年ブラックフライデー、27日まで待つと損をする——韓国各社の締切と実測4点",
            "summary": "クーパンの家電は11/29、ロケット直球の「クブルフ」は12/1、ムシンサは12/2で終わります。今年もっとも伸びたヘッドホン・スチームアイロン・ウェアラブル・エアフライヤーの4点を11月25日にクーパンで直接確認しました。同じ型番が販売者によって約2倍の値段になる例まで整理しています。",
            "description": JA_DESC,
            "tasteReview": [
                "クーパン家電11/16〜29、クブルフ11/23〜12/1（約3万点）、ムシンサ11/22〜12/2、サイバーマンデー11/30",
                "2026年上期の売上伸び率: ヘッドホン＋92.4％、スチームアイロン＋92.0％、ウェアラブル＋52.6％、エアフライヤー＋37.1％（乾燥機−12.9％）",
                "実測: ソニーWH-CH720N 143,000ウォン（28％↓）、フィリップスDST1040/30 22,100ウォン（53％↓）、NA220 68,810ウォン（65％↓）、ギャラクシーウォッチ8 358,050ウォン（14％↓）",
                "同じアイロンが別販売者で40,600〜45,340ウォン——割引率より最安値の確認が先",
            ],
            "tips": "価格は2026-11-25 08:40〜08:50 KSTのクーパン表示価格です。本記事はアフィリエイトリンクを含み、手数料を受け取る場合があります。",
        },
        "zh": {
            "title": "2026黑色星期五：等到11月27日反而更贵——韩国各平台截止日与四款实测",
            "summary": "Coupang家电到11月29日、火箭直购「Kubleop」到12月1日、Musinsa到12月2日结束。本文整理今年增长最快的耳机、蒸汽熨斗、可穿戴与空气炸锅四款于11月25日在Coupang的实际价格，以及同款在其他卖家处贵近两倍的案例。",
            "description": ZH_DESC,
            "tasteReview": [
                "Coupang家电11/16~29、Kubleop 11/23~12/1（约3万件）、Musinsa 11/22~12/2、网络星期一11/30",
                "2026上半年销售额增速：耳机+92.4%、蒸汽熨斗+92.0%、可穿戴+52.6%、空气炸锅+37.1%（烘干机−12.9%）",
                "实测：索尼WH-CH720N 143,000韩元（28%折扣）、飞利浦DST1040/30 22,100韩元（53%折扣）、NA220 68,810韩元（65%折扣）、Galaxy Watch8 358,050韩元（14%折扣）",
                "同款熨斗在其他卖家标价40,600~45,340韩元——先看最低价，再看折扣率",
            ],
            "tips": "价格为2026-11-25 08:40~08:50 KST Coupang显示价；本文含联盟链接，可能获得佣金。",
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
