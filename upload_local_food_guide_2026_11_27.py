#!/usr/bin/env python3
"""한국 편의점 신상 & 성수·을지로 로컬 맛집 4개국어 가이드 → Supabase posts + ISR revalidate.

사실 근거 (2026-11-27 확인)
 - GS25 브리오슈번 800원 / 치즈쏙치킨 2,800원, 11/20~12/15 동시 구매 2,300원, 펩시 210ml 포함 3,000원
   GS리테일 보도자료(2026-11-16) + https://www.gsretail.com/news/press-releases/detail?prrSeqno=4404
 - GS25 '맵달반반샌드' 3,900원 (TXT 미니 9집 협업, 11/19) GS리테일 보도자료
 - CU 딸기 초코 휩 카스텔라 샌드 5,500원, 11/6~11/20 포켓CU 하루 500개 한정 / 후르츠 우유 휩 샌드 11/18 / 12월 딸기 우유 휩 샌드 예정
   BGF리테일 보도자료(2026-11-05)
 - CU 무제 오디오북 디저트 4종: 마카롱 3,500 / 쿠키샌드 2,700 / 씬쿠키 2,800 / 토스트 3,000, 11/26부터 순차
   BGF리테일 보도자료(2026-11-26)
 - CU 치즈 딥핑·멜팅 시리즈 11/9부터 순차 (매장 표기 3,700원·5,700원은 보도사진 기준)
 - 세븐일레븐 시경 pick 놀면리얼바지락짬뽕라면 3,900원, 11/19 출시, 이달 말까지 더미식백미밥 증정,
   NH농협·우리카드·네이버페이·L.PAY 30% 중복 할인 (코리아세븐 보도자료 2026-11-12·11-20)
 - 세븐일레븐 남해안제철꼬막비빔밥 5,200원 11/18, BC카드 25% (11/30까지),
   전주식소고기비빔밥 금요일(11/20·11/27) 50% 2,350원, 11/18~24 비빔밥 구매 시 라면 증정 (코리아세븐 2026-11-15)
 - 편의점 부가세 즉시환급: 1회 15,000원 이상 100만 원 미만, 체류 기간 합계 500만 원, 여권 원본,
   담배·일부 주류 제외, 3사 약 2,000개 점포 (서울경제 2026-11-17·11-18)
 - 소문난성수감자탕: 서울 성동구 연무장길 45, 02-465-6580, 24시간, 번호표 없음, 일행 모두 입장, 혼밥석
   (VisitSeoul 공식 관광정보 / 식신 / 다이닝코드, 메뉴 가격 2026년 기준)
 - 원조만선호프: 서울 중구 을지로13길 19, 02-2274-1040, 노가리 2,000원, 루프탑 계단 대기, 예약·주차 불가
 - 안동장: 서울 중구 을지로 124, 02-2266-3814, 1948년경 개업 3대째, 서울미래유산(2013-175),
   11:30~21:00 연중무휴(한국관광공사), 6인 이상만 예약

이미지: GS25·CU·세븐일레븐 공식 보도사진 4장(3:4 크롭) + OpenStreetMap 지도 3장(© OpenStreetMap contributors, ODbL).
       AI 생성 이미지 0장.
"""

import json
import os
import urllib.request

SLUG = "seoul-convenience-store-new-items-and-seongsu-euljiro-local-restaurants"
BASE = "/images/products/"


def _env_local(name):
    try:
        for line in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env.local"), encoding="utf-8"):
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip()
    except OSError:
        pass
    return ""


def _require_env(name):
    value = os.environ.get(name) or _env_local(name)
    if not value:
        raise SystemExit(f"{name} is not set in the environment or .env.local")
    return value


SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = _require_env("SUPABASE_SERVICE_ROLE_KEY")
REVALIDATE_URL = "https://www.k-trand.store/api/revalidate?secret=" + _require_env("REVALIDATE_SECRET")

C = BASE + "guide-cu-strawberry-whip-sand.jpg"
G1 = BASE + "guide-gs25-brioche-cheeseburger.jpg"
G2 = BASE + "guide-cu-cheese-melting-lineup.jpg"
G3 = BASE + "guide-seven-kkomak-bibimbap.jpg"
G4 = BASE + "guide-map-seongsu-gamjatang.jpg"
G5 = BASE + "guide-map-manseon-hof.jpg"
G6 = BASE + "guide-map-andongjang.jpg"

KO = """이번 주 서울 편의점 세 곳(GS25·CU·세븐일레븐)의 공식 보도자료를 기준으로, 지금 실제로 살 만한 신상 6종과 조합 가격을 정리했다. 여기에 성수와 을지로에서 외국인 손님이 많이 찾는 로컬 맛집 3곳의 위치·영업시간·주문 방법을 붙였다. 가격과 영업시간은 모두 2026년 11월 27일 기준이다.

1. GS25 — 빵과 치킨을 따로 사서 조립하는 방식
11월 20일부터 브리오슈번(800원)과 치즈쏙치킨(2,800원)이 나왔다. 브리오슈번 안쪽에 타르타르 소스가 발라 있어, 갓 튀긴 치즈쏙치킨을 끼우면 3,600원짜리 수제버거가 된다. 12월 15일까지 두 개를 함께 사면 2,300원이고, 행사용 펩시콜라 210ml를 더하면 3,000원이다. GS25가 '모디슈머' 트렌드를 겨냥해 낸 상품이라, 매장에서 직접 조립해 먹는 방식이 정식 사용법이다.

11월 19일에는 투모로우바이투게더 미니 9집 발매에 맞춘 협업 샌드위치 '맵달반반샌드'가 3,900원에 나왔다. 매운맛과 단맛 소스를 반씩 발라 아이돌 팬덤 수요를 겨냥한 상품이다.

2. CU — 겨울 딸기 샌드위치, 앱에서 먼저 나온다
CU의 겨울 효자 상품은 생딸기 샌드위치다. 11월 6일 '딸기 초코 휩 카스텔라 샌드'가 5,500원에 나왔고, 11월 20일까지 포켓CU 앱에서 하루 500개 한정으로 예약 판매했다. 초코 카스텔라 사이에 초코 휩 크림, 초코칩, 생딸기를 넣은 166g·452kcal 제품이다. 예약 판매가 끝난 지금은 매장 재고로만 만날 수 있고, 11월 18일부터는 딸기·오렌지·샤인머스캣을 한 번에 넣은 '후르츠 우유 휩 샌드'가 매장에 나와 있다. 12월에는 '딸기 우유 휩 샌드'가 예정돼 있다.

11월 26일부터는 출판사 '무제'와 손잡은 오디오북 디저트 4종이 순차 출시됐다. 마카롱 3,500원, 쿠키샌드 2,700원, 씬쿠키 2,800원, 토스트 3,000원. 상품마다 성해나 작가 소설 '일일 반출록' 일부를 들을 수 있는 QR 카드 10종 가운데 1종이 무작위로 들어간다. 디저트를 사면서 책 한 조각을 같이 사는 셈이다.

11월 9일부터는 치즈를 찍어 먹거나 녹여 먹는 '치즈 딥핑·멜팅' 시리즈가 순차 출시 중이다. 보도사진에 찍힌 매장 표기 기준 김치감자수프 3,700원, 치즈불닭 5,700원. 전자레인지에 데우면 치즈가 늘어나는 냉장 HMR까지 포함된다.

3. 세븐일레븐 — 3,900원 라면에 즉석밥이 붙는다
11월 19일, 성시경이 기획과 레시피 개발에 참여한 '시경 pick 놀면리얼바지락짬뽕라면'이 3,900원에 나왔다. 껍질째 넣은 바지락 원물에 오징어·새우 동결건조 블록, 목이버섯·양배추·청경채 후레이크를 넣었고, 일반 유탕면보다 전분을 5%포인트 높여 국물이 면에 배도록 만들었다. 이달 말까지 사면 '더미식백미밥'을 무료로 준다. NH농협카드·우리카드·네이버페이·L.PAY로 결제하면 30% 할인이 중복 적용된다.

11월 18일에는 여수 새꼬막을 쓴 '남해안제철꼬막비빔밥'이 5,200원에 나왔다. 11월 30일까지 BC카드로 결제하면 25% 할인된다. 금요일인 오늘(11월 27일)은 '전주식소고기비빔밥'을 50% 할인한 2,350원에 판다.

4. 그래서 오늘 뭘 사면 되나 — 세 가지 조합
① 라면 + 즉석밥: 3,900원짜리 라면에 백미밥이 무료로 붙고, 카드 할인까지 겹치면 2,730원 선이 된다. 편의점 한 끼로는 이번 주 가장 싼 조합이다.
② 브리오슈번 + 치즈쏙치킨: 12월 15일까지 2,300원, 콜라까지 더하면 3,000원.
③ 꼬막비빔밥: 5,200원짜리에 BC카드 25% 할인이 붙어 3,900원. 11월 24일까지는 라면 증정도 있었지만 지금은 끝났으니 할인만 챙기면 된다.

5. 외국인 관광객이 계산대에서 바로 쓰는 세 가지
첫째, 부가세 즉시환급이다. GS25·CU·세븐일레븐 가운데 환급 단말기가 있는 매장에서 1회 15,000원 이상 100만 원 미만을 사고, 계산 전에 여권 원본을 보여주면 부가세가 바로 빠진다. 체류 기간 합계 500만 원까지 가능하고 담배와 일부 주류는 제외된다. 환급이 되는 매장은 3사 합쳐 전국 약 2,000곳으로 서울·제주·부산에 몰려 있다(서울경제 2026년 11월 17일). 가게 앞에 Tax Free 스티커가 붙어 있으면 그 매장이다.

둘째, 앱 예약 상품은 매장에 없다. CU '딸기 초코 휩 카스텔라 샌드'처럼 포켓CU 예약으로만 판매한 상품은 진열대에 없으니, 여행 중이라면 매장에 깔린 상품을 고르는 편이 빠르다.

셋째, 즉석식품은 계산 후 매장 전자레인지와 온수기를 쓰면 된다. 컵라면 물은 계산대 옆 온수기에서 받고, 도시락과 호빵은 전자레인지에 30초에서 1분 정도 돌리면 된다.

6. 성수·을지로 로컬 맛집 3곳
(1) 소문난성수감자탕 — 서울 성동구 연무장길 45, 02-465-6580. 성수역 4번 출구에서 229m, 연중무휴 24시간. 감자국식사(1인) 일반 12,000원·우거지 13,000원, 감자탕 소 32,000원·중 37,000원·대 49,000원, 수제비 사리 4,000원. 예약은 받지 않고 번호표도 없다. 대기석에 앉아 있으면 순서대로 안내하며, 일행이 모두 도착해야 들어갈 수 있다. 혼자라면 별도 혼밥석으로 바로 안내받을 수 있다. 주차는 식사 시간에만 가능하고 관리비 2,000원이 붙는다. 외국인이라면 2인 이상이 필요한 감자탕보다 1인용 감자국이 주문하기 쉽고, 남은 국물에 볶음밥 4,000원을 볶아 마무리하는 방식이 이 집의 정석이다.

(2) 원조만선호프 — 서울 중구 을지로13길 19, 02-2274-1040. 을지로3가역 4번 출구에서 도보 2분, 을지로 노가리골목. 매일 낮 12시에 열고, 마감 시각은 자료에 따라 자정과 새벽 3시로 갈린다. 예약과 주차는 받지 않는다. 노가리 2,000원, 황태 2,000원, 마늘치킨 반 마리 1만 원 안팎, 생맥주 500cc가 1·2층 5,000원, 루프탑 5,500원이다. 사람들이 앉는 곳은 계단으로만 올라가는 루프탑이라 오후 6시를 넘기면 계단에 줄이 생긴다. 앱 웨이팅이 없으니 그냥 줄을 서면 된다. 주문은 자리에서 직원에게 하고, 노가리는 손으로 뜯어 고추장·마요 소스에 찍어 먹는다. 계단이 힘들면 1·2층 실내 자리를 물어보면 된다.

(3) 안동장 — 서울 중구 을지로 124, 02-2266-3814. 을지로3가역 10번 출구에서 1분. 1948년 무렵 문을 열어 3대째 이어온 중식당으로, 서울미래유산(2013-175)에 '서울에서 가장 오래된 중식당'으로 소개된 곳이다. 영업시간은 11:30~21:00 연중무휴(한국관광공사 기준)이며, 지도 서비스에는 20:30 마감으로 표기된 곳도 있다. 주차는 불가. 굴짬뽕 12,000~13,000원, 삼선우동 11,000원, 짜장면 9,000원, 군만두 9,000원. 예약은 6인 이상만 전화로 받고 그 아래는 현장 대기다. 마늘과 굴을 넣은 굴짬뽕이 대표 메뉴라 매운 짬뽕이 부담스러운 사람도 먹기 쉽다.

7. 확인된 것과 확인되지 않은 것
확인된 것: 편의점 6종의 가격과 행사 기간은 각 사 보도자료(GS리테일 11월 16일·19일, BGF리테일 11월 5일·9일·26일, 코리아세븐 11월 12일·15일·17일)와 매장 표기 사진, 맛집 3곳의 주소·전화·영업시간은 한국관광공사·서울관광과 지도 서비스의 2026년 11월 27일 값이다.
확인되지 않은 것: '후르츠 우유 휩 샌드'의 가격, 12월 '딸기 우유 휩 샌드'의 출시일, 만선호프의 마감 시각, 안동장의 브레이크타임 유무, 만선호프의 카드 결제 여부. 방문 전에 매장이나 지도 앱에서 한 번 더 확인하는 편이 안전하다."""

EN = """This is what Seoul's three big convenience store chains actually put on the shelf this week, checked against their own press releases: six new items with real prices, three combinations that add up to a cheap meal, and three local restaurants in Seongsu and Euljiro with exact addresses, hours and ordering tips for visitors. All prices and hours are as of 27 November 2026.

1. GS25 — buy the bread and the chicken separately, build it yourself
Since 20 November, GS25 has sold Brioche Bun (800 won) and Cheese-in Chicken (2,800 won). The bun is already brushed with tartar sauce, so slipping the freshly fried chicken inside gives you a 3,600-won handmade burger. Until 15 December the pair costs 2,300 won, and adding the promo 210ml Pepsi makes it 3,000 won. This is a "modisumer" product by design: assembling it in the store is the intended way to eat it.

On 19 November the chain also released Mapdal Banban Sand (3,900 won), a collaboration sandwich timed to TOMORROW X TOGETHER's ninth mini album, with spicy and sweet sauces spread half and half.

2. CU — the winter strawberry sandwich arrives on the app first
CU's winter workhorse is the fresh strawberry sandwich. Strawberry Choco Whip Castella Sand launched on 6 November at 5,500 won and was sold by reservation only on the Pocket CU app, 500 a day, through 20 November. It is 166g and 452 kcal: chocolate castella, chocolate whip cream, chocolate chips and whole strawberries. With the reservation window closed, it is now down to store stock, and since 18 November the stores carry Fruit Milk Whip Sand with strawberry, orange and shine muscat in one pack. A Strawberry Milk Whip Sand is scheduled for December.

From 26 November, CU released four desserts made with the publisher Muje: macaron 3,500 won, cookie sand 2,700 won, thin cookie 2,800 won and toast 3,000 won. Each comes with one of ten random QR cards that play part of Seong Hae-na's novel "Iril Banchulrok" as an audiobook, so you buy a dessert and a page of a book at the same time.

Since 9 November the Cheese Dipping & Melting line has been rolling out: cheese sauces to dip into, cheese that stretches when melted. Store labels visible in the press photo read 3,700 won for the kimchi potato soup and 5,700 won for the cheese buldak, and the range includes chilled HMR trays you heat in the microwave.

3. 7-Eleven — a 3,900-won ramen that comes with a bowl of rice
On 19 November 7-Eleven released Sigyeong Pick Nolmyeon Real Bajirak Jjamppong Ramen at 3,900 won. Singer Sung Si-kyung picked the menu and developed the recipe; the cup holds whole clams in the shell, a freeze-dried seafood block of squid and shrimp, and wood ear mushroom, cabbage and bok choy flakes. Starch is about 5 percentage points higher than a standard fried noodle, so the broth clings to the noodles. Buy it before the end of November and you get a pack of The Michel white rice free, and paying with NH Nonghyup Card, Woori Card, Naver Pay or L.PAY stacks another 30% off.

On 18 November the chain added Namhae Seasonal Cockle Bibimbap at 5,200 won, made with female cockles from Yeosu; paying by BC Card takes 25% off until 30 November. Today, Friday 27 November, the Jeonju-style Beef Bibimbap is half price at 2,350 won.

4. So what should you buy today — three combinations
First, ramen plus rice: a 3,900-won cup of ramen with free white rice, and with the card discount it lands near 2,730 won. It is the cheapest convenience-store meal of the week. Second, brioche bun plus cheese chicken: 2,300 won until 15 December, 3,000 won with a cola. Third, the cockle bibimbap: 5,200 won minus 25% on BC Card is 3,900 won. The free ramen that came with bibimbap purchases ended on 24 November, so only the discount is left.

5. Three things foreign visitors can use at the counter
First, the instant VAT refund. At GS25, CU and 7-Eleven stores with a refund terminal, buy at least 15,000 won and under 1,000,000 won in one transaction and show your physical passport before paying: the tax comes off at the register. The cap is 5,000,000 won per stay, and cigarettes and some alcohol are excluded. About 2,000 stores across the three chains offer it, concentrated in Seoul, Jeju and Busan (Seoul Economic Daily, 17 November 2026). A Tax Free sticker on the door is the sign.

Second, app-only items are not in the store. Anything sold by reservation on Pocket CU, like the strawberry choco castella sand, is not on the shelf, so while travelling it is faster to pick what is displayed.

Third, use the store microwave and hot water dispenser after paying. Fill cup ramen at the dispenser next to the counter and heat lunch boxes or steamed buns for 30 seconds to a minute.

6. Three local restaurants in Seongsu and Euljiro
(1) Somunnan Seongsu Gamjatang — 45 Yeonmujang-gil, Seongdong-gu, Seoul; 02-465-6580. 229m from Seongsu Station exit 4, open 24 hours every day. Single-serving gamja-guk (pork bone soup) is 12,000 won plain or 13,000 won with dried radish greens; a gamjatang pot is 32,000 won small, 37,000 medium and 49,000 large, with hand-torn sujebi noodles at 4,000 won. No reservations and no ticket machine: sit in the waiting area and staff call you in order, and the whole party must be present. Solo diners have their own counter seats and skip the line. Parking only during meal times, 2,000 won. For visitors, the one-person gamja-guk is easier to order than the two-person minimum pot, and the house ritual is to finish by frying rice in the leftover broth for 4,000 won.

(2) Wonjo Manseon Hof — 19 Euljiro 13-gil, Jung-gu, Seoul; 02-2274-1040. Two minutes on foot from Euljiro 3-ga Station exit 4, in the Nogari Alley. Opens at noon daily; sources disagree on closing time, some saying midnight and others 3 a.m. No reservations, no parking. Nogari (dried pollack) is 2,000 won, hwangtae 2,000 won, half a garlic chicken around 10,000 won, and 500cc draft beer is 5,000 won on the first and second floors, 5,500 won on the rooftop. Everyone wants the rooftop, reached by stairs only, so a line forms on the staircase after 6 p.m. There is no app queue: just stand in line. Order from your table, tear the nogari apart with your hands and dip it in the gochujang-mayonnaise sauce, and ask about indoor seating if the stairs are a problem.

(3) Andongjang — 124 Euljiro, Jung-gu, Seoul; 02-2266-3814. One minute from Euljiro 3-ga Station exit 10. Opened around 1948 and now run by the third generation, it is listed as Seoul's oldest Chinese restaurant on the Seoul Future Heritage register (2013-175). Hours are 11:30 to 21:00, open daily, according to the Korea Tourism Organization; some map services list a 20:30 close. No parking. Oyster jjamppong is 12,000-13,000 won, samseon udon 11,000 won, jajangmyeon 9,000 won and fried dumplings 9,000 won. Reservations are taken by phone only for parties of six or more. The signature oyster jjamppong is built on garlic and oysters rather than pure heat, so it suits people who find regular jjamppong too spicy.

7. What is confirmed and what is not
Confirmed: the six convenience-store prices and promo periods come from the companies' press releases (GS Retail 16 and 19 November; BGF Retail 5, 9 and 26 November; Korea Seven 12, 15 and 17 November) and from store labels in their press photos; the restaurants' addresses, phone numbers and hours come from the Korea Tourism Organization, VisitSeoul and map services as of 27 November 2026.
Not confirmed: the price of Fruit Milk Whip Sand, the December release date of Strawberry Milk Whip Sand, Manseon Hof's closing time, whether Andongjang has a break time, and whether Manseon Hof takes cards. Check the store or a map app once more before you go."""

JA = """今週ソウルのコンビニ3社（GS25・CU・セブンイレブン）が発表した公式リリースをもとに、いま実際に買う価値のある新商品6つと組み合わせ価格を整理しました。あわせて、聖水（ソンス）と乙支路（ウルジロ）で外国人客にも人気のローカル食堂3軒の場所・営業時間・注文のしかたを付けています。価格と営業時間はすべて2026年11月27日時点です。

1. GS25 — パンとチキンを別々に買って組み立てる
11月20日からブリオッシュバン（800ウォン）とチーズチキン（2,800ウォン）が登場。バンの内側にタルタルソースが塗ってあり、揚げたてのチーズチキンを挟めば3,600ウォンの手作りバーガーになります。12月15日まで2つ同時購入で2,300ウォン、イベント用ペプシ210mlを足すと3,000ウォンです。GS25が「モディシュマー」トレンドを狙って出した商品なので、店で組んで食べるのが正式な使い方です。

11月19日にはTOMORROW X TOGETHERのミニ9集発売に合わせたコラボサンド「マプダルバンバンサンド」が3,900ウォンで出ました。辛口と甘口のソースを半々に塗った、アイドルファン向けの商品です。

2. CU — 冬のいちごサンドはアプリが先
CUの冬の稼ぎ頭はいちごサンドです。11月6日に「いちごチョコホイップカステラサンド」が5,500ウォンで登場し、11月20日までポケットCUアプリで1日500個限定の予約販売でした。チョコカステラにチョコホイップ、チョコチップ、生いちごを挟んだ166g・452kcalの商品です。予約期間が終わった今は店頭在庫のみで、11月18日からはいちご・オレンジ・シャインマスカットを一度に入れた「フルーツミルクホイップサンド」が店頭に並んでいます。12月には「いちごミルクホイップサンド」も登場予定です。

11月26日からは出版社「無題」と組んだオーディオブック・デザート4種が順次発売。マカロン3,500ウォン、クッキーサンド2,700ウォン、シンクッキー2,800ウォン、トースト3,000ウォン。商品ごとに、ソン・ヘナ作家の小説『一日搬出録』の一部を聴けるQRカード10種のうち1種がランダムで入ります。デザートと一緒に本の一節を買うようなものです。

11月9日からはチーズにつけて食べる「ディッピング」と、とろける「メルティング」のチーズシリーズが順次発売中。リリース写真の店頭表示ではキムチポテトスープ3,700ウォン、チーズプルダック5,700ウォン。電子レンジで温めるとチーズが伸びる冷蔵HMRも含まれます。

3. セブンイレブン — 3,900ウォンのラーメンにご飯が付く
11月19日、歌手ソン・シギョンが企画とレシピ開発に参加した「シギョンpick ノルミョン・リアルアサリチャンポンラーメン」が3,900ウォンで発売。殻付きのアサリを丸ごと入れ、イカとエビのフリーズドライブロック、キクラゲ・キャベツ・チンゲン菜のフレークを加え、一般の油揚げ麺よりデンプンを5ポイント高めてスープが麺に絡むようにしました。今月末まで買うと「ザ・ミシク白米」が無料。NH農協カード・ウリカード・Naver Pay・L.PAYで払うと30%割引も重なります。

11月18日には麗水（ヨス）の新アサリを使った「南海旬のアサリビビンバ」が5,200ウォンで登場。11月30日までBCカード決済で25%引きです。金曜日の今日（11月27日）は「全州式牛肉ビビンバ」が半額の2,350ウォンです。

4. 今日は何を買うべきか — 3つの組み合わせ
① ラーメン＋ご飯：3,900ウォンのラーメンに白米が無料で付き、カード割引まで重なると2,730ウォン前後。今週のコンビニ飯で一番安い組み合わせです。
② ブリオッシュバン＋チーズチキン：12月15日まで2,300ウォン、コーラ込みで3,000ウォン。
③ アサリビビンバ：5,200ウォンからBCカード25%引きで3,900ウォン。11月24日までのラーメン進呈は終了したので、いまは割引だけが残ります。

5. 外国人観光客がレジでそのまま使える3つ
第一に、付加価値税の即時還付です。GS25・CU・セブンイレブンのうち還付端末のある店で、1回15,000ウォン以上100万ウォン未満を買い、支払い前にパスポート原本を見せると税金がその場で引かれます。滞在期間の合計500万ウォンまで、タバコと一部の酒類は対象外。3社あわせて約2,000店が対応し、ソウル・済州・釜山に集中しています（ソウル経済新聞2026年11月17日）。入口にTax Freeのステッカーがある店が該当します。

第二に、アプリ予約の商品は店頭にありません。CUのいちごチョコカステラサンドのようにポケットCU予約だけで売った商品は棚にないので、旅行中は店頭に並んでいる商品を選ぶほうが早いです。

第三に、即食食品は会計後に店内の電子レンジと給湯器を使えます。カップ麺のお湯はレジ横の給湯器で入れ、弁当や蒸しパンは電子レンジで30秒から1分ほど温めます。

6. 聖水・乙支路のローカル食堂3軒
(1) ソムナン聖水カムジャタン — ソウル市城東区ヨンムジャンギル45、02-465-6580。聖水駅4番出口から229m、年中無休24時間。1人用カムジャグクは並12,000ウォン・ウゴジ（干し大根の葉）入り13,000ウォン、カムジャタンは小32,000・中37,000・大49,000ウォン、手打ちスジェビ4,000ウォン。予約も番号札もありません。待合席に座れば順番に案内され、全員そろわないと入れません。1人なら専用のカウンター席にすぐ案内されます。駐車は食事時間のみ可、管理費2,000ウォン。外国人には2人前以上必要なカムジャタンより1人用カムジャグクが頼みやすく、残ったスープに4,000ウォンのポックンパ（炒めご飯）を炒めるのがこの店の締め方です。

(2) 元祖マンソンホフ — ソウル市中区ウルジロ13ギル19、02-2274-1040。乙支路3街駅4番出口から徒歩2分、乙支路ノガリ横丁。毎日昼12時開店で、閉店時刻は資料により深夜0時と午前3時に分かれます。予約・駐車不可。ノガリ2,000ウォン、ファンテ2,000ウォン、ニンニクチキン半羽1万ウォン前後、生ビール500ccが1・2階5,000ウォン、屋上5,500ウォン。皆が座るのは階段でしか上がれない屋上なので、18時を過ぎると階段に列ができます。アプリ順番待ちはなく、そのまま並べばOK。注文は席でスタッフに伝え、ノガリは手で裂いてコチュジャンとマヨネーズのソースにつけて食べます。階段がつらければ1・2階の店内席を聞いてみてください。

(3) 安東荘（アンドンジャン） — ソウル市中区ウルジロ124、02-2266-3814。乙支路3街駅10番出口から1分。1948年頃に開業し3代続く中華料理店で、ソウル未来遺産（2013-175）に「ソウルで最も古い中華料理店」として紹介されています。営業は11:30〜21:00、年中無休（韓国観光公社基準）で、地図サービスには20:30閉店と表示するものもあります。駐車不可。カキチャンポン12,000〜13,000ウォン、三鮮うどん11,000ウォン、ジャージャー麺9,000ウォン、焼き餃子9,000ウォン。予約は6人以上の電話のみで、それ未満は当日待ちです。ニンニクとカキを使ったカキチャンポンが看板なので、辛いチャンポンが苦手な人にも食べやすいです。

7. 確認できたこと・できていないこと
確認できたこと：コンビニ6商品の価格とキャンペーン期間は各社リリース（GSリテール11月16日・19日、BGFリテール11月5日・9日・26日、コリアセブン11月12日・15日・17日）と店頭表示の写真、食堂3軒の住所・電話・営業時間は韓国観光公社・ソウル観光（VisitSeoul）と地図サービスの2026年11月27日時点の値です。
確認できていないこと：「フルーツミルクホイップサンド」の価格、12月「いちごミルクホイップサンド」の発売日、マンソンホフの閉店時刻、安東荘の休憩時間の有無、マンソンホフのカード決済可否。訪れる前に店か地図アプリでもう一度確認するのが安全です。"""

ZH = """以下以首尔三大便利店（GS25、CU、7-Eleven）本周的官方新闻稿为依据，整理了现在真正值得买的6款新品和组合价，另附圣水洞与乙支路3家当地人常去、外国游客也多的餐厅地址、营业时间和点单方式。价格和营业时间均截至2026年11月27日。

1. GS25 — 面包和炸鸡分开买，自己组装
11月20日起推出布里欧修面包（800韩元）和芝士夹心炸鸡（2,800韩元）。面包内侧已涂好塔塔酱，把现炸的芝士炸鸡夹进去，就是3,600韩元的手工汉堡。12月15日前两件一起买2,300韩元，再加活动装210ml百事可乐为3,000韩元。这是GS25针对“模迪舒默”（自己组合）趋势推出的商品，在店里组装着吃就是它的正式吃法。

11月19日还推出了配合TOMORROW X TOGETHER第九张迷你专辑的联名三明治“辣甜对半三明治”，售价3,900韩元，一半辣酱一半甜酱，瞄准偶像粉丝需求。

2. CU — 冬季草莓三明治先在App上卖
CU冬季的主力是鲜草莓三明治。11月6日“草莓巧克力奶油卡斯特拉三明治”上市，售价5,500韩元，11月6日至20日在Pocket CU App上每天限量500个预约销售。166克、452千卡，巧克力卡斯特拉夹巧克力奶油、巧克力豆和整颗草莓。预约期已结束，现在只能在门店碰库存；11月18日起门店上架了把草莓、橙子、阳光玫瑰一次装进去的“水果牛奶奶油三明治”，12月还计划推出“草莓牛奶奶油三明治”。

11月26日起，CU与出版社“无题”合作的4款有声书甜点陆续上市：马卡龙3,500韩元、曲奇夹心2,700韩元、薄曲奇2,800韩元、吐司3,000韩元。每件随机附赠10种QR卡中的1种，扫码可听成海娜小说《一日搬出录》的片段，等于买甜点顺带买一页书。

11月9日起，蘸着吃和拉丝芝士的“芝士蘸酱·融化”系列陆续上市。按新闻稿照片里的门店标价，泡菜土豆汤3,700韩元、芝士辣鸡5,700韩元，还包括微波加热后能拉丝的冷藏即食餐。

3. 7-Eleven — 3,900韩元的拉面还送一碗饭
11月19日，歌手成始璄参与企划和配方开发的“成始璄pick 惊人真蛤蜊海鲜面”上市，售价3,900韩元。整只带壳蛤蜊加上鱿鱼、虾的冻干块，配木耳、卷心菜、小白菜配料，淀粉含量比普通油炸面高约5个百分点，让汤汁挂在面上。本月内购买送一包“The Michel白米饭”，用NH农协卡、友利卡、Naver Pay或L.PAY付款还能叠加30%折扣。

11月18日推出使用丽水新蛤蜊的“南海时令蛤蜊拌饭”，售价5,200韩元，11月30日前用BC卡结算打75折。今天是周五（11月27日），“全州式牛肉拌饭”半价2,350韩元。

4. 今天该买什么 — 三种组合
① 拉面加米饭：3,900韩元的拉面送白饭，再叠加刷卡折扣大约2,730韩元，是本周最便宜的便利店一餐。
② 布里欧修面包加芝士炸鸡：12月15日前2,300韩元，加可乐3,000韩元。
③ 蛤蜊拌饭：5,200韩元用BC卡打75折为3,900韩元。11月24日前的赠拉面活动已结束，现在只剩折扣。

5. 外国游客在收银台能直接用的三件事
第一是增值税即时退税。在GS25、CU、7-Eleven设有退税终端的门店，单笔消费满15,000韩元、低于100万韩元，付款前出示护照原件，税金当场扣除。停留期间合计上限500万韩元，烟和部分酒类不在范围内。三家公司合计约2,000家门店可办理，集中在首尔、济州和釜山（首尔经济新闻2026年11月17日）。门口贴有Tax Free标识的就是。

第二，只在App预约的商品门店没有。像CU草莓巧克力卡斯特拉三明治那样只在Pocket CU预约销售的，货架上不会摆，旅行时直接挑陈列商品更快。

第三，即食食品结账后用店里的微波炉和热水器即可。杯面到收银台旁的热水器接水，盒饭和蒸包放进微波炉转30秒到1分钟。

6. 圣水洞·乙支路3家本地餐厅
(1) 有名圣水土豆排骨汤 — 首尔城东区练武场街45，02-465-6580。圣水站4号出口229米，全年无休24小时。单人土豆汤饭原味12,000韩元、加干萝卜叶13,000韩元；土豆排骨汤小份32,000、中份37,000、大份49,000韩元，手工面片4,000韩元。不接受预约，也没有号码牌：坐在等候区，店员按顺序叫号，必须同行人全部到齐才能入场。一个人可直接去单人吧台席，不用排队。停车仅限用餐时间，收管理费2,000韩元。对外国游客来说，两人份起点的排骨汤不如单人土豆汤饭好点；当地人标准的收尾是在剩汤里加4,000韩元的炒饭。

(2) 元祖万善Hof — 首尔中区乙支路13街19，02-2274-1040。乙支路3街站4号出口步行2分钟，就在乙支路烤干明太鱼（노가리）胡同。每天中午12点开门，关门时间资料不一，有的写午夜、有的写凌晨3点。不接受预约，不能停车。烤干明太鱼2,000韩元、干明太鱼2,000韩元、蒜香炸鸡半只约1万韩元，500cc生啤一二层5,000韩元、顶层5,500韩元。大家都坐只能走楼梯上去的顶层露台，过了下午6点楼梯上就排队。没有App排号，直接排队即可。点单在座位上叫店员，干明太鱼用手撕开蘸辣椒酱蛋黄酱吃。楼梯不方便的话可以问一二层的室内座位。

(3) 安东庄 — 首尔中区乙支路124，02-2266-3814。乙支路3街站10号出口1分钟。1948年前后开业、传至第三代的中餐厅，被首尔未来遗产（2013-175）介绍为“首尔最古老的中餐厅”。营业时间11:30至21:00、全年无休（韩国观光公社标准），部分地图应用标为20:30结束。不可停车。牡蛎海鲜面12,000至13,000韩元、三鲜乌冬11,000韩元、炸酱面9,000韩元、煎饺9,000韩元。预约只接受6人以上电话预订，其余现场等位。招牌是加了蒜和牡蛎的牡蛎海鲜面，怕辣的人也能吃。

7. 已确认与未确认
已确认：6款便利店商品的价格与活动期间来自各公司新闻稿（GS零售11月16日、19日，BGF零售11月5日、9日、26日，Korea Seven 11月12日、15日、17日）和新闻稿照片中的门店标价；3家餐厅的地址、电话、营业时间来自韩国观光公社、首尔观光（VisitSeoul）和地图服务2026年11月27日的数值。
未确认：“水果牛奶奶油三明治”的价格、12月“草莓牛奶奶油三明治”的上市日期、万善Hof的关门时间、安东庄是否有休息时间、万善Hof能否刷卡。出发前在门店或地图应用再确认一次更稳妥。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "convenience-food",
    "postType": "guide",
    "store": "GS25 · CU · 7-Eleven · Seoul Local",
    "priceKrw": 0,
    "releaseDate": "2026-11-27",
    "rating": 5,
    "imageUrl": C,
    "images": [C, G1, G2, G3, G4, G5, G6],
    "affiliateUrl": "https://signal.k-trand.store",
    "affiliatePlatform": "ConvenienceStore",
    "i18n": {
        "ko": {
            "title": "3,900원 라면에 즉석밥 무료… 이번 주 편의점 3사 신상 6종과 성수·을지로 맛집 3곳",
            "summary": "GS25 브리오슈번+치즈쏙치킨 2,300원, CU 생딸기 샌드 5,500원, 세븐일레븐 꼬막비빔밥 5,200원까지. 공식 보도자료로 확인한 신상 6종의 가격·기간·꿀조합과, 성수·을지로 로컬 맛집 3곳의 위치·영업시간·외국인 주문 팁을 2026년 11월 27일 기준으로 정리했습니다.",
            "description": KO,
            "tasteReview": [
                "GS25: 브리오슈번 800원 + 치즈쏙치킨 2,800원, 11/20~12/15 동시 구매 2,300원(펩시 210ml 포함 3,000원)",
                "CU: 딸기 초코 휩 카스텔라 샌드 5,500원(11/6~20 포켓CU 하루 500개 한정), 무제 오디오북 디저트 4종 2,700~3,500원",
                "세븐일레븐: 놀면리얼바지락짬뽕라면 3,900원 + 백미밥 증정(11월 말까지), 남해안제철꼬막비빔밥 5,200원(BC카드 25%)",
                "맛집 3곳: 소문난성수감자탕(24시간·예약 불가), 원조만선호프(노가리 2,000원·루프탑), 안동장(1948년·굴짬뽕)",
                "외국인 팁: 편의점 부가세 즉시환급은 1회 15,000원 이상부터, 여권 원본 필요",
            ],
            "tips": "사진은 GS25·CU·세븐일레븐이 배포한 공식 보도자료 사진을 3:4로 잘라 쓰고, 맛집 위치는 OpenStreetMap 지도(© OpenStreetMap contributors, ODbL)로 표시했습니다. 생성 이미지는 한 장도 쓰지 않았습니다. 가격·영업시간은 2026년 11월 27일 기준이며 매장과 지점에 따라 다를 수 있습니다.",
        },
        "en": {
            "title": "A 3,900-won ramen that comes with free rice: six new convenience-store items and three Seongsu·Euljiro restaurants",
            "summary": "GS25's brioche burger set at 2,300 won, CU's 5,500-won strawberry sandwich, 7-Eleven's 5,200-won cockle bibimbap — six new items with prices, promo dates and the cheapest combinations, plus addresses, hours and ordering tips for three local restaurants in Seongsu and Euljiro, as of 27 November 2026.",
            "description": EN,
            "tasteReview": [
                "GS25: brioche bun 800 won + cheese chicken 2,800 won; 2,300 won for the pair until 15 Dec (3,000 won with Pepsi 210ml)",
                "CU: strawberry choco whip castella sand 5,500 won (app-only, 500 a day, 6–20 Nov); Muje audiobook desserts 2,700–3,500 won",
                "7-Eleven: clam jjamppong ramen 3,900 won with free rice until end of November; cockle bibimbap 5,200 won (25% off with BC Card)",
                "Three restaurants: Somunnan Seongsu Gamjatang (24h, no reservations), Manseon Hof (nogari 2,000 won, rooftop), Andongjang (since 1948, oyster jjamppong)",
                "Visitor tip: instant VAT refund at convenience stores from 15,000 won per transaction, physical passport required",
            ],
            "tips": "Photos are official press images distributed by GS25, CU and 7-Eleven, cropped to 3:4; restaurant locations are drawn on OpenStreetMap (© OpenStreetMap contributors, ODbL). No AI-generated images were used. Prices and hours are as of 27 November 2026 and vary by store and branch.",
        },
        "ja": {
            "title": "3,900ウォンのラーメンにご飯が無料 — 今週のコンビニ新商品6つと聖水・乙支路の食堂3軒",
            "summary": "GS25のブリオッシュバン＋チーズチキン2,300ウォン、CUの生いちごサンド5,500ウォン、セブンイレブンのアサリビビンバ5,200ウォンまで。公式リリースで確認した新商品6つの価格・期間・お得な組み合わせと、聖水・乙支路のローカル食堂3軒の場所・営業時間・外国人向け注文のコツを2026年11月27日時点でまとめました。",
            "description": JA,
            "tasteReview": [
                "GS25：ブリオッシュバン800ウォン＋チーズチキン2,800ウォン、12/15まで2つで2,300ウォン（ペプシ210ml込み3,000ウォン）",
                "CU：いちごチョコホイップカステラサンド5,500ウォン（11/6〜20アプリ1日500個限定）、無題オーディオブックデザート4種2,700〜3,500ウォン",
                "セブンイレブン：アサリチャンポンラーメン3,900ウォン＋白米進呈（11月末まで）、アサリビビンバ5,200ウォン（BCカード25%引き）",
                "食堂3軒：ソムナン聖水カムジャタン（24時間・予約不可）、元祖マンソンホフ（ノガリ2,000ウォン・屋上）、安東荘（1948年・カキチャンポン）",
                "外国人向け：コンビニの付加価値税即時還付は1回15,000ウォン以上、パスポート原本が必要",
            ],
            "tips": "写真はGS25・CU・セブンイレブンが配布した公式リリース写真を3:4にトリミングして使用し、食堂の位置はOpenStreetMap（© OpenStreetMap contributors, ODbL）で示しました。生成画像は1枚も使っていません。価格と営業時間は2026年11月27日時点で、店舗により異なる場合があります。",
        },
        "zh": {
            "title": "3,900韩元拉面送一碗饭 — 本周三大便利店6款新品与圣水·乙支路3家餐厅",
            "summary": "从GS25布里欧修面包加芝士炸鸡2,300韩元、CU鲜草莓三明治5,500韩元，到7-Eleven蛤蜊拌饭5,200韩元。依据官方新闻稿核实6款新品价格、活动期与最划算组合，并附圣水、乙支路3家餐厅的地址、营业时间和外国游客点单技巧，数据截至2026年11月27日。",
            "description": ZH,
            "tasteReview": [
                "GS25：布里欧修面包800韩元＋芝士炸鸡2,800韩元，12月15日前两件2,300韩元（含210ml百事3,000韩元）",
                "CU：草莓巧克力奶油卡斯特拉三明治5,500韩元（11月6—20日App每日限量500个）；无题有声书甜点4款2,700—3,500韩元",
                "7-Eleven：真蛤蜊海鲜面3,900韩元送白饭（截至11月底），蛤蜊拌饭5,200韩元（BC卡75折）",
                "3家餐厅：有名圣水土豆排骨汤（24小时、不可预约）、元祖万善Hof（干明太鱼2,000韩元、露台）、安东庄（1948年、牡蛎海鲜面）",
                "游客提示：便利店增值税即时退税单笔满15,000韩元起，需护照原件",
            ],
            "tips": "照片使用GS25、CU、7-Eleven发布的官方新闻稿图片裁成3:4，餐厅位置以OpenStreetMap（© OpenStreetMap contributors, ODbL）标注，未使用任何AI生成图片。价格与营业时间为2026年11月27日数据，门店之间可能不同。",
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
