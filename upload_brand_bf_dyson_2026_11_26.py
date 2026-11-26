#!/usr/bin/env python3
"""4편 다이슨 블프 라스트찬스 위크 (4개국어) → Supabase posts + ISR revalidate.

근거 (2026-11-26 13:35~13:50 KST dyson.co.kr/promotions/black-friday-2026 직접 확인)
 - 블프 라스트찬스 위크 11월 23일 ~ 11월 30일
 - 에어랩 코안다2x (버건디 우드) 879,000→699,000(할인 180,000) + 7만원 상당 보관용 파우치, 리뷰 10,816·4.9
 - 슈퍼소닉 뉴럴(세라믹 핑크/로즈 골드)+보관 케이스 599,000→449,000(150,000) + 7만원 상당 스탠드, 리뷰 12,561·4.9
 - V16 피스톤 애니멀 서브마린 1,490,000→1,100,000(390,000), 품절 표시, 카드 최대 혜택가 990,000
 - 펜슬백 플러피 콘 799,000→619,000(180,000) + 12만원 상당 배터리, 최대 혜택가 557,100
 - 펜슬워시 499,000→299,000(200,000), 삼성/롯데카드 결제 시 5만원 캐시백
 - 스팟앤스크럽 Ai 1,690,000→1,070,000(620,000) + 9만원 상당 롤러, 최대 혜택가 963,000
 - 클린앤워시 하이진 699,000→519,000(180,000), 최대 혜택가 467,100
 - 카드: 삼성 10% 최대 10만원, 롯데/하나 10% 최대 20만원, 간편결제 청구할인 불가
 - 리퍼브 최대 62%, 액세서리 최대 71%, 11/26 20시 라이브(헤어케어·사은품·캐시백)
 - 제품 사진: 공식몰 제품컷 5장 3:4(1200×1600) 정규화. AI 생성 0장.
"""
from brand_bf_common import publish, q

SLUG = "dyson-blackfriday-last-chance-2026"

G1 = "/images/products/bfb-dyson-airwrap.jpg"
G2 = "/images/products/bfb-dyson-supersonic.jpg"
G3 = "/images/products/bfb-dyson-v16.jpg"
G4 = "/images/products/bfb-dyson-pencilback.jpg"
G5 = "/images/products/bfb-dyson-cleanwash.jpg"

KO = """다이슨이 11월 23일부터 '블프 라스트찬스 위크'를 열었다. 이름 그대로 블랙프라이데이 혜택을 한 주 더 연장한 행사로, 11월 30일에 끝난다. 첫 화면 문구는 '1년에 단 한 번, 가장 강력한 블프혜택 마지막 기회'다.
11월 26일 오후 공식몰에서 확인한 가격과 조건을 정리했다. 카드 혜택까지 적용한 '최대 혜택가'는 상품마다 함께 표시돼 있어서, 표시 가격과 실제 결제금액이 다르다는 점을 먼저 알아두면 좋다.

1. 언제까지, 얼마나
기간은 11월 23일부터 11월 30일까지다. 최대 할인율은 상품군에 따라 다르다. 본체는 20~40%, 공식 인증 리퍼브는 최대 62%, 액세서리는 최대 71%다. 액세서리 할인이 가장 세지만, 본체를 이미 가진 사람에게만 의미가 있다.
행사 구성은 네 갈래다. 헤어케어(에어랩·슈퍼소닉), 청소기(무선·물청소·로봇), 공기청정기(가습·핫앤쿨·빅+콰이엇), 조명(솔라사이클)이 함께 내려간다. 품목이 많아서 '무엇이 가장 많이 빠졌는지'를 기준으로 고르는 편이 빠르다.
오늘 확인한 할인 폭은 이렇다. 금액 기준으로 가장 큰 할인은 로봇청소기 스팟앤스크럽 Ai의 62만 원(37%)이고, 비율 기준으로는 물청소기 펜슬워시의 40%다. 헤어케어는 20~25% 선이지만 증정품 가치가 붙는다.

2. 에어랩 코안다2x — 879,000원에서 699,000원
NEW 다이슨 에어랩 코안다2x 멀티 스타일러 앤 드라이어(버건디 우드)가 879,000원에서 18만 원 내린 699,000원이다. 할인율로는 20.5%다. 여기에 7만 원 상당의 보관용 파우치가 증정품으로 붙는다. 상품평은 10,816개, 평점 4.9다.
색상은 버건디 우드, 세라믹 핑크/로즈 골드, 재스퍼 플럼 세 가지다. 오늘 화면에서는 세 색 모두 같은 가격이었다. 에어랩은 구성품이 많아 보관이 문제인데, 파우치가 포함되면 이동할 때 부담이 줄어든다.
증정품은 재고 소진 시 본품만 출고된다. 장바구니에 사은품이 함께 담기는지 확인해야 한다.

3. 슈퍼소닉 뉴럴 — 599,000원에서 449,000원
다이슨 슈퍼소닉 뉴럴 헤어드라이어(세라믹 핑크/로즈 골드)와 보관 케이스가 599,000원에서 15만 원 내린 449,000원이다. 할인율 25%로, 헤어케어 라인 중 비율이 가장 높다. 여기에 7만 원 상당의 슈퍼소닉 뉴럴 스탠드가 증정된다. 상품평 12,561개, 평점 4.9로 이번 행사 상품 중 후기가 가장 많다.
블루/코퍼와 버건디 우드 색상도 같은 가격에 올라와 있다. 드라이어 단품을 찾는다면 이 구성이 가장 실속 있다. 케이스와 스탠드가 각각 6만~7만 원대에 팔리는 액세서리라는 점을 감안하면, 449,000원은 본체 가격에 가까운 수준이다.

4. 청소기 — 가장 많이 빠진 두 모델
펜슬워시 물청소기는 499,000원에서 20만 원 내린 299,000원이다. 할인율 40%로 이번 행사 최고 비율이다. 상품평 199개, 평점 4.6으로 후기는 적지만 신제품 라인이다. 여기에 삼성카드나 롯데카드로 결제하면 5만 원 캐시백이 붙는다. 카드 캐시백까지 적용하면 실질 249,000원 수준이 된다.
로봇청소기 스팟앤스크럽 Ai는 1,690,000원에서 62만 원 내린 1,070,000원이다. 할인 금액 기준으로 이번 행사에서 가장 크다. 9만 원 상당의 Ai 마이크로파이버 롤러 2개가 증정되고, 삼성카드 10%(최대 10만 원) 또는 롯데·하나카드 10%(최대 20만 원) 청구할인까지 적용하면 최대 혜택가가 963,000원으로 표시된다.
무선청소기 V16 피스톤 애니멀 서브마린은 1,490,000원에서 39만 원 내린 1,100,000원이다. 다이슨이 만든 무선청소기 중 가장 강한 모델인데, 오늘 확인 시점에는 '제품이 현재 품절입니다' 표시가 붙어 있었다. 카드 혜택까지 적용한 최대 혜택가는 990,000원이다. 재고가 풀리면 바로 빠질 가능성이 크므로 입고 알림을 걸어두는 편이 낫다.

5. 공기청정기와 조명
공기청정기는 세 모델이 같은 폭으로 내려간다. 빅+콰이엇 포름알데히드(블루/골드)와 가습 공기청정기 PH2(화이트/골드)가 각각 1,290,000원에서 951,000원(39만 원 할인), 핫앤쿨 HP2(화이트/골드)가 1,090,000원에서 790,000원(30만 원 할인)이다. 세 모델 모두 카드 청구할인을 적용하면 최대 혜택가가 855,900원과 750,500원으로 내려간다.
겨울에는 가습 기능이 있는 PH2가 실용적이다. 건조한 실내에서 가습과 청정을 한 대로 처리하려는 수요가 몰리는 시기라 재고가 빠르다.
조명은 솔라사이클 모프 데스크형이 720,000원에서 507,000원(21만 3천 원 할인), 플로어스탠드형이 960,000원에서 673,000원(28만 7천 원 할인)이다. 책상 위 조명을 바꾸려는 사람에게는 이번이 가장 낮은 가격대다.

6. 리퍼브와 액세서리
공식 인증 리퍼브는 최대 62% 혜택가로 팔린다. 재고 소진 시 조기 종료된다. 리퍼브는 외관 흠집이 있을 수 있지만 성능 검수와 보증은 동일하게 적용된다. 새 제품 가격이 부담스러운 모델이라면 이쪽을 먼저 보는 것도 방법이다.
액세서리는 최대 71% 할인이다. 브러시 헤드나 필터처럼 소모품을 교체할 시기라면 이번 주가 가장 싸다. 다만 액세서리 딜은 2026년 마지막 딜이라고 안내돼 있어, 이후에는 연초까지 비슷한 가격을 기대하기 어렵다.

7. 카드 할인은 이렇게 계산된다
삼성카드는 10% 할인에 최대 10만 원, 롯데카드와 하나카드는 10% 할인에 최대 20만 원이다. 예를 들어 699,000원짜리 에어랩을 삼성카드로 결제하면 629,000원이 된다. 951,000원짜리 공기청정기를 롯데카드로 결제하면 855,900원이다.
주의할 점이 있다. 간편결제로 결제하면 청구할인이 적용되지 않는다. 카카오페이나 네이버페이로 결제하면 할인 전 가격이 그대로 나간다. 카드 할인을 노린다면 카드 정보를 직접 입력하는 일반 결제로 진행해야 한다.
증정품은 재고 소진 시 본품만 출고된다. 반품할 때는 증정품도 함께 반품해야 한다.

8. 오늘 밤 8시 라이브
11월 26일 오후 8시에 라이브 방송이 열린다. 헤어케어 베스트 제품 할인, 방송 한정 사은품, 캐시백, 추첨 이벤트가 함께 진행된다. 라이브 사은품은 수량이 한정돼 있어 방송 초반에 몰린다.

9. 사기 전에 확인할 것
첫째, 품절 여부다. V16처럼 인기 모델은 행사 기간 중에도 품절된다. 품절이면 알림을 걸고, 대안으로 V16 대신 다른 무선청소기나 리퍼브를 보는 편이 낫다.
둘째, 증정품 동봉 여부다. 장바구니 단계에서 사은품이 함께 담겼는지 확인해야 한다.
셋째, 카드 할인 적용 방식이다. 간편결제는 청구할인이 안 되므로 결제 수단을 먼저 정해야 한다.
넷째, 리퍼브와 신품의 차이다. 리퍼브는 가격이 낮은 대신 외관 상태가 다를 수 있다. 선물용이라면 신품을, 실사용이라면 리퍼브를 권한다.

한 줄 정리
다이슨 블프 라스트찬스 위크는 11월 30일까지다. 에어랩 코안다2x 879,000→699,000원, 슈퍼소닉 뉴럴+케이스 599,000→449,000원, 펜슬워시 499,000→299,000원, 스팟앤스크럽 Ai 1,690,000→1,070,000원이다. 카드 청구할인까지 적용하면 10~20만 원이 더 빠지지만 간편결제로는 적용되지 않는다. V16 피스톤 애니멀은 이미 품절이므로 알림을 걸어두고, 급하면 리퍼브나 다른 모델로 대체하는 편이 낫다."""

EN = """Dyson opened a "Black Friday Last Chance Week" on 23 November — the Black Friday benefit extended by one week, ending 30 November. The front page reads "the strongest Black Friday benefit of the year, one last chance."
Below is what the official store showed on the afternoon of 26 November. Note that the store also prints a "best card price" for each item, so the number on the card and the number you actually pay can differ.

1. Until when, and how much
The window is 23-30 November. The discount depends on the category: machines run 20-40%, certified refurbished up to 62%, accessories up to 71%. Accessories carry the deepest rate but only matter if you already own the machine.
Four categories are covered: hair care (Airwrap, Supersonic), floor care (cordless, wet cleaners, robots), air treatment (humidifying, hot+cool, Big+Quiet) and lighting (Solarcycle). With this many items, sorting by "which one dropped the most" is faster than browsing.
By amount, today's biggest cut is the Spot & Scrub Ai robot vacuum at 620,000 won off (37%); by rate, the Pencilwash wet cleaner at 40%. Hair care sits at 20-25% but adds gifts.

2. Airwrap Co-anda 2x — 879,000 to 699,000 won
The new Airwrap Co-anda 2x Multi-Styler and Dryer in Burgundy Wood is 699,000 won, 180,000 off 879,000 — 20.5%. A storage pouch worth 70,000 won comes as a gift. It carries 10,816 reviews at 4.9.
Three colours are offered: Burgundy Wood, Ceramic Pink/Rose Gold and Jasper Plum, all at the same price today. The Airwrap has many attachments and storage is the usual complaint, so the pouch matters for travel.
Gifts ship only while stock lasts; check that the gift lands in the cart.

3. Supersonic Nural — 599,000 to 449,000 won
The Supersonic Nural hair dryer in Ceramic Pink/Rose Gold with case is 449,000 won, 150,000 off 599,000 — 25%, the highest rate in the hair care line. A Supersonic Nural stand worth 70,000 won is included. Reviews: 12,561 at 4.9, the most of any item in this sale.
Blue/Copper and Burgundy Wood are also listed at the same price. If you want a dryer rather than a styler, this is the strongest configuration: the case and stand normally sell in the 60,000-70,000 won range, so 449,000 won is close to body-only money.

4. Floor care — the two deepest cuts
The Pencilwash wet cleaner is 299,000 won, 200,000 off 499,000 — 40%, the highest percentage here. It has 199 reviews at 4.6, a newer line. Paying with a Samsung or Lotte card adds a 50,000-won cashback, bringing the effective price near 249,000 won.
The Spot & Scrub Ai robot vacuum is 1,070,000 won, 620,000 off 1,690,000 — the largest amount off in this sale. Two Ai microfibre rollers worth 90,000 won are included, and with a Samsung card (10%, up to 100,000 won) or Lotte/Hana card (10%, up to 200,000 won) rebate the best-case price shows as 963,000 won.
The V16 Piston Animal Submarine cordless is 1,100,000 won, 390,000 off 1,490,000. It is Dyson's most powerful cordless, but when we checked it was marked sold out; with card rebates the best-case price is 990,000 won. Restock is likely to sell out immediately, so a restock alert is worth setting.

5. Air treatment and lighting
Three air purifiers move by the same amount: the Big+Quiet Formaldehyde (blue/gold) and the PH2 humidifying purifier (white/gold) are each 951,000 won, down 390,000 from 1,290,000, and the Hot+Cool HP2 (white/gold) is 790,000 won, down 300,000 from 1,090,000. With card rebates the best-case prices drop to 855,900 and 750,500 won.
In winter the PH2 with humidification is the practical pick; demand for one machine that humidifies and purifies spikes in the dry season, so stock moves.
Lighting: the Solarcycle Morph desk model is 507,000 won, down 213,000 from 720,000, and the floor stand model is 673,000 won, down 287,000 from 960,000.

6. Refurbished and accessories
Certified refurbished sells at up to 62% off and ends early when stock runs out. Units may show cosmetic marks but are inspected and warrantied the same way. If a new unit is out of budget, this is the first place to look.
Accessories go up to 71% off. If your brush heads or filters are due, this week is the cheapest. The store describes it as the last accessory deal of 2026.

7. How the card discount works
Samsung cards give 10% up to 100,000 won; Lotte and Hana cards 10% up to 200,000 won. A 699,000-won Airwrap on a Samsung card becomes 629,000; a 951,000-won purifier on a Lotte card becomes 855,900.
One catch: instant-payment wallets do not qualify. Paying with Kakao Pay or Naver Pay sends the full undiscounted amount. If you want the rebate, use a regular card payment where you enter the card details.
Gifts ship only while stock lasts, and must be returned together with the product if you send it back.

8. Live show at 8pm tonight
A live broadcast opens at 8pm on 26 November with hair-care bestsellers, broadcast-only gifts, cashback and a draw. Live gifts are limited and go in the first minutes.

9. Before you pay
Check stock first: popular models like the V16 sell out mid-event. If it is gone, set an alert and consider another cordless or a refurbished unit. Check that the gift is in the cart. Decide the payment method before checkout, since instant-payment wallets lose the rebate. And know the difference between refurbished and new: refurbished is cheaper but may show cosmetic wear — new for a gift, refurbished for yourself.

In one line
Dyson's last-chance week runs to 30 November. Airwrap Co-anda 2x 879,000 to 699,000 won, Supersonic Nural with case 599,000 to 449,000, Pencilwash 499,000 to 299,000, Spot & Scrub Ai 1,690,000 to 1,070,000. Card rebates take another 100,000-200,000 won off but not through instant-payment wallets. The V16 Piston Animal is already sold out — set an alert, or fall back to a refurbished or another model."""

JA = """ダイソンが11月23日から「ブラックフライデー ラストチャンスウィーク」を開いた。名前のとおりブラックフライデー特典を1週間延長した行事で、11月30日に終わる。最初の画面の文言は「年に一度、最も強いブラックフライデー特典の最後の機会」。
11月26日午後に公式ストアで確認した価格と条件をまとめた。カード特典まで適用した「最大特典価」が商品ごとに併記されているので、表示価格と実際の決済額が違う点を先に押さえておきたい。

1. いつまで、どれくらい
期間は11月23日から11月30日まで。最大割引率は商品群で異なる。本体は20〜40%、公式認定リファービッシュは最大62%、アクセサリーは最大71%。アクセサリーが最も深いが、本体をすでに持っている人にしか意味がない。
構成は四つ。ヘアケア（エアラップ・スーパーソニック）、掃除機（コードレス・水拭き・ロボット）、空気清浄機（加湿・ホット＆クール・ビッグ＋クワイエット）、照明（ソーラーサイクル）が同時に下がる。品数が多いので「どれが最も下がったか」で選ぶほうが早い。
今日確認した下げ幅はこうだ。金額で最大はロボット掃除機スポット＆スクラブAiの62万ウォン（37%）、比率で最大は水拭き掃除機ペンシルウォッシュの40%。ヘアケアは20〜25%台だがノベルティの価値が付く。

2. エアラップ コアンダ2x — 879,000→699,000ウォン
NEW ダイソン エアラップ コアンダ2x マルチスタイラー＆ドライヤー（バーガンディウッド）が879,000ウォンから18万ウォン引きの699,000ウォン。率にして20.5%。さらに7万ウォン相当の保管ポーチが付く。レビュー10,816件、評価4.9。
色はバーガンディウッド、セラミックピンク／ローズゴールド、ジャスパープラムの3色。今日の画面では3色とも同価格だった。エアラップは付属品が多く収納が課題になるので、ポーチが付くと持ち運びの負担が減る。
ノベルティは在庫が尽きると本体のみの出荷になる。カートに一緒に入るか確認したい。

3. スーパーソニック ニューラル — 599,000→449,000ウォン
スーパーソニック ニューラル ヘアドライヤー（セラミックピンク／ローズゴールド）と保管ケースが599,000ウォンから15万ウォン引きの449,000ウォン。25%引きでヘアケアライン中最も高い比率。7万ウォン相当のスーパーソニック ニューラル スタンドも付く。レビュー12,561件、評価4.9で今回の商品の中で最も多い。
ブルー／コッパーとバーガンディウッドも同価格で並ぶ。ドライヤー単体を探すならこの構成が最も実質的だ。ケースとスタンドは通常6万〜7万ウォン台のアクセサリーなので、449,000ウォンは本体価格に近い水準になる。

4. 掃除機 — 最も下がった2モデル
ペンシルウォッシュ水拭き掃除機は499,000ウォンから20万ウォン引きの299,000ウォン。40%引きで今回最高の比率。レビュー199件、評価4.6で件数は少ないが新しいラインだ。サムスンカードまたはロッテカードで決済すると5万ウォンのキャッシュバックが付き、実質249,000ウォン水準になる。
ロボット掃除機スポット＆スクラブAiは1,690,000ウォンから62万ウォン引きの1,070,000ウォン。金額ベースで今回最大の下げ幅。9万ウォン相当のAiマイクロファイバーローラー2個が付き、サムスンカード10%（最大10万ウォン）またはロッテ・ハナカード10%（最大20万ウォン）の請求割引まで適用すると最大特典価は963,000ウォンと表示される。
コードレス掃除機V16 ピストン アニマル サブマリンは1,490,000ウォンから39万ウォン引きの1,100,000ウォン。ダイソンで最も強いコードレスだが、確認時点で「ただいま品切れです」の表示が付いていた。カード特典込みの最大特典価は990,000ウォン。入荷すればすぐ消える可能性が高いので入荷通知を勧める。

5. 空気清浄機と照明
空気清浄機は3モデルが同じ幅で下がる。ビッグ＋クワイエット ホルムアルデヒド（ブルー／ゴールド）と加湿空気清浄機PH2（ホワイト／ゴールド）がそれぞれ1,290,000ウォンから951,000ウォン（39万ウォン引き）、ホット＆クールHP2（ホワイト／ゴールド）が1,090,000ウォンから790,000ウォン（30万ウォン引き）。カード請求割引まで適用すると最大特典価は855,900ウォンと750,500ウォンになる。
冬は加湿機能のあるPH2が実用的だ。乾燥する室内で加湿と清浄を1台で済ませたい需要が集まる時期で、在庫の回転が速い。
照明はソーラーサイクル モーフ デスク型が720,000ウォンから507,000ウォン（21万3千ウォン引き）、フロアスタンド型が960,000ウォンから673,000ウォン（28万7千ウォン引き）。机上照明を替えるなら今回が最も低い価格帯だ。

6. リファービッシュとアクセサリー
公式認定リファービッシュは最大62%の特典価で販売され、在庫が尽きると早期終了する。外観に傷がある場合があるが、性能検査と保証は同じように適用される。新品価格が負担なモデルならこちらを先に見るのも手だ。
アクセサリーは最大71%引き。ブラシヘッドやフィルターの交換時期なら今週が最も安い。ただし2026年最後のアクセサリーディールと案内されており、その後は年明けまで同水準は期待しにくい。

7. カード割引の計算
サムスンカードは10%で最大10万ウォン、ロッテカードとハナカードは10%で最大20万ウォン。たとえば699,000ウォンのエアラップをサムスンカードで決済すると629,000ウォン。951,000ウォンの空気清浄機をロッテカードで決済すると855,900ウォンになる。
注意点がある。簡易決済では請求割引が適用されない。カカオペイやネイバーペイで決済すると割引前の価格がそのまま出ていく。カード割引を狙うならカード情報を直接入力する通常決済で進める必要がある。
ノベルティは在庫が尽きると本体のみの出荷。返品時はノベルティも一緒に返す必要がある。

8. 今夜8時ライブ
11月26日午後8時にライブ配信が開かれる。ヘアケアベスト商品の割引、放送限定ノベルティ、キャッシュバック、抽選イベントが同時に進む。ライブのノベルティは数量限定で序盤に集中する。

9. 買う前に確認すること
第一に在庫。V16のように人気モデルは期間中でも品切れになる。品切れなら通知をかけ、代わりに別のコードレスやリファービッシュを見るほうがいい。第二にノベルティの同梱。カートの段階で一緒に入っているか確認する。第三にカード割引の適用方法。簡易決済では請求割引が付かないので決済手段を先に決める。第四にリファービッシュと新品の違い。リファービッシュは安い代わりに外観状態が異なることがある。贈り物なら新品、自分用ならリファービッシュがおすすめだ。

ひとことで
ダイソンのラストチャンスウィークは11月30日まで。エアラップ コアンダ2x 879,000→699,000ウォン、スーパーソニック ニューラル＋ケース599,000→449,000ウォン、ペンシルウォッシュ499,000→299,000ウォン、スポット＆スクラブAi 1,690,000→1,070,000ウォン。カード請求割引まで適用すると10〜20万ウォンがさらに引かれるが、簡易決済では適用されない。V16 ピストン アニマルはすでに品切れなので通知をかけ、急ぐならリファービッシュか別モデルで代替したい。"""

ZH = """戴森自11月23日起开启「黑五最后机会周」，即把黑五优惠延长一周，11月30日结束。首屏文案是「一年仅一次，最强黑五优惠的最后机会」。
以下是11月26日下午在官方商城确认的价格与条件。多数商品同时标出「叠加信用卡后的最优价」，因此页面价格与实付金额可能不同。

1. 到什么时候，便宜多少
期间为11月23日至11月30日。最高折扣按品类不同：整机20%～40%，官方认证翻新机最高62%，配件最高71%。配件折扣最深，但只有已有机身的人才用得上。
活动覆盖四类：美发（Airwrap、Supersonic）、地面清洁（无线、湿式、机器人）、空气处理（加湿、冷暖、Big+Quiet）与照明（Solarcycle）。品项很多，按「降幅最大」来挑比逐个浏览更快。
今天确认的降幅：按金额最大是扫地机器人Spot & Scrub Ai减62万韩元（37%）；按比例最大是湿式清洁机Pencilwash的40%。美发类在20%～25%，但附带赠品。

2. Airwrap Co-anda 2x——879,000降至699,000韩元
NEW 戴森 Airwrap Co-anda 2x 多功能造型吹风机（酒红木色）879,000降至699,000韩元，减18万（约20.5%），另赠价值7万韩元的收纳包。评价10,816条、评分4.9。
颜色有酒红木、陶瓷粉/玫瑰金、碧玉紫三种，今天三色同价。Airwrap配件多、收纳是常见痛点，附赠收纳包对出行有帮助。
赠品库存售完只发主机，请在购物车确认赠品是否一起加入。

3. Supersonic Nural——599,000降至449,000韩元
Supersonic Nural 吹风机（陶瓷粉/玫瑰金）含收纳盒599,000降至449,000韩元，减15万（25%），是美发线中比例最高的一款，另赠价值7万韩元的专用支架。评价12,561条、评分4.9，为本次活动评论最多。
蓝/铜色与酒红木色同价。若只想要吹风机而非造型器，这个组合最实在：收纳盒与支架平时各在6万至7万韩元区间，449,000韩元已接近单机价格。

4. 地面清洁——降幅最大的两款
Pencilwash 湿式清洁机499,000降至299,000韩元（40%），是本次活动最高比例。评价199条、评分4.6，属较新的产品线。用三星或乐天卡支付另有5万韩元返现，实际接近249,000韩元。
扫地机器人Spot & Scrub Ai 1,690,000降至1,070,000韩元，减62万，是本次活动金额最大。附赠价值9万韩元的Ai超细纤维滚刷2个，叠加三星卡10%（上限10万韩元）或乐天/韩亚卡10%（上限20万韩元）返现后，最优价显示为963,000韩元。
无线吸尘器V16 Piston Animal Submarine 1,490,000降至1,100,000韩元，减39万。它是戴森最强无线机型，但确认时显示「目前售罄」；叠加信用卡后的最优价为990,000韩元。到货后很可能立刻售完，建议设置到货提醒。

5. 空气净化与照明
三款空气净化器同幅下调：Big+Quiet 甲醛款（蓝/金）与加湿空气净化器PH2（白/金）各由1,290,000降至951,000韩元（减39万），Hot+Cool HP2（白/金）由1,090,000降至790,000韩元（减30万）。叠加信用卡返现后最优价为855,900与750,500韩元。
冬天PH2的加湿功能更实用，干燥季节一台同时加湿与净化的需求集中，库存走得快。
照明方面，Solarcycle Morph 台灯款720,000降至507,000韩元（减21.3万），落地款960,000降至673,000韩元（减28.7万）。想换桌面照明的，这一档是近期最低。

6. 翻新机与配件
官方认证翻新机最低至62%优惠价，库存售完即提前结束。外观可能有瑕疵，但性能检测与保修与新品一致。新品超预算的型号，可以先看这里。
配件最高71%折扣。刷头或滤网该换的话，本周最便宜。官方把这次称为2026年最后一次配件优惠，年后到明年初难有同样水平。

7. 信用卡优惠怎么算
三星卡10%、上限10万韩元；乐天与韩亚卡10%、上限20万韩元。例如699,000韩元的Airwrap用三星卡支付为629,000韩元；951,000韩元的净化器用乐天卡为855,900韩元。
注意：快捷支付不享受返现。用Kakao Pay或Naver Pay支付会按原价扣款。想拿返现必须走输入卡号的普通支付。
赠品库存售完只发主机；退货时需连同赠品一起退回。

8. 今晚8点直播
11月26日晚8点开播，含美发畅销款折扣、直播限定赠品、返现与抽奖。直播赠品数量有限，多集中在开场。

9. 购买前确认
先看库存：像V16这类热门款在活动期内也会售罄，若已售罄可设提醒，或改看其他无线机型与翻新机。其次确认赠品是否在购物车中。第三确定支付方式，快捷支付没有返现。第四区分翻新与新品：翻新更便宜但外观状态可能不同，送礼选新品、自用选翻新。

一句话总结
戴森最后机会周到11月30日。Airwrap Co-anda 2x 879,000→699,000韩元，Supersonic Nural含盒599,000→449,000韩元，Pencilwash 499,000→299,000韩元，Spot & Scrub Ai 1,690,000→1,070,000韩元。信用卡返现可再减10万至20万韩元，但快捷支付不适用。V16 Piston Animal 已售罄，建议设到货提醒，着急的话改用翻新机或其他型号。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "store": "다이슨 공식몰",
    "priceKrw": 699000,
    "releaseDate": "2026-11-26",
    "rating": 4.9,
    "imageUrl": G1,
    "images": [G1, G2, G3, G4, G5],
    "affiliateUrl": q("다이슨 에어랩 코안다2x"),
    "affiliatePlatform": "Coupang",
    "exampleItems": [
        {"name": "다이슨 에어랩 코안다2x 멀티 스타일러 앤 드라이어", "brand": "Dyson", "priceKrw": 699000, "imageUrl": G1,
         "url": q("다이슨 에어랩 코안다2x"), "category": "879,000→699,000원 · 18만원"},
        {"name": "다이슨 슈퍼소닉 뉴럴 헤어드라이어 + 보관 케이스", "brand": "Dyson", "priceKrw": 449000, "imageUrl": G2,
         "url": q("다이슨 슈퍼소닉 뉴럴"), "category": "599,000→449,000원 · 25%"},
        {"name": "다이슨 V16 피스톤 애니멀 서브마린", "brand": "Dyson", "priceKrw": 1100000, "imageUrl": G3,
         "url": q("다이슨 V16 무선청소기"), "category": "1,490,000→1,100,000원 · 품절"},
        {"name": "다이슨 펜슬백 플러피 콘", "brand": "Dyson", "priceKrw": 619000, "imageUrl": G4,
         "url": q("다이슨 펜슬백"), "category": "799,000→619,000원 · 23%"},
        {"name": "다이슨 펜슬워시 물청소기", "brand": "Dyson", "priceKrw": 299000, "imageUrl": G5,
         "url": q("다이슨 펜슬워시"), "category": "499,000→299,000원 · 40%"},
    ],
    "i18n": {
        "ko": {
            "title": "다이슨 블프 라스트찬스, 30일까지 — 에어랩 699,000원·V16은 이미 품절 (실측)",
            "summary": "11월 30일 마감. 에어랩 코안다2x 879,000→699,000원(파우치 증정), 슈퍼소닉 뉴럴+케이스 599,000→449,000원, 펜슬워시 499,000→299,000원(40%), 스팟앤스크럽 Ai 1,690,000→1,070,000원. 카드 청구할인 계산과 품절 주의점까지 정리했습니다.",
            "description": KO,
            "tasteReview": [
                "기간: 2026.11.23 ~ 11.30, 본체 20~40% / 리퍼브 최대 62% / 액세서리 최대 71%",
                "에어랩 코안다2x 879,000→699,000원(18만원↓, 파우치 증정), 슈퍼소닉 뉴럴+케이스 599,000→449,000원(25%, 스탠드 증정)",
                "펜슬워시 499,000→299,000원(40%, 카드 5만원 캐시백), 스팟앤스크럽 Ai 1,690,000→1,070,000원(62만원↓), V16 1,490,000→1,100,000원은 품절",
                "카드 청구할인 삼성 10% 최대 10만원·롯데/하나 10% 최대 20만원 — 간편결제는 청구할인 불가",
            ],
            "tips": "가격과 기간은 2026년 11월 26일 오후 다이슨 공식몰 블랙프라이데이 페이지에서 확인한 값입니다. 재고·카드사 정책·증정품 소진에 따라 달라질 수 있으니 결제 직전 화면에서 확인하세요. 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있으며, 비교 링크는 쿠팡 검색 결과로 연결됩니다.",
        },
        "en": {
            "title": "Dyson's Last-Chance Week Runs to 30 November — Airwrap at 699,000 Won, the V16 Already Sold Out",
            "summary": "Ends 30 November. Airwrap Co-anda 2x 879,000 to 699,000 with a pouch, Supersonic Nural with case 599,000 to 449,000, Pencilwash 499,000 to 299,000 (40%), Spot & Scrub Ai 1,690,000 to 1,070,000. Card rebate arithmetic and the sold-out models to watch.",
            "description": EN,
            "tasteReview": [
                "Period: 23-30 November, machines 20-40% / refurbished up to 62% / accessories up to 71%",
                "Airwrap Co-anda 2x 879,000 to 699,000 (180,000 off, pouch gift), Supersonic Nural with case 599,000 to 449,000 (25%, stand gift)",
                "Pencilwash 499,000 to 299,000 (40%, 50,000 card cashback), Spot & Scrub Ai 1,690,000 to 1,070,000, V16 1,490,000 to 1,100,000 but sold out",
                "Card rebates: Samsung 10% up to 100,000 won, Lotte/Hana 10% up to 200,000 won — instant-payment wallets do not qualify",
            ],
            "tips": "Prices and dates were read on Dyson's Black Friday page on the afternoon of 26 November 2026. Stock, card policies and gift availability can change; confirm on the payment screen. This post contains affiliate links and may earn a commission; comparison links open Coupang search results.",
        },
        "ja": {
            "title": "ダイソン ラストチャンスウィークは30日まで — エアラップ699,000ウォン・V16はすでに品切れ（実測）",
            "summary": "11月30日終了。エアラップ コアンダ2x 879,000→699,000ウォン（ポーチ付き）、スーパーソニック ニューラル＋ケース599,000→449,000ウォン、ペンシルウォッシュ499,000→299,000ウォン（40%）、スポット＆スクラブAi 1,690,000→1,070,000ウォン。カード請求割引の計算と品切れ注意点まで整理しました。",
            "description": JA,
            "tasteReview": [
                "期間：2026.11.23〜11.30、本体20〜40%／リファービッシュ最大62%／アクセサリー最大71%",
                "エアラップ コアンダ2x 879,000→699,000ウォン（18万引き・ポーチ付き）、スーパーソニック ニューラル＋ケース599,000→449,000ウォン（25%・スタンド付き）",
                "ペンシルウォッシュ499,000→299,000ウォン（40%・カード5万ウォンCB）、スポット＆スクラブAi 1,690,000→1,070,000ウォン、V16 1,490,000→1,100,000ウォンは品切れ",
                "カード請求割引はサムスン10%最大10万ウォン・ロッテ／ハナ10%最大20万ウォン — 簡易決済は対象外",
            ],
            "tips": "価格と期間は2026年11月26日午後にダイソン公式ストアのブラックフライデーページで確認した値です。在庫・カード会社の政策・ノベルティの消化により変わるため決済直前に確認してください。本記事はアフィリエイトリンクを含み手数料を受け取る場合があります。比較リンクはCoupang検索結果に移動します。",
        },
        "zh": {
            "title": "戴森最后机会周到30日——Airwrap 699,000韩元，V16已售罄（实价）",
            "summary": "11月30日结束。Airwrap Co-anda 2x 879,000→699,000韩元（赠收纳包），Supersonic Nural含盒599,000→449,000韩元，Pencilwash 499,000→299,000韩元（40%），Spot & Scrub Ai 1,690,000→1,070,000韩元。含信用卡返现算法与售罄提醒。",
            "description": ZH,
            "tasteReview": [
                "期间：2026.11.23～11.30，整机20～40%／翻新机最高62%／配件最高71%",
                "Airwrap Co-anda 2x 879,000→699,000韩元（减18万，赠包）、Supersonic Nural含盒599,000→449,000韩元（25%，赠支架）",
                "Pencilwash 499,000→299,000韩元（40%，卡返5万）、Spot & Scrub Ai 1,690,000→1,070,000韩元、V16 1,490,000→1,100,000韩元已售罄",
                "信用卡返现：三星10%上限10万韩元、乐天与韩亚10%上限20万韩元——快捷支付不适用",
            ],
            "tips": "价格与期间为2026年11月26日下午在戴森官方商城黑五页面确认的数值。库存、卡组织政策与赠品数量会变化，请在结算前确认。本文含联盟链接，可能获得佣金；比价链接跳转至Coupang搜索结果。",
        },
    },
}

if __name__ == "__main__":
    publish(POST)
