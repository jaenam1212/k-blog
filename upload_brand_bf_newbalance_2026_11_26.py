#!/usr/bin/env python3
"""2편 뉴발란스 2026 BLACK FRIDAY (4개국어) → Supabase posts + ISR revalidate.

근거 (2026-11-26 13:05~13:20 KST nbkorea.com 직접 확인)
 - 기간: 쿠폰 사용 11/23 10:00 ~ 11/28 09:59, 첫 배너 UP TO 80%
 - 등급쿠폰 3매 자동발급 VIP 20% / MANIA 15% / FAMILY 10%
 - 프로모션 코드 10만↑10%, 20만↑20% (세일 상품 추가 할인)
 - 네이버페이 20만↑ 5,000원 즉시할인 (11/21 10:00~11/28 09:59)
 - 첫구매 15%, 웰컴백 15%(최근 1년 구매 이력 없음), 개인정보 동의 이벤트 10% (11/19 10:00~11/28 09:59)
 - 원데이 특가 매일 10시 24시간(11/26 471 라인 139,000→55,000), 타임어택 17~19시·22~24시
 - 실측: 1080 V15 209,000→159,000(24%), 레벨V5 남성2E 219,000→149,000(32%),
   SC Trainer V3 249,000→169,000(32%), 880 V15 189,000→129,000(32%),
   RC HEAT 패딩점퍼 299,000→179,000(40%), 플라잉77 경량패딩 259,000→199,000(23%),
   U204L3K9 159,000→99,000(38%), U1906409 189,000→159,000(16%)
 - 제품 사진: 공식몰 제품컷 5장 3:4(1200×1600) 정규화. AI 생성 0장.
"""
from brand_bf_common import publish, q

SLUG = "new-balance-blackfriday-2026-official-store"

G1 = "/images/products/bfb-nb-1080v15.jpg"
G2 = "/images/products/bfb-nb-levelv5.jpg"
G3 = "/images/products/bfb-nb-rcheat.jpg"
G4 = "/images/products/bfb-nb-u471.jpg"
G5 = "/images/products/bfb-nb-flying77.jpg"

KO = """뉴발란스가 11월 23일부터 두 번째 블랙프라이데이를 열었다. 지난 11월 2일부터 9일까지 '블랙위크'로 한 차례 세일을 했고, 3주 만에 다시 문을 연 것이다. 이번 행사는 11월 28일 오전 9시 59분에 끝난다. 블랙프라이데이 당일인 27일보다 하루 먼저 닫히므로, 주말에 몰아서 사려던 계획이라면 일정을 앞당겨야 한다.
11월 26일 오후 공식 온라인스토어에서 확인한 가격과 혜택을 정리했다.

1. 언제까지, 얼마나
행사 첫 화면에는 '2026 BLACK FRIDAY, 세일 가격에 추가 프로모션까지, UP TO 80%'가 걸려 있다. 쿠폰 사용 기간은 11월 23일 오전 10시부터 11월 28일 오전 9시 59분까지다. 최대 80%는 일부 재고 정리 상품에 붙는 수치이고, 대표 모델은 20~40% 구간에 몰려 있다. 오늘 확인한 상품별 할인율도 16%에서 60%까지 고르게 퍼져 있다.

2. 쿠폰이 세 겹이다
첫째, 회원 등급별 쿠폰 3매가 자동 발급된다. VIP 20%, MANIA 15%, FAMILY 10%다. 등급이 낮아도 10%는 받는다는 뜻이라, 회원가입만 해두면 기본 할인은 확보된다.
둘째, 세일 상품에는 프로모션 코드가 붙는다. 10만 원 이상 구매하면 10%, 20만 원 이상이면 20%다. 코드는 금액 구간으로 나뉘므로 두 개를 함께 쓸 수는 없다.
셋째, 네이버페이로 20만 원 이상 결제하면 5,000원이 즉시 할인된다. 기간은 11월 21일 오전 10시부터 28일 오전 9시 59분까지로, 쿠폰 기간과 같다.
여기에 첫 구매 고객 15% 쿠폰과 최근 1년 구매 이력이 없는 회원에게 자동 발급되는 웰컴백 15% 쿠폰이 별도로 있다. 신규 사이트 오픈 관련 개인정보 제3자 제공에 동의하면 10% 쿠폰도 준다(11월 19일~28일 9시 59분). 이 쿠폰들은 중복 조건이 서로 다르므로, 결제 화면에서 실제로 붙는 조합을 확인해야 한다.

3. 오늘 실제로 얼마인가 — 신발
가장 먼저 볼 모델은 1080 V15다. 여성 D, 남성 2E, 남성 4E 세 가지 폭 모두 209,000원에서 24% 내린 159,000원이다. 폭만 다르고 가격은 같다. 공식몰 베스트 랭킹 1위부터 6위까지를 이 모델이 차지하고 있을 정도로 판매가 집중돼 있다.
러닝화 라인은 더 깊게 빠진다. 레벨 V5 남성 2E는 219,000원에서 32% 내린 149,000원, SC Trainer V3는 249,000원에서 32% 내린 169,000원, 880 V15 남성 2E는 189,000원에서 32% 내린 129,000원이다. 860 V15 여성 D는 189,000원에서 21% 내린 149,000원, SC Elite V5 여성은 329,000원에서 36% 내린 209,000원이다.
오늘의 원데이 특가는 471 라인이다. 정가 139,000원짜리 U471AM과 U4717K6, U4713G5 등이 60% 내린 55,000원에 올라와 있다. 원데이 특가는 매일 오전 10시에 새 상품으로 바뀌고 24시간만 유지된다. 다른 204L 라인은 159,000원에서 38% 내린 99,000원이다.

4. 오늘 실제로 얼마인가 — 의류와 용품
겨울 아우터는 할인 폭이 가장 크다. UNI RC HEAT 패딩점퍼는 299,000원에서 40% 내린 179,000원, UNI 플라잉77 슈퍼라이트 스텐드넥 경량 패딩 자켓은 259,000원에서 23% 내린 199,000원이다. UNI 액티브 라이트 다운 자켓은 159,000원에서 31% 내린 109,000원, UNI 에센셜 스탠넥 우븐자켓은 129,000원에서 40% 내린 77,900원이다.
기타 품목도 같이 내려간다. 3PACK 러닝삭스는 39,900원에서 30% 내린 27,900원, RE-ON 백팩은 99,900원에서 40% 내린 59,900원, 글로시 미니 숄더백은 49,900원에서 20% 내린 39,900원이다. 운동복을 한 번에 맞추려면 양말과 가방까지 같이 담는 편이 배송비 측면에서 낫다.

5. 조합하면 얼마가 되나
패딩점퍼(179,000원)와 1080 V15(159,000원)를 함께 담으면 338,000원이다. 20만 원을 넘으므로 20% 프로모션 코드 대상이고, 적용되면 270,400원이 된다. 여기에 네이버페이 20만 원 이상 결제 5,000원 즉시할인이 붙으면 265,400원이다. 처음 가격의 78.5% 수준이다.
여성용으로 레벨 V5(149,000원)와 RC HEAT(179,000원)를 담아도 총액은 328,000원으로 같게 20% 구간에 들어간다. 반대로 10만 원대 한 품목만 사면 코드는 10%로 내려간다. 20만 원을 조금 넘기는 구성이라면 양말이나 가방을 더해 구간을 맞추는 계산이 실제로 이득이 되는 경우가 많다.
단, 코드와 네이버페이 할인이 동시에 적용되는지, 쿠폰 대상에서 빠지는 인기 모델이 있는지는 상품마다 다르다. 위 계산은 각 할인이 모두 적용된다는 가정이며, 최종 금액은 장바구니에서 확인해야 한다.

6. 시간대별로 노릴 것
행사 기간 내내 세일가는 유지되지만, 추가 인하가 붙는 시간대가 따로 있다. 매일 오전 10시에 원데이 특가가 바뀌고 24시간 유지된다. 하루 두 번, 오후 5시부터 7시와 오후 10시부터 자정까지는 '타임 어택' 특가가 열린다. 오늘 오후 5시 회차는 아직 열리지 않은 상태로 '프로모션 오픈 전' 표시가 붙어 있었다.
인기 사이즈는 이 시간대에 가장 먼저 빠진다. 260~280 구간은 원데이 특가가 시작되는 오전 10시 직후에 재고가 줄어드는 패턴이 반복된다. 원하는 모델과 사이즈가 정해져 있다면 알림을 걸어두고 오전 10시에 바로 들어가는 편이 안전하다.

7. 28일 오전 9시 59분, 이 시간을 놓치면 끝이다
이번 행사의 실질 마감은 11월 28일 오전 9시 59분이다. 27일이 블랙프라이데이 당일이지만, 뉴발란스 기준으로는 27일 밤이 아니라 28일 아침에 쿠폰이 끊긴다. 토요일 아침에 천천히 둘러보겠다는 계획은 위험하다. 목록에 담아둔 상품은 27일 안에 결제를 끝내는 편이 낫다.
세일 종료 후에도 상품이 남아 있으면 정가로 돌아간다. 세일가와 정가 차이가 큰 모델(471 라인 60%, RC HEAT 40%)일수록 행사 이후 가격 회복 폭도 크다.

8. 사기 전에 확인할 것
최대 80%는 전체 상품 할인율이 아니다. 오늘 확인한 대표 모델 기준으로는 16~40%가 일반적이고, 60%는 원데이 특가로 나온 471 라인처럼 한정된 회차에만 나온다. 상품 목록의 할인율보다 장바구니 최종 금액을 봐야 하는 이유다.
폭(width)과 사이즈를 먼저 정해야 한다. 1080 V15는 2E·4E·D 세 가지 폭으로 나오고 가격은 같다. 러닝화는 폭이 맞지 않으면 발이 아프므로, 매장에서 신어본 폭을 기준으로 고르는 편이 좋다. 사이즈 교환은 무료로 되지만 행사 기간에는 물량이 몰린다.
등급쿠폰은 자동 발급이지만 사용 기간이 정해져 있다. 쿠폰함에서 '등급쿠폰' 이름으로 확인하고, 만료일을 결제 전에 한 번 더 보는 것이 안전하다.

한 줄 정리
뉴발란스 2026 블랙프라이데이는 11월 28일 오전 9시 59분에 끝난다. 1080 V15는 209,000원에서 159,000원, 레벨 V5는 219,000원에서 149,000원, RC HEAT 패딩점퍼는 299,000원에서 179,000원이다. 등급쿠폰 10~20%에 20만 원 이상 결제 시 20% 코드, 네이버페이 5,000원까지 겹칠 수 있으므로, 20만 원을 넘기는 구성으로 담는 것이 유리하다."""

EN = """New Balance opened a second Black Friday on 23 November. The first ran 2-9 November under the name "Black Week"; three weeks later the store has opened again. This round ends at 09:59 on 28 November — a day earlier than Black Friday itself, so a weekend shopping plan needs to move up.
Here is what the official store showed on the afternoon of 26 November.

1. Until when, and how much
The event page reads "2026 BLACK FRIDAY: up to 80%, plus additional promotions on sale prices". Coupons run from 10:00 on 23 November to 09:59 on 28 November. The 80% ceiling applies to clearance items; mainstream models sit between 20% and 40%. Discounts on the products we checked ranged from 16% to 60%.

2. Three layers of coupons
First, members receive three tier coupons automatically: VIP 20%, MANIA 15%, FAMILY 10%. Even the lowest tier gets 10%, so simply joining secures a base discount.
Second, sale items take a promo code: 10% over 100,000 won, 20% over 200,000 won. The code works by amount band, so the two cannot be combined.
Third, paying 200,000 won or more with Naver Pay takes 5,000 won off instantly, from 10:00 on 21 November to 09:59 on 28 November.
Separately, first-time buyers get a 15% coupon and members with no purchase in the past year receive a 15% welcome-back coupon automatically. Consenting to third-party data provision tied to the new site launch adds a 10% coupon (19-28 November, until 09:59). Their stacking rules differ, so confirm on the payment screen which combination actually applies.

3. Today's shoe prices
Start with the 1080 V15: 159,000 won, 24% off 209,000, in women's D and men's 2E and 4E widths, at the same price across widths. It occupies ranks one to six on the store's best-seller list.
Running models go deeper. Level V5 men's 2E is 149,000 won (32% off 219,000), SC Trainer V3 is 169,000 won (32% off 249,000), 880 V15 men's 2E is 129,000 won (32% off 189,000). 860 V15 women's D is 149,000 won (21% off 189,000) and SC Elite V5 women's is 209,000 won (36% off 329,000).
Today's one-day deal is the 471 line: U471AM, U4717K6 and U4713G5, list price 139,000 won, are down 60% to 55,000 won. The one-day deal changes every morning at 10:00 and lasts 24 hours. The 204L line sits at 99,000 won, 38% off 159,000.

4. Today's apparel and accessories
Winter outerwear carries the deepest cuts. The UNI RC HEAT padded jumper is 179,000 won (40% off 299,000) and the UNI Flying77 Superlight Standneck padded jacket is 199,000 won (23% off 259,000). The UNI Active Light down jacket is 109,000 won (31% off 159,000) and the UNI Essential Standneck woven jacket is 77,900 won (40% off 129,000).
Accessories follow: 3-pack running socks 27,900 won (30% off 39,900), RE-ON backpack 59,900 won (40% off 99,900), Glossy mini shoulder bag 39,900 won (20% off 49,900). If you are outfitting for winter running, adding socks and a bag to the same order usually beats paying delivery twice.

5. What a basket comes to
The padded jumper (179,000) plus the 1080 V15 (159,000) totals 338,000 won. That clears 200,000, so the 20% promo code applies and brings it to 270,400 won. Adding the Naver Pay discount for payments over 200,000 takes another 5,000, landing at 265,400 won — 78.5% of the starting price.
For women's sizing, Level V5 (149,000) plus RC HEAT (179,000) also totals 328,000, still inside the 20% band. A single item under 100,000 won drops you to the 10% code. When you are just short of 200,000, adding socks or a bag to reach the band often pays for itself.
Note that whether the code and the Naver Pay discount combine, and which popular models are excluded from coupons, varies by item. The arithmetic above assumes every discount applies; the final number is the one in the cart.

6. Timing
Sale prices hold for the whole period, but the extra cuts have their own hours. The one-day deal changes at 10:00 daily and runs 24 hours. Twice a day, 17:00-19:00 and 22:00-midnight, a two-hour time attack opens; today's 17:00 round was still marked "before open" when we checked.
Popular sizes go first in those windows. Widths and sizes in the 260-280 range thin out right after the 10:00 change. If you know the model and size, set an alert and go in at 10:00.

7. 09:59 on 28 November is the real deadline
The practical end of this event is 09:59 on 28 November. Black Friday is the 27th, but at New Balance the coupons stop on the morning of the 28th, not the night of the 27th. Planning to browse slowly on Saturday morning is risky; items already in your list are better paid for during the 27th.
Anything left after the sale returns to list price, and the bigger the gap now (471 line at 60% off, RC HEAT at 40%), the bigger the jump back.

8. Before you pay
"Up to 80%" is not the store-wide rate. Among the models we checked, 16-40% was typical, and 60% appeared only in limited rounds like today's 471 one-day deal. Watch the cart total, not the badge.
Decide the width first. The 1080 V15 comes in 2E, 4E and D at the same price; running shoes hurt if the width is wrong, so go with the width you have tried on. Size exchanges are free, but the event period brings heavy volume.
Tier coupons are issued automatically yet expire. Check the coupon wallet under the tier-coupon name and confirm the expiry before paying.

In one line
New Balance's 2026 Black Friday ends at 09:59 on 28 November. The 1080 V15 is 159,000 won from 209,000, Level V5 149,000 from 219,000, and the RC HEAT padded jumper 179,000 from 299,000. Tier coupons of 10-20%, a 20% code over 200,000 won and a 5,000-won Naver Pay discount can stack, so building a basket above 200,000 won works in your favour."""

JA = """ニューバランスが11月23日から2度目のブラックフライデーを開いた。11月2日から9日まで「ブラックウィーク」として一度セールをしており、3週間ぶりの再開だ。今回は11月28日午前9時59分に終わる。ブラックフライデー当日の27日より1日早く閉じるので、週末にまとめて買う予定なら前倒しが必要だ。
11月26日午後に公式オンラインストアで確認した価格と特典をまとめた。

1. いつまで、どれくらい
最初の画面には「2026 BLACK FRIDAY、セール価格に追加プロモーションまで、UP TO 80%」とある。クーポン利用期間は11月23日午前10時から11月28日午前9時59分まで。最大80%は一部の在庫整理商品に付く数字で、代表モデルは20〜40%台に集まっている。今日確認した商品別割引率も16%から60%まで広く散っている。

2. クーポンは三層
第一に、会員ランク別クーポンが3枚自動発行される。VIP20%、MANIA15%、FAMILY10%だ。最下位ランクでも10%は受け取れるので、会員登録だけでも基本割引は確保できる。
第二に、セール商品にはプロモーションコードが付く。10万ウォン以上で10%、20万ウォン以上で20%だ。コードは金額帯で分かれるため、二つを併用することはできない。
第三に、ネイバーペイで20万ウォン以上決済すると5,000ウォンが即時割引される。期間は11月21日午前10時から28日午前9時59分まで。
さらに初回購入者向け15%クーポンと、直近1年購入履歴のない会員に自動発行されるウェルカムバック15%クーポンが別にある。新サイト開設に伴う個人情報の第三者提供に同意すると10%クーポンも出る（11月19日〜28日9時59分）。重複条件がそれぞれ違うので、決済画面で実際に適用される組み合わせを確認したい。

3. 今日の靴の価格
まず見るべきは1080 V15だ。レディースD、メンズ2E、メンズ4Eの3つの幅すべて209,000ウォンから24%引きの159,000ウォン。幅だけが違い、価格は同じ。公式ストアのベストランキング1位から6位までをこのモデルが占めるほど販売が集中している。
ランニングモデルはさらに深い。レベルV5メンズ2Eは219,000ウォンから32%引きの149,000ウォン、SC Trainer V3は249,000ウォンから32%引きの169,000ウォン、880 V15メンズ2Eは189,000ウォンから32%引きの129,000ウォン。860 V15レディースDは189,000ウォンから21%引きの149,000ウォン、SC Elite V5レディースは329,000ウォンから36%引きの209,000ウォン。
今日のワンデイ特価は471ラインだ。定価139,000ウォンのU471AM、U4717K6、U4713G5などが60%引きの55,000ウォン。ワンデイ特価は毎日午前10時に切り替わり、24時間だけ続く。204Lラインは159,000ウォンから38%引きの99,000ウォン。

4. 今日のアパレルと雑貨
冬アウターの下げ幅が最も大きい。UNI RC HEAT パデッドジャンパーは299,000ウォンから40%引きの179,000ウォン、UNI フライング77 スーパーライト スタンドネック 軽量パデッドジャケットは259,000ウォンから23%引きの199,000ウォン。UNI アクティブ ライト ダウンジャケットは159,000ウォンから31%引きの109,000ウォン、UNI エッセンシャル スタンドネック ウーブンジャケットは129,000ウォンから40%引きの77,900ウォン。
雑貨も下がる。3PACK ランニングソックスは39,900ウォンから30%引きの27,900ウォン、RE-ON バックパックは99,900ウォンから40%引きの59,900ウォン、グロッシー ミニ ショルダーバッグは49,900ウォンから20%引きの39,900ウォン。冬のランニング装備を揃えるなら、靴下とバッグを同じ注文に入れたほうが送料の面で得だ。

5. 組み合わせると
パデッドジャンパー（179,000ウォン）と1080 V15（159,000ウォン）で338,000ウォン。20万ウォンを超えるので20%コードの対象となり、適用されれば270,400ウォン。さらにネイバーペイの20万ウォン以上5,000ウォン即時割引が付けば265,400ウォンで、最初の78.5%になる。
レディースならレベルV5（149,000ウォン）とRC HEAT（179,000ウォン）で328,000ウォンと、こちらも20%帯に入る。逆に10万ウォン台の1点だけならコードは10%に下がる。20万ウォンを少し超える構成なら、靴下やバッグを足して金額帯を合わせる計算が実際に得になることが多い。
ただしコードとネイバーペイ割引が同時に適用されるか、クーポン対象外の人気モデルがあるかは商品ごとに違う。上記はすべての割引が適用される前提の計算で、最終金額はカートで確認する必要がある。

6. 時間帯で狙う
セール価格は期間中ずっと続くが、追加値下げが付く時間帯が別にある。毎日午前10時にワンデイ特価が切り替わり24時間続く。1日2回、午後5時から7時と午後10時から24時には「タイムアタック」特価が開く。今日の17時回は確認時点でまだ「プロモーションオープン前」の表示だった。
人気サイズはこの時間帯に最初に消える。260〜280の帯はワンデイ特価が始まる午前10時直後に在庫が減るパターンが繰り返されている。モデルとサイズが決まっているなら通知をかけ、午前10時にすぐ入るのが安全だ。

7. 28日午前9時59分、この時刻を逃すと終わり
今回の実質的な締切は11月28日午前9時59分だ。27日がブラックフライデー当日だが、ニューバランス基準では27日の夜ではなく28日の朝にクーポンが切れる。土曜の朝にゆっくり見ようという計画は危険だ。リストに入れた商品は27日中に決済を終えたほうがいい。
セール終了後に在庫が残れば定価に戻る。セール価格と定価の差が大きいモデル（471ライン60%、RC HEAT 40%）ほど、終了後の戻り幅も大きい。

8. 買う前に確認すること
最大80%は全商品の割引率ではない。今日確認した代表モデルでは16〜40%が一般的で、60%はワンデイ特価の471ラインのように限られた回にだけ出る。商品一覧の割引率よりカートの最終金額を見るべき理由だ。
幅（ウィズ）とサイズを先に決める。1080 V15は2E・4E・Dの3幅で価格は同じ。ランニングシューズは幅が合わないと足が痛むので、店頭で履いた幅を基準に選びたい。サイズ交換は無料だが、期間中は物量が集中する。
ランククーポンは自動発行だが利用期限がある。クーポンBOXで「ランククーポン」の名前で確認し、決済前に期限をもう一度見ておくと安全だ。

ひとことで
ニューバランスの2026ブラックフライデーは11月28日午前9時59分に終わる。1080 V15は209,000→159,000ウォン、レベルV5は219,000→149,000ウォン、RC HEAT パデッドジャンパーは299,000→179,000ウォン。ランククーポン10〜20%に20万ウォン以上の20%コード、ネイバーペイ5,000ウォンまで重なる可能性があるので、20万ウォンを超える構成でまとめるのが有利だ。"""

ZH = """新百伦在11月23日开启了第二轮黑色星期五。11月2日至9日刚以「Black Week」做过一次，三周后再次开门。这一轮在11月28日上午9点59分结束，比黑五当天的27日还早一天，原打算周末集中采购的计划需要提前。
以下是11月26日下午在官方线上商城确认的价格与优惠。

1. 到什么时候，便宜多少
活动首屏写着「2026 BLACK FRIDAY，在折扣价上再加码，UP TO 80%」。优惠券使用期为11月23日上午10点至11月28日上午9点59分。最高80%只出现在清库存商品上，主力型号集中在20%至40%。我们确认的商品折扣从16%到60%不等。

2. 三层优惠券
第一，会员等级券自动发放3张：VIP 20%、MANIA 15%、FAMILY 10%。最低等级也有10%，仅注册即可锁定基础折扣。
第二，折扣商品可用促销码：满10万韩元10%、满20万韩元20%。促销码按金额档位划分，两者不能同用。
第三，用Naver Pay支付满20万韩元立减5,000韩元，期间为11月21日上午10点至28日上午9点59分。
此外还有首次购买者15%券，以及近一年无购买记录会员自动获得的回归15%券；同意新站上线的个人信息第三方提供可再得10%券（11月19日至28日9点59分）。这些券的叠加规则各不相同，需在结算页确认实际适用的组合。

3. 今天的鞋类价格
先看1080 V15：女款D、男款2E与4E三种宽度全部由209,000韩元降至159,000韩元（24%），仅是宽度不同，价格一致。它占据了官方商城畅销榜第1至第6名。
跑鞋降得更深：Level V5男款2E 219,000→149,000韩元（32%）、SC Trainer V3 249,000→169,000韩元（32%）、880 V15男款2E 189,000→129,000韩元（32%）。860 V15女款D 189,000→149,000韩元（21%），SC Elite V5女款329,000→209,000韩元（36%）。
今天的「一日特价」是471系列：标价139,000韩元的U471AM、U4717K6、U4713G5等降到55,000韩元（60%）。一日特价每天上午10点更换，仅维持24小时。204L系列为159,000→99,000韩元（38%）。

4. 今天的服饰与配件
冬季外套降幅最大：UNI RC HEAT 羽绒夹克299,000→179,000韩元（40%），UNI Flying77 超轻立领羽绒夹克259,000→199,000韩元（23%）。UNI Active Light 羽绒服159,000→109,000韩元（31%），UNI Essential 立领梭织夹克129,000→77,900韩元（40%）。
配件同步下调：3双跑步袜39,900→27,900韩元（30%），RE-ON 背包99,900→59,900韩元（40%），Glossy 迷你单肩包49,900→39,900韩元（20%）。若要一次配齐冬跑装备，把袜子和包放进同一单更省运费。

5. 组合起来要多少钱
羽绒夹克（179,000）加1080 V15（159,000）合计338,000韩元。超过20万即适用20%促销码，折后270,400韩元；再用Naver Pay满20万减5,000，则为265,400韩元，相当于原价的78.5%。
女款用Level V5（149,000）加RC HEAT（179,000）合计328,000韩元，同样落在20%档。只买十万韩元级的一件，促销码降为10%。正好差一点到20万时，加一双袜子或一个包把档位补上，往往是划算的。
不过促销码与Naver Pay是否同时适用、哪些热门款被排除，逐件不同。上述是按全部优惠都生效计算，最终金额以购物车为准。

6. 按时间段出手
折扣价全期维持，但追加降价另有时间：每天上午10点更换一日特价，持续24小时；每天两次，下午5点至7点、晚10点至24点开「时间攻击」特价。今天17点那场在确认时仍显示「活动开始前」。
热门尺码在这些时段最先消失。260至280区间常在上午10点一日特价开启后立即减少。确定型号和尺码的话，设好提醒、10点直接进场最稳。

7. 11月28日上午9点59分是真正的截止
本次活动的实际截止是11月28日上午9点59分。虽然27日是黑五当天，但新百伦的优惠券是在28日早上失效，而不是27日夜里。打算周六早上慢慢逛是危险的；已加入清单的商品最好在27日内付完。
活动结束后若仍有库存即回到原价，差价越大的型号（471系列60%、RC HEAT 40%）回升幅度也越大。

8. 购买前确认
「最高80%」并非全店折扣。我们确认的主力型号多为16%至40%，60%只出现在像今天471这类限量轮次。这就是要看购物车最终金额而非折扣标签的原因。
先确定宽度。1080 V15有2E、4E、D三种宽度且价格相同；跑鞋宽度不合会伤脚，建议按试穿过的宽度选。尺码换货免费，但活动期物流量大。
等级券虽自动发放但有期限。请在优惠券栏以「等级券」名称查找，并在付款前再确认一次到期日。

一句话总结
新百伦2026黑五在11月28日上午9点59分结束。1080 V15由209,000降至159,000韩元，Level V5由219,000降至149,000韩元，RC HEAT 羽绒夹克由299,000降至179,000韩元。等级券10%至20%、满20万的20%促销码、Naver Pay 5,000韩元可叠加，因此把购物车凑过20万更划算。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "k-fashion",
    "store": "뉴발란스 공식 온라인스토어",
    "priceKrw": 159000,
    "releaseDate": "2026-11-26",
    "rating": 4.7,
    "imageUrl": G1,
    "images": [G1, G2, G3, G4, G5],
    "affiliateUrl": q("뉴발란스 1080 v15"),
    "affiliatePlatform": "Coupang",
    "exampleItems": [
        {"name": "뉴발란스 1080 V15 (남성 4E)", "brand": "New Balance", "priceKrw": 159000, "imageUrl": G1,
         "url": q("뉴발란스 1080 v15"), "category": "209,000→159,000원 · 24%"},
        {"name": "뉴발란스 레벨 V5 (남성 2E)", "brand": "New Balance", "priceKrw": 149000, "imageUrl": G2,
         "url": q("뉴발란스 레벨 v5"), "category": "219,000→149,000원 · 32%"},
        {"name": "UNI RC HEAT 패딩점퍼", "brand": "New Balance", "priceKrw": 179000, "imageUrl": G3,
         "url": q("뉴발란스 RC HEAT 패딩"), "category": "299,000→179,000원 · 40%"},
        {"name": "뉴발란스 U471AM (원데이 특가)", "brand": "New Balance", "priceKrw": 55000, "imageUrl": G4,
         "url": q("뉴발란스 471"), "category": "139,000→55,000원 · 60%"},
        {"name": "UNI 플라잉77 슈퍼라이트 경량 패딩 자켓", "brand": "New Balance", "priceKrw": 199000, "imageUrl": G5,
         "url": q("뉴발란스 플라잉77 경량 패딩"), "category": "259,000→199,000원 · 23%"},
    ],
    "i18n": {
        "ko": {
            "title": "뉴발란스 블프, 28일 오전 9시 59분에 끝난다 — 1080 V15 159,000원·패딩 40% 실측",
            "summary": "11월 28일 09:59 마감, UP TO 80%. 1080 V15 209,000→159,000원, 레벨 V5 219,000→149,000원, RC HEAT 패딩점퍼 299,000→179,000원, 471 라인 원데이 특가 55,000원. 등급쿠폰·20% 코드·네이버페이까지 겹치는 조건을 정리했습니다.",
            "description": KO,
            "tasteReview": [
                "기간: 11/23 10:00 ~ 11/28 09:59(쿠폰 사용), 첫 배너 UP TO 80%",
                "쿠폰 3중: 등급쿠폰 VIP 20%·MANIA 15%·FAMILY 10% + 10만↑10%·20만↑20% 코드 + 네이버페이 20만↑ 5,000원",
                "1080 V15 209,000→159,000원(24%), 레벨 V5 219,000→149,000원(32%), RC HEAT 패딩 299,000→179,000원(40%), 471 라인 139,000→55,000원(60%)",
                "원데이 특가 매일 10시 24시간, 타임어택 17~19시·22~24시 — 인기 사이즈 260~280은 오전 10시 직후 소진",
            ],
            "tips": "가격과 기간은 2026년 11월 26일 오후 뉴발란스 공식 온라인스토어에서 확인한 값입니다. 쿠폰 중복 조건과 재고에 따라 최종 결제금액이 달라지므로 장바구니에서 확인하세요. 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있으며, 비교 링크는 쿠팡 검색 결과로 연결됩니다.",
        },
        "en": {
            "title": "New Balance Black Friday Ends at 09:59 on 28 November — 1080 V15 at 159,000 Won, Padded Jackets 40% Off",
            "summary": "Ends 09:59 on 28 November, up to 80%. 1080 V15 209,000 to 159,000 won, Level V5 219,000 to 149,000, RC HEAT padded jumper 299,000 to 179,000, 471 line one-day deal at 55,000. How the tier coupons, 20% code and Naver Pay discount stack.",
            "description": EN,
            "tasteReview": [
                "Period: 23 Nov 10:00 to 28 Nov 09:59 for coupons, store banner up to 80%",
                "Three coupon layers: VIP 20% / MANIA 15% / FAMILY 10%, plus 10% over 100,000 and 20% over 200,000 codes, plus 5,000 won with Naver Pay over 200,000",
                "1080 V15 209,000 to 159,000 (24%), Level V5 219,000 to 149,000 (32%), RC HEAT padded jumper 299,000 to 179,000 (40%), 471 line 139,000 to 55,000 (60%)",
                "One-day deal changes at 10:00 for 24 hours; time attack 17:00-19:00 and 22:00-24:00; sizes 260-280 go right after 10:00",
            ],
            "tips": "Prices and dates were read at the New Balance official store on the afternoon of 26 November 2026. Final totals depend on coupon stacking and stock; check the cart. This post contains affiliate links and may earn a commission; comparison links open Coupang search results.",
        },
        "ja": {
            "title": "ニューバランスのブラックフライデーは28日午前9時59分で終了 — 1080 V15 159,000ウォン・パデッド40%引き実測",
            "summary": "11月28日9:59終了、UP TO 80%。1080 V15 209,000→159,000ウォン、レベルV5 219,000→149,000ウォン、RC HEAT パデッドジャンパー299,000→179,000ウォン、471ラインのワンデイ特価55,000ウォン。ランククーポン・20%コード・ネイバーペイの重複条件を整理しました。",
            "description": JA,
            "tasteReview": [
                "期間：11/23 10:00〜11/28 9:59（クーポン利用）、最初のバナーはUP TO 80%",
                "クーポン三重：ランククーポンVIP20%・MANIA15%・FAMILY10%＋10万以上10%・20万以上20%コード＋ネイバーペイ20万以上5,000ウォン",
                "1080 V15 209,000→159,000ウォン（24%）、レベルV5 219,000→149,000ウォン（32%）、RC HEAT 299,000→179,000ウォン（40%）、471ライン139,000→55,000ウォン（60%）",
                "ワンデイ特価は毎日10時に24時間、タイムアタックは17〜19時・22〜24時 — 人気サイズ260〜280は10時直後に消化",
            ],
            "tips": "価格と期間は2026年11月26日午後にニューバランス公式オンラインストアで確認した値です。クーポンの重複条件と在庫により最終決済額が変わるためカートで確認してください。本記事はアフィリエイトリンクを含み手数料を受け取る場合があります。比較リンクはCoupang検索結果に移動します。",
        },
        "zh": {
            "title": "新百伦黑五28日上午9点59分结束——1080 V15 159,000韩元、羽绒40%折扣实价",
            "summary": "11月28日9:59截止，UP TO 80%。1080 V15 209,000→159,000韩元，Level V5 219,000→149,000韩元，RC HEAT羽绒夹克299,000→179,000韩元，471系列一日特价55,000韩元。等级券、20%促销码与Naver Pay的叠加条件一次说清。",
            "description": ZH,
            "tasteReview": [
                "期间：11/23 10:00～11/28 9:59（优惠券使用），首屏UP TO 80%",
                "三重券：等级券VIP 20%・MANIA 15%・FAMILY 10%＋满10万10%・满20万20%促销码＋Naver Pay满20万5,000韩元",
                "1080 V15 209,000→159,000韩元（24%）、Level V5 219,000→149,000韩元（32%）、RC HEAT羽绒夹克299,000→179,000韩元（40%）、471系列139,000→55,000韩元（60%）",
                "一日特价每天10点起24小时，时间攻击17～19点・22～24点——热门尺码260～280在10点后迅速售完",
            ],
            "tips": "价格与期间为2026年11月26日下午在新百伦官方线上商城确认的数值。最终金额会因优惠券叠加条件与库存变化，请在购物车确认。本文含联盟链接，可能获得佣金；比价链接跳转至Coupang搜索结果。",
        },
    },
}

if __name__ == "__main__":
    publish(POST)
