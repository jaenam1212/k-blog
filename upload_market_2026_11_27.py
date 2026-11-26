#!/usr/bin/env python3
"""트랙1 — 2026-11-27(금) 미국 시장 리포트 (4개국어) → Supabase posts + ISR revalidate.

근거 (2026-11-27 08:10~08:30 KST 확인)
 - NYSE·나스닥·SIFMA·CME 2026 추수감사절 시간표 (Nasdaq Equity Trader Alert #2026-69, USA TODAY, MLQ.ai)
 - 11/25 정규장 종가: 다우 50,182.95(+164.25, +0.33%), S&P500 7,182.78(−18.31, −0.25%),
   나스닥 23,585.80(−147.74, −0.62%), 러셀2000 2,704.06(+19.12, +0.71%) — AP·CNBC·investing.com
 - 장중 저점: 다우 48,913.74(−2.21%), S&P500 6,970.11(−3.21%), 나스닥 22,632.40(−4.6%)
 - S&P500 사상 최고 7,818.93(2026-10-06), 현재 −8.14%
 - 11/26 18:00 ET 선물 재개: S&P +0.7%, 나스닥100 +0.6%, 다우 +277p (CNBC 18:10 ET)
 - 개별주: NVDA 149.30(−3.91%) MU 601.25(−4.53%) ORCL 103.88(−5.13%) AMZN 244.43(−3.14%)
   MSFT 489.93(−1.25%) LRCX 185.01(−5.68%) AMBA −19% META 609.89(+3.40%) HP 31.15(+11.49%)
 - 매크로: 10월 PCE 3.8%·근원 3.3%, 3Q GDP 4.3%, 14개국 301조 관세 제안, 12/8~9 FOMC
 - BTC $60,390(11/27 08:17 KST), 수요일 저점 $57,500, ETF 11월 −$5.39B·수요일 −$453M, $7B 옵션 만기
 - Adobe/NRF 블프 전망·실적, KOSPI·한은 금통위(11/26)
 - 이미지: 실측 데이터 카드 6장(1200×1600), AI 생성 0장
"""
from brand_bf_common import publish

SLUG = "thanksgiving-hold-blackfriday-half-day-futures-ai-stocks-2026-11-27"
C = "/images/products/mk-1127-cover.jpg"
G1 = "/images/products/mk-1127-board.jpg"
G2 = "/images/products/mk-1127-ai.jpg"
G3 = "/images/products/mk-1127-bf.jpg"
G4 = "/images/products/mk-1127-kr.jpg"
G5 = "/images/products/mk-1127-btc.jpg"

KO = """2026년 11월 26일(목) 미국은 추수감사절로 증시를 닫았다. 다음 날인 27일(금) 블랙프라이데이에는 다시 문을 열지만, 정규장은 반나절이다. 휴장 전 마지막 거래일의 숫자, 휴장 중 움직인 선물과 비트코인, 그리고 오늘 밤 지켜볼 지표까지 한 번에 정리했다.

1. 오늘 미국 증시는 13시에 닫는다
뉴욕증권거래소(NYSE)와 나스닥은 한국 시간으로 11월 27일 23시 30분에 장을 열고 11월 28일 새벽 3시에 닫는다. 뉴욕 시간으로는 오전 9시 30분부터 오후 1시까지다. 옵션 시장은 15분 늦은 오후 1시 15분, 채권 시장은 오후 2시(SIFMA 권고)에 마감한다. CME 주가지수 선물도 오후 1시 15분에 끝나고, 이날은 금요일 저녁 재개장이 없다.
CME는 11월 25일 저녁 재개장부터 27일 마감까지를 하나의 거래일로 계산한다. 휴장 전에 넣어둔 주문이 자동으로 살아 있는 구조이므로, 장기 주문을 남겼다면 마감 전에 정리해야 한다.
추수감사절 당일에도 선물은 오후 1시까지 거래됐다가 오후 6시에 다시 열렸다. 재개 직후인 한국 시간 11월 27일 오전 8시 10분 무렵 S&P 500 선물은 0.7%, 나스닥100 선물은 0.6%, 다우 선물은 277포인트(0.6%) 올랐다. 지수가 하루 쉬는 동안 나온 재료가 나쁘지 않았다는 뜻이지만, 거래량이 적은 반나절 장에서 이 숫자가 그대로 유지된다고 보기는 어렵다.

2. 휴장 전 마지막 거래일은 '되돌림'이었다
기준점은 11월 25일 종가다. 다우존스 산업평균은 164.25포인트(0.33%) 오른 50,182.95에 마감했다. S&P 500은 18.31포인트(0.25%) 내린 7,182.78, 나스닥 종합은 147.74포인트(0.62%) 내린 23,585.80이다. 러셀 2000은 19.12포인트(0.71%) 오른 2,704.06으로 중소형주 쪽이 더 강했다.
숫자보다 장중 흐름이 이번 주의 성격을 보여준다. 다우는 장 초반 1,104.96포인트(2.21%)까지 밀렸고, 나스닥은 4.6%, S&P 500은 3.21%(6,970.11)까지 빠졌다. 이후 낙폭을 거의 다 되돌리면서 다우는 플러스로 돌아섰고, 나스닥은 950포인트를 되찾고도 마이너스로 끝났다. 같은 반등 안에서도 대형 성장주만 회복이 더뎠다는 뜻이다.
S&P 500은 10월 6일 사상 최고치(7,818.93) 대비 8.14% 낮은 자리에 있다. 고점 대비 10%를 조정으로 부르니 아직 그 문턱은 아니다. 다만 11월 한 달 동안 지수가 오르내린 폭은 올해 들어 가장 컸다.

3. AI주는 지수보다 먼저 무너지고 늦게 돌아온다
11월 25일 AI 관련주는 다시 밀렸다. 엔비디아는 3.91% 내린 149.30달러, 마이크론은 4.53% 내린 601.25달러, 오라클은 5.13% 내린 103.88달러로 52주 최저를 찍었다. 아마존은 3.14% 내린 244.43달러, 마이크로소프트는 1.25% 내린 489.93달러, 램리서치는 5.68% 내린 185.01달러였다. 실적과 가이던스가 모두 기대에 못 미친 앰바렐라는 19% 급락했다. 기술주 중심의 XLK ETF는 1% 가까이 내렸다.
반대편도 있었다. 메타는 3.40% 오른 609.89달러, HP는 11.49% 오른 31.15달러였다. HP는 4분기 조정 주당순이익 0.83달러(예상 0.75달러)와 매출 160억 달러(예상 154억 2,000만 달러)를 냈다. IBM 3.33%, 세일즈포스 2.04%처럼 기업용 소프트웨어 쪽도 올랐다.
엔비디아는 10월 고점 이후 시가총액 2조 달러 이상을 잃었다. 11월 23일 젠슨 황 CEO 복귀 발표로 하루 31.5% 급등했던 주가가 사흘 만에 그 상승분의 상당 부분을 반납한 셈이다. S&P 글로벌은 엔비디아의 AA 신용등급을 '신용관찰 하향'에 올렸고, 이사회가 진행하는 조사와 의회의 요구는 아직 끝나지 않았다.

4. 무거운 이유 세 가지
첫째는 비용이다. AI 데이터센터 자본지출이 매출보다 빨리 늘고, 그 자금을 빚으로 조달하는 회사의 조달 비용이 뛰었다. 코어위브의 2031년 만기 회사채 수익률은 11월 25일 18%에 가까워졌고, 오라클·알파벳·코어위브의 신용부도스와프(CDS) 가격은 사상 최고 수준이다.
둘째는 금리다. 10월 개인소비지출(PCE) 물가는 전년 대비 3.8%(9월 3.7%)였고 근원 PCE는 3.3%로 예상을 조금 웃돌았다. 시장은 12월 8~9일 연방공개시장위원회(FOMC)에서 25bp 인상을 사실상 기정사실로 보고 있다.
셋째는 관세다. 미국 무역대표부(USTR)가 중국·EU·일본·인도 등 14개국을 대상으로 301조 관세 15~20% 부과를 제안했다. 시행까지는 수개월이 걸린다는 설명이지만, 원가와 마진 계산은 이미 시작됐다.

5. 비트코인은 6만 달러를 지켰다
비트코인은 한국 시간 11월 27일 오전 8시 17분 기준 6만 390달러에 거래됐다. 수요일 5만 7,500달러까지 밀렸던 가격이 5%가량 되돌아온 수준이다. 다만 주간으로는 3.7% 낮고, 사상 최고치(12만 6,080달러) 대비로는 52% 아래다.
수급은 아직 불리하다. 미국 현물 비트코인 ETF는 11월 들어 53억 9,000만 달러가 빠져나가며 월간 기준 역대 최대 순유출을 기록했고, 11월 25일에도 4억 5,300만 달러가 나갔다. 7거래일 연속 유출이다. 오늘은 70억 달러 규모의 비트코인 옵션이 만기를 맞는다.
차트에서는 50일 이동평균이 200일 이동평균을 아래로 뚫는 '데드크로스'가 나왔다. 6월 저점(일봉 종가 5만 8,525달러, 주봉 종가 5만 9,517달러)이 종가 기준으로 지켜지는지가 이번 주 남은 변수다. 공포·탐욕 지수는 11로 '극단적 공포' 구간에 있다.

6. 블랙프라이데이, 미국 소비자는 얼마를 쓸까
어도비 애널리틱스는 이번 블랙프라이데이 미국 온라인 매출을 129억 달러(전년 대비 9.2% 증가)로 전망한다. 추수감사절은 69억 달러(8.5% 증가), 사이버먼데이는 151억 달러(6.2% 증가)다. 다섯 날을 합친 사이버 위크는 475억 달러(7.4% 증가)로, 11~12월 전체 온라인 지출(2,751억 달러)의 17.3%를 차지한다.
이미 집행된 숫자도 있다. 11월 1일부터 22일까지 미국 소비자는 온라인에서 825억 달러를 썼다. 전년 동기 대비 9.1% 늘었고, 추수감사절 전에 하루 40억 달러를 넘긴 날이 두 번 나온 것은 처음이다. 선구매 후지불(BNPL) 결제액은 61억 달러(6.5% 증가)였다.
전미소매협회(NRF)는 11~12월 소매 판매를 1조 130억 달러(4.2% 증가)로 본다. 주말에 쇼핑할 계획이라고 답한 소비자는 1억 8,270만 명이다. 눈여겨볼 지표는 AI다. 어도비 집계에서 추수감사절 하루 AI를 거쳐 유통 사이트로 들어온 트래픽은 전년 대비 159% 늘어 시즌 최대 증가폭을 기록했다. 모바일 비중은 63%로 사상 최고다.
변수는 물류다. '메이크 아마존 페이' 캠페인이 블랙프라이데이부터 사이버먼데이까지 이어지고, 독일 노르트라인베스트팔렌주 4개 아마존 물류센터에서는 11월 28일까지 파업이 예고됐다. 20개국 넘는 지역에서 시위와 파업이 계획돼 있다.

7. 한국은 금리를 올렸고, 지수는 버텼다
11월 26일 코스피는 13.70포인트(0.29%) 오른 4,711.21에 마감했다. 장중 4,817.77(2.56%)까지 올랐다가 막판 상승분을 반납했다. 코스닥은 0.78% 오른 655.71이다. 개인은 1조 440억 원, 외국인은 1,136억 원을 순매도했고 기관이 7,509억 원을 순매수해 지수를 받쳤다.
한국은행은 이날 금융통화위원회에서 기준금리를 3.00%에서 3.25%로 25bp 인상했다. 올해 성장률 전망은 3.3%에서 3.9%, 내년은 2.9%에서 4.1%로 크게 올렸다. 점도표 21개 점 중 7개가 3.75%, 8개가 3.50%에 찍혀 추가 인상 여지를 남겼다.
종목별로는 SK하이닉스가 2.23% 오른 105만 3,000원, 삼성전자가 0.35% 오른 17만 1,300원이었다. 반면 현대차는 3.90% 내린 25만 9,000원, LG에너지솔루션은 2.11% 내린 30만 2,000원, 삼성바이오로직스는 1.91% 내린 133만 7,000원이었다.

8. 오늘 확인할 것
오늘 밤 미국장은 반나절이다. 소매 유통주가 블랙프라이데이 초반 데이터에 어떻게 반응하는지가 오후 1시 마감 전에 드러난다. 같은 날 오전 8시 30분(ET)에는 10월 상품수지(적자 1,359억 달러 예상)와 도매재고(0.5% 증가 예상)가 발표된다. 일본에서는 11월 도쿄 소비자물가(생선 제외, 2.9% 예상)가 오늘 아침 나왔다.
다음 주의 큰 관문은 12월 8~9일 FOMC다. 그 사이 12월 9일 브로드컴, 12월 17일 마이크론 실적이 AI 자본지출 사이클에 대한 답을 준다. 지금 시장이 던지는 질문은 하나다. 금리를 올리는 국면에서 AI 지출은 계속 늘어날 수 있는가.

한 줄 정리
추수감사절로 하루 쉰 미국 증시는 오늘 밤 13시(ET)에 닫는 반나절 장으로 재개한다. 직전 거래일은 다우 0.33% 상승, 나스닥 0.62% 하락으로 갈렸고, 휴장 중 선물은 0.6~0.7% 올랐다. 비트코인은 6만 달러를 지켰고, 미국 소비자는 블랙프라이데이에 온라인으로 129억 달러를 쓸 것으로 보인다. AI주는 여전히 비용과 금리라는 두 변수 앞에 서 있다."""

EN = """U.S. markets were closed on Thursday, 26 November 2026 for Thanksgiving. They reopen on Friday the 27th, Black Friday, but only for a half session. Here is what the last full session actually printed, what moved while the market was shut, and what to watch tonight.

1. Today's session ends at 1 p.m. ET
The NYSE and Nasdaq open at 09:30 ET and close at 13:00 ET, which is 23:30 KST on 27 November to 03:00 KST on 28 November. Options close 15 minutes later at 13:15, and the bond market closes at 14:00 under SIFMA's recommendation. CME equity index futures stop at 13:15 and do not reopen on Friday evening.
CME counts everything from Wednesday's 18:00 ET reopen to Friday's close as a single trading day dated 27 November, so orders placed before the holiday can still be live. Anyone holding working orders should clear them before the close.
Futures traded until 13:00 ET on Thanksgiving itself and reopened at 18:00. Just after that reopen, at about 08:10 KST on 27 November, S&P 500 futures were up 0.7%, Nasdaq-100 futures 0.6% and Dow futures 277 points, or 0.6%. That suggests the news during the holiday was not bad, but a thin half day rarely holds an overnight move.

2. The last full session was a reversal
Start with Wednesday's close: the Dow finished at 50,182.95, up 164.25 points or 0.33%. The S&P 500 fell 18.31 points, 0.25%, to 7,182.78, and the Nasdaq Composite fell 147.74 points, 0.62%, to 23,585.80. The Russell 2000 rose 19.12 points, 0.71%, to 2,704.06, so small caps outperformed.
The intraday path matters more than the closes. The Dow fell as much as 1,104.96 points, or 2.21%; the Nasdaq was down 4.6% and the S&P 500 3.21% at 6,970.11. Both indexes then recovered most of the drop, and the Dow finished green while the Nasdaq ended lower even after clawing back 950 points. The rebound favoured everything except large-cap growth.
The S&P 500 now sits 8.14% below its record close of 7,818.93 set on 6 October. That is not yet the 10% mark people call a correction, but November has produced the widest swings of the year.

3. AI names fall first and recover last
AI stocks were hit again on Wednesday. Nvidia fell 3.91% to $149.30, Micron 4.53% to $601.25 and Oracle 5.13% to $103.88, a 52-week low. Amazon lost 3.14% to $244.43, Microsoft 1.25% to $489.93 and Lam Research 5.68% to $185.01. Ambarella dropped 19% after missing on both earnings and guidance. The technology-heavy XLK ETF closed nearly 1% lower.
There were winners too. Meta rose 3.40% to $609.89 and HP jumped 11.49% to $31.15 after fourth-quarter adjusted earnings of $0.83 a share against $0.75 expected and revenue of $16.0 billion against $15.42 billion. IBM gained 3.33% and Salesforce 2.04%.
Nvidia has shed more than $2 trillion of market value since its October peak. The stock jumped 31.5% on 23 November when Jensen Huang was reinstated as CEO, and has since given back a large part of that gain. S&P Global placed its AA rating on CreditWatch negative, and the board's investigation and congressional requests are still open.

4. Three reasons the trade stays heavy
The first is cost. Capital spending on AI data centres is rising faster than revenue, and the companies funding it with debt are paying more. CoreWeave's 2031 notes yielded close to 18% on Wednesday, and credit default swaps for Oracle, Alphabet and CoreWeave are at record levels.
The second is rates. October PCE inflation was 3.8% year over year, up from 3.7%, and core PCE came in at 3.3%, slightly above expectations. Markets treat a 25 basis point hike at the 8-9 December FOMC as settled.
The third is tariffs. The U.S. Trade Representative proposed Section 301 tariffs of 15-20% on 14 trading partners including China, the EU, Japan and India. Implementation is months away, but companies have started repricing costs and margins.

5. Bitcoin held $60,000
Bitcoin traded at $60,390 at 08:17 KST on 27 November, roughly 5% above Wednesday's low of $57,500. It is still down 3.7% on the week and 52% below its record of $126,080.
Flows remain unfriendly. U.S. spot bitcoin ETFs lost $453 million on Wednesday, a seventh straight outflow, taking November's total to about $5.39 billion, the largest monthly withdrawal on record. About $7 billion of bitcoin options expire today.
On the chart, the 50-day moving average has crossed below the 200-day, a death cross. The June lows of $58,525 on a daily close and $59,517 on a weekly close are the levels to watch. The Crypto Fear and Greed Index reads 11, extreme fear.

6. What Black Friday is worth
Adobe Analytics expects $12.9 billion of U.S. online spending on Black Friday, up 9.2% year over year, $6.9 billion on Thanksgiving (up 8.5%) and $15.1 billion on Cyber Monday (up 6.2%). Cyber Week should total $47.5 billion, up 7.4%, or 17.3% of the $275.1 billion expected online in November and December.
Some of it is already spent. From 1 to 22 November U.S. shoppers spent $82.5 billion online, up 9.1%, including two days above $4 billion before Thanksgiving for the first time. Buy now, pay later spending reached $6.1 billion, up 6.5%.
The National Retail Federation expects November-December retail sales of $1.013 trillion, up 4.2%, and 182.7 million shoppers over the weekend. The number worth watching is AI. Adobe counted 159% more traffic arriving at retail sites through AI on Thanksgiving Day, the largest jump of the season, and mobile reached a record 63% of online spend.
Logistics are the wild card. The Make Amazon Pay campaign runs from Black Friday to Cyber Monday, with strikes at four Amazon sites in North Rhine-Westphalia through 28 November and actions planned in more than 20 countries.

7. Korea raised rates and the index held
The KOSPI closed at 4,711.21 on 26 November, up 13.70 points or 0.29%, after touching 4,817.77 intraday and giving back the gain late. The KOSDAQ rose 0.78% to 655.71. Individuals sold a net 1.04 trillion won and foreigners 113.6 billion, while institutions bought 750.9 billion won.
The Bank of Korea raised its policy rate by 25 basis points to 3.25%. It lifted this year's growth forecast to 3.9% from 3.3% and next year's to 4.1% from 2.9%. Seven of the 21 dots in its dot plot sit at 3.75% and eight at 3.50%, leaving room for more tightening.
SK Hynix rose 2.23% to 1,053,000 won and Samsung Electronics 0.35% to 171,300 won. Hyundai Motor fell 3.90% to 259,000 won, LG Energy Solution 2.11% to 302,000 won and Samsung Biologics 1.91% to 1,337,000 won.

8. What to watch today
Tonight's U.S. session is half a day. Retail stocks will react to early Black Friday reads before the 13:00 close. At 08:30 ET the October goods trade balance (-$135.9 billion expected) and wholesale inventories (+0.5% expected) are released. Japan published November Tokyo CPI this morning, with core inflation expected at 2.9%.
The next big gate is the 8-9 December FOMC. In between, Broadcom reports on 9 December and Micron on 17 December, giving the first real read on the AI capital spending cycle. The market is asking one question: can AI spending keep rising while rates go up.

One line
After a Thanksgiving day off, U.S. stocks return for a session that ends at 13:00 ET. The last full day split, with the Dow up 0.33% and the Nasdaq down 0.62%, and futures have added 0.6-0.7% during the holiday. Bitcoin is holding $60,000, U.S. shoppers are expected to spend $12.9 billion online on Black Friday, and AI stocks still face the same two variables: cost and rates."""

JA = """2026年11月26日（木）、米国は感謝祭で株式市場が休場だった。翌27日（金）のブラックフライデーには再開するが、通常取引は半日だけだ。休場前の最後の取引日の数字、休場中に動いた先物とビットコイン、今夜確認すべき指標をまとめた。

1. 今日の米国市場は13時に閉まる
ニューヨーク証券取引所（NYSE）とナスダックは韓国時間11月27日23時30分に開き、28日午前3時に閉じる。ニューヨーク時間では午前9時30分から午後1時まで。オプションは15分後の午後1時15分、債券市場は午後2時（SIFMA勧告）に終わる。CMEの株価指数先物も午後1時15日に終了し、この日は金曜夜の再開がない。
CMEは25日夕方の再開から27日の終了までを一つの取引日として扱う。休場前に出した注文が生きている可能性があるため、有効注文は閉場前に確認したい。
感謝祭当日も先物は午後1時まで取引され、午後6時に再開した。再開直後の韓国時間11月27日午前8時10分ごろ、S&P500先物は0.7%、ナスダック100先物は0.6%、ダウ先物は277ポイント（0.6%）高だった。休場中の材料が悪くなかったことを示すが、薄商いの半日でこの動きが続くとは限らない。

2. 休場前の最後の取引日は「戻り」だった
基準は25日の終値だ。ダウは164.25ポイント（0.33%）高の50,182.95。S&P500は18.31ポイント（0.25%）安の7,182.78、ナスダック総合は147.74ポイント（0.62%）安の23,585.80。ラッセル2000は19.12ポイント（0.71%）高の2,704.06で、中小型株のほうが強かった。
終値より場中の動きが今週の性格を示す。ダウは一時1,104.96ポイント（2.21%）安、ナスダックは4.6%安、S&P500は3.21%安の6,970.11まで下げた。その後ほぼ戻し、ダウはプラスで終え、ナスダックは950ポイント戻してもマイナスだった。同じ戻りでも大型成長株だけ回復が遅い。
S&P500は10月6日の最高値7,818.93から8.14%下にある。調整と呼ばれる10%には届いていないが、11月の値動きの幅は今年最大だ。

3. AI株は先に崩れ、最後に戻る
25日のAI関連株は再び売られた。エヌビディアは3.91%安の149.30ドル、マイクロンは4.53%安の601.25ドル、オラクルは5.13%安の103.88ドルで52週安値。アマゾン3.14%安の244.43ドル、マイクロソフト1.25%安の489.93ドル、ラムリサーチ5.68%安の185.01ドル。決算とガイダンスがともに期待を下回ったアンバレラは19%急落した。XLK ETFは1%近く下げた。
上昇した銘柄もある。メタは3.40%高の609.89ドル、HPは11.49%高の31.15ドル。HPは4Q調整後EPS0.83ドル（予想0.75ドル）、売上160億ドル（予想154億2,000万ドル）だった。IBM3.33%、セールスフォース2.04%も上昇した。
エヌビディアは10月高値から時価総額2兆ドル以上を失った。11月23日のジェンセン・フアンCEO復帰で31.5%急騰した株価は、3日でその多くを返した。S&PグローバルはAA格付けを「クレジットウォッチ・ネガティブ」に置き、取締役会の調査と議会の要求は続いている。

4. 重い理由は三つ
第一はコスト。AIデータセンターへの設備投資が売上より速く増え、借入で資金を調達する企業の調達コストが上がった。コアウィーブの2031年債の利回りは25日に18%近くまで上昇し、オラクル・アルファベット・コアウィーブのCDSは過去最高水準だ。
第二は金利。10月PCEは前年比3.8%（9月3.7%）、コア3.3%で予想をやや上回った。市場は12月8〜9日のFOMCでの25bp利上げをほぼ確実視している。
第三は関税。USTRは中国・EU・日本・インドなど14か国に301条関税15〜20%を提案した。実施は数か月先だが、コストと利益率の再計算は始まっている。

5. ビットコインは6万ドルを維持
ビットコインは韓国時間11月27日午前8時17分時点で60,390ドル。25日の安値57,500ドルから約5%戻した水準だ。週間では3.7%安、最高値126,080ドルからは52%下にある。
資金流向は依然として不利だ。米国の現物ビットコインETFは11月に53億9,000万ドルが流出し、月間で過去最大。25日も4億5,300万ドルが流出し7営業日連続となった。今日は70億ドル規模のビットコインオプションが満期を迎える。
チャートでは50日移動平均が200日移動平均を下回るデッドクロスが発生した。6月安値（日足終値58,525ドル、週足終値59,517ドル）が終値ベースで維持されるかが焦点だ。恐怖・強欲指数は11で「極度の恐怖」にある。

6. ブラックフライデーに米国人はいくら使うのか
アドビはブラックフライデーの米国オンライン売上を129億ドル（前年比9.2%増）と予想する。感謝祭69億ドル（8.5%増）、サイバーマンデー151億ドル（6.2%増）。5日間のサイバーウィークは475億ドル（7.4%増）で、11〜12月のオンライン支出2,751億ドルの17.3%を占める。
すでに使われた数字もある。11月1日から22日までに米国の消費者はオンラインで825億ドルを使った。前年同期比9.1%増で、感謝祭前に1日40億ドルを超えた日が2日あったのは初めてだ。後払い（BNPL）決済額は61億ドル（6.5%増）だった。
NRFは11〜12月の小売売上を1兆130億ドル（4.2%増）と見る。週末に買い物をする予定の消費者は1億8,270万人。注目はAIだ。アドビ集計で感謝祭当日にAI経由で小売サイトへ流入したトラフィックは前年比159%増とシーズン最大の伸びとなった。モバイル比率は63%で過去最高だ。
変数は物流だ。「メイク・アマゾン・ペイ」の動きがブラックフライデーからサイバーマンデーまで続き、ドイツのノルトライン=ヴェストファーレン州のアマゾン4拠点では11月28日までストが予告されている。20か国以上で抗議やストが計画されている。

7. 韓国は利上げ、指数は耐えた
11月26日のコスピは13.70ポイント（0.29%）高の4,711.21で終えた。場中4,817.77（2.56%）まで上げたが終盤に戻した。コスダックは0.78%高の655.71。個人は1兆440億ウォン、外国人は1,136億ウォンを売り越し、機関が7,509億ウォンを買い越して指数を支えた。
韓国銀行は金融通貨委員会で政策金利を3.00%から3.25%へ25bp引き上げた。今年の成長率見通しを3.3%から3.9%、来年を2.9%から4.1%へ大きく上方修正した。ドットプロット21点のうち7点が3.75%、8点が3.50%で、追加利上げの余地を残した。
SKハイニックスは2.23%高の105万3,000ウォン、サムスン電子は0.35%高の17万1,300ウォン。現代自動車は3.90%安の25万9,000ウォン、LGエナジーソリューションは2.11%安の30万2,000ウォン、サムスンバイオロジクスは1.91%安の133万7,000ウォンだった。

8. 今夜確認すること
今夜の米国市場は半日だ。ブラックフライデーの初動データに小売株がどう反応するかが午後1時の閉場前に出る。午前8時30分（ET）には10月の商品貿易収支（1,359億ドルの赤字予想）と卸売在庫（0.5%増予想）が発表される。日本では11月の東京都区部CPI（生鮮除く、2.9%予想）が今朝発表された。
次の大きな関門は12月8〜9日のFOMCだ。その間に12月9日のブロードコム、12月17日のマイクロンの決算がAI設備投資サイクルへの答えを出す。市場の問いは一つ。利上げ局面でAI支出は増え続けられるのか。

一言まとめ
感謝祭で一日休んだ米国株は、今夜13時（ET）に閉まる半日の取引で再開する。直前の取引日はダウ+0.33%、ナスダック−0.62%と分かれ、休場中の先物は0.6〜0.7%上昇した。ビットコインは6万ドルを維持し、米国の消費者はブラックフライデーにオンラインで129億ドルを使う見込みだ。AI株は依然としてコストと金利という二つの変数の前に立っている。"""

ZH = """2026年11月26日（周四），美国因感恩节休市。次日27日（周五）黑色星期五重新开市，但只有半天交易。以下整理休市前最后一个交易日的数字、休市期间变动的股指期货与比特币，以及今晚需要关注的指标。

1. 今天美股13点收盘
纽约证券交易所（NYSE）与纳斯达克于韩国时间11月27日23:30开盘，11月28日凌晨3:00收盘，即纽约时间上午9:30至下午1:00。期权市场延后15分钟，下午1:15收盘；债券市场按SIFMA建议于下午2:00收盘。CME股指期货亦于下午1:15结束，且当日周五晚间不再重开。
CME将25日傍晚重开至27日收盘视为同一个交易日。休市前下的委托可能仍然有效，留有多日有效委托的人应在收盘前清理。
感恩节当天期货交易至下午1:00，下午6:00重开。重开后不久，韩国时间11月27日上午8:10左右，标普500期货上涨0.7%，纳斯达克100期货上涨0.6%，道指期货上涨277点（0.6%）。这说明休市期间的消息不差，但成交清淡的半天未必能维持这一涨幅。

2. 休市前最后一个交易日是“回补”
基准是25日收盘：道指收于50,182.95，上涨164.25点（0.33%）；标普500下跌18.31点（0.25%）至7,182.78；纳斯达克综合指数下跌147.74点（0.62%）至23,585.80；罗素2000上涨19.12点（0.71%）至2,704.06，中小盘更强。
盘中走势比收盘价更能说明本周的性质。道指一度下跌1,104.96点（2.21%），纳指下跌4.6%，标普500下跌3.21%至6,970.11。随后大部分跌幅被收复，道指转涨，纳指即使回升950点仍收跌。同一波反弹中，只有大型成长股恢复较慢。
标普500目前较10月6日的历史最高收盘7,818.93低8.14%。尚未触及通常称为调整的10%，但11月的波动幅度是今年最大的。

3. AI股先跌、后回
25日AI相关股再次下跌。英伟达跌3.91%至149.30美元，美光跌4.53%至601.25美元，甲骨文跌5.13%至103.88美元，创52周新低。亚马逊跌3.14%至244.43美元，微软跌1.25%至489.93美元，泛林集团跌5.68%至185.01美元。业绩与指引双双不及预期的安霸暴跌19%。以科技股为主的XLK ETF下跌近1%。
也有上涨的一方。Meta涨3.40%至609.89美元，惠普涨11.49%至31.15美元，第四财季调整后每股收益0.83美元（预期0.75美元），营收160亿美元（预期154.2亿美元）。IBM涨3.33%，赛富时涨2.04%。
英伟达自10月高点以来市值蒸发逾2万亿美元。11月23日黄仁勋回归CEO消息使其单日大涨31.5%，三天内已回吐大部分涨幅。标普全球将其AA评级列入“信用观察负面”，董事会调查与国会要求仍未结束。

4. 承压的三个原因
第一是成本。AI数据中心资本开支增速快于收入，靠举债融资的公司融资成本上升。CoreWeave 2031年到期债券收益率25日接近18%，甲骨文、Alphabet与CoreWeave的信用违约互换价格处于历史高位。
第二是利率。10月PCE同比3.8%（9月3.7%），核心PCE 3.3%，略高于预期。市场几乎认定12月8—9日FOMC将加息25个基点。
第三是关税。美国贸易代表办公室提议对包括中国、欧盟、日本、印度在内的14个经济体加征301条款关税15%—20%。实施需数月，但成本与利润率的重新计算已经开始。

5. 比特币守住6万美元
比特币在韩国时间11月27日上午8:17报60,390美元，较25日低点57,500美元回升约5%。但周内仍跌3.7%，较历史最高126,080美元低52%。
资金面仍不友好。美国现货比特币ETF在11月净流出53.9亿美元，为月度历史最大；25日再流出4.53亿美元，连续七个交易日净流出。今日有约70亿美元的比特币期权到期。
技术面上，50日均线跌破200日均线形成“死亡交叉”。6月低点（日线收盘58,525美元、周线收盘59,517美元）能否在收盘基础上守住，是本周剩余的关键。恐惧与贪婪指数为11，处于“极度恐惧”。

6. 黑色星期五美国人会花多少
Adobe Analytics预计黑色星期五美国线上销售额129亿美元（同比+9.2%），感恩节69亿美元（+8.5%），网络星期一151亿美元（+6.2%）。五天网络周合计475亿美元（+7.4%），占11—12月线上支出2,751亿美元的17.3%。
已经发生的数字也有。11月1日至22日，美国消费者线上支出825亿美元，同比增长9.1%，感恩节前首次出现两天单日超过40亿美元。先买后付（BNPL）金额61亿美元（+6.5%）。
全美零售联合会（NRF）预计11—12月零售销售1.013万亿美元（+4.2%），周末计划购物人数1.827亿。最值得关注的指标是AI：Adobe统计感恩节当天经AI进入零售网站的流量同比增长159%，为全季最大增幅；移动端占比达63%，创历史新高。
变量在物流。“Make Amazon Pay”行动从黑色星期五持续到网络星期一，德国北莱茵-威斯特法伦州四个亚马逊站点罢工至11月28日，20多个国家计划示威与罢工。

7. 韩国加息，指数守住
11月26日KOSPI收于4,711.21，上涨13.70点（0.29%），盘中最高4,817.77（+2.56%）后回吐涨幅。KOSDAQ涨0.78%至655.71。个人净卖出1.044万亿韩元，外国投资者净卖出1,136亿韩元，机构净买入7,509亿韩元支撑指数。
韩国银行将基准利率从3.00%上调25个基点至3.25%，并把今年增长预期从3.3%上调至3.9%、明年从2.9%上调至4.1%。点阵图21个点中有7个落在3.75%、8个落在3.50%，为继续加息留出空间。
SK海力士涨2.23%至1,053,000韩元，三星电子涨0.35%至171,300韩元。现代汽车跌3.90%至259,000韩元，LG新能源跌2.11%至302,000韩元，三星生物跌1.91%至1,337,000韩元。

8. 今晚要确认的事
今晚美股只有半天。零售股如何反应黑色星期五初期数据，会在下午1点收盘前显现。美国东部时间上午8:30公布10月商品贸易帐（预计逆差1,359亿美元）与批发库存（预计+0.5%）。日本今晨公布11月东京CPI，核心预期2.9%。
下一个大关口是12月8—9日FOMC。其间12月9日博通、12月17日美光财报将给出AI资本开支周期的答案。市场只问一个问题：在加息周期里，AI支出还能继续增长吗。

一句话总结
休市一天后，美股今晚以13:00（ET）收盘的半天交易重启。前一交易日道指+0.33%、纳指−0.62%出现分化，休市期间期货上涨0.6%—0.7%。比特币守住6万美元，美国消费者黑色星期五线上支出预计129亿美元。AI股依然面对成本与利率这两个变量。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "postType": "report",
    "store": "K-Trend Market",
    "priceKrw": 0,
    "releaseDate": "2026-11-27",
    "rating": 5,
    "imageUrl": C,
    "images": [C, G1, G2, G3, G4, G5],
    "affiliateUrl": "https://stock.naver.com/",
    "affiliatePlatform": "Coupang",
    "i18n": {
        "ko": {
            "title": "오늘 미국 증시는 13시에 닫는다 — 추수감사절 휴장 뒤 선물 +0.7%, AI주는 왜 여전히 무거운가",
            "summary": "11/26 추수감사절 휴장, 11/27 블랙프라이데이 반일장(ET 13:00 마감). 직전 11/25는 다우 50,182.95(+0.33%)·S&P 500 7,182.78(−0.25%)·나스닥 23,585.80(−0.62%). 휴장 중 선물은 S&P +0.7%·나스닥100 +0.6%로 재개, 비트코인은 6만 달러. 블랙프라이데이 온라인 129억 달러 전망까지 숫자로 정리했습니다.",
            "description": KO,
            "tasteReview": [
                "11/27(금) 반일장: NYSE·나스닥 ET 13:00 마감(한국 11/28 03:00), 옵션 13:15, 채권 14:00, CME 선물 13:15",
                "11/25 종가: 다우 50,182.95(+0.33%) · S&P 500 7,182.78(−0.25%) · 나스닥 23,585.80(−0.62%) · 러셀2000 +0.71%",
                "휴장 중 선물 재개(11/27 08:10 KST): S&P +0.7% · 나스닥100 +0.6% · 다우 +277p",
                "AI주: NVDA 149.30(−3.91%) · MU 601.25(−4.53%) · ORCL 103.88(−5.13%·52주 최저) / META +3.40% · HP +11.49%",
                "비트코인 $60,390(11/27 08:17 KST), 미 현물 ETF 11월 −$53.9억, 오늘 $70억 옵션 만기",
            ],
            "tips": "본 글은 공개된 시세·보도·공시를 정리한 정보 기록이며 특정 종목의 매수·매도를 권유하지 않습니다. 미국 지수는 2026년 11월 25일 정규장 종가, 선물·비트코인은 11월 27일 08:10~08:20 KST 조회값입니다. 반나절 장에서는 가격 변동성이 커질 수 있습니다.",
        },
        "en": {
            "title": "U.S. Stocks Close at 1 p.m. Today — Futures Up 0.7% After Thanksgiving, and Why AI Names Stay Heavy",
            "summary": "Markets were shut on 26 November and reopen for a half session on Black Friday, closing at 13:00 ET. The last full session: Dow 50,182.95 (+0.33%), S&P 500 7,182.78 (-0.25%), Nasdaq 23,585.80 (-0.62%). Futures added 0.7% during the holiday and bitcoin held $60,000, with $12.9 billion of online spending expected today.",
            "description": EN,
            "tasteReview": [
                "Half session on 27 November: NYSE and Nasdaq close 13:00 ET, options 13:15, bonds 14:00, CME futures 13:15",
                "Wednesday's close: Dow 50,182.95 (+0.33%), S&P 500 7,182.78 (-0.25%), Nasdaq 23,585.80 (-0.62%), Russell 2000 +0.71%",
                "Futures after the holiday reopen: S&P +0.7%, Nasdaq-100 +0.6%, Dow +277 points",
                "AI names: NVDA $149.30 (-3.91%), MU $601.25 (-4.53%), ORCL $103.88 (-5.13%, 52-week low); META +3.40%, HP +11.49%",
                "Bitcoin $60,390, spot ETFs -$5.39 billion in November, $7 billion of options expiring today",
            ],
            "tips": "This is a summary of public market data, reporting and filings, not investment advice. Index levels are U.S. regular-session closes on 25 November 2026; futures and bitcoin were read between 08:10 and 08:20 KST on 27 November 2026. A half session can widen price swings.",
        },
        "ja": {
            "title": "今日の米国株は13時に閉まる — 感謝祭明けの先物+0.7%、AI株が重い理由",
            "summary": "11月26日は感謝祭で休場、27日はブラックフライデーの半日取引（ET13:00終了）。直前の25日はダウ50,182.95（+0.33%）、S&P500 7,182.78（−0.25%）、ナスダック23,585.80（−0.62%）。休場中に先物はS&P+0.7%、ビットコインは6万ドルを維持し、ブラックフライデーのオンライン売上は129億ドルが見込まれる。",
            "description": JA,
            "tasteReview": [
                "27日は半日取引：NYSE・ナスダックはET13:00終了（韓国時間28日03:00）、オプション13:15、債券14:00、CME先物13:15",
                "25日終値：ダウ50,182.95（+0.33%）、S&P500 7,182.78（−0.25%）、ナスダック23,585.80（−0.62%）、ラッセル2000 +0.71%",
                "休場明けの先物：S&P+0.7%、ナスダック100+0.6%、ダウ+277ポイント",
                "AI株：NVDA 149.30ドル（−3.91%）、MU 601.25ドル（−4.53%）、ORCL 103.88ドル（−5.13%・52週安値）、META +3.40%、HP +11.49%",
                "ビットコイン60,390ドル、米現物ETFは11月に53.9億ドル流出、今日70億ドルのオプション満期",
            ],
            "tips": "本記事は公開された相場データ・報道・開示を整理した情報記録であり、個別銘柄の売買を推奨するものではありません。指数は2026年11月25日の通常取引終値、先物とビットコインは11月27日08:10〜08:20 KSTの取得値です。半日取引では値動きが大きくなることがあります。",
        },
        "zh": {
            "title": "今天美股13点收盘——感恩节后期货涨0.7%，AI股为何仍然沉重",
            "summary": "11月26日感恩节休市，27日黑色星期五恢复交易但只有半天（美东13:00收盘）。前一交易日道指50,182.95（+0.33%）、标普500 7,182.78（−0.25%）、纳指23,585.80（−0.62%）。休市期间期货上涨0.7%，比特币守住6万美元，黑色星期五线上销售预计129亿美元。",
            "description": ZH,
            "tasteReview": [
                "11月27日半天交易：NYSE与纳斯达克美东13:00收盘（韩国时间28日03:00），期权13:15，债券14:00，CME期货13:15",
                "25日收盘：道指50,182.95（+0.33%）、标普500 7,182.78（−0.25%）、纳指23,585.80（−0.62%）、罗素2000 +0.71%",
                "休市后期货：标普+0.7%、纳斯达克100 +0.6%、道指+277点",
                "AI股：NVDA 149.30美元（−3.91%）、MU 601.25美元（−4.53%）、ORCL 103.88美元（−5.13%，52周新低）、META +3.40%、HP +11.49%",
                "比特币60,390美元，美国现货ETF 11月流出53.9亿美元，今日70亿美元期权到期",
            ],
            "tips": "本文整理公开行情、报道与披露资料，不构成任何个股买卖建议。指数为2026年11月25日常规交易收盘价，期货与比特币为11月27日08:10—08:20 KST查询值。半天交易可能放大价格波动。",
        },
    },
}

if __name__ == "__main__":
    publish(POST)
