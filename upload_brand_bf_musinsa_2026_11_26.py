#!/usr/bin/env python3
"""5편 무신사 무진장 26 겨울 블랙프라이데이 (4개국어) → Supabase posts + ISR revalidate.

근거 (2026-11-26 13:40~14:00 KST musinsa.com/campaign/mujinjangsale 직접 확인)
 - 무진장 26 겨울 블랙프라이데이 11/22 19:00 ~ 12/2 24:00, 최대 80%
 - 4,781개 브랜드 / 798,610여 개 상품
 - 누적 판매 3,211,563개, 누적 판매 176,827,999,851원, 누적 할인 142,120,908,220원,
   1억 이상 브랜드 285개, 100개 이상 판매 상품 4,133개 (26일 13:46 화면)
 - 시그니처특가 판매순: 수아레 헨리넥 니트 59% 24,400원 24,609개 / 오프메이드 스웨트팬츠 65% 14,950원 24,607개
   / 트릴리온 크롭 긴팔티 54% 17,990원 16,785개 / 디미트리블랙 컴포트템프 패딩 48% 69,900원 12,503개
   / 수아레 시어쉘 패딩 61% 65,150원 9,541개
 - 20시·21시 선착순 특가 예고: 아디다스 슈퍼스타 360 2.0 부츠 5,990원(94%), 컨트리II·캠퍼스2·삼바LT 9,990원(93%)
 - 매일 10·11·20·21시 선착순 특가, 10·19시 오픈런 뽑기(최대 80% 쿠폰·최대 1만원 적립금), 11시 상품권 30%/15%
 - 결제 혜택: 카카오페이×페이머니 20만↑ 15,000원, 토스페이×삼성·롯데 12만↑ 10,000원 등
 - 제품 사진: 무신사 상품 이미지 5장 3:4(1200×1600) 정규화. AI 생성 0장.
"""
from brand_bf_common import publish, q

SLUG = "musinsa-mujinjang-winter-2026-deals"

G1 = "/images/products/bfb-musinsa-henley-knit.jpg"
G2 = "/images/products/bfb-musinsa-sweatpants.jpg"
G3 = "/images/products/bfb-musinsa-croptee.jpg"
G4 = "/images/products/bfb-musinsa-comfortemp.jpg"
G5 = "/images/products/bfb-musinsa-sheershell.jpg"

KO = """무신사의 '무진장 26 겨울 블랙프라이데이'가 11월 22일 오후 7시에 열려 12월 2일 자정에 끝난다. 4,781개 브랜드, 79만 8,610개 상품이 걸린 국내 최대 규모의 시즌 세일이다. 최대 할인율은 80%다.
11월 26일 오후 무진장 캠페인 화면에서 확인한 수치와 시간표를 정리했다. 무신사는 브랜드 공식몰과 달리 시간마다 특가가 바뀌고 쿠폰이 쏟아지는 구조라, 무엇을 언제 노려야 하는지가 실제 구매가를 좌우한다.

1. 지금까지 얼마나 팔렸나
오늘 오후 1시 46분 화면 기준 누적 판매 수량은 3,211,563개, 누적 판매 금액은 1,768억 원, 누적 할인 금액은 1,421억 원이다. 행사가 시작된 22일 저녁부터 계산하면 하루 평균 30억 원어치가 팔리고, 그중 24억 원가량이 할인으로 빠진 셈이다.
브랜드별로도 편차가 크다. 판매 금액 1억 원을 넘긴 브랜드가 285개, 100개 이상 팔린 상품이 4,133개다. 상위 상품에 판매가 몰리는 구조이므로, 인기 상품은 할인율이 높아도 사이즈가 빨리 빠진다.
행사 종료까지는 6일 남았다. 12월 2일 자정이 마지막이다.

2. 시그니처특가 — 실제로 가장 많이 팔린 순서
오늘 화면의 시그니처특가 판매 순위는 이렇다.
수아레 데일리 헨리넥 니트(5컬러) — 59% 할인 24,400원, 24,609개 판매
오프메이드 사이드핀턱 와이드 스웨트팬츠(기모 추가) — 65% 할인 14,950원, 24,607개 판매
트릴리온 에센셜 CP 이중지 크롭 긴팔티(7컬러) — 54% 할인 17,990원, 16,785개 판매
디미트리블랙 모두의 컴포트템프 미드웨이트 패딩 — 48% 할인 69,900원, 12,503개 판매
수아레 라이트 시어쉘 패딩 점퍼(6컬러) — 61% 할인 65,150원, 9,541개 판매
수아레 데일리 라운드 니트(12컬러) — 48% 할인 25,650원, 9,023개 판매
무신사 스탠다드 시티레저 메시 플리스 후디드 티셔츠 — 60% 할인 19,990원, 7,739개 판매
브렌슨 원턱 와이드 스웨트 팬츠 — 42% 할인 23,900원, 5,712개 판매
상위권은 대부분 2만 원 안팎의 니트·팬츠·티셔츠다. 겨울 아우터는 6만 원대(패딩 점퍼)와 7만 원대(미드웨이트 패딩)에 형성돼 있다. 2만 원대 니트와 7만 원대 패딩을 함께 사면 총액 9만 원대로 겨울 한 세트가 완성된다.

3. 오늘 밤 8시·9시, 5,990원짜리 운동화
무진장의 핵심은 매일 열리는 선착순 한정 수량 특가다. 오전 10시·11시, 오후 8시·9시에 열리고 수량이 정해져 있다. 오늘 밤 8시와 9시 회차에는 아디다스 슈퍼스타 360 2.0 부츠가 5,990원(94% 할인)으로 예고돼 있다.
같은 회차에 컨트리 II, 캠퍼스 2, 함부르크, 삼바 LT, 자바 로우가 모두 9,990원(92~93% 할인)이다. 반스 뉴스쿨 키즈와 푸마 FUTURE 8 플레이 TT는 5,990원(91~93%), 소렐 1964 PAC 나일론은 9,990원(94%), 스카르파 로브는 14,990원(94%)이다.
이 가격은 '특가 예정'으로, 회차가 열리는 시각에 맞춰 들어가야 산다. 오늘 저녁 8시에 알람을 맞춰두는 편이 좋다. 다만 사이즈별 수량이 적고, 결제 단계에서 품절이 뜨면 다른 상품으로 대체해야 한다.

4. 오전 10시와 오후 7시에는 뽑기가 열린다
무진장 오픈런 뽑기는 매일 오전 10시와 오후 7시에 열린다. 최대 80% 쿠폰, 최대 1만 원 무신사머니 포인트, 최대 1만 원 적립금이 나온다. 행사 기간 중 아이디당 21회까지 참여할 수 있고, 쿠폰은 발급일로부터 하루, 적립금은 7일간 쓸 수 있다.
오전 11시에는 무신사머니 상품권을 할인 판매한다. 5,000원권은 30%, 10,000원권은 15% 할인이다. 상품권으로 결제하면 쿠폰과 별개로 5~30%를 더 아끼는 효과가 난다. 선착순이라 11시 정각에 들어가야 한다.
그 밖에 매일 출석체크로 적립금 최대 5만 원(랜덤), 오픈런과 별도로 매일 10시·19시 특가 알림을 받아두면 놓치는 회차가 줄어든다.

5. 결제 혜택 — 카드 조합으로 만 원 더
무진장 기간에는 간편결제 조합 할인이 붙는다. 오늘 화면 기준으로 카카오페이와 페이머니로 20만 원 이상 결제하면 1만 5,000원, 토스페이와 삼성카드 또는 롯데카드로 12만 원 이상 결제하면 1만 원이 할인된다. 무신사페이와 무신사 삼성카드 조합은 15만 원 이상에 1만 원이다.
금액대별로 쪼개져 있으니, 결제 전에 장바구니 금액을 보고 가장 유리한 조합을 고르면 된다. 12만 원대라면 토스페이와 삼성카드 조합이, 20만 원대라면 카카오페이 페이머니 조합이 유리하다.
무신사머니 첫 결제 시 10% 추가 적립도 별도로 진행된다. 무신사머니를 새로 충전해 결제하면 적립이 붙지만, 충전 금액이 남으면 다음 쇼핑까지 묶인다는 점은 감안해야 한다.

6. 브랜드데이와 72시간 특가
시그니처 브랜드데이에는 무신사 스탠다드, 드로우핏, 트릴리온, 뉴발란스, 닥터마틴, 디스커버리 익스페디션, 마뗑킴, 락피쉬웨더웨어, 노스페이스, 살로몬, 디키즈 등이 참여한다. 브랜드별로 하루씩 혜택이 집중되는 구조라, 원하는 브랜드가 걸린 날을 확인하면 할인 폭이 커진다.
오늘 무신사 스탠다드 브랜드숍은 최대 57% 할인을 걸고 있다. 힛탠다드 타이즈 10,990원(31%), 헤비웨이트 속기모 세미 와이드 슬랙스 47,990원(20%), 램스킨 터치 글러브 44,890원(10%), 와이드 코듀로이 팬츠 31,990원(33%) 같은 가격이다.
72시간 특가는 이름 그대로 사흘만 열린다. 회차가 끝나면 사라지므로, 특가 탭을 매일 확인하는 편이 좋다.

7. 행사 마지막 주에 남는 것
무진장은 12월 2일 자정에 끝난다. 마지막 이틀인 12월 1~2일에는 '멤버스데이'가 열려 적립금을 최대 3만 원까지 지급하고, 무신사 삼성카드로 결제하면 1만 원 즉시 할인이 붙는다. 마지막에 몰아서 사려면 이 이틀을 노리는 방법도 있다.
다만 사이즈는 시간이 지날수록 줄어든다. 인기 상품은 마지막 주에 색상과 사이즈가 거의 남지 않는다. 첫 구매 목록에 있던 상품은 11월 안에 결제하는 편이 안전하다.

8. 사기 전에 확인할 것
무진장은 '최대 80%'가 붙지만, 실제로는 상품마다 할인율 차이가 크다. 오늘 판매 상위 상품도 42~65% 구간이다. 80%는 재고 정리 상품이나 뽑기 쿠폰이 붙는 경우에 나온다.
배송비도 계산에 넣어야 한다. 무신사는 브랜드별로 배송비를 받는 경우가 있어, 2만 원짜리 상품에 배송비 3,000원이 붙으면 실질 할인율이 줄어든다. '무배당발'(무료배송 당일발송) 표시가 붙은 상품을 고르면 이 문제를 피할 수 있다.
반품과 교환 조건도 브랜드마다 다르다. 특히 특가 상품은 단순 변심 반품이 제한되는 경우가 있으므로, 상품 상세의 교환·반품 안내를 먼저 확인해야 한다.

한 줄 정리
무신사 무진장 26 겨울은 12월 2일 자정까지다. 지금까지 3,211,563개·1,768억 원어치가 팔렸고, 시그니처특가는 수아레 헨리넥 니트 24,400원(59%), 오프메이드 스웨트팬츠 14,950원(65%), 디미트리블랙 패딩 69,900원(48%) 순으로 많이 나갔다. 오늘 밤 8시·9시에는 아디다스 슈퍼스타 5,990원 특가가 열리고, 10시와 19시 뽑기, 11시 상품권 할인까지 챙기면 체감가가 한 단계 더 내려간다."""

EN = """Musinsa's winter Mujinjang Black Friday opened at 19:00 on 22 November and closes at midnight on 2 December. It is the country's largest seasonal sale: 4,781 brands, 798,610 products, up to 80% off.
Below are the numbers and the timetable from the campaign page on the afternoon of 26 November. Unlike a single brand's store, Mujinjang changes its deals by the hour and hands out coupons continuously, so knowing what to target and when decides what you actually pay.

1. What has sold so far
At 13:46 today the running totals were 3,211,563 units, 176.8 billion won in sales and 142.1 billion won in discounts. Since the 22nd that is roughly 3 billion won a day, a quarter of it given away as discount.
Brands are uneven: 285 passed 100 million won in sales, and 4,133 products sold more than 100 units. Sales concentrate on the top items, which means popular products lose sizes quickly even at deep discounts.
Six days remain; midnight on 2 December is the end.

2. Signature deals — ranked by units actually sold
Today's signature-deal ranking:
Suare Daily Henley Knit (5 colours) — 59% off, 24,400 won, 24,609 sold
Offmade side-pintuck wide sweatpants (fleece-lined) — 65% off, 14,950 won, 24,607 sold
Trillion Essential CP cropped long-sleeve tee (7 colours) — 54% off, 17,990 won, 16,785 sold
Dimitri Black Comfortemp midweight padding — 48% off, 69,900 won, 12,503 sold
Suare Light Sheer Shell padded jumper (6 colours) — 61% off, 65,150 won, 9,541 sold
Suare Daily Round Knit (12 colours) — 48% off, 25,650 won, 9,023 sold
Musinsa Standard City Leisure mesh fleece hooded tee — 60% off, 19,990 won, 7,739 sold
Brenson one-tuck wide sweatpants — 42% off, 23,900 won, 5,712 sold
The top of the list is knitwear, pants and tees around 20,000 won; winter outerwear sits at 60,000-70,000 won. A 20,000-won knit plus a 70,000-won padded jacket builds a winter set for under 100,000 won.

3. 8pm and 9pm tonight — trainers at 5,990 won
The core of Mujinjang is the daily limited-quantity flash deal at 10:00, 11:00, 20:00 and 21:00. Tonight's 8pm and 9pm rounds tease adidas Superstar 360 2.0 boots at 5,990 won (94% off).
In the same rounds, Country II, Campus 2, Hamburg, Samba LT and Java Low are all 9,990 won (92-93% off). Vans New Skool Kids and PUMA Future 8 Play TT are 5,990 won (91-93%), Sorel 1964 PAC Nylon 9,990 won (94%) and Scarpa Robe 14,990 won (94%).
These are marked "deal upcoming" and require entering at the opening minute. Set an alarm for 8pm. Quantity per size is small, and if checkout shows a sellout, switch to another item.

4. Lotteries at 10:00 and 19:00
The open-run lottery opens daily at 10:00 and 19:00 with coupons up to 80%, up to 10,000 won in Musinsa Money points and up to 10,000 won in credit. Each account can enter 21 times across the event; coupons last a day and credit seven days.
At 11:00 Musinsa Money gift certificates sell at a discount: 30% off the 5,000-won certificate and 15% off the 10,000-won one. Paying with those adds 5-30% on top of coupons, but it is first-come, so enter at exactly 11:00.
Daily check-ins hand out up to 50,000 won in random credit, and turning on deal notifications at 10:00 and 19:00 reduces missed rounds.

5. Payment offers — another 10,000 won by card combination
Simple-payment combinations add discounts during the event. As shown today: Kakao Pay with Pay Money over 200,000 won takes 15,000 off; Toss Pay with a Samsung or Lotte card over 120,000 takes 10,000; Musinsa Pay with the Musinsa Samsung card over 150,000 takes 10,000.
Because the tiers differ, check the cart total and pick the best combination: around 120,000 won, Toss Pay plus Samsung; around 200,000, Kakao Pay Plus Money. A first Musinsa Money payment also earns 10% back, though money left over stays locked to the wallet.

6. Brand days and 72-hour deals
Signature brand days include Musinsa Standard, Drawfit, Trillion, New Balance, Dr. Martens, Discovery Expedition, Matin Kim, Rockfish Weatherwear, The North Face, Salomon and Dickies. Each brand gets a day, so checking when yours lands pays.
Musinsa Standard's brand shop today runs up to 57% off: Hit Standard tights 10,990 won (31% off), heavyweight fleece semi-wide slacks 47,990 won (20%), lambskin-touch gloves 44,890 won (10%), wide corduroy pants 31,990 won (33%).
72-hour deals last exactly three days and disappear, so open the deal tab daily.

7. The last days
Mujinjang ends at midnight on 2 December. On 1-2 December a Members Day pays up to 30,000 won in credit and takes 10,000 won off with the Musinsa Samsung card. If you plan to buy at the end, those two days are the ones to target.
Sizes shrink as the clock runs, though. Popular items have almost no colours or sizes left in the final week, so anything already on your list is safer bought during November.

8. Before you pay
"Up to 80%" hides a wide spread: today's top sellers ran 42-65%. The 80% appears on clearance stock or through lottery coupons. Delivery fees matter too — some brands charge shipping, and 3,000 won on a 20,000-won item cuts the real discount. Look for the "free shipping, same-day" badge. Return and exchange terms also vary by brand, and some deal items restrict change-of-mind returns, so read the product notice first.

In one line
Musinsa's winter Mujinjang runs to midnight on 2 December. So far 3,211,563 units and 176.8 billion won have moved, led by the Suare Henley Knit at 24,400 won (59% off), Offmade sweatpants at 14,950 (65%) and Dimitri Black padding at 69,900 (48%). Tonight at 8pm and 9pm adidas Superstar drops to 5,990 won, and stacking the 10:00 and 19:00 lotteries and the 11:00 gift-certificate sale takes the effective price lower still."""

JA = """ムシンサの「ムジンジャン26 冬 ブラックフライデー」が11月22日午後7時に開き、12月2日24時に終わる。4,781ブランド、798,610商品が並ぶ国内最大規模のシーズンセールで、最大80%割引だ。
11月26日午後にキャンペーン画面で確認した数値とタイムテーブルをまとめた。ブランド公式ストアと違い、時間ごとに特価が変わりクーポンが配られる構造なので、何をいつ狙うかが実際の支払額を左右する。

1. これまでにどれだけ売れたか
今日午後1時46分の画面で累計販売数は3,211,563個、累計販売額は1,768億ウォン、累計割引額は1,421億ウォン。22日の夜から数えると1日平均30億ウォンが売れ、そのうち24億ウォン前後が割引で消えている計算だ。
ブランド別の偏りも大きい。販売額1億ウォンを超えたブランドが285、100個以上売れた商品が4,133。上位商品に販売が集中するので、人気商品は割引率が高くてもサイズが早く消える。
終了までは6日。12月2日24時が最後だ。

2. シグネチャー特価 — 実際に最も売れた順
今日の画面の販売順位はこうだ。
スアレ デイリー ヘンリーネックニット（5色）— 59%引き24,400ウォン、24,609個
オフメイド サイドピンタック ワイド スウェットパンツ（起毛追加）— 65%引き14,950ウォン、24,607個
トリリオン エッセンシャルCP 二重織クロップ長袖T（7色）— 54%引き17,990ウォン、16,785個
ディミトリブラック コンフォートテンプ ミッドウェイト パディング — 48%引き69,900ウォン、12,503個
スアレ ライト シアーシェル パデッドジャンパー（6色）— 61%引き65,150ウォン、9,541個
スアレ デイリー ラウンドニット（12色）— 48%引き25,650ウォン、9,023個
ムシンサ スタンダード シティレジャー メッシュフリース フーデッドT — 60%引き19,990ウォン、7,739個
ブレンソン ワンタック ワイド スウェットパンツ — 42%引き23,900ウォン、5,712個
上位は2万ウォン前後のニット・パンツ・Tシャツだ。冬アウターは6万ウォン台（パデッドジャンパー）と7万ウォン台（ミッドウェイトパディング）に形成されている。2万ウォン台のニットと7万ウォン台のパディングで10万ウォン以下の冬セットが完成する。

3. 今夜8時・9時、5,990ウォンのスニーカー
ムジンジャンの核は毎日開かれる先着数量限定の特価だ。午前10時・11時、午後8時・9時に開かれ、数量が決まっている。今夜8時と9時の回にはアディダス スーパースター360 2.0ブーツが5,990ウォン（94%引き）と予告されている。
同じ回にカントリーII、キャンパス2、ハンブルク、サンバLT、ジャバローがすべて9,990ウォン（92〜93%引き）。バンズ ニュースクール キッズとプーマ FUTURE 8 プレイTTは5,990ウォン（91〜93%）、ソレル 1964 PAC ナイロンは9,990ウォン（94%）、スカルパ ローブは14,990ウォン（94%）だ。
これらは「特価予定」で、回が開く時刻に入る必要がある。今夜8時にアラームを合わせておきたい。サイズ別の数量は少なく、決済で品切れが出たら別商品に切り替えることになる。

4. 午前10時と午後7時は抽選
ムジンジャンのオープンラン抽選は毎日午前10時と午後7時に開かれる。最大80%クーポン、最大1万ウォンのムシンサマネーポイント、最大1万ウォンの積立金が出る。期間中IDあたり21回まで参加でき、クーポンは発行日から1日、積立金は7日間使える。
午前11時にはムシンサマネー商品券を割引販売する。5,000ウォン券は30%、10,000ウォン券は15%引き。商品券で決済するとクーポンとは別に5〜30%得する。先着なので11時ちょうどに入りたい。
ほかに毎日の出席チェックで積立金最大5万ウォン（ランダム）、10時・19時の特価通知をオンにしておくと取りこぼしが減る。

5. 決済特典 — カードの組み合わせで1万ウォン追加
期間中は簡易決済の組み合わせ割引が付く。今日の画面ではカカオペイ×ペイマネーで20万ウォン以上1万5,000ウォン、トスペイ×サムスンカードまたはロッテカードで12万ウォン以上1万ウォン、ムシンサペイ×ムシンサ サムスンカードで15万ウォン以上1万ウォンだ。
金額帯が分かれているので、カートの金額を見て最も有利な組み合わせを選べばいい。12万ウォン台ならトスペイ×サムスン、20万ウォン台ならカカオペイ×ペイマネーが有利だ。
ムシンサマネー初回決済の10%追加積立も別にある。新規チャージで積立が付くが、残高は次の買い物まで拘束される点は考慮したい。

6. ブランドデーと72時間特価
シグネチャー ブランドデーにはムシンサ スタンダード、ドローフィット、トリリオン、ニューバランス、ドクターマーチン、ディスカバリー エクスペディション、マッチンキム、ロックフィッシュ ウェザーウェア、ノースフェイス、サロモン、ディッキーズなどが参加する。ブランドごとに1日ずつ特典が集中するので、欲しいブランドの日を確認すると下げ幅が大きい。
今日のムシンサ スタンダード ブランドショップは最大57%引きだ。ヒットタンダード タイズ10,990ウォン（31%）、ヘビーウェイト起毛セミワイドスラックス47,990ウォン（20%）、ラムスキンタッチグローブ44,890ウォン（10%）、ワイドコーデュロイパンツ31,990ウォン（33%）。
72時間特価は名前のとおり3日だけ。回が終われば消えるので、特価タブを毎日見るほうがいい。

7. 最後の週に残るもの
ムジンジャンは12月2日24時に終わる。最後の2日、12月1〜2日には「メンバースデー」が開かれ、積立金を最大3万ウォン支給し、ムシンサ サムスンカード決済で1万ウォン即時割引が付く。最後にまとめ買いするならこの2日を狙う方法もある。
ただしサイズは時間とともに減る。人気商品は最後の週に色とサイズがほとんど残らない。最初のリストに入れた商品は11月中に決済したほうが安全だ。

8. 買う前に確認すること
「最大80%」とあっても商品ごとの差は大きい。今日の販売上位も42〜65%台だ。80%は在庫整理商品や抽選クーポンが付く場合に出る。
送料も計算に入れる。ムシンサはブランドごとに送料を取る場合があり、2万ウォンの商品に3,000ウォンが付くと実質割引率が下がる。「無配当発」（送料無料・当日発送）表示の商品を選べばこの問題を避けられる。
返品・交換の条件もブランドごとに違う。とくに特価商品は単純な気変わり返品が制限されることがあるので、商品詳細の案内を先に確認したい。

ひとことで
ムシンサ ムジンジャン26 冬は12月2日24時まで。これまで3,211,563個・1,768億ウォンが売れ、シグネチャー特価はスアレ ヘンリーネックニット24,400ウォン（59%）、オフメイド スウェットパンツ14,950ウォン（65%）、ディミトリブラック パディング69,900ウォン（48%）の順に出ている。今夜8時・9時にはアディダス スーパースター5,990ウォンの特価が開き、10時と19時の抽選、11時の商品券割引まで押さえれば体感価格はもう一段下がる。"""

ZH = """MUSINSA 的「无尽情26冬季黑色星期五」于11月22日晚7点开启，12月2日24点结束。4,781个品牌、798,610件商品，最高80%折扣，是国内规模最大的季节促销。
以下是11月26日下午在活动页面确认的数据与时间表。与单一品牌商城不同，无尽情按小时更换特价并持续发券，因此「盯什么、什么时候盯」直接决定实付价格。

1. 目前卖了多少
今天下午1点46分的画面显示：累计销量3,211,563件，累计销售额1,768亿韩元，累计折扣额1,421亿韩元。从22日晚算起，日均卖出约30亿韩元，其中约24亿以折扣让出。
品牌之间差距很大：销售额破1亿韩元的品牌285个，售出100件以上的商品4,133个。销量集中在头部商品，所以热门款即使折扣深，尺码也很快消失。
距离结束还有6天，12月2日24点是最后期限。

2. 招牌特价——按实际销量排序
今天的招牌特价销量顺序为：
Suare 日常亨利领针织衫（5色）59%折扣 24,400韩元，24,609件
Offmade 侧褶宽松卫裤（加绒）65%折扣 14,950韩元，24,607件
Trillion Essential CP 双层短款长袖T（7色）54%折扣 17,990韩元，16,785件
Dimitri Black Comfortemp 中厚羽绒 48%折扣 69,900韩元，12,503件
Suare 轻量纱壳羽绒夹克（6色）61%折扣 65,150韩元，9,541件
Suare 日常圆领针织衫（12色）48%折扣 25,650韩元，9,023件
MUSINSA Standard 城市休闲网眼抓绒连帽T 60%折扣 19,990韩元，7,739件
Brenson 单褶宽松卫裤 42%折扣 23,900韩元，5,712件
榜单前列基本是2万韩元左右的针织、裤子与T恤；冬季外套在6万（羽绒夹克）与7万韩元（中厚羽绒）区间。2万韩元的针织加7万韩元的羽绒，不到10万韩元就能凑齐一套冬装。

3. 今晚8点、9点——5,990韩元的球鞋
无尽情的核心是每天限量先到先得的特价，时段为上午10点、11点与晚8点、9点。今晚8点与9点预告阿迪达斯 Superstar 360 2.0 靴子5,990韩元（94%折扣）。
同一场次里 Country II、Campus 2、Hamburg、Samba LT、Java Low 均为9,990韩元（92%～93%）。Vans New Skool 童鞋与彪马 Future 8 Play TT 5,990韩元（91%～93%），Sorel 1964 PAC 尼龙9,990韩元（94%），Scarpa Robe 14,990韩元（94%）。
这些标注为「特价预告」，需在开场那一刻进入。今晚8点设好闹钟比较稳妥；每码数量很少，结算显示售罄就要换其他商品。

4. 上午10点与晚7点的抽奖
开门抽奖每天上午10点与晚7点开启，奖品有最高80%优惠券、最高1万韩元MUSINSA Money积分与最高1万韩元返利。活动期内每个账号可参与21次；券当日有效，返利7天有效。
上午11点还有MUSINSA Money 礼品券折扣销售：5,000韩元券减30%、10,000韩元券减15%。用礼品券支付相当于在优惠券之外再省5%～30%，但为先到先得，11点整进场。
此外每日签到可随机获得最高5万韩元返利；打开10点与19点的特价通知能减少漏场。

5. 支付优惠——用卡组合再省1万
活动期间有快捷支付组合优惠。今天页面显示：Kakao Pay×Pay Money满20万韩元减15,000；Toss Pay×三星或乐天卡满12万韩元减10,000；MUSINSA Pay×MUSINSA三星卡满15万减10,000。
档位不同，先看购物车金额再选最优组合：12万韩元级选Toss Pay×三星，20万韩元级选Kakao Pay×Pay Money。MUSINSA Money 首次支付另有10%返积分，但充值余额会锁在钱包里，需要权衡。

6. 品牌日与72小时特价
招牌品牌日包括 MUSINSA Standard、Drawfit、Trillion、新百伦、Dr. Martens、Discovery Expedition、Matin Kim、Rockfish Weatherwear、北面、Salomon、Dickies 等。每个品牌集中一天，查清自己想要的品牌落在哪天更划算。
今天 MUSINSA Standard 品牌馆最高57%折扣：Hit Standard 紧身裤10,990韩元（31%）、重磅加绒半宽西裤47,990韩元（20%）、羊皮触感手套44,890韩元（10%）、宽松灯芯绒裤31,990韩元（33%）。
72小时特价顾名思义只开三天，过期即消失，建议每天看一次特价页。

7. 最后一周还剩什么
无尽情在12月2日24点结束。最后两天（12月1日至2日）有「会员日」，最高发3万韩元返利，用MUSINSA三星卡支付再立减1万。想最后集中采购，可以盯这两天。
但尺码会随时间减少。热门款在最后一周几乎没有颜色和尺码；已列入清单的商品在11月内付款更安全。

8. 购买前确认
「最高80%」背后差距很大：今天销量前列也在42%～65%。80%出现在清库存商品或抽奖券上。运费也要算：部分品牌收运费，2万韩元的商品加3,000韩元运费，实际折扣就缩水，选择标有「包邮当日发」的商品可避开。
退换条件也按品牌不同，部分特价商品限制无理由退货，先读商品详情里的退换说明。

一句话总结
MUSINSA 无尽情26冬季到12月2日24点。目前已卖出3,211,563件、1,768亿韩元；招牌特价以Suare 亨利领针织24,400韩元（59%）、Offmade 卫裤14,950韩元（65%）、Dimitri Black 羽绒69,900韩元（48%）领先。今晚8点、9点有阿迪达斯 Superstar 5,990韩元特价，再叠加10点与19点抽奖、11点礼品券折扣，实际到手价还能再低一档。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "k-fashion",
    "store": "무신사",
    "priceKrw": 24400,
    "releaseDate": "2026-11-26",
    "rating": 4.6,
    "imageUrl": G1,
    "images": [G1, G2, G3, G4, G5],
    "affiliateUrl": q("남자 헨리넥 니트"),
    "affiliatePlatform": "Coupang",
    "exampleItems": [
        {"name": "수아레 데일리 헨리넥 니트 (5컬러)", "brand": "Suare", "priceKrw": 24400, "imageUrl": G1,
         "url": q("남자 헨리넥 니트"), "category": "무진장 59% · 24,609개 판매"},
        {"name": "오프메이드 사이드핀턱 와이드 스웨트팬츠 (기모)", "brand": "Offmade", "priceKrw": 14950, "imageUrl": G2,
         "url": q("기모 와이드 스웨트팬츠"), "category": "무진장 65% · 24,607개 판매"},
        {"name": "트릴리온 에센셜 CP 이중지 크롭 긴팔티", "brand": "Trillion", "priceKrw": 17990, "imageUrl": G3,
         "url": q("크롭 긴팔티"), "category": "무진장 54% · 16,785개 판매"},
        {"name": "디미트리블랙 모두의 컴포트템프 미드웨이트 패딩", "brand": "Dimitri Black", "priceKrw": 69900, "imageUrl": G4,
         "url": q("남자 숏패딩"), "category": "무진장 48% · 12,503개 판매"},
        {"name": "수아레 라이트 시어쉘 패딩 점퍼 (6컬러)", "brand": "Suare", "priceKrw": 65150, "imageUrl": G5,
         "url": q("남자 패딩 점퍼"), "category": "무진장 61% · 9,541개 판매"},
    ],
    "i18n": {
        "ko": {
            "title": "무신사 무진장 26 겨울, 12월 2일까지 — 3,211,563개 팔린 특가 순위와 오늘 8시 5,990원 운동화",
            "summary": "11월 22일~12월 2일, 최대 80%·4,781 브랜드·798,610 상품. 누적 판매 3,211,563개·1,768억 원. 수아레 헨리넥 니트 24,400원(59%), 오프메이드 스웨트팬츠 14,950원(65%), 디미트리블랙 패딩 69,900원(48%) — 실제 판매 순위와 시간대별 특가표를 정리했습니다.",
            "description": KO,
            "tasteReview": [
                "기간: 11/22 19:00 ~ 12/2 24:00, 최대 80%, 4,781 브랜드·798,610 상품",
                "누적 판매 3,211,563개·1,768억 원·할인 1,421억 원(26일 13:46), 1억 이상 브랜드 285개",
                "시그니처특가 판매순: 수아레 헨리넥 니트 24,400원(59%) · 오프메이드 스웨트팬츠 14,950원(65%) · 트릴리온 크롭티 17,990원(54%) · 디미트리블랙 패딩 69,900원(48%)",
                "오늘 20·21시 아디다스 슈퍼스타 360 2.0 5,990원(94%) 예고, 10·19시 오픈런 뽑기, 11시 상품권 30% 할인",
            ],
            "tips": "가격과 판매 수치는 2026년 11월 26일 오후 무신사 무진장 캠페인 화면에서 확인한 값이며 실시간으로 변동됩니다. 특가는 수량이 정해져 있고 브랜드별 배송비·반품 조건이 다르니 결제 전 상품 상세를 확인하세요. 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있으며, 비교 링크는 쿠팡 검색 결과로 연결됩니다.",
        },
        "en": {
            "title": "Musinsa Mujinjang Winter Runs to 2 December — 3,211,563 Units Sold, and 5,990-Won Trainers at 8pm Tonight",
            "summary": "22 November to 2 December, up to 80%, 4,781 brands and 798,610 products, 3,211,563 units and 176.8 billion won sold. Suare Henley Knit 24,400 won (59%), Offmade sweatpants 14,950 (65%), Dimitri Black padding 69,900 (48%) — the real sales ranking and hourly deal table.",
            "description": EN,
            "tasteReview": [
                "Period: 22 Nov 19:00 to 2 Dec 24:00, up to 80%, 4,781 brands and 798,610 products",
                "Running totals 3,211,563 units, 176.8 billion won, 142.1 billion won discounted (13:46 on the 26th); 285 brands over 100 million won",
                "Signature deals by units: Suare Henley Knit 24,400 (59%), Offmade sweatpants 14,950 (65%), Trillion cropped tee 17,990 (54%), Dimitri Black padding 69,900 (48%)",
                "Tonight 20:00 and 21:00: adidas Superstar 360 2.0 at 5,990 won (94%); lotteries 10:00 and 19:00; gift certificates 30% off at 11:00",
            ],
            "tips": "Prices and sales figures were read on Musinsa's Mujinjang campaign page on the afternoon of 26 November 2026 and change in real time. Deal quantities are limited and shipping and return terms vary by brand; check the product page before paying. This post contains affiliate links and may earn a commission; comparison links open Coupang search results.",
        },
        "ja": {
            "title": "ムシンサ ムジンジャン26 冬は12月2日まで — 3,211,563個売れた特価順位と今夜8時5,990ウォンのスニーカー",
            "summary": "11月22日〜12月2日、最大80%・4,781ブランド・798,610商品。累計3,211,563個・1,768億ウォン。スアレ ヘンリーネックニット24,400ウォン（59%）、オフメイド スウェットパンツ14,950ウォン（65%）、ディミトリブラック パディング69,900ウォン（48%）— 実際の販売順位と時間帯別特価表を整理しました。",
            "description": JA,
            "tasteReview": [
                "期間：11/22 19:00〜12/2 24:00、最大80%、4,781ブランド・798,610商品",
                "累計3,211,563個・1,768億ウォン・割引1,421億ウォン（26日13:46）、1億超ブランド285社",
                "シグネチャー特価の販売順：スアレ ヘンリー24,400ウォン（59%）・オフメイド14,950ウォン（65%）・トリリオン クロップT 17,990ウォン（54%）・ディミトリブラック パディング69,900ウォン（48%）",
                "今夜20・21時にアディダス スーパースター360 2.0 5,990ウォン（94%）予告、10・19時抽選、11時商品券30%引き",
            ],
            "tips": "価格と販売数は2026年11月26日午後にムシンサ ムジンジャン キャンペーン画面で確認した値で、リアルタイムに変動します。特価は数量限定でブランドごとに送料・返品条件が異なるため、決済前に商品詳細を確認してください。本記事はアフィリエイトリンクを含み手数料を受け取る場合があります。比較リンクはCoupang検索結果に移動します。",
        },
        "zh": {
            "title": "MUSINSA 无尽情26冬季到12月2日——卖出3,211,563件的特价榜与今晚8点5,990韩元球鞋",
            "summary": "11月22日～12月2日，最高80%，4,781品牌、798,610商品。累计3,211,563件、1,768亿韩元。Suare亨利领针织24,400韩元（59%）、Offmade卫裤14,950韩元（65%）、Dimitri Black羽绒69,900韩元（48%）——真实销量榜与分时特价表。",
            "description": ZH,
            "tasteReview": [
                "期间：11/22 19:00～12/2 24:00，最高80%，4,781品牌・798,610商品",
                "累计3,211,563件・1,768亿韩元・折扣1,421亿韩元（26日13:46），销售额破亿品牌285个",
                "招牌特价销量顺序：Suare亨利领24,400韩元（59%）、Offmade卫裤14,950韩元（65%）、Trillion短款T 17,990韩元（54%）、Dimitri Black羽绒69,900韩元（48%）",
                "今晚20、21点阿迪达斯Superstar 360 2.0 5,990韩元（94%）预告，10点・19点抽奖，11点礼品券30%折扣",
            ],
            "tips": "价格与销量为2026年11月26日下午在MUSINSA无尽情活动页面确认的数值，会实时变动。特价数量有限，且各品牌运费与退换条件不同，付款前请查看商品详情。本文含联盟链接，可能获得佣金；比价链接跳转至Coupang搜索结果。",
        },
    },
}

if __name__ == "__main__":
    publish(POST)
