#!/usr/bin/env python3
"""트랙2 — 블랙프라이데이 D-DAY 40만원대 노캔 헤드폰 A vs B (4개국어).

근거 (2026-11-27 08:20~08:40 KST 직접 확인)
 - 소니코리아 WH-1000XM6 제품·사양 페이지: 정가 619,000원(6색), 무게 254g, NC 30h/40h,
   통화 24h(NC), 충전 약 3.5h, BT 5.3, SBC/AAC/LDAC/LC3, 구성품(USB·3.5mm·케이스)
 - 쿠팡 '소니 WH-1000XM6' 검색: 소니 브랜드샵 619,000 → 와우할인 29% 439,000원(2일 남음), 리뷰 1,595·평점 5.0
 - 보스코리아 공식몰 QC 울트라 헤드폰 2세대: 519,000 → 489,000원(6%, 타임세일 3일), 예상 최저 454,770원,
   리퍼브 452,000원, 2년 A/S, 14일 100% 반품·환불, 반품 배송비 6,000원, 260g, BT 5.4, USB-C 오디오
 - 쿠팡 '보스 QC 울트라 2세대': 519,000 → 467,700원(9%), 리뷰 404
 - 소니코리아 겨울 캠페인(2026-11-16 보도자료·씨넷코리아): 11/16~2027/1/31 구매, 2027/2/9까지 정품등록 시
   WH-1000XM6 신세계 상품권 5만원
 - 제품 이미지: 소니 공식(sony.scene7.com) 3색, 보스 공식몰(cdn.imweb.me) 3색 → 1200x1600 정규화. AI 생성 0장.
"""
from brand_bf_common import publish, q

SLUG = "sony-wh1000xm6-vs-bose-qc-ultra-2-blackfriday-2026"

S1 = "/images/products/hd-sony-xm6-black.jpg"
S2 = "/images/products/hd-sony-xm6-platinum.jpg"
S3 = "/images/products/hd-sony-xm6-midnight.jpg"
B1 = "/images/products/hd-bose-ultra2-black.jpg"
B2 = "/images/products/hd-bose-ultra2-white.jpg"
B3 = "/images/products/hd-bose-ultra2-desert.jpg"

KO = """2026년 11월 27일은 블랙프라이데이다. 노이즈 캔슬링 헤드폰 시장에서 매년 가장 많이 비교되는 두 제품, 소니 WH-1000XM6와 보스 QC 울트라 헤드폰 2세대를 같은 날 가격으로 놓고 봤다. 정가 차이 10만 원이 오늘 실제 결제가에서도 그대로 유지되는지, 스펙과 반품 조건까지 확인했다.

1. 오늘 가격 — 소니 43만 9,000원, 보스 46만 7,700원
소니 WH-1000XM6의 정가는 619,000원이다. 쿠팡 소니 브랜드샵 기준 오늘 판매가는 와우할인 29%를 적용한 439,000원이고, 1,595개 리뷰에 평점 5.0이 붙어 있다. 샌드 스톤과 샌드 핑크는 459,000원에서 같은 439,000원으로 내려와 있다. 소니코리아 공식 스토어에서는 아직 619,000원이다. 9~11월에 진행했던 12만 원 할인 기획전이 11월 18일에 끝났기 때문이다.
보스 QC 울트라 헤드폰 2세대의 정가는 519,000원이다. 보스 공식몰은 블랙프라이데이 타임세일로 6% 할인한 489,000원에 팔고 있고, 회원 쿠폰을 적용하면 454,770원까지 내려간다. 쿠팡에서는 467,700원이다. 공식몰에는 리퍼브 상품이 452,000원에 따로 올라와 있는데, 이건 정품 신품이 아니라 리퍼브(6개월 A/S)다.
두 제품을 쿠팡 기준으로 비교하면 소니가 28,700원 싸다. 정가 차이(10만 원)와 실제 결제가 차이(2만 8,700원)가 세 배 넘게 벌어진 이유는 소니의 할인 폭이 훨씬 컸기 때문이다. 보스 공식몰 쿠폰가(454,770원)와 비교하면 격차는 15,770원으로 줄어든다.
색상별 가격 차이도 확인해야 한다. 소니는 6색 모두 439,000원으로 맞춰져 있고, 보스는 색상에 따라 재고와 가격이 조금씩 다르다.

2. 스펙 — 숫자가 갈리는 지점은 다섯 개
무게는 소니 254g, 보스 260g이다. 6g 차이는 손에 쥐었을 때보다 머리에 얹었을 때 체감이 크다. 헤드밴드 압력과 이어쿠션 형태가 다르기 때문에 무게만으로 우열을 가를 수는 없다.
배터리는 노이즈 캔슬링을 켠 상태에서 둘 다 최대 30시간이다. 끈 상태로는 소니 40시간, 보스는 몰입형 오디오를 켜면 23시간으로 줄어든다. 통화는 소니가 최대 24시간(NC 켬)이다.
충전은 소니가 약 3.5시간이고, 3분 충전으로 최대 3시간을 재생하는 급속 충전을 지원한다. 보스는 15분 충전으로 2.5시간을 쓰는 방식이다.
연결은 소니 블루투스 5.3에 LDAC·LC3, 보스 블루투스 5.4에 aptX Adaptive·Lossless다. 아이폰에서는 둘 다 AAC로 연결되므로 코덱 차이가 사라진다. 안드로이드 고음질을 원하면 소니의 LDAC이 유리하고, 퀄컴 계열 기기라면 보스의 aptX 계열이 맞는다.
유선 연결이 갈리는 지점이다. 보스는 USB-C로 디지털 오디오를 받아 무손실로 들을 수 있고 충전하면서 재생할 수 있다. 소니의 USB-C 포트는 충전용이며, 유선은 동봉된 3.5mm 케이블로 연결한다. 노트북 한 대에 USB-C 케이블 하나로 붙여 쓰려면 보스 쪽이 편하다.

3. 착용감과 소리 성향
소니 XM6는 헤어밴드를 넓히고 비건 가죽을 쓴 것이 특징이다. 30mm 드라이버에 12개 마이크, QN3 프로세서를 얹었고, 마스터링 엔지니어와 함께 튜닝했다고 밝혔다. 저음을 두텁게 깔기보다 보컬과 악기 분리를 살리는 쪽이다.
보스 QC 울트라는 이어쿠션의 비대칭 설계와 헤드밴드 쿠션으로 압박을 줄인 구조다. 개인 맞춤 사운드(CustomTune)가 귀 모양에 맞춰 음향을 보정하고, 몰입형 오디오 모드가 별도로 있다.
구매평에서 가장 자주 나오는 차이는 착용감이다. 보스 공식몰 구매평에는 "소니를 사서 써보고 반품한 뒤 보스로 왔다, 착용감이 특히 편하다"는 내용이 있고, 쿠팡 리뷰에서도 장시간 착용을 이유로 보스를 고르는 사례가 반복된다. 반대로 소니는 무게가 가볍고 접이식이라 이동이 많은 사람에게 유리하다는 평이 많다. 두 제품 모두 직접 써보지 않고 정리한 비교이므로, 착용감은 매장에서 10분 이상 써보고 결정하는 편이 안전하다.

4. 통화·연결 기능
소니는 빔포밍 마이크로 목소리를 배경 소음에서 분리하고, 헤드폰 자체에서 음소거를 할 수 있다. LE Audio를 지원해 게임 지연을 줄였고, 멀티포인트로 두 기기를 동시에 붙일 수 있다. 퀵 어텐션은 손으로 이어컵을 덮으면 대화 모드로 바뀌는 기능이다.
보스는 AI 기반 배경 소음 억제와 보이스 컨트롤을 내세운다. 2세대에서 블루투스 5.4로 올라갔고, 스냅드래곤 사운드와 구글 패스트 페어를 지원한다. 통화 품질은 두 제품 모두 실내에서는 큰 차이가 없다는 평이 우세하고, 바람 부는 야외에서 갈린다는 후기가 많다.

5. A/S와 반품 — 여기서 갈리면 총비용이 달라진다
보스는 국내 정품 기준 2년 A/S를 준다. 공식몰에서 사면 수령 후 14일 이내 100% 반품·환불 보장이 붙는다. 다만 반품 배송비는 편도 6,000원이고, 타임딜·리퍼브 상품은 이 보장에서 빠진다. 12개월 무이자 할부는 11월 한정이다.
소니는 이번 겨울 캠페인으로 정품등록 사은품을 준다. 11월 16일부터 2027년 1월 31일까지 소니 공식 온·오프라인 스토어, 판매점, 네이버 브랜드 스토어에서 사고, 2027년 2월 9일까지 정품등록과 사은품 신청을 하면 WH-1000XM6는 신세계 상품권 5만 원권을 받는다. 현금 할인은 아니지만 실질 혜택으로 계산할 수 있다. 쿠팡에서 사도 이 프로모션 대상인지는 구매 전에 소니코리아 안내로 확인해야 한다.
해외 구매는 계산이 다르다. 쿠팡 로켓직구로 들어오는 XM6는 47만~49만 원대에 올라와 있지만 국내 A/S가 제한될 수 있고, 도착도 12월 1~2일로 늦다. 국내 정품과 가격 차이가 3만~5만 원이면 A/S 기간을 감안해 정품을 고르는 편이 낫다.

6. 그래서 어느 쪽인가
노트북에 USB-C로 붙여 무손실로 듣고, 하루 8시간 이상 착용하며, 반품 보장을 원한다면 보스 QC 울트라 2세대다. 오늘 쿠팡 467,700원, 공식몰 쿠폰가 454,770원이다.
가볍게 들고 다니고, 통화와 게임 지연을 신경 쓰고, 같은 조건에서 2만~3만 원이라도 아끼고 싶다면 소니 WH-1000XM6다. 쿠팡 439,000원에 정품등록 상품권 5만 원까지 붙으면 체감가는 38만 원대까지 내려간다.
안드로이드 고음질 코덱(LDAC)이 필요하면 소니, 퀄컴 aptX 계열 기기와 붙여 쓴다면 보스로 정리된다. 아이폰만 쓴다면 코덱 차이가 없으니 착용감과 유선 연결로 결정하면 된다.
두 제품 모두 40만~50만 원대이므로, 3만 원 차이로 2년을 쓰는 조건이 달라진다고 보면 된다. 가격이 비슷할 때는 A/S 기간과 반품 조건이 실질적인 가치를 만든다.

7. 오늘 사기 전에 확인할 것
첫째, 소니 439,000원은 쿠팡 와우 회원가다. 와우가 아니면 표시가가 달라진다. 쿠팡 상품 페이지에 '와우할인·2일 남음'이 붙어 있으니 남은 기간을 확인해야 한다.
둘째, 보스 공식몰 타임세일은 종료 시각이 정해져 있다. 오늘 오전 확인 기준 3일 남짓 남았고, 수량이 떨어지면 조기 종료된다. 쿠팡 가격(467,700원)과 공식몰 쿠폰가(454,770원) 중 어느 쪽이 유리한지는 결제 직전에 다시 봐야 한다.
셋째, 리퍼브와 신품을 구분해야 한다. 보스 공식몰의 452,000원 상품은 리퍼브로 A/S가 6개월이다. 3만 원 아끼고 보증을 1년 6개월 줄이는 셈이므로, 오래 쓸 생각이면 신품이 낫다.
넷째, 색상과 재고다. 소니는 6색 모두 같은 가격이지만 인기 색은 배송일이 밀린다. 보스는 색상별 재고 편차가 크다.
다섯째, 유선 사용 계획이다. USB-C 유선이 필요하면 보스, 3.5mm면 둘 다 된다. 이 조건 하나로 선택이 끝나는 경우가 많다.

한 줄 정리
오늘 기준 소니 WH-1000XM6는 쿠팡 439,000원, 보스 QC 울트라 2세대는 쿠팡 467,700원·공식몰 쿠폰가 454,770원이다. 3만 원 차이로 갈리므로 스펙보다 조건을 보면 된다. USB-C 무손실과 2년 A/S·14일 반품은 보스, 254g 경량·LDAC·정품등록 상품권 5만 원은 소니다. 블랙프라이데이 타임세일은 수량이 떨어지면 조기 종료되므로, 색상과 재고를 확인한 뒤 결제하는 편이 안전하다.

※ 이 글은 쿠팡 파트너스 활동의 일환으로 일정액의 수수료를 받을 수 있습니다. 가격 비교 링크는 쿠팡 검색 결과로 연결됩니다. 네이버 크리에이터샵(https://cshop.naver.com/jaenam)의 '겨울 재택 데스크 셋업' 컬렉션에서도 관련 상품을 모아 볼 수 있습니다. 가격은 2026년 11월 27일 오전 확인값이며 판매처·회원 등급·쿠폰에 따라 달라집니다."""

EN = """Black Friday 2026 falls on 27 November. Two over-ear noise-cancelling headphones get compared more than any others in this market, Sony's WH-1000XM6 and Bose's QuietComfort Ultra Headphones (2nd Gen), so we put them side by side at today's prices. The list price gap is 100,000 won; what matters is whether that gap survives at checkout, and what the specs and return terms change.

1. Today's price: Sony 439,000 won, Bose 467,700 won
Sony's WH-1000XM6 lists at 619,000 won. On Coupang's Sony brand store it sells for 439,000 won after a 29% Wow discount today, with 1,595 reviews at 5.0. The Sandstone and Sand Pink options are down from 459,000 to the same 439,000. Sony Korea's own store still shows 619,000 won: the 120,000-won promotion that ran from September ended on 18 November.
Bose's QuietComfort Ultra 2nd Gen lists at 519,000 won. Bose Korea's official store runs a Black Friday time sale at 489,000 won, 6% off, and a member coupon brings it to 454,770 won. Coupang shows 467,700 won. The official store also lists a refurbished unit at 452,000 won, which is not new stock and carries six months of warranty.
On Coupang, Sony is 28,700 won cheaper today. The list-price gap of 100,000 won shrank because Sony cut far deeper. Against Bose's coupon price of 454,770 won, the gap is 15,770 won.
Colours matter too. All six Sony colours sit at 439,000 won, while Bose stock and price vary by colour.

2. Specs: five places where the numbers split
Weight is 254g for Sony and 260g for Bose. Six grams is felt on your head more than in your hand, and headband pressure and cushion shape differ, so weight alone does not decide comfort.
Battery with noise cancelling on is up to 30 hours for both. With it off, Sony runs 40 hours; Bose drops to 23 hours when immersive audio is on. Sony rates calls at up to 24 hours with ANC.
Sony charges in about 3.5 hours and supports 3 minutes of charging for up to 3 hours of playback. Bose's quick charge gives 2.5 hours from 15 minutes.
Connectivity is Bluetooth 5.3 with LDAC and LC3 on Sony, Bluetooth 5.4 with aptX Adaptive and Lossless on Bose. On an iPhone both fall back to AAC, so the codec difference disappears. For high-resolution audio on Android, Sony's LDAC is the advantage; on Qualcomm hardware, Bose's aptX family fits better.
Wired use is the clearest split. Bose accepts digital audio over USB-C, lossless, and can play while charging. Sony's USB-C port is for charging; wired listening goes through the included 3.5mm cable. If you want one USB-C cable from a laptop, Bose is the easier answer.

3. Comfort and sound
Sony widened the headband and uses vegan leather, with a 30mm driver, 12 microphones and the QN3 processor, tuned with mastering engineers. It leans toward vocal and instrument separation rather than a thick low end.
Bose uses an asymmetric ear cushion and headband cushion to reduce pressure, and CustomTune calibrates sound to your ears. Immersive audio is a separate mode.
The difference buyers mention most is comfort. Reviews on Bose's own store include one buyer who returned the Sony and switched, citing comfort above all; Coupang reviews repeat the pattern for long sessions. Sony is lighter and folds, which suits people who carry it daily. Neither of us wore both for a week, so try them in a store for at least ten minutes.

4. Calls and connection
Sony's beamforming microphones separate voice from noise, and the headset can mute itself. LE Audio cuts game latency, multipoint holds two devices, and Quick Attention switches to conversation when you cup the earcup.
Bose advertises AI-based background noise suppression and voice control, moved to Bluetooth 5.4, and supports Snapdragon Sound and Google Fast Pair. Reviews put call quality close indoors, with differences outdoors in wind.

5. Warranty and returns change the total cost
Bose gives two years of warranty on Korean official stock. Bought from its official store, it adds a 100% return and refund guarantee within 14 days, though return shipping is 6,000 won each way and time-deal or refurbished units are excluded. Twelve-month interest-free instalments are a November offer.
Sony's winter campaign pays a gift certificate for registering the product. Buy between 16 November and 31 January 2027 from Sony's official online or offline stores, resellers or the Naver brand store, register by 9 February 2027, and the WH-1000XM6 earns a 50,000-won Shinsegae gift certificate. It is not cash, but it counts. Whether a Coupang purchase qualifies should be checked with Sony Korea first.
Imports price differently. Grey-market XM6 units on Coupang's Rocket Direct run 470,000-490,000 won, may lack Korean service, and arrive on 1-2 December. If the gap to official stock is 30,000-50,000 won, the warranty is usually worth more.

6. Which one
If you want USB-C lossless from a laptop, wear them eight hours a day, and value a return guarantee, take the Bose QuietComfort Ultra 2nd Gen: 467,700 won on Coupang, 454,770 won with the official store coupon.
If you carry them daily, care about calls and game latency, and want to save 20,000-30,000 won, take the Sony WH-1000XM6: 439,000 won on Coupang, and with the 50,000-won registration certificate the effective price drops into the 380,000-won range.
Need LDAC on Android and Sony wins; using Qualcomm aptX and Bose wins. On iPhone only, the codec difference disappears, so decide on comfort and wired use.
Both sit in the 400,000-500,000 won range, so a 30,000-won difference is really a choice about two years of ownership. When prices are close, warranty and return terms create the value.

7. Before you pay today
First, Sony's 439,000 won is a Coupang Wow member price. The page shows a Wow discount with two days left, so check the clock.
Second, Bose's official time sale has an end time. It had about three days left this morning and can close early if stock runs out. Compare 467,700 won on Coupang against 454,770 won with the coupon at checkout.
Third, separate refurbished from new. Bose's 452,000-won unit is refurbished with six months of warranty. Saving 30,000 won while losing 18 months of cover is a bad trade for a long-term purchase.
Fourth, colours and stock. Sony's six colours cost the same but popular ones ship later; Bose varies more by colour.
Fifth, wired plans. USB-C means Bose, 3.5mm works on both. This single condition often ends the decision.

One line
Today Sony's WH-1000XM6 is 439,000 won on Coupang, Bose's QuietComfort Ultra 2nd Gen is 467,700 won there and 454,770 won with the official store coupon. A 30,000-won gap means conditions matter more than specs: USB-C lossless, two years of warranty and 14-day returns favour Bose; 254g, LDAC and a 50,000-won registration certificate favour Sony. Black Friday time sales close early when stock runs out, so check colour and stock before paying.

This post contains affiliate links and may earn a commission; comparison links open Coupang search results. Related items are collected in the winter desk setup collection at the Naver Creator Shop (https://cshop.naver.com/jaenam). Prices were checked on the morning of 27 November 2026 and vary by seller, membership tier and coupon."""

JA = """2026年11月27日はブラックフライデーだ。ノイズキャンセリングヘッドホンで毎年最も比較される2機種、ソニーWH-1000XM6とボーズQCウルトラヘッドホン第2世代を、同じ日の価格で並べた。定価差10万ウォンが実際の支払額でも残るのか、仕様と返品条件まで確認した。

1. 今日の価格 — ソニー43万9,000ウォン、ボーズ46万7,700ウォン
ソニーWH-1000XM6の定価は619,000ウォン。クーパンのソニーブランドストアでは本日、ワウ割引29%で439,000ウォン、レビュー1,595件で評価5.0。サンドストーンとサンドピンクは459,000ウォンから同じ439,000ウォンになっている。ソニーコリアの公式ストアはまだ619,000ウォンで、9〜11月の12万ウォン割引が11月18日に終わったためだ。
ボーズQCウルトラ第2世代の定価は519,000ウォン。ボーズ公式モールはブラックフライデーのタイムセールで6%引きの489,000ウォン、会員クーポンで454,770ウォンまで下がる。クーパンでは467,700ウォン。公式モールにはリファービッシュ品が452,000ウォンであるが、これは新品ではなく保証6か月だ。
クーパンで比べるとソニーが28,700ウォン安い。定価差10万ウォンが縮んだのはソニーの値引きが大きいためだ。ボーズ公式のクーポン価格454,770ウォンと比べれば差は15,770ウォンになる。
色ごとの差も確認したい。ソニーは6色とも439,000ウォン、ボーズは色によって在庫と価格が異なる。

2. 仕様 — 数字が分かれる5点
重さはソニー254g、ボーズ260g。6gの差は手より頭で感じる。ヘッドバンドの圧力とイヤークッションの形が違うため、重さだけで優劣は決められない。
バッテリーはノイズキャンセリングを入れて両者とも最大30時間。切るとソニー40時間、ボーズは没入オーディオを入れると23時間に減る。通話はソニーが最大24時間（NCオン）。
充電はソニーが約3.5時間で、3分充電で最大3時間再生する急速充電に対応。ボーズは15分で2.5時間だ。
接続はソニーがBluetooth 5.3でLDAC・LC3、ボーズが5.4でaptX Adaptive・Lossless。iPhoneでは両者AACになるためコーデック差は消える。Androidの高音質ならソニーのLDAC、クアルコム系ならボーズのaptXが合う。
有線が最もはっきり分かれる。ボーズはUSB-Cでデジタル音声をロスレスで受け、充電しながら再生できる。ソニーのUSB-Cは充電用で、有線は同梱の3.5mmケーブルを使う。ノートPCからUSB-C1本でつなぎたいならボーズが楽だ。

3. 装着感と音の傾向
ソニーはヘッドバンドを広げビーガンレザーを採用。30mmドライバーに12個のマイク、QN3プロセッサを載せ、マスタリングエンジニアと調整した。低音を厚くするよりボーカルと楽器の分離を生かす方向だ。
ボーズはイヤークッションの非対称設計とヘッドバンドのクッションで圧迫を減らす。個人向けサウンド調整（CustomTune）が耳の形に合わせて補正し、没入オーディオは別モードになる。
購入レビューで最も多い違いは装着感だ。ボーズ公式のレビューには「ソニーを買って返品しボーズにした、装着感が圧倒的に楽」という声があり、クーパンでも長時間使用を理由にボーズを選ぶ例が繰り返される。ソニーは軽く折りたためるため持ち歩きに向く。両方を1週間使った比較ではないので、店頭で10分以上試すのが安全だ。

4. 通話と接続
ソニーはビームフォーミングで声を雑音から分離し、ヘッドホン自体でミュートできる。LE Audioでゲーム遅延を抑え、マルチポイントで2台接続。クイックアテンションはイヤーカップを手で覆うと会話モードになる。
ボーズはAIによる背景ノイズ抑制とボイスコントロールを掲げ、第2世代でBluetooth 5.4になった。Snapdragon SoundとGoogle Fast Pairに対応する。通話品質は屋内では差が小さいという評価が多く、風のある屋外で分かれる。

5. 保証と返品で総コストが変わる
ボーズは国内正規品で2年間の保証。公式モール購入なら14日以内の100%返品・返金保証が付くが、返品送料は片道6,000ウォン、タイムセール品とリファービッシュ品は対象外。12か月無利子分割は11月限定だ。
ソニーは冬キャンペーンで製品登録の特典を出す。11月16日から2027年1月31日までにソニー公式のオンライン・実店舗、販売店、Naverブランドストアで購入し、2027年2月9日までに登録すればWH-1000XM6は新世界商品券5万ウォン分がもらえる。現金ではないが実質的な特典だ。クーパン購入が対象かは購入前にソニーコリアに確認したい。
海外購入は計算が違う。クーパンのロケット直購は47万〜49万ウォン台だが国内保証が限られ、到着も12月1〜2日と遅い。正規品との差が3万〜5万ウォンなら保証を取るほうが得だ。

6. どちらを選ぶか
ノートPCとUSB-Cでつなぎロスレスで聴き、1日8時間以上装着し、返品保証が欲しいならボーズQCウルトラ第2世代。今日クーパン467,700ウォン、公式クーポンで454,770ウォン。
軽く持ち歩き、通話とゲーム遅延を気にし、2万〜3万ウォンでも抑えたいならソニーWH-1000XM6。クーパン439,000ウォンに登録特典5万ウォンが付くと実質38万ウォン台になる。
AndroidのLDACが必要ならソニー、クアルコムaptX系ならボーズ。iPhoneだけならコーデック差が消えるので装着感と有線接続で決めればよい。
どちらも40万〜50万ウォン台なので、3万ウォンの差は「2年間の使い方」の選択だ。価格が近いときは保証と返品条件が実質的な価値になる。

7. 今日買う前に確認すること
第一に、ソニーの439,000ウォンはクーパンのワウ会員価格だ。ページには「ワウ割引・残り2日」が出ているので期限を見る。
第二に、ボーズ公式のタイムセールは終了時刻がある。今朝で残り3日ほど、在庫が尽きれば早期終了する。クーパン467,700ウォンと公式クーポン454,770ウォォンのどちらが得かは決済直前に再確認したい。
第三に、リファービッシュと新品を分けること。452,000ウォンの商品はリファービッシュで保証6か月。3万ウォンを節約して1年6か月の保証を失う計算だ。
第四に、色と在庫。ソニーは6色同価格だが人気色は出荷が遅れる。ボーズは色ごとの差が大きい。
第五に、有線の予定。USB-Cならボーズ、3.5mmなら両方。この条件ひとつで決まる場合が多い。

一言まとめ
本日、ソニーWH-1000XM6はクーパン439,000ウォン、ボーズQCウルトラ第2世代はクーパン467,700ウォン・公式クーポン454,770ウォン。3万ウォンの差なので仕様より条件で選ぶ。USB-Cロスレス・2年保証・14日返品はボーズ、254g・LDAC・登録特典5万ウォンはソニー。ブラックフライデーのタイムセールは在庫が尽きると早期終了するため、色と在庫を確認してから決済したい。

本記事はアフィリエイトリンクを含み、手数料を受け取る場合があります。比較リンクはCoupang検索結果に移動します。関連商品はNaverクリエイターショップ（https://cshop.naver.com/jaenam）の冬の在宅デスクセットアップにもまとめています。価格は2026年11月27日午前の確認値で、販売店・会員ランク・クーポンにより変わります。"""

ZH = """2026年11月27日是黑色星期五。降噪耳机市场每年被比较最多的两款产品——索尼WH-1000XM6与Bose QC Ultra头戴式耳机第二代，放在同一天的实价上对比。10万韩元的定价差在今天是否依然存在，规格与退货条件也一并核对。

1. 今天价格：索尼439,000韩元，Bose 467,700韩元
索尼WH-1000XM6定价619,000韩元。Coupang索尼品牌店今日Wow会员7.1折后439,000韩元，评论1,595条、评分5.0。砂岩色与沙粉色从459,000韩元降到同样的439,000韩元。索尼韩国官网仍为619,000韩元：9至11月的12万韩元优惠已于11月18日结束。
Bose QC Ultra第二代定价519,000韩元。Bose官方商城黑五限时特价优惠6%至489,000韩元，会员券可到454,770韩元；Coupang为467,700韩元。官方商城另有翻新品452,000韩元，但那是翻新机，保修仅6个月。
以Coupang比较，索尼便宜28,700韩元。定价差10万韩元被压缩，是因为索尼降幅更大。与Bose官方券后价454,770韩元相比，差距为15,770韩元。
颜色也会影响。索尼六种颜色同为439,000韩元，Bose则因颜色不同在库存和价格上有差异。

2. 规格：五处数字分岔
重量为索尼254g、Bose 260g。6克在头上比在手上更明显，但头梁压力与耳罩形状不同，重量不能单独决定舒适度。
开启降噪时两者最长30小时。关闭降噪时索尼40小时，Bose开启沉浸音频时降至23小时。通话方面索尼最长24小时（开降噪）。
充电方面索尼约3.5小时，支持充电3分钟播放最长3小时。Bose为充电15分钟使用2.5小时。
连接为索尼蓝牙5.3配LDAC、LC3，Bose蓝牙5.4配aptX Adaptive、Lossless。在iPhone上两者都回落到AAC，编解码差异消失。安卓高解析选索尼LDAC，高通平台则Bose的aptX更合适。
有线是最明确的分界。Bose可通过USB-C接收无损数字音频并可边充边听；索尼的USB-C仅用于充电，有线需用随附3.5mm线。若想用一根USB-C线接笔记本，Bose更方便。

3. 佩戴与声音取向
索尼加宽头梁并使用素皮，30mm单元、12个麦克风与QN3处理器，并与母带工程师共同调音，更强调人声与乐器的分离而非厚重低频。
Bose通过非对称耳罩与头梁垫减少压迫，CustomTune根据耳型校准声音，沉浸音频是单独模式。
购买评价中最常见的差异是佩戴感。Bose官方商城评价中有用户表示买了索尼后退货改用Bose，理由是佩戴明显更舒适；Coupang也有不少因长时间佩戴而选择Bose的案例。索尼更轻且可折叠，适合随身携带。这不是我们各自使用一周的对比，建议在门店试戴十分钟以上。

4. 通话与连接
索尼用波束成形把人声与噪声分离，耳机本体可静音；LE Audio降低游戏延迟，多点连接可同时连两台设备，Quick Attention在用手遮住耳罩时切换为对话模式。
Bose主打AI背景噪声抑制与语音控制，第二代升级至蓝牙5.4，支持Snapdragon Sound与Google Fast Pair。室内通话差异不大，户外有风时评价分化。

5. 保修与退货决定总成本
Bose韩国正品提供2年保修。官方商城购买另有14天内100%退货退款保障，但退货运费单程6,000韩元，限时特价与翻新品不适用。12个月免息分期为11月限定。
索尼冬季活动提供产品注册赠礼。11月16日至2027年1月31日在索尼官方线上/线下门店、经销店或Naver品牌店购买，并于2027年2月9日前完成注册，WH-1000XM6可获5万韩元新世界商品券。不是现金，但可计入实得。Coupang购买是否符合资格，需先向索尼韩国确认。
海外购买算法不同。Coupang火箭直购的XM6约47万—49万韩元，但韩国保修可能受限，到货也晚至12月1—2日。与正品差3万—5万韩元时，通常保修更值。

6. 选哪一款
想用USB-C接笔记本听无损、每天佩戴8小时以上、看重退货保障，选Bose QC Ultra第二代：今日Coupang 467,700韩元，官方券后454,770韩元。
想轻便随身、在意通话与游戏延迟、希望省下2万—3万韩元，选索尼WH-1000XM6：Coupang 439,000韩元，加上5万韩元注册商品券，实得价可到38万韩元区间。
需要安卓LDAC选索尼，使用高通aptX设备选Bose。只用iPhone时编解码差异消失，按佩戴感与有线连接决定即可。
两者都在40万—50万韩元区间，3万韩元差其实是“用两年”的条件选择。价格接近时，保修与退货条件构成实际价值。

7. 今天付款前确认
第一，索尼439,000韩元是Coupang Wow会员价。页面显示Wow折扣仅剩2天，需看期限。
第二，Bose官方限时特价有结束时间。今晨约剩3天，库存耗尽会提前结束。Coupang 467,700韩元与官方券后454,770韩元哪个更划算，应在付款前再确认。
第三，区分翻新与全新。452,000韩元为翻新品，保修6个月，等于省3万韩元却少18个月保修。
第四，颜色与库存。索尼六色同价但热门色发货较晚，Bose各色差异较大。
第五，有线计划。USB-C选Bose，3.5mm两者皆可。这一项常常直接决定选择。

一句话总结
今日索尼WH-1000XM6为Coupang 439,000韩元，Bose QC Ultra第二代Coupang 467,700韩元、官方券后454,770韩元。3万韩元差距意味着条件比规格更重要：USB-C无损、2年保修、14天退货利于Bose；254g、LDAC、5万韩元注册商品券利于索尼。黑五限时特价库存耗尽会提前结束，确认颜色与库存后再付款。

本文含联盟链接，可能获得佣金；比价链接跳转至Coupang搜索结果。相关商品也整理在Naver创作者商店（https://cshop.naver.com/jaenam）的“冬季居家桌面布置”系列。价格于2026年11月27日上午确认，因卖家、会员等级与优惠券而异。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "store": "소니 · 보스",
    "priceKrw": 439000,
    "releaseDate": "2026-11-27",
    "rating": 4.8,
    "imageUrl": S1,
    "images": [S1, B1, S2, B2, S3, B3],
    "affiliateUrl": q("소니 WH-1000XM6"),
    "affiliatePlatform": "Coupang",
    "exampleItems": [
        {"name": "소니 WH-1000XM6 (블랙)", "brand": "Sony", "priceKrw": 439000, "imageUrl": S1,
         "url": q("소니 WH-1000XM6 블랙"), "category": "쿠팡 와우 29% · 리뷰 1,595"},
        {"name": "소니 WH-1000XM6 (플래티넘 실버)", "brand": "Sony", "priceKrw": 439000, "imageUrl": S2,
         "url": q("소니 WH-1000XM6 플래티넘 실버"), "category": "6색 동일가 · 무료배송"},
        {"name": "소니 WH-1000XM6 (미드나잇 블루)", "brand": "Sony", "priceKrw": 439000, "imageUrl": S3,
         "url": q("소니 WH-1000XM6 미드나잇 블루"), "category": "254g · LDAC · 접이식"},
        {"name": "보스 QC 울트라 헤드폰 2세대 (블랙)", "brand": "Bose", "priceKrw": 467700, "imageUrl": B1,
         "url": q("보스 QC 울트라 헤드폰 2세대"), "category": "쿠팡 9% · 리뷰 404"},
        {"name": "보스 QC 울트라 헤드폰 2세대 (화이트 스모크)", "brand": "Bose", "priceKrw": 467700, "imageUrl": B2,
         "url": q("보스 QC 울트라 2세대 화이트 스모크"), "category": "공식몰 489,000 · 쿠폰가 454,770"},
        {"name": "보스 QC 울트라 헤드폰 2세대 (데저트 골드)", "brand": "Bose", "priceKrw": 467700, "imageUrl": B3,
         "url": q("보스 QC 울트라 2세대 데저트 골드"), "category": "260g · USB-C 오디오 · 2년 A/S"},
    ],
    "i18n": {
        "ko": {
            "title": "블랙프라이데이 D-DAY, 40만원대 노캔 헤드폰 A vs B — 소니 WH-1000XM6 43만9천 vs 보스 QC 울트라 2세대 46만7천",
            "summary": "오늘 실측: 소니 WH-1000XM6 쿠팡 439,000원(정가 619,000·29%·리뷰 1,595), 보스 QC 울트라 2세대 쿠팡 467,700원·공식몰 쿠폰가 454,770원. 3만 원 차이에서 갈리는 5가지 스펙(무게·배터리·코덱·USB-C 유선·A/S)과 반품 조건을 정리했습니다.",
            "description": KO,
            "tasteReview": [
                "가격: 소니 439,000원(쿠팡 와우 29%) vs 보스 467,700원(쿠팡)·489,000원(공식몰)·쿠폰가 454,770원",
                "무게 254g vs 260g, ANC 30시간 동일, 충전 3.5시간 vs 15분 급속 2.5시간",
                "소니 LDAC·블루투스 5.3 vs 보스 aptX Lossless·5.4, USB-C 무손실 유선은 보스만",
                "A/S: 보스 2년·14일 100% 반품(배송비 6,000원) vs 소니 정품등록 신세계 상품권 5만 원(2027/2/9까지 신청)",
                "리퍼브 452,000원은 6개월 A/S — 신품과 구분 필요",
            ],
            "tips": "가격은 2026년 11월 27일 오전 확인값이며 판매처·회원 등급·쿠폰에 따라 달라집니다. 쿠팡 와우 회원가와 공식몰 타임세일은 기간·수량이 정해져 있습니다. 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있으며 비교 링크는 쿠팡 검색 결과로 연결됩니다. 네이버 크리에이터샵(cshop.naver.com/jaenam)에서 관련 상품을 모아 볼 수 있습니다.",
        },
        "en": {
            "title": "Black Friday D-Day: 400,000-Won Noise-Cancelling A vs B — Sony WH-1000XM6 at 439,000 vs Bose QC Ultra 2nd Gen at 467,700",
            "summary": "Measured today: Sony WH-1000XM6 at 439,000 won on Coupang (list 619,000, 29% off, 1,595 reviews), Bose QC Ultra 2nd Gen at 467,700 won on Coupang and 454,770 won with the official store coupon. The five specs that split a 30,000-won gap, and the return terms that change the total.",
            "description": EN,
            "tasteReview": [
                "Price: Sony 439,000 won (Coupang Wow, 29% off) vs Bose 467,700 won on Coupang, 489,000 in the official store, 454,770 with coupon",
                "Weight 254g vs 260g, 30 hours of ANC on both, 3.5-hour charge vs 15 minutes for 2.5 hours",
                "Sony LDAC and Bluetooth 5.3 vs Bose aptX Lossless and 5.4; USB-C lossless audio is Bose only",
                "Warranty: Bose two years plus 14-day 100% returns (6,000 won shipping) vs Sony's 50,000-won registration gift certificate by 9 February 2027",
                "The 452,000-won refurbished unit carries only six months of warranty",
            ],
            "tips": "Prices were checked on the morning of 27 November 2026 and vary by seller, membership tier and coupon. Coupang Wow pricing and official-store time sales have deadlines and limited stock. This post contains affiliate links and may earn a commission; comparison links open Coupang search results. Related items are in the Creator Shop collection at cshop.naver.com/jaenam.",
        },
        "ja": {
            "title": "ブラックフライデー当日、40万ウォン台ノイキャンA vs B — ソニーWH-1000XM6 43万9千 vs ボーズQCウルトラ第2世代 46万7千",
            "summary": "本日の実測：ソニーWH-1000XM6はクーパン439,000ウォン（定価619,000・29%・レビュー1,595件）、ボーズQCウルトラ第2世代はクーパン467,700ウォン・公式クーポン454,770ウォン。3万ウォン差を分ける5つの仕様と返品条件を整理した。",
            "description": JA,
            "tasteReview": [
                "価格：ソニー439,000ウォン（クーパン29%引き） vs ボーズ467,700ウォン（クーパン）・489,000ウォン（公式）・クーポン454,770ウォン",
                "重さ254g vs 260g、ANC 30時間は共通、充電3.5時間 vs 15分で2.5時間",
                "ソニーLDAC・Bluetooth 5.3 vs ボーズaptX Lossless・5.4、USB-Cロスレス有線はボーズのみ",
                "保証：ボーズ2年・14日100%返品（送料6,000ウォン） vs ソニー製品登録で新世界商品券5万ウォン（2027年2月9日まで申請）",
                "リファービッシュ452,000ウォンは保証6か月 — 新品と区別が必要",
            ],
            "tips": "価格は2026年11月27日午前の確認値で、販売店・会員ランク・クーポンにより変わります。クーパンのワウ価格と公式タイムセールは期間・数量限定です。本記事はアフィリエイトリンクを含み手数料を受け取る場合があり、比較リンクはCoupang検索結果に移動します。関連商品はNaverクリエイターショップ（cshop.naver.com/jaenam）にもまとめています。",
        },
        "zh": {
            "title": "黑色星期五当日，40万韩元级降噪A vs B——索尼WH-1000XM6 43.9万 vs Bose QC Ultra二代 46.77万",
            "summary": "今日实测：索尼WH-1000XM6在Coupang为439,000韩元（定价619,000、29%、评论1,595条），Bose QC Ultra二代Coupang 467,700韩元、官方券后454,770韩元。3万韩元差距由五项规格与退货条件决定。",
            "description": ZH,
            "tasteReview": [
                "价格：索尼439,000韩元（Coupang 29%）vs Bose 467,700韩元（Coupang）、489,000韩元（官方）、券后454,770韩元",
                "重量254g vs 260g，开启降噪均为30小时，充电3.5小时 vs 15分钟用2.5小时",
                "索尼LDAC与蓝牙5.3 vs Bose aptX Lossless与5.4，USB-C无损有线仅Bose支持",
                "保修：Bose 2年、14天100%退货（运费6,000韩元）vs 索尼注册赠5万韩元商品券（2027年2月9日前申请）",
                "翻新品452,000韩元保修仅6个月，需与全新区分",
            ],
            "tips": "价格于2026年11月27日上午确认，因卖家、会员等级和优惠券而异。Coupang Wow价与官方限时特价为期间与数量限定。本文含联盟链接，可能获得佣金；比价链接跳转至Coupang搜索结果。相关商品也整理在Naver创作者商店（cshop.naver.com/jaenam）。",
        },
    },
}

if __name__ == "__main__":
    publish(POST)
