#!/usr/bin/env python3
"""유니클로 2026 겨울 감사제 일정·가격 총정리 (4개국어) → Supabase posts + ISR revalidate.

근거
 - 일정·감사 가격·사은품 조건: 유니클로 코리아 공식 감사제 페이지
   https://www.uniqlo.com/kr/ko/special-feature/cp/thanksday (2026-11-25 15:10 KST 확인)
 - 보도자료: 유니클로 2026-11-24 배포 (뉴스핌·조선비즈·뉴스1·스포츠서울·국민일보 등)
 - 제품 정가: 유니클로 공식몰 검색·상품 페이지 노출가 (2026-11-25 15:20 KST)
 - 제품 사진: image.uniqlo.com 공식 상품컷 3:4 원본 1200×1600, AI 생성 0장
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
SLUG = "uniqlo-thanks-festival-2026-two-weeks"

K = "https://www.coupang.com/np/search?q="
TAG = "&lptag=AF9412775"


def q(s):
    return K + quote(s) + TAG


COVER = "/images/products/uniqlo-puftech-parka-men.jpg"
G1 = "/images/products/uniqlo-cashmere-crew-women.jpg"
G2 = "/images/products/uniqlo-heattech-crew-men.jpg"
G3 = "/images/products/uniqlo-fleece-fullzip-men.jpg"
G4 = "/images/products/uniqlo-puftech-parka-women.jpg"
G5 = "/images/products/uniqlo-heattech-cashmere-crew.jpg"
G6 = "/images/products/uniqlo-seamless-down-parka.jpg"
G7 = "/images/products/uniqlo-merino-rib-turtle-women.jpg"
G8 = "/images/products/uniqlo-merino-turtle-men.jpg"

KO_DESC = """유니클로 코리아가 2026년 겨울 감사제를 11월 27일(금)부터 12월 10일(목)까지 14일간 연다. 감사제를 2주로 여는 것은 6년 만이다. 슬로건은 "감사의 마음으로 준비한 특별한 2주"이고, 행사는 1탄(11월 27일~12월 3일)과 2탄(12월 4일~12월 10일)으로 나뉜다. 1탄은 캐시미어·퍼프테크·후리스·히트텍, 2탄은 히트텍 캐시미어 블렌드·심리스 다운 파카·메리노 터틀넥이 중심이다. 오늘(11월 25일)은 행사 시작 이틀 전이고, 온라인 스토어의 1탄 사은품은 11월 27일 오전 2시 30분부터 선착순으로 풀린다.

1. 일정부터 정리
1탄은 11월 27일(금)~12월 3일(목), 2탄은 12월 4일(금)~12월 10일(목)이다. 두 주 모두 전국 매장과 온라인 스토어에서 동시에 열리고, 감사 가격 제품과 사은품이 주차마다 바뀐다. 참고로 지금(11월 20일~26일)은 감사제가 아니라 '기간한정 특별가격' 주간이다. 퍼프테크 재킷 69,900원, 수플레 얀 크루넥 스웨터 29,900원 같은 가격은 감사제와 다른 행사이므로, 27일 이후 가격과 같은 상품인지 반드시 제품명으로 확인해야 한다.

2. 1탄(11/27~12/3) 감사 가격
성인 캐시미어 크루넥 스웨터 129,000원 → 99,900원(29,100원, 22.6% 할인). 100% 캐시미어 소재이고, 이번 시즌 처음으로 9만 원대에 내려온다.
성인 히트텍 이너웨어 16,900원 → 14,900원(2,000원, 11.8%). 남성은 반팔이 제외된다.
후리스 풀집 재킷 39,900원 → 29,900원(10,000원, 25.1%). 1탄에서 할인율이 가장 큰 성인 아우터다.
PUFFTECH 파카 89,900원 → 69,900원(20,000원, 22.2%).
KIDS 히트텍 이너웨어 12,900원 → 9,900원, KIDS 후리스 풀집 재킷 29,900원 → 19,900원.
성인 4개 품목을 한 벌씩 담으면 275,700원이 214,600원이 된다. 61,100원(22.2%)이 빠지는 계산이다.

3. 2탄(12/4~12/10) 감사 가격
히트텍 캐시미어 블렌드 엑스트라웜 5종 24,900원 → 19,900원(5,000원, 20.1%). 이번 시즌 첫 프로모션 가격이다.
남성 심리스 다운 파카 169,000원 → 149,000원(20,000원, 11.8%). 2탄에서 할인 금액이 가장 크지만 할인율은 11.8%로 가장 낮다.
메리노 터틀넥 스웨터 49,900원 → 39,900원, 웜 보아 스웨트 팬츠 49,900원 → 39,900원(각 10,000원, 20.0%).
히트텍 액세서리 일부 19,900원~ → 14,900원~.
KIDS 히트텍 엑스트라웜 코튼 이너웨어 16,900원 → 14,900원, KIDS 보아 스웨트 팬츠 29,900원 → 19,900원.
성인 대표 4품목(히트텍 캐시미어 블렌드·심리스 다운 파카·메리노 터틀넥·웜 보아 팬츠) 기준으로는 293,700원이 248,700원, 45,000원이 빠진다.

4. 사은품은 '10만 원' 한 칸에서 갈린다
감사제 기간 1건의 구매가 10만 원 이상이면 주차별 사은품을 준다. 1탄은 포켓터블 여행용 파우치 2종 세트(S 26×20×10cm, M 40×26×10cm), 2탄은 포켓터블 더플백(50×20×30cm)이다. 색상은 블랙·브라운(2탄은 네이비·퍼플 추가)이고 온라인 단독 색상(파우치 스카이 / 더플백 핑크·스카이·베이지)도 있지만, 색상은 선택이 아니라 랜덤 증정이다.
중요한 것은 '합산 불가'다. 6만 원을 결제한 뒤 같은 날 5만 원을 더 결제해도 11만 원으로 인정되지 않는다. 1건이 10만 원을 넘어야 한다. 온라인은 1탄 11월 27일 오전 2시 30분, 2탄 12월 4일 오전 2시 30분부터 기간 내 선착순이고 재고가 떨어지면 조기에 끝난다. 오프라인 매장은 11월 27일~12월 10일 매일 매장 오픈 시점부터 일별 선착순이며, 매장별 수량이 따로다. '매장으로 배송'은 온라인 기준, ORDER&PICK은 주문 매장 기준으로 사은품이 배정된다. 예약 판매 제품만 산 경우는 대상에서 빠지고, 환불로 결제액이 10만 원 아래로 내려가면 사은품을 반납해야 한다.

5. 10만 원에 100원·200원 모자라는 조합
1탄에서 캐시미어 크루넥 스웨터만 사면 99,900원이다. 10만 원에 100원이 모자라 사은품 대상이 아니다. 여기에 히트텍 이너웨어 14,900원을 더하면 114,800원이 되고, 캐시미어와 히트텍을 함께 받는다. 퍼프테크 파카(69,900원)와 후리스 풀집 재킷(29,900원)을 함께 사면 99,800원으로 200원이 부족하다. 이때 히트텍 삭스 7,900원짜리 한 켤레를 더하면 107,700원으로 기준을 넘는다. 2탄은 심리스 다운 파카 149,000원 한 벌만으로 이미 10만 원을 넘는다.

6. 공식 목록에 아직 없는 것
11월 23일 공개된 공식 '감사 가격 제품' 목록에는 울트라라이트 다운 재킷과 히트텍 립 터틀넥이 없다. 검색에서 자주 섞이는 품목이지만, 공식 페이지는 "11월 27일 1탄에서 더 많은 제품을 기대해달라"고만 적고 있다. 2주 행사인 만큼 1탄 시작일과 2탄 시작일에 품목이 추가 공개될 가능성이 크므로, 특정 제품을 노린다면 27일과 12월 4일에 공식 페이지를 다시 확인하는 편이 안전하다. 반대로 지금 확정된 품목은 위 1·2탄 목록이 전부다.

7. 매장과 온라인 중 어디가 유리한가
가격은 같고 사은품 재고 기준이 다르다. 온라인은 1탄·2탄 첫날 새벽 2시 30분에 사은품이 열리고, 인기 색상은 그 시간에 대부분 소진된다. 매장은 오픈 시각부터 일별로 풀리므로 아침 일찍 갈 수 있다면 매장이 유리하고, 사이즈·색상 선택 폭은 온라인 스토어(스페셜 컬러 포함)가 넓다. 27일 오전 10시에는 패션 유튜버 쏭자매와 함께하는 감사제 특별 라이브도 예정돼 있다.

한 줄 정리
2026 유니클로 감사제는 11월 27일~12월 10일, 1탄은 캐시미어·후리스·퍼프테크·히트텍, 2탄은 히트텍 캐시미어 블렌드·심리스 다운 파카·메리노 터틀넥이다. 가장 큰 할인율은 후리스 풀집 재킷 25.1%, 가장 큰 할인 금액은 심리스 다운 파카 20,000원이다. 사은품은 10만 원을 넘긴 '한 건'에만 붙으므로, 99,900원·99,800원처럼 100원·200원 모자라는 조합만 피하면 같은 돈으로 한 가지를 더 받는다."""

EN_DESC = """Uniqlo Korea is running its 2026 Winter Thank You Festival from Friday 27 November to Thursday 10 December — fourteen days, and the first time in six years the event stretches to two weeks. The slogan is "two special weeks prepared with gratitude," and the sale splits into Wave 1 (27 Nov–3 Dec) and Wave 2 (4–10 Dec). Wave 1 centres on cashmere, PUFFTECH, fleece and HEATTECH; Wave 2 on HEATTECH cashmere blend, the seamless down parka and merino turtlenecks. As of 25 November the event has not started, and online gifts open at 02:30 on 27 November.

1. The schedule
Wave 1: 27 November (Fri) – 3 December (Thu). Wave 2: 4 December (Fri) – 10 December (Thu). Both run in stores nationwide and on the online store at the same time, and both the sale items and the gift change week by week. Note that the current promotion (20–26 November) is a separate "limited-time special price" week — a PUFFTECH jacket at 69,900 won or a soufflé yarn crew-neck at 29,900 won belongs to that event, not to the Thank You Festival, so check product names before comparing with post-27 November prices.

2. Wave 1 prices (27 Nov–3 Dec)
Adult cashmere crew-neck sweater 129,000 → 99,900 won (29,100 won off, 22.6%). It is 100% cashmere, and this is the first time this season it reaches the 90,000-won band.
Adult HEATTECH innerwear 16,900 → 14,900 won (2,000 won off, 11.8%). For men, short sleeves are excluded.
Fleece full-zip jacket 39,900 → 29,900 won (10,000 won off, 25.1%) — the deepest percentage cut among adult outerwear in Wave 1.
PUFFTECH parka 89,900 → 69,900 won (20,000 won off, 22.2%).
KIDS HEATTECH innerwear 12,900 → 9,900 won; KIDS fleece full-zip jacket 29,900 → 19,900 won.
One of each of the four adult items comes to 275,700 won before and 214,600 won during — 61,100 won (22.2%) saved.

3. Wave 2 prices (4–10 Dec)
HEATTECH cashmere blend extra warm, five styles: 24,900 → 19,900 won (5,000 won off, 20.1%), the first promotional price of the season.
Men's seamless down parka 169,000 → 149,000 won (20,000 won off, 11.8%) — the largest amount off in Wave 2 and the smallest percentage.
Merino turtleneck sweater 49,900 → 39,900 won; warm boa sweat pants 49,900 → 39,900 won (10,000 won off each, 20.0%).
Selected HEATTECH accessories from 19,900 → from 14,900 won.
KIDS HEATTECH extra warm cotton innerwear 16,900 → 14,900 won; KIDS boa sweat pants 29,900 → 19,900 won.
The four headline adult items (HEATTECH cashmere blend, seamless down parka, merino turtleneck, warm boa pants) go from 293,700 to 248,700 won — 45,000 won saved.

4. The gift turns on a single 100,000-won order
During the event, one order of 100,000 won or more earns that week's gift: a two-piece pocketable travel pouch set in Wave 1 (S 26×20×10cm, M 40×26×10cm) and a pocketable duffle bag in Wave 2 (50×20×30cm). Colours are black and brown (Wave 2 adds navy and purple), with online-only colours (sky for the pouch; pink, sky and beige for the duffle), but the colour is random, not chosen.
The order cannot be split or combined: paying 60,000 won and then 50,000 won the same day does not count as 110,000. Online gifts open at 02:30 on 27 November and 4 December and run while stock lasts, ending early when it runs out. In stores the gift is given daily from opening, 27 November to 10 December, with separate stock per store. "Ship to store" orders follow online stock; ORDER&PICK follows the pickup store's stock. Orders of pre-sale items only are excluded, and if a refund drops the order below 100,000 won the gift must be returned.

5. Where 100 or 200 won decides the gift
In Wave 1, the cashmere crew-neck alone is 99,900 won — 100 won short, so no gift. Add a 14,900-won HEATTECH top and the order is 114,800 won, with both the sweater and the innerwear. The PUFFTECH parka (69,900) plus the fleece full-zip (29,900) comes to 99,800 won, 200 won short; one pair of HEATTECH socks at 7,900 won takes it to 107,700 and over the line. In Wave 2 the seamless down parka at 149,000 won clears 100,000 on its own.

6. What is not on the official list yet
The official "sale price products" list published on 23 November does not include the Ultra Light Down jacket or the HEATTECH rib turtleneck, although both circulate in search results. The official page only says more products will come with Wave 1 on 27 November. Since this is a two-week event, more items are likely to appear on 27 November and 4 December; if you are targeting a specific product, check the official page again on those dates. Everything confirmed so far is the Wave 1 and Wave 2 list above.

7. Store or online
Prices are identical; gift stock rules differ. Online gifts open at 02:30 on the first day of each wave and popular colours usually go then. Stores release gifts daily from opening, so an early visit helps if you can make it; the online store has the wider size and colour range, including special colours. A special live stream with fashion creator Song sisters is scheduled for 10:00 on 27 November.

Bottom line
The 2026 Uniqlo Thank You Festival runs 27 November to 10 December. Wave 1 is cashmere, fleece, PUFFTECH and HEATTECH; Wave 2 is HEATTECH cashmere blend, the seamless down parka and merino turtlenecks. The deepest percentage cut is the fleece full-zip at 25.1%; the biggest amount off is 20,000 won on the seamless down parka. The gift attaches only to a single order above 100,000 won, so avoiding combinations that land at 99,900 or 99,800 won is worth one more item for the same money."""

JA_DESC = """ユニクロ韓国が2026年冬の「感謝祭」を11月27日（金）から12月10日（木）まで14日間開催する。感謝祭が2週間にわたるのは6年ぶりだ。スローガンは「感謝の気持ちで用意した特別な2週間」で、第1弾（11月27日〜12月3日）と第2弾（12月4日〜12月10日）に分かれる。第1弾はカシミヤ・パフィテック・フリース・ヒートテック、第2弾はヒートテックカシミヤブレンド・シームレスダウンパーカ・メリノタートルネックが中心となる。11月25日現在は開催前で、オンラインの第1弾ギフトは11月27日午前2時30分から先着で始まる。

1. 日程
第1弾は11月27日（金）〜12月3日（木）、第2弾は12月4日（金）〜12月10日（木）。全国の店舗とオンラインストアで同時に開催され、セール価格の商品もギフトも週ごとに変わる。なお現在（11月20日〜26日）は感謝祭ではなく「期間限定特別価格」の週だ。パフィテックジャケット69,900ウォン、スフレヤーンクルーネック29,900ウォンといった価格は別イベントであり、27日以降の価格と比較する前に商品名で確認する必要がある。

2. 第1弾（11/27〜12/3）の価格
レディース・メンズ カシミヤクルーネックスウェーター 129,000→99,900ウォン（29,100ウォン引き、22.6%）。カシミヤ100%で、今シーズン初めて9万ウォン台になる。
ヒートテックインナー 16,900→14,900ウォン（2,000ウォン引き、11.8%）。メンズは半袖が対象外。
フリースフルジップジャケット 39,900→29,900ウォン（10,000ウォン引き、25.1%）。第1弾の大人用アウターで割引率が最も高い。
パフィテックパーカ 89,900→69,900ウォン（20,000ウォン引き、22.2%）。
KIDSヒートテックインナー 12,900→9,900ウォン、KIDSフリースフルジップジャケット 29,900→19,900ウォン。
大人用4品を各1点買うと275,700ウォンが214,600ウォンになり、61,100ウォン（22.2%）安くなる。

3. 第2弾（12/4〜12/10）の価格
ヒートテックカシミヤブレンド エクストラウォーム5種 24,900→19,900ウォン（5,000ウォン引き、20.1%）。今シーズン初のプロモーション価格。
メンズ シームレスダウンパーカ 169,000→149,000ウォン（20,000ウォン引き、11.8%）。第2弾で割引額は最大だが割引率は最も低い。
メリノタートルネックスウェーター 49,900→39,900ウォン、ウォームボアスウェットパンツ 49,900→39,900ウォン（各10,000ウォン引き、20.0%）。
ヒートテックアクセサリー一部 19,900ウォン〜→14,900ウォン〜。
KIDSヒートテック エクストラウォームコットンインナー 16,900→14,900ウォン、KIDSボアスウェットパンツ 29,900→19,900ウォン。
大人用の代表4品（ヒートテックカシミヤブレンド、シームレスダウンパーカ、メリノタートルネック、ウォームボアパンツ）では293,700ウォンが248,700ウォンになり、45,000ウォン安くなる。

4. ギフトは「10万ウォン」の1件で決まる
期間中、1回の購入が10万ウォン以上なら週ごとのギフトがもらえる。第1弾はポケッタブルトラベルポーチ2種セット（S 26×20×10cm、M 40×26×10cm）、第2弾はポケッタブルダッフルバッグ（50×20×30cm）。色はブラック・ブラウン（第2弾はネイビー・パープルも）で、オンライン限定色（ポーチはスカイ、ダッフルはピンク・スカイ・ベージュ）もあるが、色は選べずランダム進呈だ。
重要なのは合算できないこと。6万ウォンを払ったあと同日に5万ウォンを追加で払っても11万ウォンとは認められない。1件で10万ウォンを超える必要がある。オンラインは第1弾が11月27日午前2時30分、第2弾が12月4日午前2時30分から期間中先着で、在庫が尽きれば早期終了する。店舗は11月27日〜12月10日に毎日開店時点から日別先着で、店舗ごとに数量が異なる。「店舗へ配送」はオンライン基準、ORDER&PICKは注文店舗基準でギフトが割り当てられる。予約販売商品のみの購入は対象外で、返品で決済額が10万ウォンを下回るとギフトを返却する必要がある。

5. 100ウォン・200ウォン足りない組み合わせ
第1弾でカシミヤクルーネックスウェーターだけを買うと99,900ウォン。10万ウォンに100ウォン足りず対象外だ。ここにヒートテックインナー14,900ウォンを足すと114,800ウォンになり、カシミヤとインナーを一緒に受け取れる。パフィテックパーカ（69,900ウォン）とフリースフルジップ（29,900ウォン）の組み合わせは99,800ウォンで200ウォン足りない。この場合はヒートテックソックス7,900ウォンを1足足せば107,700ウォンで基準を超える。第2弾はシームレスダウンパーカ149,000ウォン1点だけで10万ウォンを超える。

6. 公式リストにまだないもの
11月23日に公開された公式の「感謝価格商品」リストに、ウルトラライトダウンジャケットとヒートテックリブタートルネックは入っていない。検索でよく混ざる商品だが、公式ページは「11月27日の第1弾でより多くの商品を期待してほしい」とだけ書いている。2週間のイベントだけに、第1弾・第2弾の開始日に商品が追加公開される可能性が高い。特定の商品が目的なら27日と12月4日に公式ページを再確認するのが安全だ。逆に、いま確定しているのは上記の第1弾・第2弾のリストがすべてである。

7. 店舗とオンラインのどちらが有利か
価格は同じで、ギフト在庫の基準が違う。オンラインは各弾初日の午前2時30分にギフトが解放され、人気色はその時間にほぼなくなる。店舗は開店時点から日別に配られるので、朝早く行けるなら店舗が有利だ。サイズと色の選択肢はオンライン（スペシャルカラー含む）が広い。11月27日午前10時にはファッション系ユーチューバー「ソン姉妹」との感謝祭特別ライブも予定されている。

まとめ
2026年ユニクロ感謝祭は11月27日〜12月10日。第1弾はカシミヤ・フリース・パフィテック・ヒートテック、第2弾はヒートテックカシミヤブレンド・シームレスダウンパーカ・メリノタートルネック。割引率が最も高いのはフリースフルジップの25.1%、割引額が最も大きいのはシームレスダウンパーカの20,000ウォン。ギフトは10万ウォンを超える「1件」にだけ付くので、99,900ウォン・99,800ウォンのように100ウォン・200ウォン足りない組み合わせだけ避ければ、同じ金額でもう1品受け取れる。"""

ZH_DESC = """优衣库韩国将于2026年11月27日（周五）至12月10日（周四）举办冬季"感谢祭"，共14天。感谢祭延长至两周是6年来首次。口号是"以感谢之心准备的特别两周"，活动分为第1波（11月27日—12月3日）和第2波（12月4日—12月10日）。第1波以羊绒、PUFFTECH、摇粒绒、HEATTECH为主，第2波以HEATTECH羊绒混纺、无缝羽绒大衣、美利奴高领毛衣为主。11月25日尚未开始，线上第1波赠品从11月27日凌晨2点30分起先到先得。

1. 日程
第1波：11月27日（周五）—12月3日（周四）。第2波：12月4日（周五）—12月10日（周四）。全国门店与线上商店同时举行，折扣商品和赠品每周更换。需要注意的是，现在（11月20日—26日）是"限期特别价格"周，并非感谢祭。PUFFTECH夹克69,900韩元、苏芙蕾纱圆领毛衣29,900韩元属于另一活动，与27日之后的价格比较前必须核对商品名称。

2. 第1波（11/27—12/3）价格
成人羊绒圆领毛衣 129,000→99,900韩元（降29,100韩元，22.6%）。100%羊绒，本季首次进入9万韩元区间。
成人HEATTECH内衣 16,900→14,900韩元（降2,000韩元，11.8%）；男款短袖不参加。
摇粒绒全拉链夹克 39,900→29,900韩元（降10,000韩元，25.1%），是第1波成人外套中折扣率最高的。
PUFFTECH大衣 89,900→69,900韩元（降20,000韩元，22.2%）。
KIDS HEATTECH内衣 12,900→9,900韩元，KIDS摇粒绒全拉链夹克 29,900→19,900韩元。
四件成人单品各买一件，275,700韩元变为214,600韩元，省下61,100韩元（22.2%）。

3. 第2波（12/4—12/10）价格
HEATTECH羊绒混纺极暖5款 24,900→19,900韩元（降5,000韩元，20.1%），本季首次促销价。
男款无缝羽绒大衣 169,000→149,000韩元（降20,000韩元，11.8%），第2波降幅金额最大但降幅比例最低。
美利奴高领毛衣 49,900→39,900韩元，保暖抓绒卫裤 49,900→39,900韩元（各降10,000韩元，20.0%）。
部分HEATTECH配件 19,900韩元起→14,900韩元起。
KIDS HEATTECH极暖棉质内衣 16,900→14,900韩元，KIDS抓绒卫裤 29,900→19,900韩元。
以四件成人代表单品计算，293,700韩元变为248,700韩元，省下45,000韩元。

4. 赠品取决于"10万韩元"这一笔订单
活动期间单笔购买满10万韩元即可获赠当周礼品：第1波为可收纳旅行收纳袋2件套（S 26×20×10cm、M 40×26×10cm），第2波为可收纳行李袋（50×20×30cm）。颜色为黑色、棕色（第2波另有藏青、紫色），也有线上限定色（收纳袋天蓝；行李袋粉、天蓝、米色），但颜色随机发放，不能挑选。
关键是不可合并：先付6万韩元、当天再付5万韩元，不会被认定为11万韩元，必须单笔超过10万韩元。线上第1波从11月27日凌晨2点30分、第2波从12月4日凌晨2点30分起，活动期内先到先得，库存售完即提前结束。门店在11月27日—12月10日每天开店起按日先到先得，各店数量不同。"配送至门店"按线上库存，ORDER&PICK按取货门店库存发放。只购买预售商品不在赠送范围，若退款后金额低于10万韩元需退还赠品。

5. 差100韩元、200韩元的组合
第1波只买羊绒圆领毛衣是99,900韩元，差100韩元不达标。再加一件14,900韩元的HEATTECH内衣就是114,800韩元，毛衣和内衣都能拿到。PUFFTECH大衣（69,900）加摇粒绒全拉链夹克（29,900）合计99,800韩元，差200韩元；再加一双7,900韩元的HEATTECH袜子即107,700韩元，超过门槛。第2波的无缝羽绒大衣149,000韩元单件就已超过10万韩元。

6. 官方清单上还没有的
11月23日公开的官方"感谢价格商品"清单中，没有Ultra Light Down羽绒服和HEATTECH罗纹高领。这两款在搜索结果中常被混入，但官方页面只写"11月27日第1波将有更多商品"。活动长达两周，第1波与第2波开始日很可能追加公开商品；若锁定某件商品，建议在27日和12月4日再查官方页面。反之，目前已确定的就是上述第1波与第2波清单。

7. 门店还是线上
价格相同，赠品库存规则不同。线上在各波首日凌晨2点30分开放赠品，热门颜色几乎当场售罄。门店每天开店起发放，能早去则门店更有利；尺码和颜色选择线上更广（含特别色）。11月27日上午10点还有与时尚博主"宋姐妹"的感谢祭特别直播。

一句话总结
2026优衣库感谢祭为11月27日—12月10日。第1波是羊绒、摇粒绒、PUFFTECH、HEATTECH，第2波是HEATTECH羊绒混纺、无缝羽绒大衣、美利奴高领。折扣率最高的是摇粒绒全拉链夹克25.1%，降幅金额最大的是无缝羽绒大衣20,000韩元。赠品只给单笔超过10万韩元的订单，只要避开99,900、99,800韩元这种差100、200韩元的组合，同样的钱就能多拿一件。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "k-fashion",
    "store": "유니클로",
    "priceKrw": 69900,
    "releaseDate": "2026-11-25",
    "rating": 4.7,
    "imageUrl": COVER,
    "images": [G1, G2, G3, G4, G5, G6, G7, G8],
    "affiliateUrl": "https://www.uniqlo.com/kr/ko/special-feature/cp/thanksday",
    "affiliatePlatform": "Uniqlo",
    "exampleItems": [
        {
            "name": "유니클로 캐시미어 크루넥 스웨터 (여성)",
            "brand": "UNIQLO",
            "priceKrw": 99900,
            "imageUrl": G1,
            "url": q("유니클로 캐시미어 크루넥 스웨터"),
            "category": "1탄 · 129,000→99,900원",
        },
        {
            "name": "유니클로 히트텍 크루넥T(9부) (남성)",
            "brand": "UNIQLO",
            "priceKrw": 14900,
            "imageUrl": G2,
            "url": q("유니클로 히트텍 크루넥 티셔츠"),
            "category": "1탄 · 16,900→14,900원",
        },
        {
            "name": "유니클로 후리스 풀집 재킷",
            "brand": "UNIQLO",
            "priceKrw": 29900,
            "imageUrl": G3,
            "url": q("유니클로 후리스 풀집 재킷"),
            "category": "1탄 · 39,900→29,900원",
        },
        {
            "name": "유니클로 PUFFTECH 파카 (남성)",
            "brand": "UNIQLO",
            "priceKrw": 69900,
            "imageUrl": COVER,
            "url": q("유니클로 퍼프테크 파카"),
            "category": "1탄 · 89,900→69,900원",
        },
        {
            "name": "유니클로 히트텍 캐시미어 블렌드 크루넥T 엑스트라웜",
            "brand": "UNIQLO",
            "priceKrw": 19900,
            "imageUrl": G5,
            "url": q("유니클로 히트텍 캐시미어 블렌드"),
            "category": "2탄 · 24,900→19,900원",
        },
        {
            "name": "유니클로 심리스 다운 파카 (남성)",
            "brand": "UNIQLO",
            "priceKrw": 149000,
            "imageUrl": G6,
            "url": q("유니클로 심리스 다운 파카"),
            "category": "2탄 · 169,000→149,000원",
        },
        {
            "name": "유니클로 메리노 립 터틀넥 스웨터 (여성)",
            "brand": "UNIQLO",
            "priceKrw": 39900,
            "imageUrl": G7,
            "url": q("유니클로 메리노 터틀넥 스웨터"),
            "category": "2탄 · 49,900→39,900원",
        },
    ],
    "i18n": {
        "ko": {
            "title": "유니클로 감사제 2026, 6년 만에 2주로 늘었다…1탄 27일·2탄 12월 4일 뭐가 얼마나 싸지나",
            "summary": "11월 27일~12월 10일, 1탄은 캐시미어·후리스·퍼프테크·히트텍, 2탄은 히트텍 캐시미어 블렌드·심리스 다운 파카·메리노 터틀넥. 공식 감사 가격과 10만 원 사은품 조건, 100원·200원 모자라는 조합까지 숫자로 정리했습니다.",
            "description": KO_DESC,
            "tasteReview": [
                "1탄(11/27~12/3): 캐시미어 크루넥 129,000→99,900원, 후리스 풀집 39,900→29,900원, 퍼프테크 파카 89,900→69,900원, 히트텍 16,900→14,900원",
                "2탄(12/4~12/10): 히트텍 캐시미어 블렌드 24,900→19,900원, 심리스 다운 파카 169,000→149,000원, 메리노 터틀넥 49,900→39,900원",
                "사은품은 1건 10만 원 이상 — 99,900원(캐시미어 단독)은 100원 부족, 99,800원(퍼프테크+후리스)은 200원 부족",
                "11/23 공개된 공식 목록에 울트라라이트 다운·히트텍 립 터틀넥은 없음, 11/27 추가 공개 예고",
            ],
            "tips": "가격은 2026년 11월 25일 유니클로 코리아 공식 감사제 페이지와 공식몰 노출가 기준이며, 매장·재고·쿠폰에 따라 달라질 수 있습니다. 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있습니다.",
        },
        "en": {
            "title": "Uniqlo Korea's Thank You Festival 2026 runs two weeks for the first time in six years — every price in Wave 1 and Wave 2",
            "summary": "27 November to 10 December. Wave 1: cashmere, fleece, PUFFTECH, HEATTECH. Wave 2: HEATTECH cashmere blend, seamless down parka, merino turtleneck. The official prices, the 100,000-won gift rule, and the combinations that miss it by 100 won.",
            "description": EN_DESC,
            "tasteReview": [
                "Wave 1 (27 Nov–3 Dec): cashmere crew-neck 129,000→99,900 won, fleece full-zip 39,900→29,900, PUFFTECH parka 89,900→69,900, HEATTECH 16,900→14,900",
                "Wave 2 (4–10 Dec): HEATTECH cashmere blend 24,900→19,900 won, seamless down parka 169,000→149,000, merino turtleneck 49,900→39,900",
                "The gift needs a single 100,000-won order: 99,900 won for the cashmere alone is 100 won short, 99,800 for parka plus fleece is 200 won short",
                "The official 23 November list has no Ultra Light Down or HEATTECH rib turtleneck; more items are promised for 27 November",
            ],
            "tips": "Prices are from Uniqlo Korea's official festival page and store listings on 25 November 2026 and may change with store, stock and coupons. This post contains affiliate links and may earn a commission.",
        },
        "ja": {
            "title": "ユニクロ感謝祭2026は6年ぶり2週間 — 11/27第1弾・12/4第2弾の価格を全部確認",
            "summary": "11月27日〜12月10日。第1弾はカシミヤ・フリース・パフィテック・ヒートテック、第2弾はヒートテックカシミヤブレンド・シームレスダウンパーカ・メリノタートルネック。公式価格と10万ウォンギフトの条件、100ウォン足りない組み合わせまで数字で整理。",
            "description": JA_DESC,
            "tasteReview": [
                "第1弾(11/27〜12/3): カシミヤクルーネック129,000→99,900ウォン、フリースフルジップ39,900→29,900ウォン、パフィテックパーカ89,900→69,900ウォン、ヒートテック16,900→14,900ウォン",
                "第2弾(12/4〜12/10): ヒートテックカシミヤブレンド24,900→19,900ウォン、シームレスダウンパーカ169,000→149,000ウォン、メリノタートルネック49,900→39,900ウォン",
                "ギフトは1件10万ウォン以上 — カシミヤ単品99,900ウォンは100ウォン不足、パーカ+フリース99,800ウォンは200ウォン不足",
                "11/23公開の公式リストにウルトラライトダウン・ヒートテックリブタートルネックはなし、11/27に追加公開予告",
            ],
            "tips": "価格は2026年11月25日のユニクロ韓国公式感謝祭ページと公式ストア表示価格です。店舗・在庫・クーポンにより変わります。本記事はアフィリエイトリンクを含み、手数料を受け取る場合があります。",
        },
        "zh": {
            "title": "优衣库韩国2026感谢祭：6年来首次两周，11月27日第1波与12月4日第2波实价清单",
            "summary": "11月27日至12月10日。第1波为羊绒、摇粒绒、PUFFTECH、HEATTECH，第2波为HEATTECH羊绒混纺、无缝羽绒大衣、美利奴高领。官方价格、10万韩元赠品规则，以及差100韩元的组合一并整理。",
            "description": ZH_DESC,
            "tasteReview": [
                "第1波(11/27—12/3)：羊绒圆领129,000→99,900韩元，摇粒绒全拉链39,900→29,900韩元，PUFFTECH大衣89,900→69,900韩元，HEATTECH 16,900→14,900韩元",
                "第2波(12/4—12/10)：HEATTECH羊绒混纺24,900→19,900韩元，无缝羽绒大衣169,000→149,000韩元，美利奴高领49,900→39,900韩元",
                "赠品需单笔满10万韩元——羊绒单件99,900韩元差100韩元，大衣加摇粒绒99,800韩元差200韩元",
                "11月23日官方清单中无Ultra Light Down与HEATTECH罗纹高领，11月27日将追加公开",
            ],
            "tips": "价格为2026年11月25日优衣库韩国官方感谢祭页面与官方商店显示价，可能因门店、库存和优惠券而变化。本文含联盟链接，可能获得佣金。",
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
    urllib.request.urlopen(urllib.request.Request(REVALIDATE_URL), timeout=90)
    print("[+] Revalidated")
except Exception as e:
    print(f"[-] Revalidate error: {e}")
