#!/usr/bin/env python3
"""트랙1 — 2026-11-27(금) 미국 블프 반일장 마감 리포트 (4개국어) → Supabase posts + ISR.

실측 근거 (2026-11-28 08:00~08:30 KST 교차 확인)
 - 종가: 다우 50,774.94(+591.99, +1.18%), S&P 500 7,297.49(+114.71, +1.60%),
   나스닥 24,129.50(+543.70, +2.31%), 러셀2000 2,750.30(+46.24, +1.71%)
   — CNBC(11/27 13:11 ET 갱신), Reuters(11/27 17:18 ET), Cedar Global Markets(11/27)
 - 주간: S&P +5.6%(2025-04 이후 최대), 나스닥 +6.68%, 다우 +5.46%(2022-10 이후 최대)
   11월(11/30 하루 남김): S&P −3.7%, 나스닥 −5.1%, S&P는 10/6 사상최고 7,818.93 대비 −6.67%
   VIX 25.13(주간 −30%), 거래량 109.7억 주, NYSE 상승/하락 3.25:1
 - 반도체: 필라델피아 반도체지수 9,186.71(+4.7%), 마이크론 646.95(+7.6%), 마벨 +7.3%,
   AMD 424.54(+4.6%), 샌디스크 +약 16%, 엔비디아 +0.8%, 브로드컴 +약 4%,
   테슬라 400.00(+5.2%), 아마존 254.12(+4.0%), 메타 +3%대 — Reuters·CNBC·Cedar
 - 앤트로픽(ANT): 공모가 $83(11/18, 9.8억 주·813억 달러 조달), 11/19 시초 $111.50·종가 $97.17,
   11/24 종가 $81.91, 11/25 장중 $73.85·종가 $82.79, 11/27 종가 $91.88(+10.98%), 주간 +3.3%
   — Bloomberg(11/27), Axios(11/24), stockanalysis.com(11/27), Crypto Briefing(11/27)
 - 소비: Adobe 블프 온라인 $12.9B(+9.2%)·추수감사절 $6.9B(+8.5%)·사이버먼데이 $15.1B(+6.2%)·
   사이버위크 $47.5B(+7.4%), 11/1~22 $82.5B(+9.1%)·BNPL $6.1B(+6.5%), NRF 11~12월 $1.013조(+4.2%)·
   주말 쇼핑 1억 8,270만 명
 - 매크로: 10월 PCE 3.8%·근원 3.3%, 3Q GDP 4.3%, 12/8~9 FOMC(발표 12/9), 10Y 4.91%·2Y 4.63%,
   금 $3,628(+2.6%)·은 $43.23(+7.9%), 브렌트 주간 +약 2%·금요일 −2%대
 - 비트코인: $59,733(11/28 07:00 KST, 24h −1.66%), 고가 $62,140·저가 $58,700,
   ETH $1,662(−1.74%)·XRP $0.9483(−0.45%)·SOL $71.87(+1.28%), 공포탐욕 12, 김프 +1.55%, 11월 약 −20%
 - 이미지: 실측 데이터 카드 6장(1200×1600), AI 생성 0장
"""
from brand_bf_common import publish

SLUG = "black-friday-half-session-close-2026-11-27-ai-rebound-anthropic"
C = "/images/products/mk-1128-cover.jpg"
G1 = "/images/products/mk-1128-week.jpg"
G2 = "/images/products/mk-1128-ai.jpg"
G3 = "/images/products/mk-1128-ant.jpg"
G4 = "/images/products/mk-1128-retail.jpg"
G5 = "/images/products/mk-1128-btc.jpg"

KO = """2026년 11월 27일(금) 미국 증시는 블랙프라이데이 반나절 장을 쓰고 오후 1시(ET)에 문을 닫았다. 추수감사절로 하루 쉬고 돌아온 시장은 이번 달 가장 많이 맞았던 AI·반도체주를 다시 사들이며 지수를 끌어올렸다. 다우는 592포인트 올라 2022년 10월 이후 가장 큰 주간 상승률을 남겼고, S&P 500은 4월 이후 최고의 한 주를 보냈다.

1. 마감 숫자
다우존스 산업평균은 591.99포인트(1.18%) 오른 50,774.94에 마감했다. S&P 500은 114.71포인트(1.60%) 오른 7,297.49, 나스닥 종합은 543.70포인트(2.31%) 오른 24,129.50이다. 러셀 2000은 46.24포인트(1.71%) 오른 2,750.30으로 중소형주도 함께 올랐다.
거래소는 한국 시간으로 11월 28일 새벽 3시에 닫혔다. 채권 시장은 오후 2시, CME 주가지수 선물은 오후 1시 15분에 끝났다. 미국 증시는 11월 30일(월)에 정규 시간으로 돌아오고, 그날이 11월의 마지막 거래일이다.
거래량은 109억 7,000만 주였다. 뉴욕증권거래소에서는 오른 종목이 내린 종목의 3.25배, 나스닥에서는 3,677개 대 1,135개로 상승 쪽이 압도했다. 공포지수(VIX)는 25.13으로 내려 이번 주에만 30% 빠졌다. 한 주 전 금요일 35.89까지 치솟았던 지수다.

2. 이번 주는 최고, 이번 달은 최악
주간 성적으로는 S&P 500이 5.6% 올라 2025년 4월 이후 가장 좋은 한 주를 기록했다. 나스닥은 6.68%, 다우는 5.46% 올랐다. 문제는 그 앞이다. 11월 마지막 날을 하루 남긴 시점에서 S&P 500은 이번 달 3.7% 내렸고, 나스닥은 5.1% 빠졌다. 2008년 이후 가장 나쁜 11월이다.
S&P 500은 10월 6일 사상 최고치(7,818.93)보다 6.67% 낮은 자리에 있다. 조정 기준인 10%에는 못 미치지만, 11월 한 달 동안 오르내린 폭은 올해 들어 가장 컸다. 한 주에 지수가 5~7%씩 움직인 달이었다.
이 흐름을 만든 건 세 가지다. 첫째, AI 설비투자 자금을 빚으로 조달하는 비용이 뛰었다. 둘째, 10월 개인소비지출(PCE) 물가가 전년 대비 3.8%로 예상을 웃돌면서 12월 금리 인상이 기정사실로 굳어졌다. 셋째, 중간선거 이후 AI 규제 강화 우려가 커졌다.

3. 반등을 끌어올린 것은 반도체였다
금요일 상승의 중심에는 이번 달 가장 많이 밀렸던 종목들이 있었다. 필라델피아 반도체지수는 4.7% 오른 9,186.71에 마감했다. 마이크론은 7.6% 오른 646.95달러, 마벨은 7.3% 올랐다. 샌디스크는 16% 가까이 급등했고, AMD는 4.6% 오른 424.54달러였다.
엔비디아는 장중 약세를 보이다 막판에 0.8% 상승으로 마감했다. 브로드컴은 4% 가까이 올랐다. 대형 기술주 중에서는 테슬라가 5.2% 오른 400달러, 아마존이 4.0% 오른 254.12달러, 메타가 3%대 상승을 기록했다.
해리스파이낸셜의 제이미 콕스는 "시장이 너무 과매도돼 반등이 불가피했다"고 말했다. 모건스탠리 인베스트먼트 매니지먼트의 앤드루 슬리먼은 "빠른 자금이 기술주에서 레버리지를 줄인 만큼 다음 주까지 추격 매수가 이어질 수 있다"고 봤다. 반대로 AI 설비투자와 부채 조달을 걱정하는 쪽은 이 반등을 되돌림으로 본다.

4. 앤트로픽의 첫 주 — 사상 최대 IPO의 롤러코스터
이번 주 개별 종목에서 가장 화제였던 것은 앤트로픽(나스닥: ANT)이다. 11월 18일 공모가를 주당 83달러로 확정해 9억 8,000만 주, 813억 달러를 조달했다. 사상 최대 규모 IPO다. 다음 날 나스닥에서 111.50달러에 시초가를 형성해 공모가보다 34% 높게 출발했고, 첫날 종가는 97.17달러였다.
이후 흔들렸다. 11월 24일 81.91달러로 공모가 아래에서 마감했고, 25일에는 장중 73.85달러까지 밀렸다. 주관사가 그린슈즈(초과배정) 옵션을 너무 일찍 소진해 하락을 방어하지 못했다는 지적이 나왔다. 25일 종가는 82.79달러로 여전히 공모가를 밑돌았다.
금요일에 분위기가 바뀌었다. AI주 전반이 반등하면서 앤트로픽은 10.98% 오른 91.88달러에 마감했다. 상장 첫날 이후 가장 높은 종가이자, 공모가 대비로는 10.7% 높은 수준이다. 주간으로는 3.3% 올랐다. 다만 시초가 111.50달러와 첫날 종가 97.17달러는 아직 넘지 못했다.

5. 미국 소비는 꺾이지 않았다
어도비 애널리틱스는 이번 블랙프라이데이 미국 온라인 매출을 129억 달러(전년 대비 9.2% 증가)로 본다. 추수감사절 69억 달러(8.5% 증가), 사이버먼데이 151억 달러(6.2% 증가)다. 다섯 날을 합친 사이버 위크는 475억 달러(7.4% 증가)로, 11~12월 전체 온라인 지출(2,751억 달러)의 17.3%를 차지한다.
이미 집행된 숫자도 있다. 11월 1일부터 22일까지 미국 소비자는 온라인에서 825억 달러를 썼다. 전년 대비 9.1% 늘었고, 선구매 후지불(BNPL) 결제액은 61억 달러(6.5% 증가)였다. 전미소매협회(NRF)는 11~12월 소매 판매를 1조 130억 달러(4.2% 증가)로 전망하고, 주말에 쇼핑할 계획이라고 답한 소비자는 1억 8,270만 명이다.
유통주도 같이 올랐다. CNBC는 AI 자본지출 우려로 자금이 월마트·코스트코 같은 유통주로 옮겨갔다고 전했다. 아마존은 4.0% 상승했지만, 물류센터 파업(Make Amazon Pay)은 블랙프라이데이부터 사이버먼데이까지 이어진다.

6. 매크로 — 다음 관문은 12월 9일
금리는 여전히 부담이다. 미국 10년물 국채 금리는 4.91%, 2년물은 4.63% 수준이다. 10월 PCE 물가는 3.8%, 근원은 3.3%로 예상을 조금 웃돌았다. 3분기 국내총생산(GDP) 성장률은 4.3%로 잠정치보다 높았다. 이 두 숫자 때문에 시장은 12월 8~9일 연방공개시장위원회(FOMC)에서 25bp 인상을 거의 반영하고 있다.
원자재는 반대로 움직였다. 금 선물은 2.6% 오른 온스당 3,628달러, 은은 7.9% 오른 43.23달러였다. 브렌트유는 이란계 후티의 사우디 에너지시설 공격으로 이번 주 2%가량 올랐고, 금요일 장중에는 2% 넘게 빠졌다.

7. 비트코인은 6만 달러 아래로
비트코인은 한국 시간 11월 28일 오전 7시 기준 59,733달러에 거래됐다. 24시간 동안 1.66% 내렸고, 고가 62,140달러·저가 58,700달러를 오갔다. 이더리움은 1,662달러(-1.74%), 리플은 0.9483달러(-0.45%)로 밀렸고, 솔라나는 71.87달러(+1.28%)로 올랐다.
주식이 반등한 뒤 나스닥100이 초반 상승분을 반납하자 비트코인도 6만 달러 아래로 내려왔다. 이달 최대 규모인 70억 달러 옵션 만기가 겹쳤다. 공포·탐욕 지수는 12로 '극단적 공포' 구간이고, 11월 수익률은 약 -20%다. 갤럭시리서치는 58,525달러의 일봉 종가 이탈이 추가 하락 신호라고 봤다. 국내 프리미엄(김치 프리미엄)은 1.55%다.

8. 다음 주에 볼 것
11월 30일(월)은 정규장이 돌아오는 날이자 11월의 마지막 거래일이다. 월말 리밸런싱 물량이 나오는 날이라 지수보다 종목 장세가 될 가능성이 있다. 12월 9일 FOMC가 최대 관문이고, 같은 날 브로드컴, 17일 마이크론 실적이 AI 설비투자 사이클에 대한 답을 준다.
시장이 던지는 질문은 하나로 모인다. 금리를 올리는 국면에서 AI 지출은 계속 늘어날 수 있는가. 금요일 반등은 그 질문에 대한 답이 아니라, 너무 많이 빠진 값에 대한 되돌림이었다.

한 줄 정리
미국 증시는 추수감사절 다음 날 반나절 장에서 다우 1.18%, S&P 500 1.60%, 나스닥 2.31% 올랐다. 주간으로는 5~7% 상승으로 2022년 이후 최고였지만, 11월 전체로는 S&P 500 -3.7%, 나스닥 -5.1%다. 반등을 끌어올린 것은 반도체였고, 화제의 앤트로픽은 공모가 위로 돌아왔다."""

EN = """U.S. stocks closed early at 1 p.m. ET on Friday, 27 November 2026 for the Black Friday half session. A day after Thanksgiving, investors bought back the AI and chip names that had been hit hardest this month, and the indexes finished the week at their best levels since spring.

1. The closing numbers
The Dow Jones Industrial Average rose 591.99 points, or 1.18%, to 50,774.94. The S&P 500 added 114.71 points, or 1.60%, to 7,297.49, and the Nasdaq Composite gained 543.70 points, or 2.31%, to 24,129.50. The Russell 2000 rose 46.24 points, or 1.71%, to 2,750.30, so small caps joined in.
The exchanges shut at 03:00 KST on 28 November, with bonds closing at 14:00 ET and CME equity index futures at 13:15. Regular hours return on Monday, 30 November, the last trading day of the month.
Volume was 10.97 billion shares. Advancers outnumbered decliners 3.25 to 1 on the NYSE and 3,677 to 1,135 on the Nasdaq. The VIX fell to 25.13, down about 30% on the week after closing at 35.89 the previous Friday.

2. Best week of the year, worst November since 2008
For the week, the S&P 500 gained 5.6%, its best since April 2025. The Nasdaq rose 6.68% and the Dow 5.46%, its best week since October 2022. With one session left, November is still a loss: the S&P 500 is down 3.7% for the month and the Nasdaq 5.1%.
The S&P 500 sits 6.67% below its record close of 7,818.93 on 6 October. That is short of the 10% mark people call a correction, but the November range was the widest of the year.
Three things drove it: the rising cost of funding AI capital spending with debt, an October PCE inflation reading of 3.8% that locked in expectations for a December rate hike, and worries about tougher AI regulation after the midterm elections.

3. Chips led the bounce
The Philadelphia Semiconductor Index rose 4.7% to 9,186.71. Micron gained 7.6% to $646.95, Marvell 7.3%, and Sandisk almost 16%. AMD rose 4.6% to $424.54.
Nvidia was weak for most of the session and still closed 0.8% higher. Broadcom added almost 4%. Among the megacaps, Tesla rose 5.2% to $400.00, Amazon 4.0% to $254.12 and Meta more than 3%.
"The market is so oversold that a bounce was inevitable," said Jamie Cox of Harris Financial Group. Andrew Slimmon of Morgan Stanley Investment Management said fast money had deleveraged out of tech and could be forced to chase back in next week. The bears read Friday as a retracement, not a change in the AI cost story.

4. Anthropic's first week
Anthropic (Nasdaq: ANT) was the week's most watched listing. It priced at $83 a share on 18 November, selling 980 million shares and raising $81.3 billion in the largest IPO on record. It opened at $111.50 on 19 November, 34% above the offer price, and closed its first day at $97.17.
Then it wobbled. It closed at $81.91 on 24 November, below the IPO price, and traded as low as $73.85 on the 25th before closing at $82.79. Investors blamed bankers for exhausting the greenshoe too early, leaving no support as the stock fell.
Friday reversed it. With AI names rallying, Anthropic closed 10.98% higher at $91.88, its best finish since day one and 10.7% above the IPO price. It gained 3.3% on the week but remains below its $111.50 open and $97.17 first close.

5. The U.S. consumer has not cracked
Adobe Analytics expects $12.9 billion of U.S. online spending on Black Friday, up 9.2% year over year, $6.9 billion on Thanksgiving (+8.5%) and $15.1 billion on Cyber Monday (+6.2%). Cyber Week should reach $47.5 billion, up 7.4%, or 17.3% of the $275.1 billion expected online in November and December.
Some of it is already spent: $82.5 billion online from 1 to 22 November, up 9.1%, with buy now, pay later at $6.1 billion (+6.5%). The National Retail Federation expects $1.013 trillion of holiday retail sales (+4.2%) and 182.7 million shoppers over the weekend.
Retail stocks rose with the market. CNBC reported money moving toward Walmart and Costco as investors questioned AI capital spending. Amazon gained 4.0% even as Make Amazon Pay strikes run from Black Friday to Cyber Monday.

6. Macro: the next gate is 9 December
Treasury yields remain the pressure point: 4.91% on the 10-year and 4.63% on the two-year. October PCE inflation was 3.8% with a 3.3% core, and third-quarter GDP growth was revised up to 4.3%. Traders now almost fully price a 25 basis point hike at the 8-9 December FOMC.
Commodities moved the other way. Gold futures rose 2.6% to $3,628 an ounce and silver 7.9% to $43.23. Brent gained about 2% on the week after Houthi attacks on Saudi energy infrastructure and fell more than 2% during Friday's session.

7. Bitcoin slipped back below $60,000
Bitcoin traded at $59,733 at 07:00 KST on 28 November, down 1.66% in 24 hours, in a range of $58,700 to $62,140. Ether fell 1.74% to $1,662 and XRP 0.45% to $0.9483, while Solana rose 1.28% to $71.87.
Bitcoin fell under $60,000 after the Nasdaq 100 gave up its early gains, and about $7 billion of options expired, the largest expiry this month. The Fear and Greed Index reads 12, extreme fear, and bitcoin is down roughly 20% in November. Galaxy Research said a daily close below $58,525 would signal a materially lower low.

8. What to watch
Monday, 30 November brings regular hours and the last trading day of November, with month-end rebalancing that may favour single stocks over indexes. The 8-9 December FOMC is the main gate, with Broadcom reporting on 9 December and Micron on the 17th.
The market is asking one question: can AI spending keep rising while rates go up. Friday's rally was not an answer to that. It was a bounce from prices that had fallen too far.

One line
In the Black Friday half session the Dow rose 1.18%, the S&P 500 1.60% and the Nasdaq 2.31%, capping a 5-7% week that was the best since 2022, while November still shows the S&P 500 down 3.7% and the Nasdaq down 5.1%. Chips led the bounce, and Anthropic closed back above its IPO price."""

JA = """2026年11月27日（金）、米国株式市場はブラックフライデーの半日取引を終え、東部時間13時に閉まった。感謝祭の休場明けに、今月最も売られたAI・半導体株を買い戻す動きが広がり、主要指数は週間で春以降最强の水準に戻した。

1. 終値
ダウは591.99ポイント（1.18%）高の50,774.94。S&P500は114.71ポイント（1.60%）高の7,297.49、ナスダック総合は543.70ポイント（2.31%）高の24,129.50。ラッセル2000も1.71%高の2,750.30だった。
取引所は韓国時間11月28日午前3時に閉場。債券は14時、CME株価指数先物は13時15分に終了した。通常取引は11月30日（月）に戻り、同日が11月最後の取引日になる。
出来高は109億7,000万株。ニューヨーク証券取引所の値上がり対値下がりは3.25倍、ナスダックは3,677対1,135。VIXは25.13まで下がり、週間で約30%下落した。前週金曜は35.89だった。

2. 週間は最高、11月は2008年以来の最悪
週間ではS&P500が5.6%高と2025年4月以来の上昇率、ナスダック6.68%高、ダウ5.46%高（2022年10月以来）だった。一方、11月は残り1日でS&P500が3.7%安、ナスダックが5.1%安。2008年以来最悪の11月になる。
S&P500は10月6日の最高値7,818.93を6.67%下回る。調整局面と呼ばれる10%には届かないが、11月の値幅は今年最大だった。
背景は3つ。AI設備投資の負債調達コスト上昇、10月PCEが前年比3.8%となり12月利上げ観測が固まったこと、中間選挙後のAI規制強化への懸念だ。

3. 反発を導いたのは半導体
フィラデルフィア半導体指数は4.7%高の9,186.71。マイクロンが7.6%高の646.95ドル、マーベルが7.3%高、サンディスクは約16%上昇した。AMDは4.6%高の424.54ドル。
エヌビディアは終日軟調だったが0.8%高で引けた。ブロードコムは約4%高。テスラ5.2%高の400.00ドル、アマゾン4.0%高の254.12ドル、メタは3%台の上昇だった。
ハリス・ファイナンシャルのジェイミー・コックス氏は「市場が売られすぎていたので反発は避けられなかった」と述べた。モルガン・スタンレーのアンドリュー・スリモン氏は、テックから急速にレバレッジを落とした資金が来週にかけて買い戻しに動く可能性を指摘した。

4. アンソロピックの最初の一週間
今週最も注目されたのはアンソロピック（ナスダック：ANT）。11月18日に公開価格83ドルで9億8,000万株を売り出し、813億ドルを調達した史上最大のIPOだ。19日は111.50ドルで初値を付け、公開価格を34%上回った。初日終値は97.17ドル。
その後は不安定だった。24日は81.91ドルと公開価格を下回り、25日には一時73.85ドルまで下落。幹事がグリーンシューを早く使い切り、下落を支えられなかったとの指摘が出た。25日終値は82.79ドル。
金曜に流れが変わった。AI株の反発で10.98%高の91.88ドルと、初日以来の高値で引けた。公開価格より10.7%高い。週間では3.3%高だが、初値111.50ドルと初日終値97.17ドルは依然下回っている。

5. 米消費は崩れていない
アドビ・アナリティクスはブラックフライデーの米オンライン売上を129億ドル（前年比9.2%増）と予想。感謝祭69億ドル（8.5%増）、サイバーマンデー151億ドル（6.2%増）。サイバーウィーク5日間は475億ドル（7.4%増）で、11〜12月のオンライン支出2,751億ドルの17.3%を占める。
すでに使われた数字もある。11月1〜22日に825億ドル（9.1%増）、BNPL決済は61億ドル（6.5%増）。NRFは11〜12月の小売売上を1兆130億ドル（4.2%増）、週末の買い物予定者を1億8,270万人と見る。
小売株も上昇した。CNBCはAI資本支出への懸念からウォルマートやコストコに資金が移ったと伝えた。アマゾンは4.0%高だが、メイク・アマゾン・ペイのストはサイバーマンデーまで続く。

6. マクロ：次の関門は12月9日
米10年債利回りは4.91%、2年債は4.63%。10月PCEは3.8%（コア3.3%）、7〜9月期GDPは4.3%に上方修正され、市場は12月8〜9日のFOMCで25bp利上げをほぼ織り込んでいる。
商品は逆方向。金先物は2.6%高の1オンス3,628ドル、銀は7.9%高の43.23ドル。ブレントはフーシー派のサウジ施設攻撃で週間約2%上昇し、金曜は2%超下落した。

7. ビットコインは6万ドル割れ
ビットコインは11月28日07:00（韓国時間）時点で59,733ドル、24時間で1.66%安。高値62,140ドル、安値58,700ドル。イーサリアムは1,662ドル（1.74%安）、リップル0.9483ドル（0.45%安）、ソラナは71.87ドル（1.28%高）。
ナスダック100が上げ幅を縮めた後に6万ドルを割り、今月最大の70億ドル規模のオプション満期が重なった。恐怖・強欲指数は12（極度の恐怖）、11月は約20%安。ギャラクシーリサーチは58,525ドルの日足終値割れを追加下落の信号とした。韓国プレミアムは1.55%。

8. 来週の注目
11月30日（月）は通常取引に戻り、11月最後の取引日。月末リバランスで指数より個別株が動きやすい。8〜9日のFOMCが最大の関門で、9日にブロードコム、17日にマイクロンの決算がAI設備投資サイクルへの答えを出す。
市場の問いは1つ。利上げ局面でAI支出は増え続けられるのか。金曜の反発はその答えではなく、下がりすぎた価格の戻りだった。

一行まとめ
感謝祭明けの半日取引でダウ1.18%、S&P500 1.60%、ナスダック2.31%高。週間5〜7%は2022年以来の上昇だが、11月はS&P500が3.7%安、ナスダックが5.1%安。反発を導いたのは半導体で、アンソロピックは公開価格を上回って引けた。"""

ZH = """2026年11月27日（周五），美国股市在黑色星期五进行半天交易，于美东时间下午1点收盘。感恩节休市一天后，资金回流到本月受创最重的AI与半导体股，三大指数录得春季以来最佳单周表现。

1. 收盘数字
道琼斯工业平均指数上涨591.99点（1.18%），收于50,774.94点。标普500上涨114.71点（1.60%），收于7,297.49点；纳斯达克综合指数上涨543.70点（2.31%），收于24,129.50点。罗素2000上涨46.24点（1.71%），收于2,750.30点。
交易所于韩国时间11月28日凌晨3点关闭，债券市场下午2点、CME股指期货下午1点15分结束。11月30日（周一）恢复常规交易，同时也是11月最后一个交易日。
成交量为109.7亿股。纽约证交所上涨与下跌家数比为3.25比1，纳斯达克为3,677比1,135。VIX回落至25.13，本周下跌约30%，上周五曾收于35.89。

2. 本周最佳，11月最差
本周标普500上涨5.6%，为2025年4月以来最佳；纳斯达克上涨6.68%，道琼斯上涨5.46%，为2022年10月以来最佳单周。但11月只剩一个交易日，标普500本月仍下跌3.7%，纳斯达克下跌5.1%，为2008年以来最差的11月。
标普500较10月6日历史高点7,818.93点低6.67%，未达到通常所说的10%调整线，但11月的波动幅度为年内最大。
三条主线：AI资本开支的债务融资成本上升；10月PCE同比3.8%使12月加息预期固化；中期选举后AI监管趋严的担忧。

3. 半导体领涨
费城半导体指数上涨4.7%，收于9,186.71点。美光上涨7.6%至646.95美元，迈威尔上涨7.3%，闪迪大涨近16%，AMD上涨4.6%至424.54美元。
英伟达盘中偏弱，收盘仍涨0.8%；博通上涨近4%。大型科技股中，特斯拉涨5.2%至400.00美元，亚马逊涨4.0%至254.12美元，Meta涨幅超过3%。
哈里斯金融集团的杰米·考克斯表示："市场超卖得太厉害，反弹不可避免。"摩根士丹利的安德鲁·斯利蒙认为，快钱已在科技股降杠杆，下周可能被迫追高。

4. Anthropic的第一周
本周最受关注的新股是Anthropic（纳斯达克：ANT）。11月18日以每股83美元定价，发行9.8亿股，募资813亿美元，为史上最大IPO。19日以111.50美元开盘，高于发行价34%，首日收于97.17美元。
随后走弱。24日收于81.91美元跌破发行价，25日盘中最低73.85美元，收于82.79美元。市场批评承销商过早用尽超额配售权，未能在下跌中提供支撑。
周五形势逆转。随着AI股反弹，Anthropic上涨10.98%，收于91.88美元，为上市首日以来最高收盘价，比发行价高10.7%。本周累计上涨3.3%，但仍低于111.50美元的开盘价和97.17美元的首日收盘价。

5. 美国消费未失速
Adobe Analytics预计黑色星期五美国线上消费129亿美元（同比增长9.2%），感恩节69亿美元（增长8.5%），网络星期一151亿美元（增长6.2%）。网络周五天合计475亿美元（增长7.4%），占11至12月线上支出2,751亿美元的17.3%。
已经落地的数字：11月1日至22日线上支出825亿美元（增长9.1%），先买后付61亿美元（增长6.5%）。全美零售商联合会（NRF）预计11至12月零售销售1.013万亿美元（增长4.2%），周末购物人数1.827亿。
零售股同步上涨。CNBC称，因担忧AI资本开支，资金转向沃尔玛、好市多等零售股。亚马逊上涨4.0%，但"让亚马逊买单"罢工将持续到网络星期一。

6. 宏观：下一个关口是12月9日
美国10年期国债收益率4.91%，2年期4.63%。10月PCE为3.8%（核心3.3%），三季度GDP上修至4.3%，市场几乎完全计入12月8至9日FOMC加息25个基点。
大宗商品反向走强：黄金期货上涨2.6%至每盎司3,628美元，白银上涨7.9%至43.23美元。布伦特原油因胡塞武装袭击沙特能源设施本周上涨约2%，周五盘中下跌超过2%。

7. 比特币跌破6万美元
11月28日韩国时间7点，比特币报59,733美元，24小时下跌1.66%，区间为58,700至62,140美元。以太坊跌1.74%至1,662美元，瑞波币跌0.45%至0.9483美元，索拉纳涨1.28%至71.87美元。
纳斯达克100回吐早盘涨幅后比特币跌破6万美元，本月最大规模的70亿美元期权同日到期。恐慌与贪婪指数为12（极度恐慌），11月累计下跌约20%。Galaxy Research认为，日线收于58,525美元下方将意味着更低的低点。

8. 下周关注
11月30日恢复常规交易并结束11月，月末再平衡可能让个股比指数更活跃。12月8至9日FOMC是最大关口，9日博通、17日美光财报将回答AI资本开支周期的问题。
市场只问一个问题：在加息周期里，AI支出还能继续增长吗。周五的反弹不是答案，只是跌得太多的价格回补。

一句话总结
感恩节次日的半天交易中，道指涨1.18%、标普500涨1.60%、纳指涨2.31%；单周5%至7%为2022年以来最佳，但11月标普500仍跌3.7%、纳指跌5.1%。半导体领涨，Anthropic重回发行价上方。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "postType": "report",
    "store": "K-Trend Market",
    "priceKrw": 0,
    "releaseDate": "2026-11-28",
    "rating": 5,
    "imageUrl": C,
    "images": [C, G1, G2, G3, G4, G5],
    "affiliateUrl": "https://stock.naver.com/",
    "affiliatePlatform": "Coupang",
    "i18n": {
        "ko": {
            "title": "블프 반일장 마감 — 다우 592p 반등, 2022년 이후 최고의 한 주… 앤트로픽은 공모가 위로",
            "summary": "11/27(금) 미국 증시는 13시(ET) 반나절 장으로 마감했다. 다우 50,774.94(+1.18%), S&P 500 7,297.49(+1.60%), 나스닥 24,129.50(+2.31%)로 반등했고, 주간으로는 S&P +5.6%로 2025년 4월 이후 최고다. 다만 11월 전체로는 S&P -3.7%, 나스닥 -5.1%다. 반등은 반도체가 이끌었고, 사상 최대 IPO 앤트로픽은 91.88달러(+10.98%)로 공모가 위를 회복했다.",
            "description": KO,
            "tasteReview": [
                "11/27(금) 종가: 다우 50,774.94(+591.99, +1.18%) · S&P 500 7,297.49(+114.71, +1.60%) · 나스닥 24,129.50(+543.70, +2.31%) · 러셀2000 2,750.30(+1.71%)",
                "반나절 장: NYSE·나스닥 13:00 ET(한국 11/28 03:00) 마감, 채권 14:00, CME 선물 13:15. 11/30(월) 정규장 복귀",
                "주간: S&P +5.6%(2025-04 이후 최대) · 나스닥 +6.68% · 다우 +5.46%(2022-10 이후 최대) / 11월: S&P -3.7%, 나스닥 -5.1%, 사상최고 대비 -6.67%",
                "반도체: 필반도체 9,186.71(+4.7%) · MU 646.95(+7.6%) · AMD 424.54(+4.6%) · 샌디스크 +약 16% · NVDA +0.8% · TSLA 400.00(+5.2%) · AMZN 254.12(+4.0%)",
                "앤트로픽(ANT): 공모가 $83 → 11/25 저점 $73.85 → 11/27 $91.88(+10.98%), 주간 +3.3%. 비트코인 $59,733(24h -1.66%), 공포탐욕 12",
            ],
            "tips": "본 글은 공개된 시세·보도·공시를 정리한 정보 기록이며 특정 종목의 매수·매도를 권유하지 않습니다. 지수는 2026년 11월 27일 정규장(반일장) 종가, 비트코인은 11월 28일 07:00 KST 조회값입니다. 반나절 장은 거래량이 적어 가격 변동이 커질 수 있습니다.",
        },
        "en": {
            "title": "Black Friday Half Session: Dow Jumps 592 Points to Its Best Week Since 2022, Anthropic Back Above IPO Price",
            "summary": "U.S. stocks closed early at 1 p.m. ET on 27 November 2026. The Dow finished at 50,774.94 (+1.18%), the S&P 500 at 7,297.49 (+1.60%) and the Nasdaq at 24,129.50 (+2.31%), capping a week in which the S&P gained 5.6%, its best since April 2025. November is still negative at -3.7% for the S&P and -5.1% for the Nasdaq. Chips led the bounce and Anthropic closed at $91.88 (+10.98%), back above its $83 IPO price.",
            "description": EN,
            "tasteReview": [
                "Close on 27 November: Dow 50,774.94 (+591.99, +1.18%), S&P 500 7,297.49 (+114.71, +1.60%), Nasdaq 24,129.50 (+543.70, +2.31%), Russell 2000 2,750.30 (+1.71%)",
                "Half session: NYSE and Nasdaq closed 13:00 ET, bonds 14:00, CME futures 13:15; regular hours return 30 November",
                "Week: S&P +5.6% (best since April 2025), Nasdaq +6.68%, Dow +5.46% (best since October 2022). November: S&P -3.7%, Nasdaq -5.1%, 6.67% below the record",
                "Chips: SOX 9,186.71 (+4.7%), MU $646.95 (+7.6%), AMD $424.54 (+4.6%), Sandisk +16%, NVDA +0.8%, TSLA $400.00 (+5.2%), AMZN $254.12 (+4.0%)",
                "Anthropic (ANT): $83 IPO, low of $73.85 on 25 November, close of $91.88 (+10.98%) on 27 November, +3.3% on the week. Bitcoin $59,733 (-1.66%), Fear and Greed 12",
            ],
            "tips": "This is a summary of public market data, reporting and filings, not investment advice. Index levels are regular-session closes on 27 November 2026 and bitcoin was read at 07:00 KST on 28 November 2026. A half session has thinner volume and can widen price swings.",
        },
        "ja": {
            "title": "ブラックフライデー半日取引 — ダウ592p反発で2022年以来の高値、アンソロピックは公開価格を回復",
            "summary": "11月27日（金）の米国株は東部時間13時の半日取引で終了。ダウ50,774.94（+1.18%）、S&P500 7,297.49（+1.60%）、ナスダック24,129.50（+2.31%）と反発し、週間ではS&P500が5.6%高と2025年4月以来の上昇率。ただし11月はS&P500が3.7%安、ナスダックが5.1%安。半導体が主導し、史上最大のIPOアンソロピックは91.88ドル（+10.98%）で公開価格を上回った。",
            "description": JA,
            "tasteReview": [
                "11月27日終値: ダウ50,774.94（+591.99、+1.18%）、S&P500 7,297.49（+114.71、+1.60%）、ナスダック24,129.50（+543.70、+2.31%）、ラッセル2000 2,750.30（+1.71%）",
                "半日取引: NYSE・ナスダックはET13:00終了（韓国時間28日03:00）、債券14:00、CME先物13:15。30日に通常取引へ",
                "週間: S&P500 +5.6%（2025年4月以来最大）、ナスダック+6.68%、ダウ+5.46%（2022年10月以来）。11月: S&P500 -3.7%、ナスダック-5.1%、最高値比-6.67%",
                "半導体: SOX 9,186.71（+4.7%）、MU 646.95ドル（+7.6%）、AMD 424.54ドル（+4.6%）、サンディスク+約16%、NVDA +0.8%、TSLA 400.00ドル（+5.2%）、AMZN 254.12ドル（+4.0%）",
                "アンソロピック（ANT）: 公開価格83ドル → 25日安値73.85ドル → 27日91.88ドル（+10.98%）、週間+3.3%。ビットコイン59,733ドル（-1.66%）、恐怖指数12",
            ],
            "tips": "本記事は公開された相場データ・報道・開示を整理した情報記録であり、個別銘柄の売買を推奨するものではありません。指数は2026年11月27日の通常取引（半日）終値、ビットコインは11月28日07:00 KSTの取得値です。半日取引は出来高が薄く値動きが大きくなることがあります。",
        },
        "zh": {
            "title": "黑色星期五半天交易——道指反弹592点创2022年以来最佳周线，Anthropic重回发行价上方",
            "summary": "11月27日（周五）美股于美东13点提前收盘。道指50,774.94（+1.18%）、标普500 7,297.49（+1.60%）、纳指24,129.50（+2.31%）。本周标普上涨5.6%，为2025年4月以来最佳，但11月仍下跌3.7%，纳指下跌5.1%。半导体领涨，史上最大IPO Anthropic收于91.88美元（+10.98%），重回83美元发行价上方。",
            "description": ZH,
            "tasteReview": [
                "11月27日收盘：道指50,774.94（+591.99，+1.18%）、标普500 7,297.49（+114.71，+1.60%）、纳指24,129.50（+543.70，+2.31%）、罗素2000 2,750.30（+1.71%）",
                "半天交易：NYSE与纳斯达克美东13:00收盘（韩国时间28日03:00），债券14:00，CME期货13:15；30日恢复常规交易",
                "本周：标普+5.6%（2025年4月以来最佳）、纳指+6.68%、道指+5.46%（2022年10月以来最佳）；11月：标普-3.7%、纳指-5.1%，较历史高点低6.67%",
                "半导体：费半9,186.71（+4.7%）、美光646.95美元（+7.6%）、AMD 424.54美元（+4.6%）、闪迪+约16%、英伟达+0.8%、特斯拉400.00美元（+5.2%）、亚马逊254.12美元（+4.0%）",
                "Anthropic（ANT）：发行价83美元，25日最低73.85美元，27日收91.88美元（+10.98%），本周+3.3%。比特币59,733美元（-1.66%），恐慌指数12",
            ],
            "tips": "本文整理公开行情、报道与披露资料，不构成任何个股买卖建议。指数为2026年11月27日常规交易（半天）收盘价，比特币为11月28日07:00 KST查询值。半天交易成交量较低，波动可能放大。",
        },
    },
}

if __name__ == "__main__":
    publish(POST)
