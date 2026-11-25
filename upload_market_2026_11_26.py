#!/usr/bin/env python3
"""2026-11-26 아침 증시 리포트: 2026-11-25(수) 미국장 마감 → Supabase posts(4개국어) + ISR revalidate.

모든 수치는 2026-11-26 08:20~08:35 KST 확인:
 - 야후 파이낸스 일별 종가/시세(work/market-2026-11-26/quotes.json, quotes2.json), ^GSPC 실화면 캡처
 - CNBC 라이브 블로그(11/25), CNBC PCE(11/25 08:31 ET), CNBC 관세 301조(11/25), CNBC 종목 무버(11/25)
 - AP(11/25), MarketWatch(11/25), investinglive(11/25), S&P 글로벌 신용평가 보도(CNBC)
 - 연합뉴스·매일경제(11/25 마감), YTN, 파이낸셜뉴스(11/26 금통위), 한국은행
"""

import json
import os
import urllib.request

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
SLUG = "thanksgiving-eve-ai-rout-dow-rebound-2026-11-26"

C = "/images/products/market-ai-rout-cover-2026-11-26.png"
G1 = "/images/products/market-ai-rout-index-board-2026-11-26.png"
G2 = "/images/products/market-ai-rout-intraday-2026-11-26.png"
G3 = "/images/products/market-ai-rout-movers-2026-11-26.png"
G4 = "/images/products/market-ai-rout-macro-2026-11-26.png"
G5 = "/images/products/market-ai-rout-calendar-2026-11-26.png"

KO_DESC = """11월 25일(수) 뉴욕 정규장은 하루에 두 번 방향을 바꿨다. 개장 직후 다우는 1,104포인트(2.21%) 빠지고 S&P 500은 3.21% 밀렸고, 나스닥은 4.6% 하락해 약세장 문턱(고점 대비 −20%)까지 2%포인트 남짓 남겼다. 오후장에 매도가 멈추자 다우는 플러스로 돌아서 50,182.95(+164.25, +0.33%)에 마감했다. S&P 500은 −0.25%(7,182.78), 나스닥은 −0.62%(23,585.80)로 지수별로 갈렸고 러셀 2000은 +0.71% 올랐다. 이 글은 그 하루를 숫자로 정리하고, 왜 지수가 갈렸는지, 다음 관문이 무엇인지 남긴다.

1. 숫자부터 — 다우 +0.33%, S&P −0.25%, 나스닥 −0.62%
S&P 500은 18.31포인트(0.25%) 내린 7,182.78, 나스닥 종합지수는 147.73포인트(0.62%) 내린 23,585.80, 다우존스는 164.25포인트(0.33%) 오른 50,182.95에 마감했다. 러셀 2000은 19.12포인트(0.71%) 오른 2,704.06, 나스닥 100은 167.27포인트(0.64%) 내린 26,046.90이다. S&P 500의 연초 이후 상승률은 5%로 줄었다.
거래량은 S&P 500 기준 34억7,000만 주로 20일 평균(52억9,000만 주)의 3분의 2 수준이었다. 다음 날 추수감사절 휴장을 앞둔 얇은 장이었다.
변동성은 오히려 커졌다. VIX는 장중 33.70까지 올랐다가 28.29(+7.32%)로 마감했다. 전일 종가 26.36보다 높고, 20을 크게 웃도는 수준이 두 달째 이어지고 있다.
채권은 강했다. 미 10년물 금리는 4.848%로 5.6bp 내렸고, 2년물은 8.2bp 내린 4.588%, 30년물은 5.235%다. 달러인덱스는 103.70(−0.11%)으로 약해졌다. 유가는 WTI 83.86달러(+2.21%), 브렌트 90.52달러(−0.96%)였고, 금은 3,597.40달러(+1.00%)로 반등했다. 장중 3,425.20달러까지 밀려 2025년 8월 말 이후 처음 3,500달러 아래를 찍은 뒤 되돌린 값이다.

2. 장중에 무슨 일이 있었나
개장 직후 나스닥은 3.3%, 다우는 765포인트(1.5%), S&P 500은 2.3% 밀리며 출발했다. 오전 중 S&P 500 저점은 6,970.11(−3.21%)까지 내려갔고, 다우는 1,104.96포인트(2.21%) 빠진 48,913.74를 찍었다. 나스닥 저점은 −4.6%였다.
반등은 세 가지가 겹치며 나왔다. 첫째, 마이클 버리가 이날 뉴스레터에서 "팔란티어 풋과 메트라이프 풋을 빼면 지금은 일시적으로 거의 전부 롱"이라고 적은 글이 오후장에 퍼졌다. 둘째, 추수감사절을 앞둔 얇은 거래에서 매도 물량이 줄자 가격이 빠르게 되돌아왔다. 셋째, 미 당국이 상원 보좌진에게 '젠슨 황과 관계를 맺었던 중국 기술경영진이 중국 정보기관의 지시를 받았다는 증거가 없다'고 브리핑했다는 보도가 나오며 기술주 낙폭이 줄었다.
결과적으로 다우는 저점에서 1,269포인트를 되찾아 플러스로 끝났고, S&P 500은 저점 대비 3.0% 올랐지만 플러스로 돌아서지는 못했다. 나스닥은 저점에서 950포인트 넘게 회복하고도 −0.62%로 마감했다. S&P 500 종목 중 오른 종목이 내린 종목의 3배였는데 지수는 내렸다는 점이 이날의 성격을 보여준다. 지수는 기술주 몇 개가 끌어내렸고, 나머지는 올랐다.

3. 물가가 다시 올라갔다 — 10월 PCE 3.8%
이날 오전 발표된 10월 개인소비지출(PCE) 물가지수는 전년 대비 3.8% 올랐다. 9월 3.7%에서 0.1%포인트 더 높아진 값이고, 연준 목표(2%)의 두 배에 가깝다. 식품·에너지를 뺀 근원 PCE는 3.3%로 시장 예상(3.2%)을 0.1%포인트 웃돌았다. 전월 대비로는 0.3% 상승이었다.
같은 날 나온 3분기 국내총생산(GDP) 수정치는 연율 4.3%로 상향됐다. 소비는 4.2%, 연준이 수요 판단에 참고하는 '민간 국내 최종판매'는 5.8% 늘었다. 신규 실업수당 청구는 18만9,000건으로 예상(20만 건)을 밑돌며 1960년대 말 수준에 가까운 낮은 값을 이어갔다.
시장 반응은 금리였다. CME 페드워치 기준 12월 8~9일 FOMC의 25bp 인상은 100% 반영돼 있다. 2027년 추가 인상은 두 차례까지 반영됐고, 세 번째 확률은 1/3로 전일(50%)보다 낮아졌다. 물가가 뜨거운데도 채권 금리가 내린 것은, 시장이 '경기 둔화'를 함께 가격에 넣기 시작했다는 신호로 읽힌다.

4. 관세 — 14개국에 301조, 중국은 약 45%
미 무역대표부(USTR)는 이날 중국·EU·일본·인도 등 14개국을 대상으로 무역법 301조에 근거한 새 관세를 제안했다. 대부분 15~20%이고, 기존 무역합의에서 정한 세율을 넘지 않으며 기존 관세에 더해지지 않는다고 당국자는 설명했다. 예외는 중국이다. 중국에는 20%가 붙고, 2018년 강제기술이전 관련 25% 위에 얹혀 약 45%가 된다. 7월 기준 미국의 대중 평균 관세율은 36.5%였다.
제이미슨 그리어 무역대표부 대표는 CNBC에 "실제 시행까지는 몇 달이 걸린다"고 말했다. 당장의 물가 충격이 아니라 협상 카드라는 뜻이지만, 시장은 이날 아침 이 헤드라인에 먼저 반응했다.

5. 화제 AI주 셋 — 엔비디아·마이크론·앤트로픽
엔비디아(NVDA)는 149.30달러로 3.91% 내렸다. 11월 한 달로는 27% 하락이다. 10월 30일 204.64달러에서 149.30달러가 됐고, 52주 최고가 243.37달러와 비교하면 39% 낮다. 이날 S&P 글로벌이 신용등급(AA) 전망을 'CreditWatch Negative'로 내렸다. 사유는 경영·지배구조 리스크, 이사회 독립성, 최고경영자 의존(키맨) 리스크다. 다음 주로 예고된 미 상원 청문회와 회계 조사도 남아 있다.
마이크론(MU)은 601.25달러로 4.57% 내렸다. 10월 말 884.74달러 대비 32% 하락이다. BNP파리바가 메모리 공급 과잉을 경고하면서 메모리 종목이 함께 밀렸다. 반도체 ETF(SMH)는 11월 11일 이후 17% 넘게 빠져 2025년 4월 이후 가장 나쁜 10거래일을 기록 중이다.
앤트로픽(ANT)은 82.79달러로 1.08% 올랐지만 여전히 공모가 83달러 아래다. 11월 19일 상장 이후 4거래일 만인 전일 81.91달러로 공모가를 처음 밑돌았고, 이날 소폭 반등했다. 오라클 −5.13%, 알파벳 −2.13%, 아마존 −3.12%도 AI 설비투자 우려에 함께 밀렸다.
반대로 오른 AI 관련주도 있다. 메타(META) +3.40%, 팔란티어 +1.49%, 슈퍼마이크로 +3.05%, 브로드컴 −0.07%로 보합이었다. 스페이스X(SPCX)는 FCC가 AI 컴퓨팅 위성 100만 기 발사를 승인했다는 소식에 1.30% 올랐다.

6. 오른 쪽은 따로 있었다 — 메타와 HP
메타는 609.89달러로 3.40% 올랐다. 같은 날 임원이 "AI 에이전트 '뮤즈'가 광고 전환율을 끌어올린다"고 말한 것이 재료가 됐다. 지난주 AI 에이전트가 넣은 주문의 51%가 메타를 통해 이뤄졌다는 집계도 함께 인용됐다. 다만 올해 설비투자 가이던스가 1,350억~1,450억 달러로 영업현금흐름을 웃도는 부담은 남아 있다.
HP(HPQ)는 31.15달러로 11.49% 급등했다. 4분기 조정 EPS 0.83달러(예상 0.75달러), 매출 160억 달러(예상 154.2억 달러)로 모두 예상을 넘었고, 배당을 30센트에서 31센트로 올렸다. IBM +3.33%, 세일즈포스 +2.04%, 액손 +7.43%도 올랐다.
델(DELL)은 297.06달러로 0.60% 올랐다. 전일 발표한 3분기 실적은 조정 EPS 9.45달러(예상 6.59달러), 매출 549.4억 달러(예상 493.2억 달러), AI 서버 수주잔고 1,323억 달러였다. 좋은 실적에도 전일 시간외에서 11.8% 빠졌던 것을 이날 하루로 다 되돌리지는 못했다.

7. 한국은 어제 −6.16%, 오늘 금통위
한국 시장은 하루 먼저 급락했다. 11월 25일 코스피는 308.52포인트(6.16%) 내린 4,697.51에 마감했다. 1월 13일(4,692.64) 이후 10개월여 만의 최저 종가이고, 6월 19일 장중 고점(9,385.59) 대비 50.22% 낮은 자리다. 개장 8분 만에 매도 사이드카가 발동했고, 장중 4,672.55(−6.66%)까지 밀렸다.
삼성전자는 9.87% 내린 17만700원, SK하이닉스는 11.05% 내린 103만 원으로 마감했다. 삼성전자 시가총액은 997조9,598억 원으로 3월 31일 이후 처음 1,000조 원 아래로 내려왔다. 외국인은 1조8,994억 원을 순매도했고(11월 6일 이후 최대), 개인은 1조4,232억 원을 순매수했다. 코스닥은 2.29% 내린 650.64다.
오늘(11월 26일) 오전 10시에는 한국은행 금융통화위원회가 열린다. 기준금리 3.00%에서 3.25%로의 인상이 우세하다. 금융투자협회 설문에서 채권 보유·운용 종사자 100명 중 54명이 인상을 예상했고, 3분기 GDP가 전기 대비 1.0% 늘어 한은 전망(0.3%)을 크게 웃돈 점, 소비자물가와 근원물가가 모두 2.8%인 점이 인상 근거로 꼽힌다. 함께 나오는 점도표와 수정 성장률 전망이 다음 숫자다.

8. 다음 관문
미국 시장은 11월 26일 추수감사절로 휴장하고, 27일에는 13시(ET)에 조기 마감한다. 한국은 26일 정상 거래한다. 12월 8~9일 FOMC에서 25bp 인상이 기정사실로 반영돼 있고, 12월 9일 브로드컴, 12월 17일 마이크론 실적이 AI 설비투자 사이클의 답을 줄 차례다.

한 줄 정리
이날은 "지수가 오른 날"도 "무너진 날"도 아니었다. 다우는 1,104포인트를 잃었다가 되찾았고, 나스닥은 끝내 못 돌아왔고, S&P 500 종목 4개 중 3개는 올랐다. 갈린 기준은 AI 하드웨어와 나머지다. 물가(PCE 3.8%)와 관세(14개국 301조)라는 새 악재가 얹힌 상태에서, 시장은 12월 9일 FOMC와 브로드컴 실적까지 'AI에 얼마를 더 걸 수 있는지'를 계속 계산할 것이다."""

EN_DESC = """Wednesday 25 November was a session that changed direction twice. Minutes after the open the Dow was down 1,104.96 points (2.21%), the S&P 500 was off 3.21% and the Nasdaq was 4.6% lower — within two percentage points of a bear market. The selling stopped in the afternoon, and the Dow closed higher at 50,182.95 (+164.25, +0.33%). The S&P 500 finished down 0.25% at 7,182.78 and the Nasdaq down 0.62% at 23,585.80, while the Russell 2000 gained 0.71%.

1. The numbers
The S&P 500 lost 18.31 points to 7,182.78, the Nasdaq Composite 147.73 points to 23,585.80 and the Dow added 164.25 points to 50,182.95. The Russell 2000 rose 19.12 points (0.71%) to 2,704.06 and the Nasdaq 100 fell 167.27 points (0.64%) to 26,046.90. The S&P 500's year-to-date gain is now 5%.
Volume was thin: 3.47 billion shares on the S&P 500 against a 20-day average of 5.29 billion, the day before Thanksgiving.
Volatility rose even as the Dow recovered. The VIX traded as high as 33.70 before closing at 28.29 (+7.32%), still well above 20 for a second month.
Bonds rallied. The 10-year Treasury yield fell 5.6 basis points to 4.848%, the 2-year dropped 8.2bp to 4.588% and the 30-year sat at 5.235%. The dollar index slipped 0.11% to 103.70. WTI crude settled at $83.86 (+2.21%) and Brent at $90.52 (−0.96%). Gold rose 1.00% to $3,597.40 after touching $3,425.20 intraday, its first trip below $3,500 since late August 2025.

2. What happened during the session
The Nasdaq opened 3.3% lower, the Dow down 765 points and the S&P 500 down 2.3%. The S&P 500's low of 6,970.11 was 3.21% below Tuesday's close; the Dow's low was 48,913.74, down 1,104.96 points; the Nasdaq was down 4.6% at its worst.
Three things combined to turn it around. First, a Michael Burry newsletter note circulated in the afternoon saying that apart from Palantir and MetLife puts he was "temporarily almost entirely long". Second, with thin pre-holiday volume, selling simply ran out. Third, reports that U.S. officials told congressional staffers in a classified briefing there was no evidence the Chinese tech executive connected to Jensen Huang was directed by Chinese intelligence eased the pressure on tech.
The Dow recovered 1,269 points from its low to close green. The S&P 500 climbed 3.0% off its low but never turned positive. The Nasdaq clawed back more than 950 points and still closed down 0.62%. More than three S&P 500 stocks rose for every one that fell — a reminder that a handful of tech names moved the index, not the market.

3. Inflation got worse: October PCE at 3.8%
October's PCE price index rose 0.3% on the month and 3.8% year over year, up from 3.7% in September and nearly double the Fed's 2% target. Core PCE came in at 3.3%, a tenth above the 3.2% consensus.
Third-quarter GDP was revised up to a 4.3% annualized rate, with consumer spending up 4.2% and real final sales to private domestic purchasers up 5.8%. Initial jobless claims fell to 189,000, below the 200,000 expected and near the lowest levels since the late 1960s.
Markets still fully price a 25bp hike at the 8–9 December FOMC. Two hikes are priced for 2027, with the odds of a third down to about one in three from 50% on Tuesday. Yields falling on a hot inflation print is the market beginning to price slower growth alongside it.

4. Tariffs: Section 301 on 14 partners, China near 45%
The USTR proposed new Section 301 tariffs on 14 economies including China, the EU, Japan and India. Most rates are 15–20%, do not stack on existing duties and do not exceed levels already agreed in trade deals, a senior official said. China is the exception: 20% on top of the 25% imposed in 2018 over forced technology transfer, taking the effective rate to roughly 45%, against an average of 36.5% in July. Trade Representative Jamieson Greer told CNBC the measures are unlikely to take effect for months.

5. Three AI stocks in focus
Nvidia fell 3.91% to $149.30 and is down 27% in November, from $204.64 on 30 October — 39% below its 52-week high of $243.37. S&P Global placed its AA rating on CreditWatch Negative, citing management and governance risk, board independence and key-man risk. A Senate hearing and an accounting probe are still ahead.
Micron fell 4.57% to $601.25, down 32% from $884.74 at the end of October, after BNP Paribas warned of memory oversupply. The VanEck Semiconductor ETF (SMH) has lost more than 17% since 11 November, its worst 10-session stretch since April 2025.
Anthropic rose 1.08% to $82.79 but remains below its $83 IPO price, having closed under it for the first time on Tuesday. Oracle fell 5.13%, Alphabet 2.13% and Amazon 3.12%. On the other side, Meta gained 3.40%, Palantir 1.49% and Super Micro 3.05%, while SpaceX rose 1.30% after the FCC approved one million AI computing satellites.

6. The winners were elsewhere: Meta and HP
Meta rose 3.40% to $609.89 after an executive said its Muse AI agent lifts ad conversions; Meta accounted for 51% of AI-agent orders placed in the past week. The offsetting worry is capex: guidance of $135–145 billion this year runs above operating cash flow.
HP jumped 11.49% to $31.15 on fourth-quarter adjusted EPS of $0.83 (expected $0.75), revenue of $16 billion (expected $15.42 billion) and a dividend increase to 31 cents. IBM gained 3.33%, Salesforce 2.04% and Axon 7.43%. Dell added 0.60% to $297.06 after reporting adjusted EPS of $9.45 on revenue of $54.94 billion and an AI backlog of $132.3 billion.

7. Korea fell 6.16% on Wednesday; the BOK decides today
The KOSPI closed at 4,697.51, down 308.52 points or 6.16% — its lowest close since 13 January and 50.22% below its 19 June intraday high of 9,385.59. A sell-side sidecar triggered eight minutes after the open and the index touched 4,672.55 (−6.66%). Samsung Electronics fell 9.87% to 170,700 won, dropping below a 1,000-trillion-won market cap for the first time since 31 March, and SK Hynix fell 11.05% to 1,030,000 won. Foreigners sold a net 1.8994 trillion won, the largest since 6 November, while retail bought 1.4232 trillion won. The KOSDAQ fell 2.29% to 650.64.
The Bank of Korea meets at 10:00 today. A 25bp hike from 3.00% to 3.25% is expected: 54 of 100 bond professionals surveyed by the Korea Financial Investment Association expect an increase, with third-quarter GDP growth of 1.0% quarter on quarter far above the BOK's 0.3% forecast and both headline and core inflation at 2.8%.

8. What comes next
U.S. markets are closed on Thursday for Thanksgiving and close early at 13:00 ET on Friday; Korea trades normally. The 8–9 December FOMC, Broadcom's results on 9 December and Micron's on 17 December are the next answers on whether the AI capex cycle is slowing.

In one line
This was neither a good day nor a crash. The Dow lost 1,104 points and got all of them back, the Nasdaq did not, and three out of four S&P 500 stocks rose. The line that split the market was AI hardware versus everything else — with PCE at 3.8% and tariffs on 14 economies now added to the calculation."""

JA_DESC = """11月25日（水）のニューヨーク市場は、1日のうちに2度方向を変えた。寄り付き直後にダウは1,104.96ポイント（2.21%）下落し、S&P500は3.21%安、ナスダックは4.6%安で弱気相場の入り口（高値比−20%）まで2%ポイント強に迫った。午後に売りが止まるとダウはプラスに転じ、50,182.95（+164.25、+0.33%）で引けた。S&P500は−0.25%（7,182.78）、ナスダックは−0.62%（23,585.80）と指数ごとに分かれ、ラッセル2000は+0.71%だった。

1. 数字から
S&P500は18.31ポイント安の7,182.78、ナスダック総合は147.73ポイント安の23,585.80、ダウは164.25ポイント高の50,182.95。ラッセル2000は19.12ポイント高の2,704.06、ナスダック100は167.27ポイント安の26,046.90。S&P500の年初来上昇率は5%に縮んだ。
出来高はS&P500ベースで34億7,000万株と、20日平均（52億9,000万株）の3分の2。感謝祭の前日の薄い市場だった。
ボラティリティはむしろ上がった。VIXは寄り後に33.70まで上昇し、28.29（+7.32%）で引けた。20を大きく上回る水準が2か月続いている。
債券は買われた。米10年債利回りは5.6bp低下の4.848%、2年債は8.2bp低下の4.588%、30年債は5.235%。ドル指数は103.70（−0.11%）。WTIは83.86ドル（+2.21%）、ブレントは90.52ドル（−0.96%）。金は3,597.40ドル（+1.00%）で、一時3,425.20ドルまで下げて2025年8月末以来はじめて3,500ドルを割った後に戻した。

2. 場中に何が起きたか
寄り付き直後、ナスダックは3.3%安、ダウは765ポイント安、S&P500は2.3%安で始まった。S&P500の安値は6,970.11（−3.21%）、ダウの安値は48,913.74（−1,104.96ポイント）、ナスダックは最大−4.6%だった。
反発は3つが重なった。第一に、マイケル・バーリが「パランティアとメットライフのプットを除けば、今は一時的にほぼ全面ロング」と書いたニュースレターが午後に広がった。第二に、感謝祭前の薄商いで売りが尽きた。第三に、米当局が上院スタッフに対し、ジェンセン・フアンと関係があった中国の技術経営者が中国の情報機関の指示を受けた証拠はないと説明したとの報道で、ハイテク株の下げが縮んだ。
ダウは安値から1,269ポイント戻してプラスで終了。S&P500は安値から3.0%戻したがプラスには届かず、ナスダックは950ポイント以上戻しても−0.62%だった。S&P500銘柄では上昇が下落の3倍だったのに指数は下げた——指数を動かしたのはテクノロジー数銘柄だった。

3. インフレは再加速：10月PCE 3.8%
10月のPCE価格指数は前月比+0.3%、前年比+3.8%で、9月の3.7%から0.1ポイント上昇した。FRBの目標（2%）のほぼ2倍。食品・エネルギーを除くコアPCEは3.3%で、市場予想（3.2%）を0.1ポイント上回った。
同日発表の7〜9月期GDP改定値は年率4.3%に上方修正され、個人消費は4.2%、FRBが需要判断に使う「民間国内最終販売」は5.8%増。新規失業保険申請は18万9,000件で予想（20万件）を下回り、1960年代末並みの低水準が続く。
市場は12月8〜9日のFOMCでの25bp利上げを100%織り込んでいる。2027年は2回までの利上げが織り込まれ、3回目の確率は前日の50%から3分の1に下がった。インフレが高い日に利回りが下がったのは、市場が景気減速も同時に値付けし始めたという合図だ。

4. 関税：14か国に301条、中国は約45%
USTRは中国・EU・日本・インドなど14か国を対象に、通商法301条に基づく新関税を提案した。多くは15〜20%で、既存関税に上乗せされず、これまでの通商合意の水準を超えないと当局者は説明した。例外は中国で、2018年の技術移転関連25%の上に20%が乗り、実効で約45%になる。7月時点の対中平均関税率は36.5%だった。グリアー通商代表はCNBCに「発効まで数か月かかる」と述べている。

5. 話題のAI株3つ
エヌビディアは3.91%安の149.30ドル。11月だけで27%下落し、10月30日の204.64ドルから52週高値243.37ドル比では39%低い。S&PグローバルはAA格付けを「クレジットウォッチ・ネガティブ」に指定し、経営・ガバナンス、取締役会の独立性、キーマンリスクを挙げた。来週の上院公聴会と会計調査も残る。
マイクロンは4.57%安の601.25ドルで、10月末の884.74ドルから32%下落。BNPパリバがメモリーの供給過剰を警告した。半導体ETF（SMH）は11月11日以降17%超下落し、2025年4月以来最悪の10営業日となっている。
アントロピックは1.08%高の82.79ドルだが、公開価格83ドルを依然下回る。前日に上場後はじめて公開価格を割り込み、この日は小幅に戻した。オラクル−5.13%、アルファベット−2.13%、アマゾン−3.12%。一方でメタ+3.40%、パランティア+1.49%、スーパーマイクロ+3.05%、スペースXはFCCがAI計算衛星100万基を承認したことで+1.30%だった。

6. 上がった側：メタとHP
メタは3.40%高の609.89ドル。幹部が「AIエージェント『ミューズ』が広告の転換率を押し上げる」と述べ、直近1週間にAIエージェントが入れた注文の51%がメタ経由だったという集計も材料になった。一方で今年の設備投資は1,350億〜1,450億ドルと営業キャッシュフローを上回る。
HPは11.49%高の31.15ドル。4Q調整EPS 0.83ドル（予想0.75ドル）、売上160億ドル（予想154.2億ドル）で予想を上回り、配当を30セントから31セントに増やした。IBM +3.33%、セールスフォース+2.04%、アクソン+7.43%。デルは0.60%高の297.06ドルで、3Q調整EPS 9.45ドル、売上549.4億ドル、AI受注残1,323億ドルだった。

7. 韓国は前日−6.16%、今日は金融通貨委員会
コスピは308.52ポイント（6.16%）安の4,697.51で引けた。1月13日以来約10か月ぶりの安値で、6月19日の日中高値（9,385.59）比−50.22%。寄り付き8分で売りサイドカーが発動し、日中は4,672.55（−6.66%）まで下げた。サムスン電子は9.87%安の17万700ウォン、SKハイニックスは11.05%安の103万ウォン。サムスン電子の時価総額は997兆9,598億ウォンと3月31日以来はじめて1,000兆ウォンを下回った。外国人は1兆8,994億ウォンを売り越し、個人は1兆4,232億ウォンを買い越した。コスダックは2.29%安の650.64。
今日（11月26日）午前10時に韓国銀行の金融通貨委員会がある。基準金利は3.00%から3.25%への引き上げが有力で、債券運用担当者100人のうち54人が引き上げを予想。7〜9月期GDPが前期比1.0%増と韓国銀行の見通し（0.3%）を大きく上回り、消費者物価とコア物価がともに2.8%という点が根拠だ。

8. 次の関門
米国市場は26日の感謝祭で休場、27日は東部時間13時に早期終了。韓国は26日は通常取引。12月8〜9日のFOMC、12月9日のブロードコム、12月17日のマイクロンの決算がAI設備投資サイクルの答えになる。

一行まとめ
この日は「上がった日」でも「崩れた日」でもない。ダウは1,104ポイントを失って取り戻し、ナスダックは戻り切らず、S&P500銘柄の4分の3は上がった。分けたのはAIハードウェアとそれ以外。PCE 3.8%と14か国への関税という新しい材料を抱えたまま、市場は12月9日のFOMCとブロードコム決算まで計算を続ける。"""

ZH_DESC = """11月25日（周三）纽约常规交易时段一天之内两次改变方向。开盘后道指下跌1,104.96点（2.21%），标普500跌3.21%，纳指跌4.6%，距熊市门槛（较高点−20%）仅剩约2个百分点。午盘后抛售停止，道指转涨收于50,182.95点（+164.25，+0.33%）。标普500跌0.25%收7,182.78点，纳指跌0.62%收23,585.80点，罗素2000涨0.71%。

1. 先看数字
标普500跌18.31点至7,182.78点，纳指综合跌147.73点至23,585.80点，道指涨164.25点至50,182.95点。罗素2000涨19.12点（0.71%）至2,704.06点，纳指100跌167.27点（0.64%）至26,046.90点。标普500年内涨幅收窄至5%。
成交清淡：标普500成交34.7亿股，仅为20日均值（52.9亿股）的三分之二，正值感恩节前一日。
波动率反而上升。VIX盘中最高升至33.70，收于28.29（+7.32%），连续两个月明显高于20。
债券走强：10年期美债收益率降5.6个基点至4.848%，2年期降8.2个基点至4.588%，30年期报5.235%。美元指数跌0.11%至103.70。WTI原油收83.86美元（+2.21%），布伦特90.52美元（−0.96%）。黄金涨1.00%至3,597.40美元，盘中一度跌至3,425.20美元，为2025年8月底以来首次跌破3,500美元后回升。

2. 盘中发生了什么
开盘后纳指跌3.3%、道指跌765点、标普500跌2.3%。标普500盘中低点6,970.11点（−3.21%），道指低点48,913.74点（−1,104.96点），纳指最大跌幅4.6%。
反弹由三件事叠加而成。一是迈克尔·伯里的通讯在午后流传，称"除帕兰提尔和大都会人寿的看跌期权外，目前几乎全部做多"。二是感恩节前的清淡成交中卖盘耗尽。三是媒体报道美国官员在机密简报中告诉国会工作人员，没有证据显示与黄仁勋有关系的中国技术高管受中国情报机构指使，科技股跌幅因此收窄。
道指从低点回升1,269点收涨；标普500从低点回升3.0%但未能转正；纳指回升逾950点仍收跌0.62%。标普500成分股中上涨家数是下跌的三倍，而指数仍然下跌——推动指数的是少数科技股，不是整个市场。

3. 通胀再度升温：10月PCE 3.8%
10月PCE物价指数环比涨0.3%，同比涨3.8%，高于9月的3.7%，接近美联储2%目标的两倍。核心PCE为3.3%，比市场预期的3.2%高出0.1个百分点。
同日公布的三季度GDP修正值为年化4.3%，个人消费增4.2%，美联储关注的实际私人国内最终销售增5.8%。上周初请失业金人数降至18.9万，低于预期的20万，接近1960年代末以来的低位。
市场已完全计入12月8—9日FOMC加息25个基点。2027年另有两次加息被计入，第三次的概率从周二的50%降至约三分之一。通胀数据偏热而收益率下行，说明市场开始同时为增长放缓定价。

4. 关税：对14个经济体启动301条款，中国约45%
美国贸易代表办公室提议对中国、欧盟、日本、印度等14个经济体加征301条款新关税。多数税率为15%—20%，不与现有关税叠加，也不超过此前贸易协议的水平。中国是例外：在2018年因强制技术转让加征的25%之上再加20%，实际税率约45%，而7月时对华平均关税为36.5%。贸易代表格里尔对CNBC表示，措施"数月内不会生效"。

5. 三只热门AI股
英伟达跌3.91%至149.30美元，11月累计下跌27%，从10月30日的204.64美元跌至当前水平，较52周高点243.37美元低39%。标普全球将其AA评级列入"信用观察负面"，理由是管理与治理风险、董事会独立性以及关键人物风险；下周的参议院听证会与会计调查仍未结束。
美光跌4.57%至601.25美元，较10月底的884.74美元下跌32%。法国巴黎银行警告存储芯片供应过剩。半导体ETF（SMH）自11月11日以来跌逾17%，为2025年4月以来最差的10个交易日。
Anthropic涨1.08%至82.79美元，仍低于83美元的发行价，前一日上市后首次收于发行价之下。甲骨文跌5.13%，Alphabet跌2.13%，亚马逊跌3.12%。另一方面，Meta涨3.40%，帕兰提尔涨1.49%，超微涨3.05%，SpaceX在美国联邦通信委员会批准发射100万颗AI计算卫星后涨1.30%。

6. 上涨的一方：Meta与惠普
Meta涨3.40%至609.89美元，公司高管称AI智能体"Muse"提升了广告转化率，过去一周AI智能体下的订单中有51%来自Meta。但今年资本开支指引为1,350亿—1,450亿美元，高于经营现金流。
惠普大涨11.49%至31.15美元，第四财季调整后每股收益0.83美元（预期0.75美元），营收160亿美元（预期154.2亿美元），并将股息从30美分提高至31美分。IBM涨3.33%，赛富时涨2.04%，Axon涨7.43%。戴尔涨0.60%至297.06美元，第三财季调整后每股收益9.45美元，营收549.4亿美元，AI订单储备1,323亿美元。

7. 韩国昨日跌6.16%，今日召开金融货币委员会
KOSPI收于4,697.51点，跌308.52点（6.16%），为1月13日以来最低收盘，较6月19日盘中高点（9,385.59）低50.22%。开盘8分钟即触发卖出熔断，盘中一度跌至4,672.55（−6.66%）。三星电子跌9.87%至170,700韩元，市值997.96万亿韩元，为3月31日以来首次跌破1,000万亿韩元；SK海力士跌11.05%至1,030,000韩元。外国投资者净卖出1.8994万亿韩元，个人净买入1.4232万亿韩元。KOSDAQ跌2.29%至650.64点。
今日（11月26日）上午10点，韩国银行召开金融货币委员会。基准利率从3.00%上调至3.25%的可能性较大：韩国金融投资协会调查的100名债券从业者中有54人预计加息，三季度GDP环比增长1.0%远超韩国银行0.3%的预测，消费者物价与核心物价均为2.8%。

8. 下一道关口
美国市场26日因感恩节休市，27日于东部时间13点提前收盘；韩国26日正常交易。12月8—9日FOMC、12月9日博通财报与12月17日美光财报将给出AI资本开支周期的答案。

一句话总结
这既不是上涨的一天，也不是崩塌的一天。道指丢掉1,104点后全部收回，纳指没能回来，标普500成分股有四分之三上涨。分水岭是AI硬件与其余部分。在PCE 3.8%和对14个经济体加征关税的新材料之下，市场会一直计算到12月9日FOMC与博通财报为止。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "postType": "report",
    "store": "K-Trend Market",
    "priceKrw": 0,
    "releaseDate": "2026-11-26",
    "rating": 5,
    "imageUrl": C,
    "images": [G1, G2, G3, G4, G5],
    "affiliateUrl": "https://stock.naver.com/",
    "affiliatePlatform": "Coupang",
    "i18n": {
        "ko": {
            "title": "1,100포인트 폭락을 되돌린 하루…다우 +0.33%, 나스닥은 왜 못 돌아왔나",
            "summary": "다우 50,182.95(+0.33%), S&P 500 7,182.78(−0.25%), 나스닥 23,585.80(−0.62%). 장중 1,104포인트 빠졌던 다우는 플러스로, 나스닥은 저점에서 950포인트를 되찾고도 마이너스. PCE 3.8%·관세 14개국·AI주 약세까지 숫자로 정리했습니다.",
            "description": KO_DESC,
            "tasteReview": [
                "다우 +0.33% vs 나스닥 −0.62% — 장중 다우 저점은 −1,104.96포인트(2.21%), S&P 500 저점은 −3.21%",
                "10월 PCE 3.8%(9월 3.7%), 근원 3.3% — 12월 FOMC 25bp 인상 100% 반영, 2027년 세 번째 인상 확률은 1/3로 하락",
                "엔비디아 149.30달러(−3.91%, 11월 −27%) S&P 글로벌 CreditWatch Negative / 마이크론 601.25달러(−4.57%, 10월 말 대비 −32%)",
                "코스피 4,697.51(−6.16%) 10개월여 만의 최저, 오늘 오전 10시 한국은행 금통위 — 3.25% 인상 우세",
            ],
            "tips": "본 글은 공개된 시세·보도·리포트를 정리한 정보 기록이며, 특정 종목의 매수·매도를 권유하지 않습니다. 가격은 2026년 11월 25일(미국) 정규장 종가와 11월 26일 08시 30분 KST 조회 기준입니다.",
        },
        "en": {
            "title": "The Dow Erased a 1,100-Point Plunge. The Nasdaq Couldn't — What Split Wednesday's Session",
            "summary": "Dow 50,182.95 (+0.33%), S&P 500 7,182.78 (−0.25%), Nasdaq 23,585.80 (−0.62%). The Dow fell 1,104 points intraday and finished green; the Nasdaq recovered 950 points and still closed lower. PCE at 3.8%, tariffs on 14 economies, and the AI names that keep falling, in numbers.",
            "description": EN_DESC,
            "tasteReview": [
                "Dow +0.33% vs Nasdaq −0.62%: the Dow's intraday low was −1,104.96 points (2.21%), the S&P 500's −3.21%",
                "October PCE 3.8% from 3.7%, core 3.3%: a 25bp December hike is fully priced, odds of a third 2027 hike down to one in three",
                "Nvidia $149.30 (−3.91%, −27% in November) on S&P Global's CreditWatch Negative; Micron $601.25 (−4.57%, −32% from late October)",
                "KOSPI 4,697.51 (−6.16%), lowest close in ten months; the Bank of Korea decides at 10:00 today with a hike to 3.25% expected",
            ],
            "tips": "This is a summary of public market data, reporting and broker research, not investment advice. Prices are U.S. regular-session closes on 25 November 2026, retrieved 26 November 2026 08:30 KST.",
        },
        "ja": {
            "title": "1,100ポイントの急落を戻した一日 — ダウ+0.33%、ナスダックが戻り切れなかった理由",
            "summary": "ダウ50,182.95（+0.33%）、S&P500 7,182.78（−0.25%）、ナスダック23,585.80（−0.62%）。場中に1,104ポイント下げたダウはプラスで終え、ナスダックは950ポイント戻してもマイナス。PCE 3.8%、14か国への関税、下げ続けるAI株を数字で整理しました。",
            "description": JA_DESC,
            "tasteReview": [
                "ダウ+0.33% vs ナスダック−0.62%：ダウの日中安値は−1,104.96ポイント（2.21%）、S&P500は−3.21%",
                "10月PCE 3.8%（9月3.7%）、コア3.3%：12月FOMCの25bp利上げは100%織り込み、2027年3回目の確率は3分の1に低下",
                "エヌビディア149.30ドル（−3.91%、11月−27%）がS&Pグローバルのクレジットウォッチ・ネガティブ、マイクロン601.25ドル（−4.57%、10月末比−32%）",
                "コスピ4,697.51（−6.16%）は約10か月ぶり安値、今日午前10時に韓国銀行の金融通貨委員会 — 3.25%への引き上げが有力",
            ],
            "tips": "本記事は公開された相場データ・報道・リポートを整理した情報記録であり、個別銘柄の売買を推奨するものではありません。価格は2026年11月25日（米国）通常取引の終値、11月26日08時30分KST時点の取得値です。",
        },
        "zh": {
            "title": "一天之内抹平1,100点暴跌：道指+0.33%，纳指为何没能回来",
            "summary": "道指50,182.95（+0.33%）、标普500 7,182.78（−0.25%）、纳指23,585.80（−0.62%）。道指盘中一度下跌1,104点后收涨，纳指回升950点仍收跌。10月PCE 3.8%、对14个经济体加征关税、持续下跌的AI股，全部用数字整理。",
            "description": ZH_DESC,
            "tasteReview": [
                "道指+0.33% vs 纳指−0.62%：道指盘中低点−1,104.96点（2.21%），标普500低点−3.21%",
                "10月PCE 3.8%（9月3.7%）、核心3.3%：12月FOMC加息25个基点已完全计入，2027年第三次加息概率降至三分之一",
                "英伟达149.30美元（−3.91%，11月−27%）被标普全球列入信用观察负面；美光601.25美元（−4.57%，较10月底−32%）",
                "KOSPI 4,697.51（−6.16%）为约十个月最低收盘，今日上午10点韩国银行金融货币委员会，加息至3.25%可能性较大",
            ],
            "tips": "本文整理公开行情、报道与研究资料，不构成任何个股买卖建议。价格为2026年11月25日（美国）常规交易时段收盘价，11月26日08时30分KST查询值。",
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
except Exception as e:  # noqa: BLE001
    print(f"[-] Revalidate error: {e}")
