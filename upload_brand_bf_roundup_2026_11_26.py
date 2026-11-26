#!/usr/bin/env python3
"""1편 총정리: 브랜드 공식몰 자체 블프 5곳 (4개국어) → Supabase posts + ISR revalidate.

근거 (2026-11-26 12:50~13:40 KST 직접 연 공식몰 화면)
 - 뉴발란스 nbkorea.com/event/blackfridayfw2026_main.action: 2026 BLACK FRIDAY UP TO 80%,
   쿠폰 사용 11/23 10:00~11/28 09:59, 등급쿠폰 VIP20/MANIA15/FAMILY10, 코드 10만↑10%/20만↑20%,
   네이버페이 20만↑ 5,000원(11/21~11/28 09:59). 1080 V15 209,000→159,000, 레벨V5 219,000→149,000,
   UNI RC HEAT 패딩점퍼 299,000→179,000, U471AM 139,000→55,000
 - 크록스 crocs.co.kr: 블랙프라이데이 앵콜 11/25 09:00~11/30 09:00, 최대 70%+2개15%/3개25%,
   바야 라인드 84,900→49,900(41%), 바야 플랫폼 퍼즈 스트랩 라인드 99,900→59,900(40%),
   멜로우 리커버리 79,900→29,900(63%), 11/26 20시 라이브
 - 다이슨 dyson.co.kr/promotions/black-friday-2026: 블프 라스트찬스 위크 11/23~11/30,
   에어랩 코안다2x 879,000→699,000, 슈퍼소닉 뉴럴+케이스 599,000→449,000,
   V16 피스톤 애니멀 1,490,000→1,100,000(품절), 스팟앤스크럽 1,690,000→1,070,000
 - 무신사 musinsa.com/campaign/mujinjangsale: 무진장 26 겨울 11/22 19:00~12/2 24:00, 최대 80%,
   4,781 브랜드·798,610 상품, 누적 판매 3,211,563개
 - 푸마 kr.puma.com: PUMA PRE-BLACK 26.11.12~26.11.26, 슬립캣 부츠 169,000→84,000
 - 나이키 11/17~11/23, 아디다스 11/10~11/20 종료(각 사 공지·보도)
 - 제품 사진: 위 공식몰 제품컷 4장을 3:4(1200×1600)로 정규화. AI 생성 0장.
"""
from brand_bf_common import publish, q

SLUG = "brand-official-blackfriday-2026-roundup-5"

G1 = "/images/products/bfb-nb-1080v15.jpg"
G2 = "/images/products/bfb-crocs-baya-lined.jpg"
G3 = "/images/products/bfb-dyson-airwrap.jpg"
G4 = "/images/products/bfb-musinsa-comfortemp.jpg"

KO = """11월 27일이 블랙프라이데이다. 그런데 국내 브랜드 공식몰에서는 이미 세일이 끝난 곳이 많다. 나이키 공식몰은 11월 17일부터 23일까지, 아디다스는 11월 10일부터 20일까지 블랙프라이데이를 진행하고 문을 닫았다. 미국 블랙프라이데이 날짜만 보고 기다리면 국내 공식몰 할인은 놓친다는 뜻이다.
11월 26일 오후, 뉴발란스·크록스·다이슨·무신사·푸마 공식몰을 직접 열어 지금 실제로 할인이 걸려 있는지 확인했다. 다섯 곳 모두 오늘 기준으로 세일이 살아 있었고, 각 사가 공지한 기간과 대표 상품의 현재 가격을 아래에 정리했다.

1. 한눈에 보는 다섯 곳
뉴발란스 — 11월 23일 10시 ~ 11월 28일 9시 59분 / 최대 80% / 등급쿠폰 VIP 20%·MANIA 15%·FAMILY 10%, 10만 원 이상 10%·20만 원 이상 20% 코드 / 1080 V15 209,000→159,000원
크록스 — 11월 25일 9시 ~ 11월 30일 9시 / 최대 70% / 2개 15%·3개 25% 추가 할인, 지비츠 참 5개 40% / 바야 라인드 클로그 84,900→49,900원
다이슨 — 11월 23일 ~ 11월 30일 / 최대 40%(리퍼브 최대 62%, 액세서리 최대 71%) / 카드 청구할인 삼성 10%·롯데·하나 10%(최대 20만 원) / 에어랩 코안다2x 879,000→699,000원
무신사 무진장 — 11월 22일 19시 ~ 12월 2일 24시 / 최대 80% / 4,781개 브랜드·798,610개 상품, 시그니처특가·72시간특가 / 수아레 헨리넥 니트 59% 24,400원
푸마 — 11월 12일 ~ 11월 26일(오늘 마감) / 프리 블랙 / - / 슬립캣 부츠 169,000→84,000원
다섯 곳 중 오늘이 마지막 날인 곳은 푸마다. 내일 아침에 가장 먼저 닫히는 곳은 뉴발란스다. 11월 28일 오전 9시 59분에 쿠폰 사용이 끝난다.

2. 뉴발란스 — 내일 오전 9시 59분에 끝난다
공식 행사 페이지 첫 화면에 '2026 BLACK FRIDAY, 세일 가격에 추가 프로모션까지, UP TO 80%'가 걸려 있다. 쿠폰 사용 기간은 11월 23일 오전 10시부터 11월 28일 오전 9시 59분까지다. 종료일 밤까지 쓰는 방식이 아니라 28일 아침 9시 59분에 끊긴다는 점을 먼저 기억해야 한다.
혜택은 세 겹이다. 회원 등급별 쿠폰 3매가 자동 발급되고(VIP 20%, MANIA 15%, FAMILY 10%), 세일 상품에는 10만 원 이상 10%, 20만 원 이상 20% 프로모션 코드가 붙는다. 네이버페이로 20만 원 이상 결제하면 5,000원이 즉시 할인된다. 첫 구매 고객과 최근 1년 구매 이력이 없는 고객에게는 15% 쿠폰이 따로 나온다.
오늘 확인한 가격은 이렇다. 1080 V15는 여성 D·남성 2E·4E 모두 209,000원에서 24% 내린 159,000원이다. 베스트 랭킹 1위부터 6위까지를 이 모델이 차지하고 있다. 레벨 V5 남성 2E는 219,000원에서 32% 내린 149,000원, UNI RC HEAT 패딩점퍼는 299,000원에서 40% 내린 179,000원이다. 139,000원짜리 471 라인은 '원데이 특가'로 55,000원까지 내려가 있다. 원데이 특가는 매일 오전 10시에 바뀌고 24시간만 유지된다.

3. 크록스 — 30일 오전 9시까지, 오늘 밤 8시 라이브
'블랙프라이데이 앵콜'이 11월 25일 오전 9시에 열려 11월 30일 오전 9시에 끝난다. 첫 화면에는 지비츠 참 최대 30% 할인과 11월 26일 오후 8시 라이브 방송 안내가 함께 걸려 있다. 라이브에서는 타임특가와 추가 할인, 사은품이 나온다.
추가 할인이 단순하다. 대상 상품을 2개 사면 15%, 3개 이상 사면 25%가 더 빠진다. 여기에 클래식 클로그 같은 기본 모델은 컬러에 따라 가격이 크게 갈린다. 오늘 기준 정가 69,900원인 클래식 클로그는 색상에 따라 54,900원(21%), 49,900원(29%), 29,900원(57%)까지 내려가 있었다. 같은 신발인데 색만 바꿔도 2만 원 이상 차이가 나는 셈이다.
오늘 확인한 대표 가격은 바야 라인드 클로그 84,900원에서 41% 내린 49,900원, 바야 플랫폼 퍼즈 스트랩 라인드 클로그 99,900원에서 40% 내린 59,900원, 언퍼게터블 코지 클로그 84,900원에서 24% 내린 64,900원, 멜로우 리커버리 클로그 79,900원에서 63% 내린 29,900원이다.

4. 다이슨 — 30일까지, 라스트찬스 위크
다이슨은 '블프 라스트찬스 위크'라는 이름으로 11월 23일부터 30일까지 한 주를 더 연다. 첫 화면 문구는 '1년에 단 한 번, 가장 강력한 블프혜택 마지막 기회'다.
오늘 확인한 가격은 NEW 에어랩 코안다2x 멀티 스타일러 앤 드라이어(버건디 우드)가 879,000원에서 18만 원 내린 699,000원, 슈퍼소닉 뉴럴 헤어드라이어와 보관 케이스가 599,000원에서 15만 원 내린 449,000원이다. 두 상품 모두 7만 원 상당의 증정품이 붙는다. 물청소기 펜슬워시는 499,000원에서 20만 원 내린 299,000원, 로봇청소기 스팟앤스크럽 Ai는 1,690,000원에서 62만 원 내린 1,070,000원이다.
가장 강한 무선청소기인 V16 피스톤 애니멀은 1,490,000원에서 39만 원 내린 1,100,000원에 올라와 있는데, 확인 시점에 품절 표시가 붙어 있었다. 카드 청구할인까지 적용하면 최대 혜택가가 990,000원으로 표시된다. 재고가 다시 풀리는지 알림을 걸어두는 편이 낫다.
카드 혜택도 계산에 넣어야 한다. 삼성카드 10%(최대 10만 원), 롯데·하나카드 10%(최대 20만 원) 청구할인이 붙는다. 699,000원짜리 에어랩을 삼성카드로 결제하면 629,000원이 된다. 단, 간편결제로 결제하면 청구할인이 적용되지 않는다.

5. 무신사 무진장 — 12월 2일까지, 오늘 밤 8시·9시 특가
무신사의 '무진장 26 겨울 블랙프라이데이'는 11월 22일 오후 7시에 열려 12월 2일 자정에 끝난다. 4,781개 브랜드, 79만 8,610개 상품이 걸려 있고 최대 80% 할인이다. 오늘 오후 확인한 누적 판매 수량은 3,211,563개, 누적 판매 금액은 1,768억 원, 누적 할인 금액은 1,421억 원이었다. 하루 평균 30억 원어치가 팔리고, 그중 24억 원가량이 할인으로 빠진 셈이다.
브랜드 자체 세일과 다른 점은 시간표다. 매일 오전 10시·11시, 오후 8시·9시에 선착순 한정 수량 특가가 열린다. 오늘 밤 8시와 9시 회차에는 아디다스 슈퍼스타 360 2.0 부츠가 5,990원(94% 할인), 컨트리 II와 캠퍼스 2, 삼바 LT가 9,990원(93%)으로 예고돼 있다. 오전 10시와 오후 7시에는 오픈런 뽑기로 최대 80% 쿠폰과 최대 1만 원 적립금이 나온다.
지금 판매 순위가 높은 시그니처특가 상품은 수아레 데일리 헨리넥 니트(59% 할인 24,400원, 24,609개 판매), 오프메이드 사이드핀턱 와이드 스웨트팬츠(65% 할인 14,950원, 24,607개), 트릴리온 크롭 긴팔티(54% 할인 17,990원, 16,785개), 디미트리블랙 컴포트템프 미드웨이트 패딩(48% 할인 69,900원, 12,503개), 수아레 라이트 시어쉘 패딩 점퍼(61% 할인 65,150원, 9,541개) 순이다.

6. 푸마 — 오늘이 마지막 날
푸마 공식몰은 'PUMA PRE - BLACK'을 11월 12일부터 11월 26일까지 연다. 오늘이 마지막 날이다. 첫 화면에 걸린 슬립캣 부츠는 169,000원에서 50% 내린 84,000원이다. 블랙프라이데이 당일보다 먼저 여는 대신 먼저 닫는 구조라, 내일 푸마를 찾으면 이미 끝나 있을 가능성이 크다.

7. 왜 국내 공식몰은 미국보다 먼저 끝날까
미국 블랙프라이데이는 추수감사절 다음 날인 11월 27일이고, 사이버먼데이는 11월 30일이다. 반면 국내 브랜드 공식몰은 11월 초에서 중순에 세일을 시작해 블프 전에 닫는 경우가 많다. 올해도 뉴발란스가 11월 초에 한 차례, 11월 23일부터 또 한 차례 열었고, 아디다스와 나이키는 20일과 23일에 끝났다. 재고를 시즌 초에 정리하고, 12월 연말 세일과 채널별 행사를 따로 가져가려는 운영 방식으로 보인다.
그래서 '블프는 11월 27일'이라는 달력만 보고 움직이면 국내 공식몰 기준으로는 늦다. 11월 넷째 주에는 브랜드 앱 알림을 켜 두고, 공식몰 행사 페이지를 직접 여는 편이 확실하다.

8. 공식몰과 플랫폼, 어디가 쌀까
같은 모델이라도 채널에 따라 최종 결제가가 다르다. 비교할 때 기준은 세 가지다. 첫째, 상품 정가가 같은지. 공식몰은 권장소비자가, 플랫폼은 판매자 재량가로 표시되므로 정가 자체가 다를 수 있다. 둘째, 쿠폰이 중복되는지. 뉴발란스는 등급쿠폰과 금액별 코드, 네이버페이 즉시할인을 함께 쓰는 구조지만 일부 인기 모델은 쿠폰 대상에서 빠진다. 셋째, 배송과 교환 조건이다. 공식몰은 무료 배송·무료 반품이 기본인 경우가 많고, 사이즈 교환도 자사 물류로 처리된다.
무신사 무진장은 같은 뉴발란스를 브랜드데이로 더 싸게 푸는 경우가 있다. 반대로 공식몰은 컬러와 사이즈가 남아 있고 등급쿠폰이 붙는다. 사려는 모델이 정해져 있다면 두 곳의 장바구니 최종 금액을 나란히 놓고 비교하는 것이 가장 정확하다.

9. 오늘 밤부터 내일 아침까지 순서
오늘 오후 8시, 크록스 라이브와 다이슨 라이브가 동시에 열린다. 라이브 한정 사은품과 타임특가는 수량이 짧다. 오후 8시·9시에는 무신사 선착순 특가(아디다스 5,990원 등)도 열린다. 오늘 안에 푸마 슬립캣 부츠를 살지 결정해야 한다.
내일(27일) 오전에는 뉴발란스가 급하다. 쿠폰 사용이 28일 오전 9시 59분에 끝나므로, 27일 안에 원하는 사이즈를 확보하는 편이 안전하다. 크록스와 다이슨은 30일까지이므로 27~29일에 여유가 있고, 무신사는 12월 2일까지라 가장 늦다. 다만 인기 사이즈와 컬러는 기간이 남아도 먼저 사라진다.

10. 사기 전에 확인할 것
'최대 80%', '최대 70%'는 그 브랜드의 모든 상품이 그 값이라는 뜻이 아니다. 80%는 일부 재고 정리 상품에 붙고, 인기 모델은 20~30% 선에 머문다. 표시된 할인율보다 장바구니 최종 금액을 봐야 하는 이유다.
같은 모델도 컬러와 사이즈에 따라 가격이 다르다. 크록스 클래식 클로그처럼 색상별로 29,900원부터 54,900원까지 갈리는 사례가 대표적이다. 반대로 뉴발란스 1080 V15는 폭(2E·4E·D)만 다르고 가격은 같다.
쿠폰은 중복 조건이 상품마다 다르다. 등급쿠폰과 프로모션 코드, 카드 청구할인, 네이버페이 즉시할인은 서로 겹치지 않는 조합이 있으므로 결제 직전 화면에서 한 번 더 확인해야 한다. 품절도 빠르다. 다이슨 V16은 오늘 이미 품절 표시가 붙었고, 뉴발란스 인기 사이즈(260~280)는 원데이 특가가 시작되는 오전 10시에 가장 먼저 빠진다.

한 줄 정리
국내 브랜드 공식몰 블랙프라이데이는 미국보다 먼저 시작해 먼저 끝난다. 11월 26일 지금 열려 있는 곳은 뉴발란스(28일 09:59 마감), 크록스(30일 09:00), 다이슨(30일), 무신사 무진장(12월 2일), 푸마(오늘 마감) 다섯 곳이다. 오늘 밤에는 크록스·다이슨 라이브와 무신사 8시·9시 특가를, 내일 아침에는 뉴발란스 쿠폰 마감을 먼저 챙기면 된다."""

EN = """Black Friday falls on 27 November this year. Yet in Korea, many brand stores have already finished their sales: Nike Korea ran 17-23 November and adidas Korea ran 10-20 November, then closed. Waiting for the US Black Friday date means missing the Korean official-store discounts entirely.
On the afternoon of 26 November we opened the official stores of New Balance, Crocs, Dyson, Musinsa and PUMA to check whether discounts were actually live. All five were running, and the periods and current prices below are what each site displayed at that time.

1. The five at a glance
New Balance — 23 Nov 10:00 to 28 Nov 09:59 / up to 80% / tier coupons VIP 20%, MANIA 15%, FAMILY 10%, plus promo codes 10% over 100,000 won and 20% over 200,000 won / 1080 V15 209,000 → 159,000 won
Crocs — 25 Nov 09:00 to 30 Nov 09:00 / up to 70% / extra 15% for two pairs, 25% for three or more, 40% on five Jibbitz charms / Baya Lined Clog 84,900 → 49,900 won
Dyson — 23 Nov to 30 Nov / up to 40% (refurbished up to 62%, accessories up to 71%) / card rebates: Samsung 10%, Lotte and Hana 10% up to 200,000 won / Airwrap Co-anda 2x 879,000 → 699,000 won
Musinsa Mujinjang — 22 Nov 19:00 to 2 Dec 24:00 / up to 80% / 4,781 brands and 798,610 products / Suare Henley Knit 59% off at 24,400 won
PUMA — 12 Nov to 26 Nov (final day today) / pre-Black Friday / - / Slipcat Boots 169,000 → 84,000 won
PUMA closes today. New Balance closes first of the rest, at 09:59 on 28 November, when its coupons expire.

2. New Balance — ends 09:59 tomorrow morning
The event page carries "2026 BLACK FRIDAY: up to 80%, plus additional promotions on sale prices". Coupons run from 10:00 on 23 November to 09:59 on 28 November, so the deadline is the morning of the 28th, not the night before.
Three layers of benefit stack. Members receive three tier coupons automatically (VIP 20%, MANIA 15%, FAMILY 10%); sale items take a promo code that gives 10% over 100,000 won or 20% over 200,000 won; and paying 200,000 won or more with Naver Pay takes another 5,000 won off. First-time buyers and customers with no purchase in the past year get a separate 15% coupon.
Prices checked today: the 1080 V15 is 159,000 won, 24% off 209,000, in women's D and men's 2E and 4E widths, and it holds ranks one to six in the store's best-seller list. Level V5 men's 2E is 149,000 won (32% off 219,000), and the UNI RC HEAT padded jumper is 179,000 won (40% off 299,000). The 471 line, listed at 139,000 won, appears at 55,000 won as a one-day special that changes every morning at 10:00 and lasts 24 hours.

3. Crocs — until 09:00 on 30 November, with a live show at 8pm tonight
The Black Friday Encore opened at 09:00 on 25 November and closes at 09:00 on 30 November. The front page also advertises up to 30% off Jibbitz charms and a live broadcast at 8pm on 26 November with time-deal pricing, extra discounts and gifts.
The stacking rule is simple: 15% off when you buy two qualifying pairs, 25% off for three or more. Colour matters as much as the model. The Classic Clog, list price 69,900 won, showed 54,900 won (21% off), 49,900 won (29%) and 29,900 won (57%) depending on colour — a gap of more than 20,000 won between two colours of the same shoe.
Prices seen today: Baya Lined Clog 84,900 → 49,900 (41%), Baya Platform Fuzz Strap Lined Clog 99,900 → 59,900 (40%), Unfurgettable Cozy Clog 84,900 → 64,900 (24%), Mellow Recovery Clog 79,900 → 29,900 (63%).

4. Dyson — last-chance week until 30 November
Dyson added a week under the name "Black Friday Last Chance Week", running 23-30 November, with the line "the strongest Black Friday benefit of the year, one last chance".
Today's prices: the new Airwrap Co-anda 2x Multi-Styler and Dryer in Burgundy Wood is 699,000 won, 180,000 off 879,000, with a gift worth 70,000 won. The Supersonic Nural hair dryer with case is 449,000 won, 150,000 off 599,000, with a stand as a gift. The Pencilwash wet cleaner is 299,000 won, 200,000 off 499,000, and the Spot & Scrub Ai robot vacuum is 1,070,000 won, 620,000 off 1,690,000.
The V16 Piston Animal, Dyson's most powerful cordless vacuum, is listed at 1,100,000 won, 390,000 off 1,490,000 — and showed as sold out when we checked, with a best-case card price of 990,000 won. Setting a restock alert is the sensible move.
Card rebates belong in the arithmetic: Samsung cards give 10% back up to 100,000 won, Lotte and Hana cards 10% up to 200,000 won. Paying 699,000 won for the Airwrap with a Samsung card brings it to 629,000 won, but instant-payment wallets do not qualify for the rebate.

5. Musinsa Mujinjang — until 2 December, with 8pm and 9pm deals tonight
Musinsa's winter Mujinjang Black Friday opened at 19:00 on 22 November and closes at midnight on 2 December, covering 4,781 brands and 798,610 products at up to 80% off. When we checked this afternoon the running totals were 3,211,563 units sold, 176.8 billion won in sales and 142.1 billion won in discounts — roughly 3 billion won a day, a quarter of it given away as discount.
What separates it from a brand sale is the timetable. Limited-quantity flash deals open at 10:00, 11:00, 20:00 and 21:00 every day. Tonight at 20:00 and 21:00 the lineup teases adidas Superstar 360 2.0 boots at 5,990 won (94% off) and Country II, Campus 2 and Samba LT at 9,990 won (93%). At 10:00 and 19:00 an open-run lottery hands out coupons of up to 80% and up to 10,000 won in credit.
The signature deals ranked by units sold: Suare Daily Henley Knit (59% off, 24,400 won, 24,609 sold), Offmade side-pintuck wide sweatpants (65% off, 14,950 won, 24,607), Trillion cropped long-sleeve tee (54% off, 17,990 won, 16,785), Dimitri Black Comfortemp midweight padding (48% off, 69,900 won, 12,503) and Suare Light Sheer Shell padded jumper (61% off, 65,150 won, 9,541).

6. PUMA — today is the last day
PUMA's official store runs "PUMA PRE-BLACK" from 12 to 26 November, and today is the final day. The Slipcat Boots on the front page are 84,000 won, 50% off 169,000. It opens earlier than Black Friday and closes earlier too, so looking for PUMA tomorrow will most likely find the sale gone.

7. Why Korean official stores finish before the US
American Black Friday is 27 November, the day after Thanksgiving, and Cyber Monday is 30 November. Korean brand stores tend to start in early-to-mid November and close before Black Friday itself. This year New Balance ran an early-November round and a second from 23 November; adidas and Nike finished on the 20th and 23rd. The pattern looks like clearing stock at the start of the season and keeping December's year-end sales separate.
So a calendar that says "Black Friday is 27 November" arrives late for Korean official stores. In the fourth week of November, turn on brand app notifications and open the event pages directly.

8. Official store or platform
The same model can settle at different prices depending on the channel. Compare on three points. First, whether the list price is the same: official stores show the recommended retail price while platforms show seller pricing. Second, whether coupons stack: New Balance combines tier coupons, amount-based codes and a Naver Pay discount, but some popular models are excluded. Third, shipping and exchange terms: official stores usually include free delivery and free returns, and handle size exchanges through their own logistics.
Musinsa's Mujinjang sometimes sells the same New Balance shoe cheaper through a brand day, while the official store may still hold your colour and size plus a tier coupon. If you know the model, put the two final cart totals side by side.

9. The order of play from tonight to tomorrow morning
At 8pm tonight the Crocs and Dyson live shows open at the same time; live-only gifts and time deals run out quickly. At 8pm and 9pm Musinsa opens its limited flash deals, adidas at 5,990 won among them. PUMA's Slipcat Boots have to be decided today.
Tomorrow morning New Balance is the urgent one: coupons expire at 09:59 on the 28th, so securing your size during the 27th is safer. Crocs and Dyson run to the 30th, and Musinsa to 2 December — but popular sizes and colours disappear while the clock still has days left.

10. Check before you pay
"Up to 80%" does not mean every item in that brand is 80% off. The top rate sits on clearance stock; popular models stay at 20-30%. That is why the final cart total matters more than the badge.
The same model can differ by colour and size. Crocs' Classic Clog ranges from 29,900 to 54,900 won by colour, while New Balance's 1080 V15 costs the same across widths. Coupon stacking rules differ item by item, so confirm on the payment screen whether the tier coupon, promo code, card rebate and Naver Pay discount actually combine. And stock moves fast: Dyson's V16 was already marked sold out today, and New Balance's popular sizes go first when the one-day deal opens at 10:00.

In one line
Korean brand stores start before the US Black Friday and finish before it. As of 26 November the live ones are New Balance (ends 09:59 on the 28th), Crocs (09:00 on the 30th), Dyson (the 30th), Musinsa Mujinjang (2 December) and PUMA (today). Tonight, take the Crocs and Dyson live shows and Musinsa's 8pm and 9pm deals; tomorrow morning, catch the New Balance coupon deadline."""

JA = """今年のブラックフライデーは11月27日だ。ところが韓国のブランド公式ストアでは、すでにセールが終わっているところが多い。ナイキ公式ストアは11月17日から23日まで、アディダスは11月10日から20日までブラックフライデーを実施して閉じた。アメリカのブラックフライデーの日付だけを見て待つと、韓国公式ストアの割引は逃すことになる。
11月26日午後、ニューバランス・クロックス・ダイソン・ムシンサ・プーマの公式ストアを直接開き、いま実際に割引がかかっているかを確認した。5社すべて今日時点でセールは生きており、各社が告知した期間と代表商品の現在価格を以下にまとめた。

1. ひと目でわかる5社
ニューバランス — 11月23日10:00〜11月28日9:59 / 最大80% / 会員ランククーポンVIP20%・MANIA15%・FAMILY10%、10万ウォン以上10%・20万ウォン以上20%コード / 1080 V15 209,000→159,000ウォン
クロックス — 11月25日9:00〜11月30日9:00 / 最大70% / 2足15%・3足25%追加割引、ジビッツチャーム5個40% / バヤ ラインド クロッグ 84,900→49,900ウォン
ダイソン — 11月23日〜11月30日 / 最大40%（リファービッシュ最大62%、アクセサリー最大71%） / カード請求割引サムスン10%・ロッテ・ハナ10%（最大20万ウォン） / エアラップ コアンダ2x 879,000→699,000ウォン
ムシンサ ムジンジャン — 11月22日19:00〜12月2日24:00 / 最大80% / 4,781ブランド・798,610商品 / スアレ ヘンリーネックニット59%引き24,400ウォン
プーマ — 11月12日〜11月26日（今日最終日） / プリブラック / - / スリップキャット ブーツ 169,000→84,000ウォン
今日が最終日なのはプーマだ。残りのうち最も早く閉じるのはニューバランスで、11月28日午前9時59分にクーポン利用が終わる。

2. ニューバランス — 明日午前9時59分に終了
公式イベントページの最初の画面には「2026 BLACK FRIDAY、セール価格に追加プロモーションまで、UP TO 80%」とある。クーポン利用期間は11月23日午前10時から11月28日午前9時59分まで。最終日の夜まで使えるのではなく、28日の朝9時59分で切れる点を先に覚えておきたい。
特典は三層だ。会員ランク別クーポンが3枚自動発行され（VIP20%、MANIA15%、FAMILY10%）、セール商品には10万ウォン以上10%、20万ウォン以上20%のプロモーションコードが付く。ネイバーペイで20万ウォン以上決済すると5,000ウォンが即時割引される。初回購入者と直近1年購入履歴のない会員には15%クーポンが別に出る。
今日確認した価格はこうだ。1080 V15はレディースD・メンズ2E・4Eすべて209,000ウォンから24%引きの159,000ウォン。ベストランキング1位から6位までをこのモデルが占めている。レベルV5メンズ2Eは219,000ウォンから32%引きの149,000ウォン、UNI RC HEAT パデッドジャンパーは299,000ウォンから40%引きの179,000ウォン。139,000ウォンの471ラインは「ワンデイ特価」で55,000ウォンまで下がっている。ワンデイ特価は毎日午前10時に切り替わり、24時間だけ続く。

3. クロックス — 30日午前9時まで、今夜8時ライブ
「ブラックフライデー アンコール」が11月25日午前9時に開き、11月30日午前9時に終わる。最初の画面にはジビッツチャーム最大30%割引と11月26日午後8時のライブ配信の案内が並ぶ。ライブではタイム特価と追加割引、ノベルティが出る。
追加割引は単純だ。対象商品を2足買うと15%、3足以上で25%がさらに引かれる。加えてクラシック クロッグのような定番モデルは色によって価格が大きく割れる。今日時点で定価69,900ウォンのクラシック クロッグは、色によって54,900ウォン（21%）、49,900ウォン（29%）、29,900ウォン（57%）まで下がっていた。同じ靴でも色を変えるだけで2万ウォン以上の差になる。
今日確認した代表価格は、バヤ ラインド クロッグ84,900→49,900ウォン（41%）、バヤ プラットフォーム ファズ ストラップ ラインド クロッグ99,900→59,900ウォン（40%）、アンフォゲッタブル コージー クロッグ84,900→64,900ウォン（24%）、メロウ リカバリー クロッグ79,900→29,900ウォン（63%）。

4. ダイソン — 30日まで、ラストチャンスウィーク
ダイソンは「ブラックフライデー ラストチャンスウィーク」として11月23日から30日まで1週間延長する。最初の画面の文言は「年に一度、最も強いブラックフライデー特典の最後の機会」。
今日確認した価格は、NEW エアラップ コアンダ2x マルチスタイラー＆ドライヤー（バーガンディウッド）が879,000ウォンから18万ウォン引きの699,000ウォン、スーパーソニック ニューラル ヘアドライヤーと保管ケースが599,000ウォンから15万ウォン引きの449,000ウォン。どちらも7万ウォン相当のノベルティが付く。水拭き掃除機ペンシルウォッシュは499,000ウォンから20万ウォン引きの299,000ウォン、ロボット掃除機スポット＆スクラブAiは1,690,000ウォンから62万ウォン引きの1,070,000ウォン。
最強のコードレス掃除機V16 ピストン アニマルは1,490,000ウォンから39万ウォン引きの1,100,000ウォンに並んでいるが、確認時点で品切れ表示が付いていた。カード請求割引まで適用した最大特典価は990,000ウォンと表示される。入荷通知をかけておくのが賢明だ。
カード特典も計算に入れる。サムスンカード10%（最大10万ウォン）、ロッテ・ハナカード10%（最大20万ウォン）の請求割引が付く。699,000ウォンのエアラップをサムスンカードで決済すれば629,000ウォンになる。ただし簡易決済では請求割引は適用されない。

5. ムシンサ ムジンジャン — 12月2日まで、今夜8時・9時特価
ムシンサの「ムジンジャン26 冬 ブラックフライデー」は11月22日午後7時に開き、12月2日24時に終わる。4,781ブランド、798,610商品、最大80%割引だ。今日午後に確認した累計販売数は3,211,563個、累計販売額は1,768億ウォン、累計割引額は1,421億ウォン。1日平均30億ウォンが売れ、そのうち約24億ウォンが割引で消えている計算だ。
ブランド自身のセールと違うのはタイムテーブルだ。毎日午前10時・11時、午後8時・9時に先着数量限定の特価が開く。今夜8時と9時の回にはアディダス スーパースター360 2.0ブーツが5,990ウォン（94%引き）、カントリーIIとキャンパス2、サンバLTが9,990ウォン（93%）と予告されている。午前10時と午後7時にはオープンラン抽選で最大80%クーポンと最大1万ウォンの積立金が出る。
いま販売順位の高いシグネチャー特価は、スアレ デイリー ヘンリーネックニット（59%引き24,400ウォン、24,609個販売）、オフメイド サイドピンタック ワイド スウェットパンツ（65%引き14,950ウォン、24,607個）、トリリオン クロップ長袖T（54%引き17,990ウォン、16,785個）、ディミトリブラック コンフォートテンプ ミッドウェイト パディング（48%引き69,900ウォン、12,503個）、スアレ ライト シアーシェル パデッドジャンパー（61%引き65,150ウォン、9,541個）の順だ。

6. プーマ — 今日が最終日
プーマ公式ストアは「PUMA PRE-BLACK」を11月12日から11月26日まで開く。今日が最終日だ。最初の画面のスリップキャット ブーツは169,000ウォンから50%引きの84,000ウォン。ブラックフライデー当日より早く開き、早く閉じる構造なので、明日プーマを探すともう終わっている可能性が高い。

7. なぜ韓国の公式ストアはアメリカより早く終わるのか
アメリカのブラックフライデーは感謝祭の翌日11月27日、サイバーマンデーは11月30日だ。一方、韓国のブランド公式ストアは11月初旬から中旬に始めてブラックフライデー前に閉じる例が多い。今年もニューバランスが11月初旬に一度、11月23日からもう一度開き、アディダスとナイキは20日と23日に終わった。シーズン序盤に在庫を整理し、12月の年末セールとチャネル別施策を別に持つ運営に見える。
だから「ブラックフライデーは11月27日」というカレンダーだけを見て動くと、韓国公式ストア基準では遅い。11月の第4週にはブランドアプリの通知をオンにし、公式ストアのイベントページを直接開くほうが確実だ。

8. 公式ストアとプラットフォーム、どちらが安いか
同じモデルでもチャネルによって最終決済額は変わる。比較の基準は三つ。第一に定価が同じか。公式ストアは希望小売価格、プラットフォームは販売者の裁量価格なので定価自体が違いうる。第二にクーポンが重複するか。ニューバランスはランククーポンと金額別コード、ネイバーペイ即時割引を併用できる構造だが、一部の人気モデルは対象外になる。第三に配送と交換の条件。公式ストアは無料配送・無料返品が基本のことが多く、サイズ交換も自社物流で処理される。
ムシンサのムジンジャンは同じニューバランスをブランドデーでもっと安く出すことがある。逆に公式ストアは色とサイズが残り、ランククーポンも付く。買うモデルが決まっているなら、二つのカートの最終金額を並べて比べるのが最も正確だ。

9. 今夜から明日の朝までの順番
今日午後8時、クロックスとダイソンのライブが同時に開く。ライブ限定ノベルティとタイム特価は数量が短い。午後8時・9時にはムシンサの先着特価（アディダス5,990ウォンなど）も開く。今日中にプーマのスリップキャット ブーツを買うか決める必要がある。
明日（27日）午前はニューバランスが急ぐ。クーポン利用が28日午前9時59分に終わるので、27日中に欲しいサイズを確保するのが安全だ。クロックスとダイソンは30日までなので27〜29日に余裕があり、ムシンサは12月2日までで最も遅い。ただし人気サイズと色は期間が残っていても先に消える。

10. 買う前に確認すること
「最大80%」「最大70%」はそのブランドの全商品がその価格という意味ではない。80%は一部の在庫整理商品に付き、人気モデルは20〜30%台にとどまる。表示された割引率よりカートの最終金額を見るべき理由だ。
同じモデルでも色とサイズで価格が違う。クロックスのクラシック クロッグのように色別に29,900ウォンから54,900ウォンまで割れる例が代表的だ。逆にニューバランスの1080 V15は幅（2E・4E・D）だけが違い、価格は同じだ。
クーポンは重複条件が商品ごとに違う。ランククーポンとプロモーションコード、カード請求割引、ネイバーペイ即時割引は重ならない組み合わせがあるので、決済直前の画面でもう一度確認したい。品切れも速い。ダイソンのV16は今日すでに品切れ表示が付き、ニューバランスの人気サイズ（260〜280）はワンデイ特価が始まる午前10時に最初に消える。

ひとことで
韓国のブランド公式ストアのブラックフライデーはアメリカより早く始まり、早く終わる。11月26日現在開いているのはニューバランス（28日9:59終了）、クロックス（30日9:00）、ダイソン（30日）、ムシンサ ムジンジャン（12月2日）、プーマ（今日終了）の5社。今夜はクロックス・ダイソンのライブとムシンサの8時・9時特価を、明日の朝はニューバランスのクーポン期限を先に押さえればいい。"""

ZH = """今年的黑色星期五是11月27日。但在韩国，不少品牌官方商城已经结束了促销：耐克韩国官方商城为11月17日至23日，阿迪达斯为11月10日至20日，之后便已收尾。只盯着美国黑五的日期等待，就会错过韩国官方商城的折扣。
11月26日下午，我们直接打开了新百伦、卡骆驰、戴森、MUSINSA以及彪马的官方商城，确认是否真的有折扣在跑。五个站点当天全部仍在进行，下面整理各家公布的期间与代表商品的当前价格。

1. 五家一览
新百伦 — 11月23日10:00～11月28日9:59 / 最高80% / 会员等级券 VIP 20%、MANIA 15%、FAMILY 10%，满10万韩元10%、满20万韩元20%促销码 / 1080 V15 209,000→159,000韩元
卡骆驰 — 11月25日9:00～11月30日9:00 / 最高70% / 买2双15%、3双以上25%追加折扣，智必星5个40% / Baya Lined 洞洞鞋 84,900→49,900韩元
戴森 — 11月23日～11月30日 / 最高40%（翻新机最高62%，配件最高71%） / 信用卡返现：三星10%、乐天与韩亚10%（上限20万韩元） / Airwrap Co-anda 2x 879,000→699,000韩元
MUSINSA「无尽情」 — 11月22日19:00～12月2日24:00 / 最高80% / 4,781个品牌、798,610件商品 / Suare 亨利领针织衫 59%折扣 24,400韩元
彪马 — 11月12日～11月26日（今天最后一天） / 黑五预热 / - / Slipcat 靴子 169,000→84,000韩元
今天结束的是彪马；其余之中最先关门的是新百伦，优惠券在11月28日上午9点59分失效。

2. 新百伦 — 明天上午9点59分结束
活动页首屏写着「2026 BLACK FRIDAY，在折扣价上再加码，UP TO 80%」。优惠券使用期为11月23日上午10点至11月28日上午9点59分，不是最后一天晚上，而是28日早上9点59分截止，这一点要先记住。
优惠分三层：会员等级券自动发放3张（VIP 20%、MANIA 15%、FAMILY 10%）；折扣商品可用满10万韩元减10%、满20万韩元减20%的促销码；用Naver Pay支付满20万韩元再立减5,000韩元。首次购买者与近一年无购买记录的会员另有15%优惠券。
今天确认的价格：1080 V15 女款D、男款2E与4E均为209,000韩元降至159,000韩元（24%），该型号占据畅销榜第1至第6名。Level V5 男款2E 219,000→149,000韩元（32%），UNI RC HEAT 羽绒夹克 299,000→179,000韩元（40%）。标价139,000韩元的471系列以「一日特价」降到55,000韩元，一日特价每天上午10点更换，仅维持24小时。

3. 卡骆驰 — 30日上午9点截止，今晚8点直播
「黑色星期五返场」于11月25日上午9点开启，11月30日上午9点结束。首屏同时挂着智必星最高30%折扣和11月26日晚8点直播的提示，直播中有时段特价、追加折扣与赠品。
叠减规则很简单：买2件15%，3件以上25%。此外，像经典洞洞鞋这类基础款，价格随颜色大幅变化：标价69,900韩元的经典洞洞鞋，今天按颜色分别为54,900韩元（21%）、49,900韩元（29%）和29,900韩元（57%）。同一双鞋换个颜色，差价超过2万韩元。
今天确认的代表价格：Baya Lined 洞洞鞋 84,900→49,900韩元（41%）、Baya Platform Fuzz Strap Lined 99,900→59,900韩元（40%）、Unfurgettable Cozy 84,900→64,900韩元（24%）、Mellow Recovery 79,900→29,900韩元（63%）。

4. 戴森 — 到30日，最后机会周
戴森以「黑五最后机会周」为名，从11月23日延长到30日。首屏文案是「一年仅一次，最强黑五优惠的最后机会」。
今天确认的价格：NEW Airwrap Co-anda 2x 多功能造型吹风机（酒红木色）879,000降至699,000韩元（减18万），赠价值7万韩元礼品；Supersonic Nural 吹风机含收纳盒 599,000降至449,000韩元（减15万），赠支架。湿式清洁机 Pencilwash 499,000降至299,000韩元（减20万），扫地机器人 Spot & Scrub Ai 1,690,000降至1,070,000韩元（减62万）。
最强无线吸尘器 V16 Piston Animal 标价1,490,000降至1,100,000韩元（减39万），但确认时显示已售罄，叠加信用卡返现后的最优价显示为990,000韩元。设置到货提醒更为稳妥。
信用卡优惠要算进去：三星卡返现10%（上限10万韩元），乐天、韩亚卡10%（上限20万韩元）。699,000韩元的Airwrap用三星卡支付即为629,000韩元。但使用快捷支付则不享受返现。

5. MUSINSA 无尽情 — 到12月2日，今晚8点与9点特价
MUSINSA 的「无尽情26冬季黑色星期五」于11月22日晚7点开启，12月2日24点结束，覆盖4,781个品牌、798,610件商品，最高80%折扣。今天下午确认的累计销量为3,211,563件，累计销售额1,768亿韩元，累计折扣额1,421亿韩元——日均卖出约30亿韩元，其中约24亿以折扣让出。
它与品牌自身促销的不同在于时间表：每天上午10点、11点和晚上8点、9点开抢先限量特价。今晚8点与9点预告阿迪达斯 Superstar 360 2.0 靴子5,990韩元（94%折扣），Country II、Campus 2、Samba LT 均为9,990韩元（93%）。上午10点与晚7点的开门抽奖最多给80%优惠券和1万韩元积分。
目前销量领先的招牌特价依次为：Suare 日常亨利领针织衫（59%折扣24,400韩元，24,609件）、Offmade 侧褶宽松卫裤（65%折扣14,950韩元，24,607件）、Trillion 短款长袖T恤（54%折扣17,990韩元，16,785件）、Dimitri Black Comfortemp 中厚羽绒（48%折扣69,900韩元，12,503件）、Suare 轻量纱壳羽绒夹克（61%折扣65,150韩元，9,541件）。

6. 彪马 — 今天是最后一天
彪马官方商城把「PUMA PRE-BLACK」开在11月12日至11月26日，今天是最后一天。首屏的Slipcat靴子为169,000降至84,000韩元（50%）。它比黑五更早开始也更早结束，明天再找彪马，很可能已经结束。

7. 为什么韩国官方商城比美国更早结束
美国黑五在感恩节次日的11月27日，网络星期一为11月30日。韩国品牌官方商城则多在11月初至中旬开始，在黑五之前收尾。今年新百伦11月初开过一次，11月23日再开一次；阿迪达斯与耐克分别在20日和23日结束。看起来是赛季初清理库存、把12月年末促销与各渠道活动分开运营的做法。
所以只按「黑五是11月27日」的日历行动，对韩国官方商城来说已经晚了。11月第四周应打开品牌App通知，并直接进官方商城的活动页。

8. 官方商城与平台，哪里更便宜
同一型号在不同渠道的最终支付价不同。比较看三点：第一，标价是否相同——官方商城显示建议零售价，平台显示卖家定价；第二，优惠券能否叠加——新百伦可以叠加等级券、金额促销码与Naver Pay立减，但部分热门款被排除；第三，配送与换货条件——官方商城多为免运费免退货运费，尺码换货也由自有物流处理。
MUSINSA 无尽情有时会在品牌日把同款新百伦放得更低；反过来，官方商城可能还有你要的颜色和尺码，并附等级券。已确定型号的话，把两个购物车的最终金额并排比较最准确。

9. 从今晚到明早的顺序
今晚8点，卡骆驰与戴森的直播同时开启，直播限定赠品与时段特价数量很少。晚8点与9点，MUSINSA 的限量特价也会开（含阿迪达斯5,990韩元等）。彪马Slipcat靴子要在今天之内决定。
明天（27日）上午最急的是新百伦：优惠券28日上午9点59分到期，在27日内拿下想要的尺码更安全。卡骆驰与戴森到30日，27至29日还有余裕；MUSINSA 到12月2日最晚。但热门尺码与颜色即使期限未到也会先消失。

10. 购买前要确认
「最高80%」「最高70%」并不意味着该品牌所有商品都是这个折扣：最高值出现在清库存商品上，热门款多在20%至30%。这就是要看购物车最终金额而不是折扣标签的原因。
同一型号在不同颜色和尺码上价格不同。卡骆驰经典洞洞鞋按颜色从29,900到54,900韩元；而新百伦1080 V15只是宽度（2E、4E、D）不同，价格一致。优惠券的叠加条件逐件不同，等级券、促销码、信用卡返现与Naver Pay立减存在互斥组合，付款前要在结算页再确认一次。缺货也很快：戴森V16今天已显示售罄，新百伦的热门尺码（260至280）会在上午10点一日特价开启时最先消失。

一句话总结
韩国品牌官方商城的黑五比美国更早开始、也更早结束。截至11月26日仍在进行的是新百伦（28日9:59截止）、卡骆驰（30日9:00）、戴森（30日）、MUSINSA 无尽情（12月2日）与彪马（今天截止）。今晚先看卡骆驰与戴森直播和MUSINSA 8点、9点特价，明早先抓住新百伦的优惠券期限即可。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "k-fashion",
    "store": "공식몰",
    "priceKrw": 159000,
    "releaseDate": "2026-11-26",
    "rating": 4.8,
    "imageUrl": G1,
    "images": [G1, G2, G3, G4],
    "affiliateUrl": q("뉴발란스 1080 v15"),
    "affiliatePlatform": "Coupang",
    "exampleItems": [
        {"name": "뉴발란스 1080 V15", "brand": "New Balance", "priceKrw": 159000, "imageUrl": G1,
         "url": q("뉴발란스 1080 v15"), "category": "209,000→159,000원 · 24%"},
        {"name": "크록스 바야 라인드 클로그", "brand": "Crocs", "priceKrw": 49900, "imageUrl": G2,
         "url": q("크록스 바야 라인드 클로그"), "category": "84,900→49,900원 · 41%"},
        {"name": "다이슨 에어랩 코안다2x 멀티 스타일러 앤 드라이어", "brand": "Dyson", "priceKrw": 699000, "imageUrl": G3,
         "url": q("다이슨 에어랩 코안다2x"), "category": "879,000→699,000원 · 18만원"},
        {"name": "디미트리블랙 컴포트템프 미드웨이트 패딩", "brand": "Dimitri Black", "priceKrw": 69900, "imageUrl": G4,
         "url": q("남자 숏패딩"), "category": "무진장 특가 69,900원 · 48%"},
    ],
    "i18n": {
        "ko": {
            "title": "브랜드 공식몰 블프, 지금 열린 곳은 5곳뿐 — 뉴발란스·크록스·다이슨·무신사·푸마 실측 가격 (11/26)",
            "summary": "내일이 블랙프라이데이지만 나이키·아디다스 공식몰은 이미 끝났습니다. 11월 26일 직접 확인한 결과 지금 열려 있는 브랜드 자체 세일은 뉴발란스(28일 09:59 마감), 크록스(30일), 다이슨(30일), 무신사 무진장(12/2), 푸마(오늘 마감) 다섯 곳입니다.",
            "description": KO,
            "tasteReview": [
                "뉴발란스: 11/23 10:00~11/28 09:59, UP TO 80%, 등급쿠폰 VIP 20%·MANIA 15%·FAMILY 10%, 1080 V15 209,000→159,000원",
                "크록스: 11/25 09:00~11/30 09:00, 최대 70%+2개 15%·3개 25%, 바야 라인드 84,900→49,900원, 11/26 20시 라이브",
                "다이슨: 11/23~11/30 라스트찬스 위크, 에어랩 코안다2x 879,000→699,000원, V16 1,490,000→1,100,000원(품절)",
                "무신사 무진장: 11/22 19:00~12/2 24:00, 최대 80%, 4,781 브랜드·798,610 상품 / 푸마 PRE-BLACK 11/12~11/26(오늘 마감), 슬립캣 부츠 169,000→84,000원",
            ],
            "tips": "가격과 기간은 2026년 11월 26일 오후 각 브랜드 공식몰 화면에서 확인한 값이며, 재고·카드 혜택·쿠폰 조건에 따라 달라질 수 있습니다. 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있으며, 비교 상품 링크는 쿠팡 검색 결과로 연결됩니다. 직접 고른 상품은 네이버 크리에이터샵(https://cshop.naver.com/jaenam)에서도 모아 볼 수 있습니다.",
        },
        "en": {
            "title": "Brand Black Friday: Only Five Official Stores Are Still Open — New Balance, Crocs, Dyson, Musinsa and PUMA, Priced Today",
            "summary": "Black Friday is tomorrow, but Nike and adidas Korea have already closed their sales. On 26 November five brand stores were still running: New Balance (ends 09:59 on the 28th), Crocs (the 30th), Dyson (the 30th), Musinsa Mujinjang (2 December) and PUMA (today).",
            "description": EN,
            "tasteReview": [
                "New Balance: 23 Nov 10:00 to 28 Nov 09:59, up to 80%, tier coupons VIP 20% / MANIA 15% / FAMILY 10%, 1080 V15 209,000 to 159,000 won",
                "Crocs: 25 Nov 09:00 to 30 Nov 09:00, up to 70% plus 15% for two pairs and 25% for three, Baya Lined 84,900 to 49,900 won, live show at 8pm on 26 Nov",
                "Dyson: last-chance week 23-30 Nov, Airwrap Co-anda 2x 879,000 to 699,000 won, V16 1,490,000 to 1,100,000 won (sold out)",
                "Musinsa Mujinjang: 22 Nov 19:00 to 2 Dec 24:00, up to 80%, 4,781 brands and 798,610 products / PUMA PRE-BLACK 12-26 Nov (last day), Slipcat Boots 169,000 to 84,000 won",
            ],
            "tips": "Prices and dates were read on each brand's official store on the afternoon of 26 November 2026 and may change with stock, card offers and coupon conditions. This post contains affiliate links and may earn a commission; comparison links open Coupang search results. Picks can also be browsed at the Naver creator shop (https://cshop.naver.com/jaenam).",
        },
        "ja": {
            "title": "ブランド公式ストアのブラックフライデー、いま開いているのは5社だけ — ニューバランス・クロックス・ダイソン・ムシンサ・プーマ実測価格",
            "summary": "明日はブラックフライデーだが、ナイキとアディダスの韓国公式ストアはすでに終了。11月26日に確認したところ、開いているのはニューバランス（28日9:59終了）、クロックス（30日）、ダイソン（30日）、ムシンサ ムジンジャン（12月2日）、プーマ（今日終了）の5社でした。",
            "description": JA,
            "tasteReview": [
                "ニューバランス：11/23 10:00〜11/28 9:59、UP TO 80%、ランククーポンVIP20%・MANIA15%・FAMILY10%、1080 V15 209,000→159,000ウォン",
                "クロックス：11/25 9:00〜11/30 9:00、最大70%＋2足15%・3足25%、バヤ ラインド 84,900→49,900ウォン、11/26 20時ライブ",
                "ダイソン：11/23〜11/30 ラストチャンスウィーク、エアラップ コアンダ2x 879,000→699,000ウォン、V16 1,490,000→1,100,000ウォン（品切れ）",
                "ムシンサ ムジンジャン：11/22 19:00〜12/2 24:00、最大80%、4,781ブランド・798,610商品 / プーマ PRE-BLACK 11/12〜11/26（今日終了）、スリップキャット 169,000→84,000ウォン",
            ],
            "tips": "価格と期間は2026年11月26日午後に各ブランド公式ストアの画面で確認した値で、在庫・カード特典・クーポン条件により変わります。本記事はアフィリエイトリンクを含み手数料を受け取る場合があります。比較リンクはCoupangの検索結果に移動します。選んだ商品はNAVERクリエイターショップ（https://cshop.naver.com/jaenam）でもまとめて見られます。",
        },
        "zh": {
            "title": "品牌官方商城黑五，现在还开着的只有5家——新百伦、卡骆驰、戴森、MUSINSA、彪马当天实价",
            "summary": "明天就是黑五，但耐克与阿迪达斯韩国官方商城已经结束。11月26日确认后仍在进行的是新百伦（28日9:59截止）、卡骆驰（30日）、戴森（30日）、MUSINSA无尽情（12月2日）与彪马（今天截止）五家。",
            "description": ZH,
            "tasteReview": [
                "新百伦：11/23 10:00～11/28 9:59，UP TO 80%，等级券VIP 20%・MANIA 15%・FAMILY 10%，1080 V15 209,000→159,000韩元",
                "卡骆驰：11/25 9:00～11/30 9:00，最高70%＋买2件15%・3件25%，Baya Lined 84,900→49,900韩元，11/26 20点直播",
                "戴森：11/23～11/30 最后机会周，Airwrap Co-anda 2x 879,000→699,000韩元，V16 1,490,000→1,100,000韩元（售罄）",
                "MUSINSA无尽情：11/22 19:00～12/2 24:00，最高80%，4,781品牌・798,610商品 / 彪马 PRE-BLACK 11/12～11/26（今天截止），Slipcat 169,000→84,000韩元",
            ],
            "tips": "价格与期间为2026年11月26日下午在各品牌官方商城页面确认的数值，可能因库存、信用卡优惠与优惠券条件变动。本文含联盟链接，可能获得佣金；比价链接跳转至Coupang搜索结果。所选商品也可在NAVER创作者商店（https://cshop.naver.com/jaenam）查看。",
        },
    },
}

if __name__ == "__main__":
    publish(POST)
