#!/usr/bin/env python3
"""트랙2 — 2026 블프 막차: 11/29(일) 쿠팡 가전 vs 11/30(월) 삼성닷컴·LGE.COM (4개국어).

실측 (2026-11-28 08:30~08:45 KST, 삼성닷컴·LGE.COM 화면에서 직접 읽은 값)
 - 삼성 갤럭시 북6 프로 16형(40.6cm) Ultra 5 / 512GB, NT960XJG-KC51G: 최대 혜택가 2,892,300원 (카드 7% 반영)
 - LG 그램 Pro AI 2026 16Z95U-GS5WK (40.6cm, 라이젠 AI 5): 최대혜택가 2,334,300원
 - 삼성 2026 Neo QLED QNH70 85형(214cm) KQ85QNH70AFXKR: 최대 혜택가 2,501,700원 (쿠폰 적용 예상가+카드 반영, 21%)
 - LG 올레드 AI (스탠드형) B6 77형(194cm) OLED77B6BNA: 최대혜택가 3,461,900원
 - LG 트롬 오브제컬렉션 워시타워 25/21kg WL2521EGNR: 3,000,000 → 최대혜택가 2,538,900원 (30%)
 - LG 디오스 AI 오브제컬렉션 냉장고(매직스페이스) 870L T876MEE1H1: 2,490,000 → 최대혜택가 2,129,700원 (19%)
 - LG 코드제로 오브제컬렉션 A9 AX920BWE: 740,000 → 최대혜택가 641,700원 (37%)
 기간: 쿠팡 가전·디지털 블프 11/16~11/29(쿠팡 뉴스룸 11/15), 삼성위크 4회차 '블랙 프라이데이 라스트 위크'
   11/23~11/30(삼성닷컴 카운트다운), LGE.COM '블랙프라이데이 with 코리아 그랜드 페스티벌' 10/29~11/30
   (타임딜 D-2 표기), 쿠팡 로켓직구 '쿠블프' 11/23~12/1, 롯데하이마트 블프 ~11/30(보도 기준)
 - 이미지: 삼성닷컴·LGE.COM 공식 제품컷 7장 → 900×1200 JPEG, AI 생성 0장
"""
from brand_bf_common import publish, q

SLUG = "black-friday-final-weekend-samsung-lg-coupang-2026-11-30"
G1 = "/images/products/sb-book6pro.jpg"
G2 = "/images/products/lg-grampro16.jpg"
G3 = "/images/products/sb-neoqled-qnh70.jpg"
G4 = "/images/products/lg-oled77b6.jpg"
G5 = "/images/products/lg-washtower.jpg"
G6 = "/images/products/lg-fridge870.jpg"
G7 = "/images/products/lg-cordzero-a9.jpg"

KO = """블랙프라이데이가 끝났다고 세일이 끝난 게 아니다. 국내 대형 세일은 이번 주말과 월요일에 걸쳐 닫힌다. 쿠팡 가전·디지털 블랙프라이데이는 11월 29일(일), 삼성닷컴의 '블랙 프라이데이 라스트 위크'와 LG전자 공식몰(LGE.COM) 행사는 11월 30일(월)에 끝난다. 11월 28일(토) 오전에 삼성닷컴과 LGE.COM 화면에서 직접 읽은 30만 원 이상 제품 가격을 정리했다.

1. 마감 시각부터 정리
쿠팡 가전·디지털 블랙프라이데이는 11월 16일 시작해 11월 29일(일)에 끝난다. 삼성닷컴은 11월 1일부터 진행한 '삼성위크'의 4회차로 11월 23일부터 30일까지 '블랙 프라이데이 라스트 위크'를 운영 중이고, 행사 페이지에는 회차 종료까지 남은 시간이 실시간으로 표시된다. LG전자 공식몰은 10월 29일부터 11월 30일까지 '블랙프라이데이 with 코리아 그랜드 페스티벌'을 열고 있고, 타임딜 상품에는 'D-2'가 붙어 있다. 로켓직구 '쿠블프'는 11월 23일부터 12월 1일(화)까지다. 롯데하이마트 블프도 보도 기준 11월 30일까지다.
정리하면 이렇다. 국내 배송 가전·IT를 노린다면 11월 29일(일)이 쿠팡의 마지막 날이고, 삼성·LG 공식몰과 하이마트는 하루 더 남아 11월 30일(월) 자정에 닫힌다. 해외 직구는 12월 1일(화)까지다.
한 가지 주의할 점. 각 사가 표시하는 가격은 '즉시 할인가'가 아니라 쿠폰과 카드 결제 혜택을 모두 반영한 '최대 혜택가'인 경우가 많다. 아래 가격은 화면에 표시된 최대 혜택가 기준이며, 결제 카드와 쿠폰 적용 여부에 따라 실제 청구액이 달라진다.

2. 노트북 — 삼성 갤럭시 북6 프로 vs LG 그램 Pro
삼성 갤럭시 북6 프로 16형(40.6cm, 코어 울트라 5 338H, 512GB, 모델명 NT960XJG-KC51G)은 삼성닷컴에서 최대 혜택가 2,892,300원에 올라 있다. 카드사 결제 혜택 7%가 반영된 가격이다. 같은 시리즈 35.6cm 모델은 2,752,800원이다.
LG 그램 Pro AI 2026(40.6cm, AMD 라이젠 AI 5, 모델명 16Z95U-GS5WK)은 LGE.COM에서 최대혜택가 2,334,300원이다.
같은 16형이라도 프로세서가 다르다. 삼성은 인텔 코어 울트라 5, LG는 AMD 라이젠 AI 5다. 두 회사 모두 코파일럿+ PC로 분류하고, 무게와 배터리 사용 시간은 모델별로 다시 확인해야 한다. 표시가만 보면 LG가 55만 원가량 싸다. 다만 삼성은 카드 7% 할인과 삼성닷컴 쿠폰, LG는 앱 전용 쿠폰팩(구매 금액 구간별)이 각각 붙는 구조라, 실제 청구액은 결제 수단에 따라 달라진다.

3. TV — 삼성 Neo QLED 85형 vs LG 올레드 77형
삼성 2026 Neo QLED QNH70 85형(214cm, KQ85QNH70AFXKR)은 최대 혜택가 2,501,700원이다. 표시 기준 21% 할인이고, 쿠폰 적용 예상가에 카드 혜택이 더해진 값이다. 같은 화면에서 2026 Mini LED MH75 85형(사운드바 포함)은 1,804,200원(39%), 2025 QLED QF6A 85형은 1,890,000원(40%)으로 나왔다. QF6A는 재입고 알림 신청 상태였다.
LG 올레드 AI B6 77형(194cm, OLED77B6BNA)은 최대혜택가 3,461,900원이다. 같은 행사에 LG QNED AI 75형(189cm)이 1,422,900원, 65형이 1,097,400원으로 올라 있다.
여기서 주의할 것. 삼성 85형 Neo QLED와 LG 77형 올레드는 화면 크기도, 패널 방식도 다르다. 가격만으로 우열을 가릴 수 없다. 어두운 방에서 명암비와 시야각을 중시하면 올레드, 밝은 거실에서 밝기와 번인 걱정 없는 장시간 시청을 중시하면 미니 LED·Neo QLED가 맞다. 같은 크기로 비교하려면 LG 83형 올레드나 삼성 77형 라인업 가격을 따로 확인해야 한다.

4. 생활가전 — 마감 임박한 LG 쪽 할인 폭
LG 트롬 오브제컬렉션 워시타워 25/21kg(WL2521EGNR)은 표시가 3,000,000원에서 최대혜택가 2,538,900원으로 내려왔다. 30% 할인이다. 세탁기와 건조기를 한 몸체에 올린 모델로, 설치 공간과 배수·전원 조건을 먼저 확인해야 한다.
LG 디오스 AI 오브제컬렉션 냉장고(매직스페이스) 870L(T876MEE1H1)은 2,490,000원에서 2,129,700원(19%)이다. 1등급 모델이고, '닷컴 ONLY' 표기가 붙어 있다.
무선청소기 LG 코드제로 오브제컬렉션 A9(AX920BWE, 흡입 전용)은 740,000원에서 641,700원으로 37% 내려 할인 폭이 가장 크다. 100만 원 이하 제품 중에서는 이번 행사에서 가장 눈에 띄는 숫자다.
대형가전은 가격보다 일정이 문제다. 연말에는 설치 물량이 몰려 배송·설치일이 밀린다. 11월 30일 주문이 12월 중순 설치로 이어질 수 있으니, 이사나 입주 날짜가 정해져 있다면 주문 전에 설치 가능일을 먼저 확인해야 한다.

5. 쿠폰·카드 구조를 알아야 실제 금액이 보인다
LG전자 공식몰은 앱 전용 쿠폰팩을 준다. 구매 금액 50만 원 이상 5만 원, 100만 원 이상 10만 원, 150만 원 이상 15만 원, 200만 원 이상 20만 원, 250만 원 이상 23만 원, 300만 원 이상 27만 원이다. 6장을 다 쓰는 게 아니라, 한 번의 결제 금액 구간에 해당하는 쿠폰 1장을 쓰는 구조다. 쿠폰은 앱에서만 쓸 수 있고 11월 30일에 소멸한다.
삼성닷컴은 50만 원 이상 결제 시 삼성·KB국민·롯데카드 7% 결제일 할인이 11월 30일까지 이어진다. 삼성카드로 300만·500만·700만·1,000만 원 이상 결제하면 10만·20만·30만·50만 원 캐시백도 붙는다. 다만 삼성카드 추가 3%(최대 10%)는 11월 24일에 이미 끝났다. 무이자 할부는 100만 원 이상 12개월, 200만 원 이상 24개월이다.
중요한 건 '결제일 할인'의 성격이다. 카드 결제일 할인은 결제 화면 금액이 아니라 다음 카드 청구서에서 깎인다. 주문 화면에 표시된 금액이 그대로 청구됐다고 착각하지 말아야 한다. 또 카드사 예산이 소진되면 행사 기간 중이라도 조기 종료될 수 있다고 각 사가 명시하고 있다.

6. 사기 전에 확인할 다섯 가지
첫째, 같은 이름이라도 모델명 끝자리가 다른 유통 전용 모델이 있다. 노트북·TV·냉장고 모두 모델명으로 비교해야 한다. 둘째, '최대 혜택가'는 카드·쿠폰·구독 조건을 모두 채웠을 때의 금액이다. 내 카드로 결제했을 때의 청구액을 장바구니에서 확인해야 한다. 셋째, 쿠팡 가전 블프는 11월 29일에 끝나지만 개별 특가는 그 전에 품절될 수 있다. 넷째, 대형가전은 설치비·폐가전 수거 여부와 사다리차 비용을 따로 봐야 한다. 다섯째, 구매 취소 시 받은 포인트·캐시백은 반납해야 한다.
이번 주말에 살 게 정해져 있다면 순서는 이렇다. 쿠팡에서 최저가를 먼저 확인하고(11월 29일 마감), 삼성·LG 공식몰의 카드·쿠폰 조건과 비교해 청구액이 더 낮은 쪽을 고른다(11월 30일 마감). 두 곳 모두 예산 소진 시 조기 종료를 명시하고 있으니, 조건이 맞으면 마지막 날까지 미루기보다 오늘 결제하는 편이 안전하다.

한 줄 정리
쿠팡 가전·디지털 블프는 11월 29일(일), 삼성닷컴 '블랙 프라이데이 라스트 위크'와 LG전자 공식몰은 11월 30일(월)에 끝난다. 11월 28일 오전 실측 기준 갤럭시 북6 프로 16형 2,892,300원, 그램 Pro AI 2026 2,334,300원, Neo QLED QNH70 85형 2,501,700원, 올레드 77B6 3,461,900원, LG 워시타워 2,538,900원(-30%), 코드제로 A9 641,700원(-37%)이다. 표시가는 모두 카드·쿠폰 반영 최대 혜택가이므로 청구액은 결제 수단으로 다시 확인해야 한다."""

EN = """Black Friday is over, but the Korean sales are not. The big domestic promotions close across this weekend and Monday. Coupang's appliance and digital Black Friday ends on Sunday, 29 November. Samsung.com's Black Friday Last Week and LG's official store, LGE.COM, both end on Monday, 30 November. Here are prices for products above 300,000 won, read directly from the Samsung and LG store pages on the morning of Saturday, 28 November.

1. Deadlines first
Coupang's appliance and digital event runs from 16 November to 29 November. Samsung.com is running the fourth round of Samsung Week, the Black Friday Last Week, from 23 to 30 November, with a live countdown on the event page. LGE.COM has run Black Friday with the Korea Grand Festival since 29 October and closes on 30 November; its time deals show D-2. Coupang's Rocket Direct import event, Kubleop, runs to 1 December. Lotte Hi-Mart's promotion also ends 30 November, according to press reports.
So for a Korean delivery, Sunday is Coupang's last day and Monday is the last day for the Samsung and LG stores. One caveat matters more than the dates: the headline numbers are usually maximum benefit prices, combining coupon values with card billing discounts. What you actually pay depends on your card and whether the coupons apply.

2. Laptops: Galaxy Book6 Pro vs LG Gram Pro
The Samsung Galaxy Book6 Pro 16-inch (40.6cm, Core Ultra 5 338H, 512GB, model NT960XJG-KC51G) shows a maximum benefit price of 2,892,300 won, including a 7% card discount. The 14-inch version is 2,752,800 won.
The LG Gram Pro AI 2026 (40.6cm, AMD Ryzen AI 5, model 16Z95U-GS5WK) shows 2,334,300 won on LGE.COM.
Same screen size, different processors: Intel Core Ultra 5 against AMD Ryzen AI 5. Both are marketed as Copilot+ PCs. On the displayed price LG is about 550,000 won cheaper, but Samsung stacks a 7% card discount and store coupons while LG uses an app-only coupon pack tied to the order value, so the final bill depends on how you pay.

3. TVs: Samsung Neo QLED 85-inch vs LG OLED 77-inch
The 2026 Samsung Neo QLED QNH70 85-inch (214cm, KQ85QNH70AFXKR) shows 2,501,700 won, a 21% discount that includes an estimated coupon value plus card benefits. On the same page the 2026 Mini LED MH75 85-inch with a soundbar is 1,804,200 won (39%) and the 2025 QLED QF6A 85-inch is 1,890,000 won (40%), the latter awaiting restock.
The LG OLED AI B6 77-inch (194cm, OLED77B6BNA) is 3,461,900 won. LG's QNED AI 75-inch is 1,422,900 won and the 65-inch 1,097,400 won.
These are not equivalent products. Different sizes, different panel technology. For contrast and viewing angles in a dark room OLED wins; for a bright living room and long sessions without burn-in worry, mini LED and Neo QLED are the safer pick. Comparing like for like means checking LG's 83-inch OLED or Samsung's 77-inch line-up separately.

4. Appliances: the deepest cuts are on LG
The LG Tromm Objet Collection Wash Tower 25/21kg (WL2521EGNR) drops from 3,000,000 won to 2,538,900 won, a 30% cut. It stacks a washer and dryer in one body, so measure the space and check drainage and power first.
The LG Dios AI Objet Collection refrigerator with Magic Space, 870L (T876MEE1H1), falls from 2,490,000 to 2,129,700 won (19%). It is a first-grade efficiency model marked online-only.
The LG CordZero Objet Collection A9 stick vacuum (AX920BWE) falls from 740,000 to 641,700 won, 37% off and the largest percentage cut in this group.
Delivery timing matters more than price for large appliances. Year-end installation queues are long, and an order on 30 November can land in mid-December. If you have a move-in date, confirm the installation slot before paying.

5. How the coupons and cards actually work
LGE.COM gives an app-only coupon pack by order value: 50,000 won off above 500,000, 100,000 above 1,000,000, 150,000 above 1,500,000, 200,000 above 2,000,000, 230,000 above 2,500,000 and 270,000 above 3,000,000. You use one coupon per order, not all six, and they expire on 30 November.
Samsung.com keeps a 7% statement discount for Samsung, KB Kookmin and Lotte cards on purchases above 500,000 won through 30 November, plus cashback of 100,000 to 500,000 won for Samsung card spending of 3 to 10 million won. The extra 3% Samsung card discount ended on 24 November. Interest-free instalments run 12 months above 1,000,000 won and 24 months above 2,000,000 won.
Remember that a statement discount is not a checkout discount: it appears on your card bill, not on the order screen. Both companies also state that card budgets can run out and end the benefit early.

6. Five checks before you pay
Compare by model number, because retailers carry derivatives with different suffixes. Confirm your own card's final bill in the cart rather than trusting the headline price. On Coupang, individual deals can sell out before Sunday. For large appliances, check installation fees, haul-away and ladder charges. And if you cancel, points and cashback must be returned.
The practical order for this weekend: check Coupang first (closes Sunday), then compare the Samsung and LG store card and coupon terms and take whichever bill is lower (closes Monday). Both state that benefits can end early when budgets run out, so if the terms fit, paying today is safer than waiting for the last hour.

One line
Coupang's appliance Black Friday ends Sunday 29 November; Samsung.com's Black Friday Last Week and LGE.COM end Monday 30 November. Measured on the morning of 28 November: Galaxy Book6 Pro 16-inch 2,892,300 won, Gram Pro AI 2026 2,334,300 won, Neo QLED QNH70 85-inch 2,501,700 won, OLED 77B6 3,461,900 won, LG Wash Tower 2,538,900 won (-30%) and CordZero A9 641,700 won (-37%). All are maximum benefit prices, so check your own card's bill."""

JA = """ブラックフライデーが終わっても、韓国の大型セールはまだ閉まっていない。クーパン（Coupang）の家電・デジタル・ブラックフライデーは11月29日（日）、サムスンドットコムの「ブラックフライデー・ラストウィーク」とLG電子公式モール（LGE.COM）は11月30日（月）に終了する。11月28日（土）午前、両社の商品ページで直接確認した30万ウォン以上の価格をまとめた。

1. まず締切
クーパンの家電・デジタル・ブラックフライデーは11月16日から29日まで。サムスンドットコムは11月1日開始の「サムスンウィーク」第4弾として11月23日から30日まで「ブラックフライデー・ラストウィーク」を開催し、ページには残り時間が表示されている。LGE.COMは10月29日から11月30日まで「ブラックフライデー with コリア・グランド・フェスティバル」を実施中で、タイムセールには「D-2」が付く。クーパンのロケット直購「クブルプ」は12月1日（火）まで。
つまり韓国国内配送は日曜がクーパンの最終日、月曜がサムスン・LG公式モールの最終日だ。ただし表示価格はクーポンとカード決済特典を合算した「最大特典価」であることが多い。実際の請求額はカードとクーポン次第で変わる。

2. ノートPC — Galaxy Book6 Pro と LG gram Pro
サムスン Galaxy Book6 Pro 16型（40.6cm、Core Ultra 5 338H、512GB、型番 NT960XJG-KC51G）は最大特典価2,892,300ウォン（カード7%反映）。14型は2,752,800ウォン。
LG gram Pro AI 2026（40.6cm、AMD Ryzen AI 5、型番 16Z95U-GS5WK）はLGE.COMで2,334,300ウォン。
同じ16型でもCPUが違う。インテル Core Ultra 5 と AMD Ryzen AI 5 で、双方ともCopilot+ PCを名乗る。表示価格ではLGが約55万ウォン安いが、サムスンはカード7%とストアクーポン、LGはアプリ専用クーポン（購入額別）という構造の違いがあり、支払い方法で請求額が変わる。

3. TV — Samsung Neo QLED 85型 と LG OLED 77型
サムスン 2026 Neo QLED QNH70 85型（214cm、KQ85QNH70AFXKR）は2,501,700ウォン（21%、クーポン適用予想価＋カード特典）。同じ画面で2026 Mini LED MH75 85型（サウンドバー付き）は1,804,200ウォン（39%）、2025 QLED QF6A 85型は1,890,000ウォン（40%、入荷待ち）。
LG OLED AI B6 77型（194cm、OLED77B6BNA）は3,461,900ウォン。LG QNED AI 75型は1,422,900ウォン、65型は1,097,400ウォン。
サイズもパネル方式も違うので価格だけで優劣は決められない。暗い部屋でコントラストと視野角を重視するならOLED、明るいリビングで焼き付きを気にせず長時間見るならミニLED・Neo QLEDが向く。同サイズで比べるならLG 83型OLEDやサムスン77型を別途確認する必要がある。

4. 生活家電 — 値下げ幅が大きいのはLG
LG Tromm Objet Collection ウォッシュタワー 25/21kg（WL2521EGNR）は3,000,000ウォンから2,538,900ウォンへ30%下落。洗濯機と乾燥機が一体型なので、設置スペースと排水・電源を先に確認したい。
LG Dios AI Objet Collection 冷蔵庫（マジックスペース）870L（T876MEE1H1）は2,490,000ウォンから2,129,700ウォン（19%）。1等級で「オンライン限定」表記。
LG CordZero Objet Collection A9（AX920BWE、吸引専用）は740,000ウォンから641,700ウォンで37%減。今回のなかで下落率が最も大きい。
大型家電は価格より日程だ。年末は設置が混み、11月30日の注文が12月中旬の設置になることがある。引越しや入居日が決まっているなら、支払い前に設置可能日を確認すべきだ。

5. クーポンとカードの仕組み
LGE.COMはアプリ専用クーポンを購入額別に配る。50万ウォン以上5万、100万以上10万、150万以上15万、200万以上20万、250万以上23万、300万以上27万ウォン。6枚すべてではなく1回の注文に1枚で、11月30日で消滅する。
サムスンドットコムは50万ウォン以上の決済でサムスン・KB国民・ロッテカードの7%請求割引が11月30日まで。サムスンカードで300万〜1,000万ウォン決済なら10万〜50万ウォンのキャッシュバック。ただしサムスンカード追加3%（最大10%）は11月24日に終了した。無利子分割は100万ウォン以上12ヶ月、200万ウォン以上24ヶ月。
「請求割引」は注文画面ではなくカード請求時に引かれる。画面の金額がそのまま請求されるわけではない。カード予算が尽きると早期終了もあると各社が明記している。

6. 支払い前の確認5つ
型番の末尾が違う流通専用モデルに注意。自分のカードでの請求額をカートで確認。クーパンの個別特価は日曜より前に売り切れることがある。大型家電は設置費・廃家電回収・梯子車費用を確認。キャンセル時はポイントとキャッシュバックの返還が必要だ。
今週末の実務的な順序は、まずクーパンで最安を確認し（日曜締切）、次にサムスン・LG公式モールのカードとクーポン条件を比べて請求額が低い方を選ぶ（月曜締切）。両社とも予算枯渇による早期終了を明記しているので、条件が合えば最終日まで待たず今日払う方が安全だ。

一行まとめ
クーパンの家電ブラックフライデーは11月29日（日）、サムスンドットコムのラストウィークとLGE.COMは11月30日（月）まで。28日午前の実測ではGalaxy Book6 Pro 16型2,892,300ウォン、gram Pro AI 2026 2,334,300ウォン、Neo QLED QNH70 85型2,501,700ウォン、OLED 77B6 3,461,900ウォン、LGウォッシュタワー2,538,900ウォン（-30%）、CordZero A9 641,700ウォン（-37%）。いずれも最大特典価なので、請求額は支払い方法で再確認を。"""

ZH = """黑色星期五结束了，但韩国的大型促销并没有结束。酷澎（Coupang）家电与数码黑色星期五在11月29日（周日）结束，三星官网的"黑色星期五最后一周"和LG电子官方商城（LGE.COM）在11月30日（周一）结束。以下是11月28日（周六）上午在三星期与LG商城页面直接查到的30万韩元以上产品价格。

1. 先看截止时间
酷澎家电与数码黑色星期五为11月16日至29日。三星官网自11月1日开始的"三星周"第四轮即"黑色星期五最后一周"，时间为11月23日至30日，页面显示实时倒计时。LGE.COM自10月29日起举办"黑色星期五×韩国大庆典"，至11月30日结束，限时特价标有"D-2"。酷澎火箭直购"쿠블프"至12月1日（周二）。乐天Hi-Mart促销据媒体报道也到11月30日。
也就是说，韩国国内配送：周日是酷澎的最后一天，周一是三星与LG官方商城的最后一天。但要注意，页面显示价多为"最大优惠价"，即优惠券与信用卡结算优惠合计后的价格，实际支付额取决于卡种和券的适用情况。

2. 笔记本：三星Galaxy Book6 Pro 与 LG gram Pro
三星Galaxy Book6 Pro 16英寸（40.6cm，Core Ultra 5 338H，512GB，型号NT960XJG-KC51G）最大优惠价2,892,300韩元（含信用卡7%优惠）。14英寸为2,752,800韩元。
LG gram Pro AI 2026（40.6cm，AMD Ryzen AI 5，型号16Z95U-GS5WK）在LGE.COM为2,334,300韩元。
同样16英寸，处理器不同：英特尔Core Ultra 5对AMD Ryzen AI 5，两者都标称Copilot+ PC。按标价LG便宜约55万韩元，但三星叠加信用卡7%与商城券，LG为按金额区间发放的应用专用券，最终账单随支付方式变化。

3. 电视：三星Neo QLED 85英寸 与 LG OLED 77英寸
三星2026 Neo QLED QNH70 85英寸（214cm，KQ85QNH70AFXKR）为2,501,700韩元（21%，含券预估与卡优惠）。同页面2026 Mini LED MH75 85英寸含回音壁为1,804,200韩元（39%），2025 QLED QF6A 85英寸为1,890,000韩元（40%，需等补货）。
LG OLED AI B6 77英寸（194cm，OLED77B6BNA）为3,461,900韩元。LG QNED AI 75英寸为1,422,900韩元，65英寸为1,097,400韩元。
尺寸与面板类型都不同，不能只比价格。暗房间看重对比度与视角选OLED；明亮客厅长时间观看、担心烧屏则选Mini LED与Neo QLED。要同尺寸比较，需另查LG 83英寸OLED或三星77英寸产品线。

4. 生活家电：LG降幅最大
LG Tromm Objet Collection洗烘塔25/21kg（WL2521EGNR）从3,000,000韩元降至2,538,900韩元，降幅30%。洗衣与烘干一体，需先确认安装空间、排水与电源。
LG Dios AI Objet Collection冰箱（Magic Space）870L（T876MEE1H1）从2,490,000降至2,129,700韩元（19%），一级能效，标注线上专供。
LG CordZero Objet Collection A9（AX920BWE，纯吸尘）从740,000降至641,700韩元，降37%，是本组降幅最大的。
大型家电的关键是日程而非价格。年末安装排期紧张，11月30日下单可能12月中旬才安装。若已定搬家或入住日期，付款前应先确认可安装日期。

5. 优惠券与信用卡的真实规则
LGE.COM按订单金额发放应用专用券：满50万减5万、满100万减10万、满150万减15万、满200万减20万、满250万减23万、满300万减27万。一次订单只能用一张，11月30日失效。
三星官网满50万韩元使用三星、KB国民、乐天卡可享7%账单折扣至11月30日；三星卡消费300万至1,000万韩元另有10万至50万韩元返现。三星卡额外3%（最高10%）已于11月24日结束。免息分期为满100万12个月、满200万24个月。
注意账单折扣不在结算页面显示，而是在信用卡账单中扣减。两家都注明卡预算耗尽可能提前结束活动。

6. 付款前的五项确认
确认型号后缀，流通渠道常有衍生型号；在购物车确认自己卡的真实账单；酷澎个别特价可能在周日之前售罄；大型家电需核对安装费、旧机回收与吊装费；取消订单须退还积分与返现。
周末的实务顺序：先在酷澎确认最低价（周日截止），再比较三星与LG官方商城的卡与券条件，选账单更低的一方（周一截止）。两家都注明预算耗尽会提前结束，条件合适就今天付款，比等到最后一天更稳妥。

一句话总结
酷澎家电黑色星期五11月29日（周日）截止，三星官网最后一周与LGE.COM 11月30日（周一）截止。28日上午实测：Galaxy Book6 Pro 16英寸2,892,300韩元、gram Pro AI 2026 2,334,300韩元、Neo QLED QNH70 85英寸2,501,700韩元、OLED 77B6 3,461,900韩元、LG洗烘塔2,538,900韩元（-30%）、CordZero A9 641,700韩元（-37%）。均为最大优惠价，实际账单需按支付方式再确认。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "store": "삼성닷컴 · LGE.COM",
    "priceKrw": 2334300,
    "releaseDate": "2026-11-28",
    "rating": 4.7,
    "imageUrl": G1,
    "images": [G1, G2, G3, G4, G5, G6, G7],
    "affiliateUrl": q("갤럭시 북6 프로 16형"),
    "affiliatePlatform": "Coupang",
    "exampleItems": [
        {"name": "삼성 갤럭시 북6 프로 16형 Ultra 5 / 512GB (NT960XJG-KC51G)", "brand": "Samsung", "priceKrw": 2892300, "imageUrl": G1,
         "url": q("갤럭시 북6 프로 16형"), "category": "삼성닷컴 최대 혜택가 2,892,300원 · 카드 7% 반영"},
        {"name": "LG 그램 Pro AI 2026 16Z95U-GS5WK (40.6cm · 라이젠 AI 5)", "brand": "LG", "priceKrw": 2334300, "imageUrl": G2,
         "url": q("LG 그램 프로 2026"), "category": "LGE.COM 최대혜택가 2,334,300원 · 11/30 마감"},
        {"name": "삼성 2026 Neo QLED QNH70 85형 (KQ85QNH70AFXKR)", "brand": "Samsung", "priceKrw": 2501700, "imageUrl": G3,
         "url": q("삼성 Neo QLED QNH70 85"), "category": "삼성닷컴 최대 혜택가 2,501,700원 · 21%"},
        {"name": "LG 올레드 AI B6 77형 (OLED77B6BNA)", "brand": "LG", "priceKrw": 3461900, "imageUrl": G4,
         "url": q("LG 올레드 77 B6"), "category": "LGE.COM 최대혜택가 3,461,900원 · 11/30 마감"},
        {"name": "LG 트롬 오브제컬렉션 워시타워 25/21kg (WL2521EGNR)", "brand": "LG", "priceKrw": 2538900, "imageUrl": G5,
         "url": q("LG 워시타워 25 21"), "category": "3,000,000 → 2,538,900원 · 30%"},
        {"name": "LG 디오스 AI 오브제컬렉션 냉장고 870L (T876MEE1H1)", "brand": "LG", "priceKrw": 2129700, "imageUrl": G6,
         "url": q("LG 디오스 냉장고 870L"), "category": "2,490,000 → 2,129,700원 · 19%"},
        {"name": "LG 코드제로 오브제컬렉션 A9 (AX920BWE)", "brand": "LG", "priceKrw": 641700, "imageUrl": G7,
         "url": q("LG 코드제로 A9 AX920"), "category": "740,000 → 641,700원 · 37%"},
    ],
    "i18n": {
        "ko": {
            "title": "블프 막차 — 쿠팡은 29일, 삼성·LG 공식몰은 30일 마감… 30만원+ 실측가 7종",
            "summary": "쿠팡 가전·디지털 블프는 11/29(일), 삼성닷컴 '블랙 프라이데이 라스트 위크'와 LGE.COM은 11/30(월) 마감이다. 11/28 오전 공식몰에서 직접 읽은 값: 갤럭시 북6 프로 16형 2,892,300원, 그램 Pro AI 2026 2,334,300원, Neo QLED QNH70 85형 2,501,700원, 올레드 77B6 3,461,900원, LG 워시타워 2,538,900원(30%↓), 코드제로 A9 641,700원(37%↓). 카드·쿠폰 구조와 청구액 주의점까지 정리했습니다.",
            "description": KO,
            "tasteReview": [
                "마감: 쿠팡 가전·디지털 블프 11/16~11/29 · 삼성위크 4회차 11/23~11/30 · LGE.COM 10/29~11/30 · 쿠팡 쿠블프 11/23~12/1",
                "노트북: 갤럭시 북6 프로 16형 Ultra5/512GB 2,892,300원(카드 7%) vs 그램 Pro AI 2026 16Z95U-GS5WK 2,334,300원",
                "TV: Neo QLED QNH70 85형 2,501,700원(21%) vs 올레드 B6 77형 3,461,900원 — 크기·패널이 달라 단순 비교 불가",
                "생활가전: LG 워시타워 3,000,000→2,538,900원(30%) · 디오스 냉장고 870L 2,490,000→2,129,700원(19%) · 코드제로 A9 740,000→641,700원(37%)",
                "쿠폰: LG 앱 6종(50만↑5만 … 300만↑27만, 1주문 1장) / 삼성 7% 결제일 할인(50만↑), 삼성카드 10%는 11/24 종료 · 예산 소진 시 조기 종료 명시",
            ],
            "tips": "가격은 2026년 11월 28일 08:30~08:45 KST에 삼성닷컴·LGE.COM 상품 화면에서 직접 확인한 값이며, 쿠폰·카드 결제 혜택을 반영한 '최대 혜택가'입니다. 실제 청구액은 결제 카드와 쿠폰 적용 여부에 따라 달라지고, 재고·행사 조건은 실시간으로 바뀝니다. 카드 결제일 할인은 주문 화면이 아니라 카드 청구서에서 차감됩니다.",
        },
        "en": {
            "title": "Black Friday Final Weekend: Coupang Ends Sunday, Samsung and LG Stores End Monday — 7 Measured Prices Above 300,000 Won",
            "summary": "Coupang's appliance Black Friday closes on Sunday 29 November; Samsung.com's Black Friday Last Week and LGE.COM close on Monday 30 November. Prices read on the morning of 28 November: Galaxy Book6 Pro 16-inch 2,892,300 won, Gram Pro AI 2026 2,334,300 won, Neo QLED QNH70 85-inch 2,501,700 won, OLED 77B6 3,461,900 won, LG Wash Tower 2,538,900 won (-30%) and CordZero A9 641,700 won (-37%). Includes how the card and coupon stacks work.",
            "description": EN,
            "tasteReview": [
                "Deadlines: Coupang appliances 16-29 November, Samsung Week round 4 23-30 November, LGE.COM 29 October-30 November, Coupang Kubleop to 1 December",
                "Laptops: Galaxy Book6 Pro 16-inch 2,892,300 won versus LG Gram Pro AI 2026 (16Z95U-GS5WK) 2,334,300 won",
                "TVs: Neo QLED QNH70 85-inch 2,501,700 won versus OLED B6 77-inch 3,461,900 won; sizes and panels differ",
                "Appliances: LG Wash Tower 3,000,000 to 2,538,900 (-30%), Dios 870L refrigerator 2,490,000 to 2,129,700 (-19%), CordZero A9 740,000 to 641,700 (-37%)",
                "Coupons: LGE app pack 50,000-270,000 won by order value, one per order; Samsung 7% statement discount above 500,000 won, extra 3% ended 24 November, early end when budgets run out",
            ],
            "tips": "Prices were read from the Samsung.com and LGE.COM product pages between 08:30 and 08:45 KST on 28 November 2026 and are maximum benefit prices that include coupon and card billing benefits. Your actual bill depends on your card and coupon eligibility, and stock and terms change in real time. Statement discounts appear on the card bill, not at checkout.",
        },
        "ja": {
            "title": "ブラックフライデー最終週末 — 쿠팡は29日、サムスン・LG公式モールは30日締切、30万ウォン以上の実測7種",
            "summary": "쿠팡の家電ブラックフライデーは11月29日（日）、サムスンドットコムの「ラストウィーク」とLGE.COMは11月30日（月）まで。28日午前の実測値はGalaxy Book6 Pro 16型2,892,300ウォン、gram Pro AI 2026 2,334,300ウォン、Neo QLED QNH70 85型2,501,700ウォン、OLED 77B6 3,461,900ウォン、LGウォッシュタワー2,538,900ウォン（-30%）、CordZero A9 641,700ウォン（-37%）。カードとクーポンの仕組みも整理。",
            "description": JA,
            "tasteReview": [
                "締切: 쿠팡家電11/16~29、サムスンウィーク第4弾11/23~30、LGE.COM 10/29~11/30、쿠팡クブルプ11/23~12/1",
                "ノートPC: Galaxy Book6 Pro 16型2,892,300ウォン vs gram Pro AI 2026（16Z95U-GS5WK）2,334,300ウォン",
                "TV: Neo QLED QNH70 85型2,501,700ウォン vs OLED B6 77型3,461,900ウォン（サイズ・パネルが異なる）",
                "生活家電: LGウォッシュタワー3,000,000→2,538,900（-30%）、冷蔵庫870L 2,490,000→2,129,700（-19%）、CordZero A9 740,000→641,700（-37%）",
                "クーポン: LGEアプリ6種（50万以上5万〜300万以上27万、1注文1枚）、サムスン7%請求割引（50万以上）、追加3%は11/24終了、予算枯渇で早期終了",
            ],
            "tips": "価格は2026年11月28日08:30〜08:45 KSTにサムスンドットコム・LGE.COMの商品画面で確認した値で、クーポンとカード特典を反映した「最大特典価」です。実際の請求額はカードとクーポン適用で変わり、在庫・条件はリアルタイムに変わります。請求割引は注文画面ではなくカード請求時に反映されます。",
        },
        "zh": {
            "title": "黑色星期五最后周末——쿠팡29日结束，三星与LG官方商城30日结束，30万韩元以上实测7款",
            "summary": "쿠팡家电黑色星期五11月29日（周日）截止，三星官网最后一周与LGE.COM 11月30日（周一）截止。28日上午实测：Galaxy Book6 Pro 16英寸2,892,300韩元、gram Pro AI 2026 2,334,300韩元、Neo QLED QNH70 85英寸2,501,700韩元、OLED 77B6 3,461,900韩元、LG洗烘塔2,538,900韩元（-30%）、CordZero A9 641,700韩元（-37%）。并整理优惠券与信用卡规则。",
            "description": ZH,
            "tasteReview": [
                "截止：쿠팡家电11/16~29、三星周第四轮11/23~30、LGE.COM 10/29~11/30、쿠팡쿠블프11/23~12/1",
                "笔记本：Galaxy Book6 Pro 16英寸2,892,300韩元 vs gram Pro AI 2026（16Z95U-GS5WK）2,334,300韩元",
                "电视：Neo QLED QNH70 85英寸2,501,700韩元 vs OLED B6 77英寸3,461,900韩元（尺寸与面板不同）",
                "生活家电：LG洗烘塔3,000,000→2,538,900（-30%）、冰箱870L 2,490,000→2,129,700（-19%）、CordZero A9 740,000→641,700（-37%）",
                "优惠券：LGE应用6种（满50万减5万至满300万减27万，每单一张）、三星7%账单折扣（满50万）、额外3%已于11/24结束、预算耗尽可提前结束",
            ],
            "tips": "价格为2026年11月28日08:30—08:45 KST在三星期官网与LGE.COM商品页面确认的数值，为含优惠券与信用卡优惠的“最大优惠价”。实际账单取决于卡种与券的适用情况，库存与条件实时变化。账单折扣不在结算页面而在此后信用卡账单中扣减。",
        },
    },
}

if __name__ == "__main__":
    publish(POST)
