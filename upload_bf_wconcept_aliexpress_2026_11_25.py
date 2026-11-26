#!/usr/bin/env python3
"""W컨셉 더블유위크(오늘 마감) + 알리익스프레스 블프(12/3) 실측 → Supabase (4개국어).

근거
 - W컨셉 더블유위크: 신세계그룹 뉴스룸·전자신문 2026-11-09 (11/9~25, 약 20만 개, 최대 85%, 550여 브랜드,
   매일 10시 균일가 오픈런(9,900원·59,900원), 매일 18시 50% 쿠폰 + 참여 브랜드 30% 쿠폰, 뷰티·라이프 최대 30%)
 - W컨셉 상품가: 2026-11-25 확인 — 프론트로우 캐시미어 하프 코트(307059292) 499,000원→표시 판매가 203,841원(59%),
   무니드 PLAIN DEEP U-NECK 니트(308840498) 104,000원→72,800원(쿠폰 30%, 배송 3,500원)
 - 알리익스프레스 블프: PRNewswire·전자신문 2026-11-19 (11/19~12/3, 최대 70%, 4단계 테마)
 - 알리 할인코드·키보드 실측: 2026-11-25 아침 가격 기록(프라이스갭) — AJAZZ AK820 26,004원, 세일 전 33,000원, 11/20 최저 25,059원
 - 사진: W컨셉·알리익스프레스 실제 상품 이미지 3장 (AI 생성 0장)
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


SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or _env_local("SUPABASE_SERVICE_ROLE_KEY")
REVALIDATE_URL = ("https://www.k-trand.store/api/revalidate?secret="
                  + _require_env("REVALIDATE_SECRET"))
SLUG = "wconcept-w-week-aliexpress-blackfriday-2026"

K = "https://www.coupang.com/np/search?q="
TAG = "&lptag=AF9412775"


def q(s):
    return K + quote(s) + TAG


C = "/images/products/bf-wconcept-frontrow-coat.jpg"
G1 = "/images/products/bf-wconcept-mooneed-knit.jpg"
G2 = "/images/products/bf-aliexpress-ajazz-ak820.jpg"

KO_DESC = """마감일이 다른 두 행사가 오늘 겹친다. W컨셉 '더블유위크'는 11월 25일 오늘 끝나고, 알리익스프레스 블랙프라이데이는 12월 3일까지 남아 있다. 성격이 달라서 한 글에 같이 담았다. 앞은 겨울옷, 뒤는 가성비 IT·데스크템이다.
W컨셉 더블유위크는 11월 9일 시작해 17일간 열렸다. 패션·뷰티·라이프 약 20만 개 상품이 참여하고, 공식 발표 기준 최대 85% 할인이다. 550여 개 브랜드가 24시간 릴레이 특가와 단독 특가를 걸었고, 매일 오전 10시에는 9,900원·59,900원 균일가 오픈런, 매일 오후 6시에는 선착순 50% 할인쿠폰과 참여 브랜드 30% 쿠폰이 나왔다. 뷰티·라이프는 별도 30% 쿠폰이 붙었다.

1. W컨셉 — 표시 판매가가 실제 결제액이다
프론트로우 캐시미어 하프 코트(상품 307059292)는 정상가 499,000원에 상품할인 50%, 여기에 한파대비 추가 할인과 쿠폰이 붙어 표시 판매가가 203,841원(59% 할인)이다. 캐시미어 30%·울 70% 혼방, 색상은 블랙과 아이보리, 사이즈 XS·S·M이다. 배송은 무료이고 오후 4시까지 결제하면 당일 출고다.
무니드 PLAIN DEEP U-NECK 니트(상품 308840498)는 정상가 104,000원에서 30% 쿠폰이 적용돼 72,800원이다. 메리노울 10%·캐시미어 3% 혼방, 원사이즈 3컬러다. 다만 10만 원 미만이면 배송비 3,500원이 붙어 실결제는 76,300원이다. 쿠폰 하나로 10만 원 선을 넘기지 못하면 배송비가 할인액을 갉아먹는다.
여기서 봐야 할 것은 '최대 85%'라는 숫자다. 85%는 행사 전체에서 일부 상품에만 붙는 값이고, 코트처럼 단가가 높은 상품은 50% 안팎에서 추가 쿠폰이 얹히는 구조다. 쿠폰마다 최소 구매금액과 할인 한도가 따로 걸리므로, 상품 페이지의 '할인내역'에서 실제 차감액을 확인해야 한다. 남은 시간이 하루도 안 남았으니 결제 화면 숫자로 판단하는 게 맞다.

2. 알리익스프레스 — 12월 3일까지, 단계가 나뉜다
알리익스프레스 블랙프라이데이는 11월 19일 시작해 12월 3일까지 15일간 열린다. 광군제가 끝난 다음 날 바로 이어지는 올해 마지막 대형 세일이고, 플랫폼 인기 상품 기준 최대 70% 할인이다. 행사는 네 단계로 쪼개진다. 11월 19~23일 톱 브랜드 데이, 24~26일 생활필수품 '알급날', 27~30일 베스트셀러, 12월 1~3일 해외직구 특가 '초이스데이'다.
할인코드는 금액대별로 나뉜다. 21달러 이상 3달러, 58달러 이상 8달러, 98달러 이상 13달러, 149달러 이상 19달러, 222달러 이상 26달러, 375달러 이상 45달러다. 여기에 카드사·페이 결제 할인이 겹치고, 일부는 앱에서만 받을 수 있는 다운로드 전용 코드다.
실제 품목 하나를 보자. AJAZZ AK820 기계식 키보드는 11월 25일 아침 26,004원이다. 알리 표시 할인율은 58%이고, 세일 직전(10월 27일) 가격 33,000원과 비교하면 21% 낮다. 다만 11월 20일에는 25,059원까지 내려갔고, 35일 평균은 30,333원이었다. 최근 판매 8,324개, 긍정 평가 98%다.
중요한 건 알리의 '표시 할인율'을 그대로 믿지 않는 것이다. 알리는 정가 표시도 함께 움직이기 때문에, 할인율이 50%에서 58% 사이를 오가도 실제 판매가는 25,000~33,000원 사이에서 움직였다. 판단 기준은 할인율이 아니라 오늘의 판매가와 지난달 판매가다.

3. 두 행사를 같이 볼 때의 계산
W컨셉은 오늘 밤이 사실상 마감이다. 오후 6시 50% 쿠폰이 마지막 회차이고, 브랜드별 24시간 특가는 브랜드마다 종료 시각이 다르다. 겨울 코트처럼 단가가 높은 상품은 쿠폰 한도에 걸려 할인 폭이 줄어들 수 있으니, 결제 화면에서 최종 금액을 확인하고 사야 한다.
알리는 12월 3일까지 시간이 있지만 배송이 문제다. 중국에서 오는 주문은 보통 2~3주 걸리고, 12월 초에 주문하면 연말 선물로 쓰기 어렵다. 또 알리는 미국발이 아니므로 목록통관 면세 기준이 200달러가 아니라 150달러다. 150달러를 넘으면 넘은 금액만이 아니라 물품가격 전체에 관세와 부가세가 붙는다. 키보드·마우스 같은 소액 IT 기기는 대부분 기준 안쪽이지만, 모니터나 미니 PC를 함께 담으면 선을 넘는다.
AS도 다르다. 알리 직구 상품은 국내 AS가 사실상 없고, 하자 발생 시 반품·환불 절차가 길다. W컨셉은 국내 브랜드 정품이라 교환·반품이 쉽다. 같은 돈이면 겨울옷은 오늘 W컨셉에서, 소모품·악세서리는 알리에서 사는 게 합리적이다.

결제 전 확인 세 가지
첫째, 마감 시각이다. W컨셉은 오늘, 알리는 12월 3일이다. W컨셉은 브랜드별 특가 종료 시각이 달라 상품 페이지에서 확인해야 한다.
둘째, 쿠폰의 최소 구매금액과 할인 한도다. 50% 쿠폰이 30만 원짜리 코트에 15만 원을 깎아주지 않는 경우가 흔하다.
셋째, 배송일과 관부가세다. 알리는 2~3주, W컨셉은 당일 출고다. 알리 주문 합계가 150달러를 넘지 않는지도 확인해야 한다.

한 줄 정리
오늘 안에 끝내야 하는 것은 W컨셉이다. 프론트로우 코트는 499,000원에서 203,841원(59%), 무니드 니트는 104,000원에서 72,800원(배송비 포함 76,300원)까지 내려왔다. 알리는 12월 3일까지이므로 연말 선물이 아니면 서두를 이유가 없고, 150달러 기준과 2~3주 배송을 계산에 넣어야 한다."""

EN_DESC = """Two sales with different deadlines overlap today. W Concept's W Week ends on November 25, today, while AliExpress's Black Friday runs to December 3. They are different kinds of shopping: winter clothing in the first, budget IT and desk gear in the second.
W Week began on November 9 and ran 17 days. About 200,000 fashion, beauty and lifestyle products took part, with an official maximum discount of 85%, and some 550 brands ran 24-hour relay deals and brand-exclusive prices. Every day at 10 a.m. there was a flat-price open run at 9,900 and 59,900 won, and at 6 p.m. a first-come 50% coupon plus 30% brand coupons; beauty and lifestyle had a separate 30% coupon.

1. W Concept — the listed price is what you pay
The Frontrow cashmere half coat (product 307059292) lists at 499,000 won, with 50% off, a cold-wave extra discount and coupons applied to a listed price of 203,841 won, 59% off. It is 30% cashmere and 70% wool, in black or ivory, sizes XS to M, with free shipping and same-day dispatch for orders before 4 p.m.
The Mooneed plain deep U-neck knit (308840498) drops from 104,000 won to 72,800 won with a 30% coupon. It is 10% merino and 3% cashmere, one size, three colours — but under 100,000 won a 3,500-won shipping fee applies, so the real total is 76,300 won. If one coupon does not push you past the free-shipping line, shipping eats the discount.
The number to watch is "up to 85%". That ceiling applies to a few items across the event; high-ticket coats sit around 50% plus stacked coupons. Each coupon carries its own minimum spend and cap, so read the discount breakdown on the product page. With less than a day left, judge by the number on the checkout screen.

2. AliExpress — through December 3, in stages
AliExpress Black Friday started November 19 and runs to December 3, 15 days, the last big sale of the year right after 11.11, with up to 70% off popular items. It is split into four stages: Top Brand Day November 19-23, "Al-geup-nal" household essentials November 24-26, Bestsellers November 27-30, and the cross-border deals day Choice Day December 1-3.
Discount codes step by basket size: $3 off $21, $8 off $58, $13 off $98, $19 off $149, $26 off $222, $45 off $375, stacked with card and wallet discounts; some codes are download-only in the app.
One real item: the AJAZZ AK820 mechanical keyboard is 26,004 won on the morning of November 25. AliExpress shows 58% off, and against the pre-sale price of 33,000 won on October 27 it is 21% lower. It did fall to 25,059 won on November 20, and the 35-day average is 30,333 won, with 8,324 recent sales and 98% positive.
The lesson is not to trust the displayed rate. AliExpress moves its list price too: the badge swung between 50% and 58% while the actual price moved between 25,000 and 33,000 won. Compare today's price with last month's, not the badge.

3. Looking at both together
W Week effectively ends tonight. The 6 p.m. 50% coupon is the last round, and each brand's 24-hour deal closes at its own time. On expensive coats, coupon caps can shrink the real discount, so check the final amount at checkout.
AliExpress has until December 3, but shipping is the constraint: China orders take two to three weeks, so an early-December order is a poor year-end gift. And because AliExpress ships from China, not the US, the duty-free list-clearance limit is $150, not $200; above it the whole value is taxed. Keyboards and mice stay under, but a monitor or mini PC can push you over.
Warranty differs too: AliExpress items have effectively no Korean service and long return routes, while W Concept sells Korean brand goods with easy exchanges. For the same money, buy winter clothing at W Concept today and consumables or accessories from AliExpress.

Three checks before paying
First, the deadline: W Concept today, AliExpress December 3, with per-brand closing times on W Concept. Second, each coupon's minimum spend and cap — a 50% coupon often does not take 150,000 won off a 300,000-won coat. Third, delivery and duty: two to three weeks from AliExpress versus same-day dispatch from W Concept, and keep the AliExpress basket under $150.

Bottom line
What must be finished today is W Concept: the Frontrow coat at 203,841 won from 499,000 (59% off) and the Mooneed knit at 72,800 won from 104,000 (76,300 with shipping). AliExpress has until December 3, so there is no rush unless it is a year-end gift — and then the $150 limit and two-to-three-week shipping belong in the calculation."""

JA_DESC = """締切の違う2つのセールが今日重なります。Wコンセプトの「Wウィーク」は11月25日の今日で終わり、アリエクスプレスのブラックフライデーは12月3日まで続きます。性格が違うので1本にまとめました。前半は冬物、後半はコスパIT・デスク用品です。
Wウィークは11月9日から17日間。ファッション・ビューティー・ライフ約20万点が参加し、公式発表で最大85%オフ。約550ブランドが24時間リレー特価と単独特価を出し、毎日午前10時に9,900ウォン・59,900ウォンの均一価格オープンラン、毎日午後6時に先着50%クーポンと参加ブランド30%クーポンが配られました。ビューティー・ライフは別枠の30%クーポンもありました。

1. Wコンセプト——表示販売価格が実際の支払額
フロントロウのカシミヤハーフコート(商品307059292)は定価499,000ウォンに商品割引50%、さらに寒波対策の追加割引とクーポンが乗って表示販売価格203,841ウォン(59%オフ)。カシミヤ30%・ウール70%、ブラックとアイボリー、XS〜M、送料無料で午後4時までの決済なら当日出荷です。
ムニードのPLAIN DEEP U-NECKニット(308840498)は定価104,000ウォンから30%クーポンで72,800ウォン。メリノウール10%・カシミヤ3%、ワンサイズ3色ですが、10万ウォン未満は送料3,500ウォンが付き実質76,300ウォンです。クーポン1枚で送料無料ラインを超えられないと、送料が割引を削ります。
見るべきは「最大85%」という数字です。85%は一部商品だけの上限で、コートのような高単価品は50%前後に追加クーポンが乗る構造。クーポンごとに最低購入額と割引上限があるので、商品ページの割引内訳で実際の差引額を確認してください。残り1日を切っているので、決済画面の数字で判断するのが正解です。

2. アリエクスプレス——12月3日まで、段階が分かれる
アリエクのブラックフライデーは11月19日から12月3日までの15日間。11.11の翌日に始まる今年最後の大型セールで、人気商品は最大70%オフ。4段階に分かれます。11月19〜23日トップブランドデー、24〜26日生活必需品の「アルグプナル」、27〜30日ベストセラー、12月1〜3日越境特価の「チョイスデー」。
割引コードは金額帯別で、21ドル以上3ドル、58ドル以上8ドル、98ドル以上13ドル、149ドル以上19ドル、222ドル以上26ドル、375ドル以上45ドル。カード・ペイ決済割引も重なり、一部はアプリ内ダウンロード専用コードです。
実例を1つ。AJAZZ AK820メカニカルキーボードは11月25日朝で26,004ウォン。アリエク表示は58%オフ、セール直前(10月27日)の33,000ウォンと比べ21%安い。ただし11月20日には25,059ウォンまで下がり、35日平均は30,333ウォン。最近の販売8,324個、肯定評価98%です。
大事なのは表示割引率を信じないこと。アリエクは定価表示も動くため、バッジは50〜58%を行き来しても実売価格は25,000〜33,000ウォンの範囲でした。基準は割引率ではなく、今日の価格と先月の価格です。

3. 2つを並べて考える
Wコンセプトは今夜が実質締切。午後6時の50%クーポンが最終回で、ブランド別24時間特価はブランドごとに終了時刻が違います。高額コートはクーポン上限で割引が縮むことがあるので、決済画面の最終金額で判断を。
アリエクは12月3日までありますが送料が制約です。中国発は通常2〜3週間、12月初旬の注文は年末の贈り物に間に合いません。また中国発なのでリスト通関の免税基準は200ドルではなく150ドル。超えると全額に課税されます。キーボードやマウスは範囲内でも、モニターやミニPCを足すと超えます。
保証も違います。アリエクは国内サービスが実質なく返品手続きも長く、Wコンセプトは国内ブランド正規品で交換が容易です。同じ金額なら冬物は今日Wコンセプトで、消耗品・アクセサリーはアリエクで買うのが合理的です。

支払い前の確認3点
第一に締切。Wコンセプトは今日、アリエクは12月3日。Wコンセプトはブランド別の終了時刻を商品ページで確認。第二にクーポンの最低購入額と上限。50%クーポンが30万ウォンのコートから15万ウォンを引かないことはよくあります。第三に配送日と関税。アリエク2〜3週間、Wコンセプトは当日出荷。アリエクの合計が150ドルを超えないかも確認を。

まとめ
今日中に終えるべきはWコンセプト。フロントロウのコートは499,000ウォン→203,841ウォン(59%)、ムニードのニットは104,000ウォン→72,800ウォン(送料込み76,300ウォン)。アリエクは12月3日までなので年末の贈り物でなければ急ぐ理由はなく、150ドル基準と2〜3週間の配送を計算に入れるべきです。"""

ZH_DESC = """两个截止日不同的活动今天重叠。W Concept的「W Week」11月25日今天结束，速卖通黑色星期五持续到12月3日。性质不同，本文合并介绍：前者是冬装，后者是性价比IT与桌面用品。
W Week从11月9日开始，历时17天。时尚、美妆、生活约20万件商品参加，官方最高85%折扣，约550个品牌推出24小时接力特价与单独特价。每天上午10点有9,900韩元、59,900韩元均一价抢购，每天下午6点发放先到先得50%优惠券与参与品牌30%券；美妆与生活另有30%券。

1. W Concept——显示售价就是实际支付额
Frontrow羊绒半大衣（商品307059292）定价499,000韩元，商品折扣50%，加上寒潮额外折扣与优惠券，显示售价203,841韩元（59%折扣）。羊绒30%、羊毛70%，黑色与象牙白，XS~M，免运费，下午4点前付款当日出库。
Mooneed PLAIN DEEP U-NECK针织（308840498）定价104,000韩元，30%券后72,800韩元。美利奴羊毛10%、羊绒3%，均码三色；但不满10万韩元需加3,500韩元运费，实付76,300韩元。一张券跨不过免运线，运费就吃掉折扣。
要看清「最高85%」。85%只适用于部分商品，像大衣这种高单价商品多为50%左右再加券。每张券都有最低消费与折扣上限，应在商品页的「折扣明细」确认实际扣减额。只剩不到一天，用结算页的数字判断才准确。

2. 速卖通——到12月3日，分四个阶段
速卖通黑五从11月19日到12月3日，共15天，是双十一之后今年最后的大促，人气商品最高70%折扣。分四阶段：11月19~23日顶级品牌日、24~26日生活必需品「Al-geup-nal」、27~30日畅销榜、12月1~3日跨境特价「Choice Day」。
优惠码按金额分档：满21美元减3、满58减8、满98减13、满149减19、满222减26、满375减45，可与银行卡、钱包折扣叠加，部分为App内下载专用码。
一个实例：AJAZZ AK820机械键盘11月25日早为26,004韩元，速卖通显示58%折扣；与促销前（10月27日）33,000韩元相比低21%。但11月20日曾降到25,059韩元，35天均价30,333韩元，近期销量8,324件、好评98%。
关键是不要相信显示折扣率。速卖通的定价也会变动：标识在50%~58%之间摆动时，实际售价只在25,000~33,000韩元之间。判断依据应是今天的价格与上月的价格。

3. 两个活动一起看
W Week今晚实质截止。下午6点的50%券是最后一轮，各品牌24小时特价结束时间不同。高价大衣可能受券上限限制，需在结算页确认最终金额。
速卖通到12月3日，但物流是限制：中国发货通常2~3周，12月初下单难以作为年末礼物。且因来自中国，清单通关免税限额是150美元而非200美元，超额按全额课税。键盘鼠标在额度内，但加上显示器或迷你主机就会超。
售后也不同：速卖通在韩国几乎没有售后、退货流程长；W Concept是韩国品牌正品，换货方便。同样的钱，冬装今天在W Concept买、耗材与配件在速卖通买更合理。

付款前三项确认
第一，截止时间：W Concept今天、速卖通12月3日，W Concept需确认各品牌结束时间。第二，优惠券的最低消费与上限，50%券常常不会给30万韩元大衣减15万。第三，配送日与关税：速卖通2~3周、W Concept当日出库，还要确认速卖通合计不超过150美元。

一句话总结
今天必须结束的是W Concept：Frontrow大衣499,000→203,841韩元（59%），Mooneed针织104,000→72,800韩元（含运费76,300）。速卖通到12月3日，若不是年末礼物就不必着急，但要把150美元限额与2~3周物流算进去。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "store": "W컨셉·알리익스프레스",
    "priceKrw": 203841,
    "releaseDate": "2026-11-25",
    "rating": 4.5,
    "imageUrl": C,
    "images": [G1, G2],
    "affiliateUrl": q("겨울 코트 니트"),
    "affiliatePlatform": "Coupang",
    "exampleItems": [
        {
            "name": "프론트로우 캐시미어 하프 코트 (W컨셉, 59% 할인)",
            "brand": "FRONTROW",
            "priceKrw": 203841,
            "imageUrl": "/images/products/bf-wconcept-frontrow-coat.jpg",
            "url": "https://www.wconcept.co.kr/Product/307059292",
            "category": "코트",
        },
        {
            "name": "무니드 PLAIN DEEP U-NECK 니트 (W컨셉, 30% 쿠폰)",
            "brand": "MOONEED",
            "priceKrw": 72800,
            "imageUrl": "/images/products/bf-wconcept-mooneed-knit.jpg",
            "url": "https://www.wconcept.co.kr/Product/308840498",
            "category": "니트",
        },
        {
            "name": "AJAZZ AK820 기계식 키보드 (알리익스프레스)",
            "brand": "AJAZZ",
            "priceKrw": 26004,
            "imageUrl": "/images/products/bf-aliexpress-ajazz-ak820.jpg",
            "url": "https://ko.aliexpress.com/",
            "category": "키보드",
        },
    ],
    "i18n": {
        "ko": {
            "title": "오늘 끝나는 W컨셉 더블유위크, 12월 3일까지 알리 블프 — 실결제가로 계산한 3종",
            "summary": "W컨셉 더블유위크는 11/9~25(오늘 마감), 알리익스프레스 블프는 11/19~12/3입니다. 프론트로우 캐시미어 코트는 499,000원→203,841원(59%), 무니드 니트는 104,000원→72,800원(배송 포함 76,300원), 알리 AJAZZ AK820 키보드는 26,004원(세일 전 33,000원 대비 21%↓)입니다.",
            "description": KO_DESC,
            "tasteReview": [
                "W컨셉 더블유위크 11/9~25, 약 20만 개·최대 85%, 550여 브랜드, 매일 10시 오픈런·18시 50% 쿠폰",
                "프론트로우 캐시미어 하프 코트 499,000원→203,841원(59%), 무니드 U넥 니트 104,000원→72,800원(+배송 3,500원)",
                "알리 블프 11/19~12/3, 최대 70%, 톱브랜드데이·알급날·베스트셀러·초이스데이 4단계",
                "알리 할인코드: $21↑ -3 / $58↑ -8 / $98↑ -13 / $149↑ -19 / $222↑ -26 / $375↑ -45",
                "AJAZZ AK820 26,004원 — 세일 전 33,000원 대비 21%↓, 11/20 최저 25,059원, 알리 표시 할인율은 50~58%로 흔들림",
                "중국발은 목록통관 150달러 기준, 배송 2~3주, 국내 AS 사실상 없음",
            ],
            "tips": "가격은 2026-11-25 확인값이며 쿠폰·카드할인에 따라 달라집니다. 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있습니다.",
        },
        "en": {
            "title": "W Concept's W Week Ends Today, AliExpress Runs to December 3 — 3 Items at Real Checkout Prices",
            "summary": "W Concept's W Week runs November 9-25 and ends today, while AliExpress Black Friday runs November 19-December 3. The Frontrow cashmere coat falls from 499,000 won to 203,841 (59% off), the Mooneed knit from 104,000 to 72,800 (76,300 with shipping), and the AJAZZ AK820 keyboard is 26,004 won, 21% below its pre-sale 33,000 won.",
            "description": EN_DESC,
            "tasteReview": [
                "W Week November 9-25, about 200,000 items, up to 85% off, 550 brands, 10 a.m. open run and 6 p.m. 50% coupon daily",
                "Frontrow cashmere half coat 499,000 to 203,841 won (59% off); Mooneed U-neck knit 104,000 to 72,800 won plus 3,500 shipping",
                "AliExpress Black Friday November 19-December 3, up to 70% off, in four stages from Top Brand Day to Choice Day",
                "AliExpress codes: $3 off $21, $8 off $58, $13 off $98, $19 off $149, $26 off $222, $45 off $375",
                "AJAZZ AK820 at 26,004 won, 21% below the 33,000-won pre-sale price; low of 25,059 won on Nov 20; the displayed rate swung 50-58%",
                "Chinese shipments: $150 list-clearance limit, two to three weeks delivery, effectively no Korean warranty",
            ],
            "tips": "Prices were checked on 25 November 2026 and move with coupons and card discounts. This post contains affiliate links and may earn a commission.",
        },
        "ja": {
            "title": "今日終わるWコンセプトWウィーク、12月3日までアリエク——実支払額で計算した3点",
            "summary": "WコンセプトのWウィークは11/9〜25で今日終了、アリエクのブラックフライデーは11/19〜12/3。フロントロウのカシミヤコートは499,000→203,841ウォン(59%オフ)、ムニードのニットは104,000→72,800ウォン(送料込み76,300)、アリエクのAJAZZ AK820キーボードは26,004ウォン(セール前33,000ウォン比21%安)です。",
            "description": JA_DESC,
            "tasteReview": [
                "Wウィーク11/9〜25、約20万点・最大85%オフ、550ブランド、毎日10時オープンラン・18時50%クーポン",
                "フロントロウのカシミヤハーフコート499,000→203,841ウォン(59%)、ムニードのUネックニット104,000→72,800ウォン(+送料3,500)",
                "アリエク11/19〜12/3、最大70%オフ、トップブランドデー・アルグプナル・ベストセラー・チョイスデーの4段階",
                "アリエクコード: 21ドル以上3ドル、58ドル8ドル、98ドル13ドル、149ドル19ドル、222ドル26ドル、375ドル45ドル",
                "AJAZZ AK820 26,004ウォン——セール前33,000ウォン比21%安、11/20最安25,059ウォン、表示割引率は50〜58%で変動",
                "中国発はリスト通関150ドル基準、配送2〜3週間、国内保証は実質なし",
            ],
            "tips": "価格は2026-11-25確認値で、クーポンやカード割引により変わります。本記事はアフィリエイトリンクを含み手数料を受け取る場合があります。",
        },
        "zh": {
            "title": "今天截止的W Concept W Week，与到12月3日的速卖通黑五——按实付价计算的3件",
            "summary": "W Concept的W Week为11/9~25（今天截止），速卖通黑五为11/19~12/3。Frontrow羊绒大衣从499,000降至203,841韩元（59%折扣），Mooneed针织从104,000降至72,800韩元（含运费76,300），速卖通AJAZZ AK820键盘26,004韩元（比促销前33,000低21%）。",
            "description": ZH_DESC,
            "tasteReview": [
                "W Week 11/9~25，约20万件、最高85%折扣、550个品牌，每天10点抢购、18点50%券",
                "Frontrow羊绒半大衣499,000→203,841韩元（59%），Mooneed U领针织104,000→72,800韩元（另加运费3,500）",
                "速卖通11/19~12/3，最高70%折扣，顶级品牌日·Al-geup-nal·畅销榜·Choice Day四阶段",
                "速卖通优惠码：满21美元减3、58减8、98减13、149减19、222减26、375减45",
                "AJAZZ AK820 26,004韩元——比促销前33,000低21%，11/20最低25,059，显示折扣率在50~58%间摆动",
                "中国发货适用150美元清单通关限额，物流2~3周，韩国基本无售后",
            ],
            "tips": "价格为2026-11-25确认值，随优惠券与银行卡折扣变化。本文含联盟链接，可能获得佣金。",
        },
    },
}

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
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
