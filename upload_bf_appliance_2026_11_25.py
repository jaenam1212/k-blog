#!/usr/bin/env python3
"""쿠팡 가전 블프 팩트체크 (2026) → Supabase posts + ISR revalidate (4개국어).

근거
 - 쿠팡 판매가·정가·리뷰·설치일: 2026-11-25 11:50~12:10 KST 쿠팡 검색 화면 직접 확인
 - LG전자 공식몰(lge.co.kr) OLED55C6KNA: 2,989,000원 정가, 9% 할인 2,706,300원, 평점 4.9·리뷰 90
 - 다이슨 코리아(dyson.co.kr) 에어랩 i.d. 세라믹 핑크 161829-01: 699,000원 권장가, 판매가 689,000원, 평점 4.6
 - 삼성전자 뉴스룸(2025-01-01): 갤럭시북5 프로 16형 16GB/512GB 출시가 2,458,000원(전작 대비 13만2,000원 인하)
 - 사진: LG전자·다이슨·삼성전자 실제 제품 이미지 3장 (AI 생성 0장)
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


SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or _env_local("SUPABASE_SERVICE_ROLE_KEY")
REVALIDATE_URL = "https://www.k-trand.store/api/revalidate?secret=kblog2026"
SLUG = "coupang-appliance-blackfriday-factcheck-2026"

K = "https://www.coupang.com/np/search?q="
TAG = "&lptag=AF9412775"


def q(s):
    return K + quote(s) + TAG


C = "/images/products/bf-appliance-lg-oled55c6.jpg"
G1 = "/images/products/bf-appliance-dyson-airwrap-id.jpg"
G2 = "/images/products/bf-appliance-galaxybook5-pro.jpg"

KO_DESC = """쿠팡 가전·디지털 블랙프라이데이는 11월 16일부터 29일까지다. 그런데 이 행사에서 가장 많이 나오는 숫자 '최대 21% 할인'은 상품 페이지에 적힌 정가를 기준으로 계산된다. 정가가 얼마로 잡혀 있느냐에 따라 같은 판매가도 30% 할인이 되고 2% 할인이 된다. 그래서 이번에는 할인율을 보지 않고, 제조사 공식몰 판매가와 출시가를 나란히 놓고 비교했다. 쿠팡이 공개하지 않는 '블프 직전 가격 인상' 여부도 이 방법이면 간접적으로 드러난다.
기준 시각은 11월 25일 오전 11시 50분부터 12시 10분까지다. 쿠팡 판매가·정가·리뷰·설치 가능일을 직접 확인했고, 비교 대상은 LG전자 공식몰, 다이슨 코리아 공식몰, 삼성전자 출시 보도자료다.

1. 진짜로 내린 것 — LG 올레드 evo AI 55C6KNA
쿠팡 로켓배송 판매가는 2,334,300원이다. 표시된 정가는 2,989,000원, 할인율 21%다. 리뷰 132개에 설치일은 11월 26일부터 12월 26일 사이에서 고를 수 있다.
LG전자 공식몰에서 같은 모델(스탠드형)은 정가 2,989,000원에 9% 할인한 2,706,300원이다. 쿠팡이 372,000원, 13.7% 싸다. 공식몰 할인율(9%)의 세 배가 넘는 폭이 쿠팡에서 실제로 붙어 있다는 뜻이다. 이건 '할인인 척'이 아니라 진짜 인하로 봐도 되는 사례다.
다만 같은 검색 화면에 이름이 비슷한 모델이 여럿 섞여 있다. 55B6NNA가 1,361,000원, 55B5NNA가 1,332,390원(29% 할인)이다. C6는 올레드 evo(밝기 부스터 적용), B6·B5는 일반 올레드다. 100만 원 차이의 절반은 세대와 패널 등급 차이다. 화면 크기만 보고 고르면 이 차이를 놓친다.

2. 진짜로 내린 것 — 다이슨 에어랩 i.d. 멀티 스타일러
쿠팡에서 세라믹 핑크(161829-01)는 699,000원 정가에 29% 할인한 495,200원, 버건디 우드(492321-01)는 31% 할인한 476,510원이다. 둘 다 '쿠폰할인' 표기가 붙어 있고 리뷰는 2,297개다. 다음 날 도착 보장이다.
다이슨 코리아 공식몰은 같은 모델을 권장소비자가 699,000원, 판매가 689,000원에 판다. 평점 4.6, 무상 보증 2년이다. 쿠팡 쿠폰가(476,510원)와 비교하면 212,490원, 30.8% 차이다. 공식몰이 689,000원에 팔면서 쿠팡에서 47만 원대에 팔리는 것은, 쿠팡 쪽에 별도 쿠폰 예산이 붙어 있다는 뜻이다. 쿠폰이 끝나면 이 가격은 사라진다.
주의할 점은 모델명이다. 에어랩은 '에어랩 i.d.'와 '에어랩 2x(신형)', '에어랩 오리진(3툴 구성)'이 함께 검색된다. 3툴 구성은 툴 개수가 다르고, 2x는 모터 출력이 다르다. 가격만 비교하면 가장 기본 구성이 가장 싸 보인다.

3. 할인처럼 보이지만 2.4%짜리 — 갤럭시북5 프로 16
쿠팡에서 갤럭시북5 프로 NT960XHA-K51A(인텔 울트라5, 16GB, 512GB)는 정가 2,832,000원에 15% 할인한 2,398,000원으로 표시된다. 리뷰 1,204개, 할인 폭 434,000원이라고 읽힌다.
그런데 삼성전자가 이 모델을 출시할 때 밝힌 16형·16GB·512GB 가격은 2,458,000원이다(전작 대비 13만2,000원 인하한 가격). 쿠팡 판매가 2,398,000원과 비교하면 차액은 60,000원, 2.4%다. 즉 '15% 할인'의 대부분은 정가를 출시가보다 37만 원 높게 잡아 만든 숫자다. 실제로 아낀 돈은 6만 원이다.
같은 검색에서 갤럭시북5(NT750XHW-A51A, 15.6형·1TB)는 2,199,000원에서 9% 할인한 1,981,070원이다. 프로가 아닌 모델과의 차이까지 같이 봐야 한다.

4. 이름이 같아도 가격이 두 배인 함정
LG 올레드 55C6 계열 검색 결과에는 2,334,300원(로켓배송) 말고도 1,675,000원짜리 스탠드형이 함께 나온다. 모델명 표기가 비슷하지만 판매자와 구성이 다르다. 설치 방식(스탠드·벽걸이)과 판매자 보증을 확인하지 않고 가격만 보고 고르면, 설치비나 AS에서 차액이 다시 나간다.
쿠팡은 상품 페이지에 최근 가격 이력을 공개하지 않는다. 그래서 '블프 직전에 올리고 할인하는 척했는지'는 쿠팡 화면만으로는 증명할 수 없다. 대신 제조사 공식몰 가격과 출시가를 대조하면, 할인율이 실제인지 정가 부풀리기인지 구분된다. 이번 3종에서는 LG TV와 다이슨은 실제 인하, 갤럭시북은 정가 부풀리기 쪽이었다.

결제 전에 확인할 세 가지
첫째, 정가가 제조사 출시가와 같은지 본다. 다르면 할인율은 광고 숫자다.
둘째, 쿠폰 종류와 종료 시점을 확인한다. '쿠폰할인' 표기는 쿠폰이 소진되면 사라진다. 카드 즉시할인·무이자 할부가 겹치는지도 결제 화면에서 확인해야 한다.
셋째, 설치일과 반품 조건이다. TV·노트북은 방문설치 일정이 11월 26일~12월 26일로 잡혀 있어, 연말 전 설치가 필요하면 날짜를 먼저 고정해야 한다.

한 줄 정리
이번 쿠팡 가전 블프에서 확실히 싼 것은 LG 올레드 55C6KNA(공식몰 대비 13.7%↓)와 다이슨 에어랩 i.d.(30.8%↓)였고, 갤럭시북5 프로의 '15% 할인'은 실제로는 2.4%(6만 원)였다. 할인율이 아니라 제조사 공식몰 가격과 출시가를 기준으로 비교하는 것이 이번 주 가전 구매에서 돈을 지키는 방법이다."""

EN_DESC = """Coupang's appliance and digital Black Friday runs from November 16 to 29. The number it advertises most, "up to 21% off," is calculated against whatever list price sits on the product page. The same selling price becomes a 30% discount or a 2% discount depending on that list price. So this time we ignored the discount badge and lined up the maker's own official-store price and launch price instead. That method also exposes, indirectly, the pre-Black Friday price bump Coupang does not disclose.
Everything here was checked between 11:50 and 12:10 on November 25: Coupang prices, list prices, reviews and installation windows, against LG's official store, Dyson Korea's official store and Samsung's launch release.

1. A real cut — LG OLED evo AI 55C6KNA
Coupang's Rocket Delivery price is 2,334,300 won against a 2,989,000-won list, a 21% discount, with 132 reviews and an installation date selectable between November 26 and December 26.
LG's own store sells the same stand model at 2,706,300 won, 9% off the same 2,989,000-won list. Coupang is 372,000 won, or 13.7%, cheaper — more than three times the official store's discount. This is a real cut, not a badge.
The same search page also mixes in similar names: 55B6NNA at 1,361,000 won and 55B5NNA at 1,332,390 won (29% off). The C6 is OLED evo with the brightness booster; the B6 and B5 are standard OLED. Half of that million-won gap is generation and panel grade, not size.

2. A real cut — Dyson Airwrap i.d. Multi-styler
On Coupang, the ceramic pink (161829-01) is 495,200 won, 29% off 699,000 won, and the burgundy wood (492321-01) is 476,510 won, 31% off. Both carry a coupon discount and 2,297 reviews, arriving tomorrow.
Dyson Korea's official store sells the same model at a 699,000-won recommended price and a 689,000-won selling price, rated 4.6 with a two-year warranty. Against Coupang's 476,510 won that is 212,490 won, or 30.8%. An official store at 689,000 won while Coupang sells at 476,510 won means Coupang is carrying its own coupon budget — and that price disappears when the coupon does.
Watch the model name: Airwrap i.d., the newer Airwrap 2x and the three-tool Airwrap Origin all appear together. Tool counts and motor output differ, so a price-only comparison makes the base kit look like the best buy.

3. Looks like a discount, is 2.4% — Galaxy Book5 Pro 16
Coupang lists the Galaxy Book5 Pro NT960XHA-K51A (Intel Ultra 5, 16GB, 512GB) at 2,398,000 won, 15% off a 2,832,000-won list, with 1,204 reviews — apparently a 434,000-won saving.
But Samsung announced this configuration (16-inch, 16GB, 512GB) at 2,458,000 won at launch, already 132,000 won below its predecessor. Against 2,398,000 won the real gap is 60,000 won, or 2.4%. Most of the "15%" comes from a list price set 374,000 won above the launch price. The money actually saved is 60,000 won.
The same search shows the non-Pro Galaxy Book5 (NT750XHW-A51A, 15.6-inch, 1TB) at 1,981,070 won, 9% off 2,199,000 won.

4. The same name at double the price
The 55C6 results include a 1,675,000-won stand model alongside the 2,334,300-won Rocket listing. The name looks the same; the seller and configuration are not. Pick on price alone and the difference comes back as installation fees or a weaker warranty.
Coupang does not publish price history, so "did they raise it just before Black Friday" cannot be proven from the Coupang page alone. Comparing against the maker's official store and launch price separates a real discount from an inflated list. Of the three items here, LG and Dyson were real; the Galaxy Book was the inflated list.

Three checks before paying
First, does the list price match the maker's launch price? If not, the discount rate is advertising.
Second, which coupon, and until when? A "coupon discount" vanishes when the coupon runs out, and card discounts or interest-free instalments need checking on the payment screen.
Third, installation date and returns. TV and laptop installation windows run November 26 to December 26, so fix the date first if you need it before year-end.

Bottom line
In this Coupang appliance sale the genuine cuts were the LG OLED 55C6KNA (13.7% below the official store) and the Dyson Airwrap i.d. (30.8% below); the Galaxy Book5 Pro's "15% off" was really 2.4%, or 60,000 won. Comparing against the maker's official price and launch price, rather than the badge, is how you keep your money on appliances this week."""

JA_DESC = """クーパンの家電・デジタルブラックフライデーは11月16日から29日まで。そこで最も多く見かける「最大21％オフ」は、商品ページに書かれた定価を基準に計算されます。定価の取り方次第で、同じ販売価格が30％引きにも2％引きにもなります。そこで今回は割引率を見ず、メーカー公式ストアの販売価格と発売価格を並べて比較しました。クーパンが公開しない「ブラックフライデー直前の値上げ」も、この方法なら間接的に見えてきます。
基準時刻は11月25日午前11時50分から12時10分。クーパンの販売価格・定価・レビュー・設置可能日を確認し、比較対象はLG電子公式ストア、ダイソンコリア公式ストア、サムスン電子の発売資料です。

1. 本当に下がった — LG OLED evo AI 55C6KNA
クーパンのロケット配送価格は2,334,300ウォン、表示定価2,989,000ウォンで21％引き。レビュー132件、設置日は11月26日から12月26日で選べます。
LG電子公式ストアの同じモデル（スタンド型）は定価2,989,000ウォンの9％引きで2,706,300ウォン。クーパンが372,000ウォン、13.7％安い。公式ストアの割引率（9％）の3倍以上が実際に付いています。これは「割引のふり」ではなく本当の値下げです。
ただし同じ検索画面に似た名前のモデルが混在します。55B6NNAが1,361,000ウォン、55B5NNAが1,332,390ウォン（29％引き）。C6はOLED evo（輝度ブースター搭載）、B6・B5は通常のOLEDです。100万ウォンの差の半分は世代とパネル等級の違いです。

2. 本当に下がった — ダイソン エアラップ i.d.
クーパンではセラミックピンク（161829-01）が699,000ウォンの29％引き495,200ウォン、バーガンディウッド（492321-01）が31％引き476,510ウォン。いずれもクーポン割引表示があり、レビュー2,297件、翌日到着です。
ダイソンコリア公式ストアは同じモデルを希望小売価格699,000ウォン、販売価格689,000ウォンで販売（評価4.6、2年保証）。クーポン価格476,510ウォンと比べると212,490ウォン、30.8％の差です。公式が689,000ウォンの商品がクーパンで47万ウォン台ということは、クーパン側に別枠のクーポン予算があるということで、クーポンが終わればこの価格は消えます。
注意すべきは型番です。エアラップ i.d.、新型のエアラップ2x、3ツール構成のエアラップ オリジンが一緒に出てきます。ツール数もモーター出力も違うので、価格だけ比べると最安の基本構成が得に見えます。

3. 割引に見えて2.4％ — ギャラクシーブック5 Pro 16
クーパンではギャラクシーブック5 Pro NT960XHA-K51A（Intel Ultra 5、16GB、512GB）が定価2,832,000ウォンの15％引き、2,398,000ウォンと表示されます。レビュー1,204件、43万4,000ウォンの節約に見えます。
しかしサムスン電子がこの構成（16型・16GB・512GB）を発売したときの価格は2,458,000ウォン（前作より13万2,000ウォン値下げ）です。2,398,000ウォンとの差は60,000ウォン、2.4％。つまり「15％引き」の大半は、定価を発売価格より37万4,000ウォン高く設定して作った数字です。
同じ検索にはProでないギャラクシーブック5（NT750XHW-A51A、15.6型・1TB）が2,199,000ウォンの9％引き、1,981,070ウォンでも出ています。

4. 名前は同じで価格が2倍の罠
55C6の検索結果には2,334,300ウォン（ロケット配送）のほかに1,675,000ウォンのスタンド型も並びます。型番表記は似ていますが販売者と構成が違います。設置方式と販売者保証を確認せず価格だけで選ぶと、設置費や保証で差額が戻ってきます。
クーパンは価格履歴を公開していません。ですから「直前値上げ」はクーパンの画面だけでは証明できません。メーカー公式ストアの価格と発売価格を突き合わせれば、割引率が本物か定価の水増しかが分かれます。今回の3点ではLGとダイソンが本物、ギャラクシーブックが水増し側でした。

支払い前の確認3点
第一に、定価がメーカーの発売価格と同じか。違えば割引率は広告の数字です。
第二に、クーポンの種類と終了時期。クーポン割引はクーポンが尽きれば消えます。カード割引や無金利分割が重なるかも決済画面で確認を。
第三に、設置日と返品条件。テレビとノートPCは設置日程が11月26日〜12月26日なので、年末前の設置が必要なら先に日付を押さえます。

まとめ
今回のクーパン家電セールで確実に安いのはLG OLED 55C6KNA（公式ストア比13.7％安）とダイソン エアラップ i.d.（30.8％安）で、ギャラクシーブック5 Proの「15％引き」は実際には2.4％（6万ウォン）でした。割引率ではなくメーカー公式価格と発売価格で比べることが、今週の家電買い物でお金を守る方法です。"""

ZH_DESC = """Coupang家电·数码黑色星期五从11月16日持续到29日。活动里最常见的「最高21%折扣」是按商品页面标注的定价计算的。定价怎么标，同一个售价就能变成30%折扣或2%折扣。因此本文不看折扣率，而是把厂商官方商城售价与上市价并排比较。Coupang不公开的「黑五前先涨价」也能通过这个方法间接看出来。
基准时间为11月25日上午11时50分至12时10分，确认了Coupang售价、定价、评论与可安装日期，比较对象为LG电子官方商城、戴森韩国官方商城和三星电子上市资料。

1. 真的降了 — LG OLED evo AI 55C6KNA
Coupang火箭配送价为2,334,300韩元，标价2,989,000韩元，折扣21%，评论132条，安装日期可在11月26日至12月26日之间选择。
LG电子官方商城的同款（底座型）为2,706,300韩元（定价2,989,000韩元的9%折扣）。Coupang便宜372,000韩元、13.7%，超过官方商城折扣率的三倍，属于真实降价。
不过同一搜索结果里混有相似型号：55B6NNA为1,361,000韩元、55B5NNA为1,332,390韩元（29%折扣）。C6是OLED evo（带亮度增强），B6·B5是普通OLED，100万韩元差价的一半来自世代与面板等级。

2. 真的降了 — 戴森 Airwrap i.d.
Coupang上陶瓷粉（161829-01）为495,200韩元（699,000韩元的29%折扣），酒红木（492321-01）为476,510韩元（31%折扣），均标注优惠券折扣，评论2,297条，次日到达。
戴森韩国官方商城同款建议零售价699,000韩元、售价689,000韩元，评分4.6、保修2年。与Coupang的476,510韩元相差212,490韩元、30.8%。官方卖689,000韩元的商品在Coupang卖到47万韩元区间，说明Coupang另有优惠券预算，券结束后价格就会消失。
注意型号：Airwrap i.d.、新型Airwrap 2x、3配件版Airwrap Origin会一起出现，配件数与电机输出不同，只看价格会让基础款显得最划算。

3. 看起来是折扣，其实只有2.4% — Galaxy Book5 Pro 16
Coupang标价2,832,000韩元、15%折扣后2,398,000韩元，评论1,204条，看起来省了434,000韩元。
但三星电子发布该配置（16英寸、16GB、512GB）时的价格为2,458,000韩元（比前作低132,000韩元）。与2,398,000韩元相比，实际差价仅60,000韩元、2.4%。也就是说「15%」的大部分来自把定价标得比上市价高374,000韩元。真正省下的只有6万韩元。
同一搜索中非Pro的Galaxy Book5（NT750XHW-A51A，15.6英寸·1TB）为1,981,070韩元（2,199,000韩元的9%折扣）。

4. 同名却贵一倍的陷阱
55C6搜索结果里除了2,334,300韩元（火箭配送）还有1,675,000韩元的底座型。型号写法相似，但卖家与配置不同。不看安装方式与卖家保修、只比价格，差额会以安装费或保修形式还回去。
Coupang不公开价格历史，所以「黑五前涨价」无法仅凭页面证明。与厂商官方商城价格和上市价对照，才能分辨真实折扣与虚高定价。本文三件中，LG与戴森属于真实降价，Galaxy Book属于虚高定价。

付款前的三项确认
第一，定价是否等于厂商上市价；不同则折扣率只是广告数字。
第二，优惠券种类与结束时间；券用尽后「券折扣」会消失，刷卡折扣与免息分期也要在结算页确认。
第三，安装日期与退货条件；电视与笔记本的安装日程为11月26日至12月26日，若需年前安装要先锁定日期。

一句话总结
本次Coupang家电活动中真正便宜的是LG OLED 55C6KNA（比官方商城低13.7%）和戴森Airwrap i.d.（低30.8%），Galaxy Book5 Pro的「15%折扣」实际只有2.4%（6万韩元）。与厂商官方价和上市价比，而不是看折扣标，才是本周买家电守住钱包的方法。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "store": "쿠팡",
    "priceKrw": 2334300,
    "releaseDate": "2026-11-25",
    "rating": 4.7,
    "imageUrl": C,
    "images": [G1, G2],
    "affiliateUrl": q("가전 블랙프라이데이"),
    "affiliatePlatform": "Coupang",
    "exampleItems": [
        {
            "name": "LG 올레드 evo AI TV OLED55C6KNA 스탠드형",
            "brand": "LG전자",
            "priceKrw": 2334300,
            "imageUrl": "/images/products/bf-appliance-lg-oled55c6.jpg",
            "url": q("LG 올레드 55C6KNA"),
            "category": "TV",
        },
        {
            "name": "다이슨 에어랩 i.d. 멀티 스타일러 앤 드라이어 161829-01",
            "brand": "다이슨",
            "priceKrw": 495200,
            "imageUrl": "/images/products/bf-appliance-dyson-airwrap-id.jpg",
            "url": q("다이슨 에어랩 i.d"),
            "category": "헤어스타일러",
        },
        {
            "name": "삼성 갤럭시북5 프로 NT960XHA-K51A 16GB 512GB",
            "brand": "삼성전자",
            "priceKrw": 2398000,
            "imageUrl": "/images/products/bf-appliance-galaxybook5-pro.jpg",
            "url": q("갤럭시북5 프로 NT960XHA"),
            "category": "노트북",
        },
    ],
    "i18n": {
        "ko": {
            "title": "쿠팡 가전 블프 '15% 할인'의 실체 — 공식몰 가격과 맞대조한 3종",
            "summary": "쿠팡 가전 블랙프라이데이는 11/16~29. 할인율 대신 제조사 공식몰 가격과 출시가를 기준으로 3종을 맞대조했습니다. LG 올레드 55C6KNA는 공식몰보다 13.7% 싸 진짜 인하, 다이슨 에어랩 i.d.는 30.8% 싸 진짜, 갤럭시북5 프로의 '15% 할인'은 실제로 2.4%(6만 원)였습니다.",
            "description": KO_DESC,
            "tasteReview": [
                "LG 올레드 55C6KNA: 쿠팡 2,334,300원 vs LG 공식몰 2,706,300원 → 13.7% 실제 인하(리뷰 132)",
                "다이슨 에어랩 i.d.: 쿠팡 476,510~495,200원(쿠폰) vs 공식몰 689,000원 → 최대 30.8% 실제 인하(리뷰 2,297)",
                "갤럭시북5 프로: 쿠팡 '15% 할인' 2,398,000원 vs 삼성 출시가 2,458,000원 → 실제 2.4%(6만 원)",
                "쿠팡은 가격 이력을 공개하지 않음 — 공식몰·출시가 대조가 '할인인 척'을 가려내는 방법",
                "같은 55C6 검색에 1,675,000원짜리 다른 셀러 상품 혼재, 설치일은 11/26~12/26",
            ],
            "tips": "가격은 2026-11-25 11:50~12:10 KST 확인값이며 쿠폰·카드할인에 따라 달라집니다. 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있습니다.",
        },
        "en": {
            "title": "What Coupang's '15% Off' Appliance Deal Really Is: 3 Items Checked Against Official Prices",
            "summary": "Coupang's appliance Black Friday runs November 16-29. Instead of the discount badge, three items were checked against the maker's official-store price and launch price: LG's OLED 55C6KNA is 13.7% below LG's store and real, Dyson's Airwrap i.d. is 30.8% below and real, and the Galaxy Book5 Pro's '15% off' is actually 2.4%, or 60,000 won.",
            "description": EN_DESC,
            "tasteReview": [
                "LG OLED 55C6KNA: Coupang 2,334,300 won vs LG store 2,706,300 won (13.7% real cut, 132 reviews)",
                "Dyson Airwrap i.d.: Coupang 476,510-495,200 won with coupon vs official 689,000 won (up to 30.8% real cut)",
                "Galaxy Book5 Pro: Coupang '15% off' 2,398,000 won vs Samsung launch price 2,458,000 won (really 2.4%)",
                "Coupang publishes no price history, so the official-store and launch price comparison is what separates a real cut from a raised list price",
                "The same 55C6 search mixes a 1,675,000-won listing from another seller; installation windows run Nov 26 to Dec 26",
            ],
            "tips": "Prices were checked at 11:50-12:10 KST on 25 November 2026 and move with coupons and card discounts. This post contains affiliate links and may earn a commission.",
        },
        "ja": {
            "title": "クーパン家電「15％オフ」の実体——公式価格と突き合わせた3点",
            "summary": "クーパン家電のブラックフライデーは11/16〜29。割引率ではなくメーカー公式ストア価格と発売価格で3点を比較しました。LG OLED 55C6KNAは公式比13.7％安で本当の値下げ、ダイソン エアラップ i.d.は30.8％安で本物、ギャラクシーブック5 Proの「15％引き」は実際2.4％（6万ウォン）でした。",
            "description": JA_DESC,
            "tasteReview": [
                "LG OLED 55C6KNA: クーパン2,334,300ウォン vs LG公式2,706,300ウォン→13.7％の実質値下げ（レビュー132件）",
                "ダイソン エアラップ i.d.: クーパン476,510〜495,200ウォン（クーポン）vs 公式689,000ウォン→最大30.8％",
                "ギャラクシーブック5 Pro: クーパン「15％引き」2,398,000ウォン vs 発売価格2,458,000ウォン→実際は2.4％（6万ウォン）",
                "クーパンは価格履歴を非公開——公式ストア・発売価格との対比が「割引のふり」を見分ける方法",
                "同じ55C6検索に167万5,000ウォンの別販売者商品が混在、設置日は11/26〜12/26",
            ],
            "tips": "価格は2026-11-25 11:50〜12:10 KSTの確認値で、クーポンやカード割引により変わります。本記事はアフィリエイトリンクを含み、手数料を受け取る場合があります。",
        },
        "zh": {
            "title": "Coupang家电「15%折扣」的真相——与官方价格对照的3件",
            "summary": "Coupang家电黑五为11/16~29。本文不看折扣率，而用厂商官方商城价与上市价对照三件：LG OLED 55C6KNA比官方低13.7%（真实降价）、戴森Airwrap i.d.低30.8%（真实）、Galaxy Book5 Pro的「15%折扣」实际只有2.4%（6万韩元）。",
            "description": ZH_DESC,
            "tasteReview": [
                "LG OLED 55C6KNA：Coupang 2,334,300韩元 vs LG官方2,706,300韩元→实际降13.7%（评论132条）",
                "戴森Airwrap i.d.：Coupang 476,510~495,200韩元（优惠券）vs 官方689,000韩元→最高降30.8%",
                "Galaxy Book5 Pro：Coupang「15%折扣」2,398,000韩元 vs 上市价2,458,000韩元→实际仅2.4%（6万韩元）",
                "Coupang不公开价格历史——对照官方商城价与上市价才能辨别「假折扣」",
                "同一55C6搜索结果混有1,675,000韩元的其他卖家商品，安装日期为11/26~12/26",
            ],
            "tips": "价格为2026-11-25 11:50~12:10 KST确认值，随优惠券与银行卡折扣变化。本文含联盟链接，可能获得佣金。",
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
