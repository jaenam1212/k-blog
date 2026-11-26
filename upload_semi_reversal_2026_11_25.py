#!/usr/bin/env python3
"""2026-11-25(수) 아침 증시 리포트: 2026-11-24(화) 미국 정규장 마감 → Supabase posts(4개국어) + ISR revalidate.

모든 수치는 2026-11-25 08:20~08:35 KST 확인:
 - 야후 파이낸스 일별 종가·시세(quotes.json, quotes2.json), 야후 파이낸스 실화면 캡처
 - CNBC 라이브 블로그(11/24), 로이터 3건(마감·관세 조사·Trading Day), 연합뉴스(11/25 07:06), 인베스토피디아
 - IBD·글로벌이코노믹(미즈호·UBS·BNP 목표가), 아이뉴스24, 뉴데일리
 - 델 테크놀로지 IR 보도자료(11/24 16:05 ET)·CNBC·로이터, 인베스팅닷컴 어닝콜
 - CME FedWatch·asiatoday·investinglive PCE 프리뷰
 - 한국: 머니투데이·파이낸셜포스트·아주경제·서울경제 마감시황, 미래에셋 마켓클로징
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


def _require_env(name):
    """Environment variable (or .env.local) only: the repository holds no secrets."""
    value = os.environ.get(name) or _env_local(name)
    if not value:
        raise SystemExit(
            f"{name} is not set. Set it in the environment or in .env.local "
            f"(see .env.example). Secrets are never stored in the repository."
        )
    return value


SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or _env_local("SUPABASE_SERVICE_ROLE_KEY")
REVALIDATE_URL = ("https://www.k-trand.store/api/revalidate?secret="
                  + _require_env("REVALIDATE_SECRET"))
SLUG = "semi-reversal-dell-anthropic-2026-11-25"

C = "/images/products/market-semi-reversal-cover-2026-11-25.png"
G1 = "/images/products/market-semi-reversal-index-board-2026-11-25.png"
G2 = "/images/products/market-semi-reversal-movers-2026-11-25.png"
G3 = "/images/products/market-semi-reversal-chart-2026-11-25.png"
G4 = "/images/products/market-semi-reversal-drivers-2026-11-25.png"
G5 = "/images/products/market-semi-reversal-dell-calendar-2026-11-25.png"

KO_DESC = """11월 24일 화요일 뉴욕은 한 방향으로 움직이지 않았다. 다우존스는 423.39포인트(0.85%) 오른 50,018.70에 마감했고, 러셀2000도 0.57% 올랐다. 반대로 S&P 500은 36.08포인트(0.50%) 내린 7,201.09, 나스닥 종합은 356.02포인트(1.48%) 내린 23,733.54였다. 같은 날 필라델피아 반도체지수(SOX)는 7.88% 폭락해 8,832.50을 기록했다. 지수가 아니라 'AI 하드웨어'가 따로 무너진 하루였다.
전날 젠슨 황의 CEO 복귀로 나스닥이 6.51%, 필반이 14.03% 뛰었던 것을 생각하면 방향이 정확히 반대다. 시장은 이틀 동안 같은 뉴스를 두 번 다르게 읽었다.

1. 숫자 — 필반 −7.88%, 다우 +0.85%
S&P 500 정보기술 업종은 2.8% 내려 11개 업종 중 가장 나빴고, 헬스케어는 2.9% 올라 가장 좋았다. 업종 11개 중 8개가 하락했지만, 지수는 그 하락을 반도체 한 칸에 몰아넣는 모양새로 갈렸다.
반도체 안에서는 낙폭이 고르지 않았다. 엔비디아 −5.86%(155.38달러), 마이크론 −11.01%(629.79달러), AMD −8.86%(413.27달러), 마벨 −9.10%, ARM −8.55%, 인텔 −8.15%, SK하이닉스 ADR −9.90%, 브로드컴 −3.98%, TSMC ADR −3.96%. 반도체 ETF(SOXX)는 8.27%, 미국 상장 메모리 ETF(DRAM)는 9.22% 내렸다. 네오클라우드도 코어위브 −11.85%, 아이렌 −11.54%, 네비우스 −10.73%로 전날 상승분을 그대로 반납했다.
금리와 달러는 조용했다. 미 10년물 국채 금리는 4.904%로 전일(4.918%)보다 0.014%포인트 낮았고, 달러인덱스는 103.85로 0.45% 내렸다. 금 선물은 2.49% 내린 3,560.50달러, WTI는 1.78% 오른 81.60달러, 비트코인은 5만9,948달러로 2.06% 하락했다. VIX는 26.36으로 거의 제자리였다. 공포가 커진 게 아니라, 반도체 안에 몰려 있던 돈이 빠진 하루다.
오른 쪽은 소비재·유통·헬스케어였다. 앤프 +19.69%, 콜스 +19.48%, 딕스스포팅굿즈 +14.59%, 달러트리 +11.18%, 나이키 +5.89%, 암젠 +5.54%, 세일즈포스 +4.21%. 애플도 1.43% 올랐다. 같은 날 유통업체들이 실적을 내놓으면서 'AI가 아닌 쪽'으로 자금이 옮겨간 흔적이 숫자로 남았다.

2. 왜 반도체만 무너졌나 — 실적이 아니라 '전망'이 팔렸다
첫째, 설비투자 전망이 깎였다. 미즈호는 2027년 글로벌 AI 캐펙스 전망을 1조5,000억 달러에서 1조4,000억 달러로, 2028년을 2조 달러에서 1조8,000억 달러로 내렸다. 근거로 향후 2년간 5GW 규모 데이터센터가 지연되거나 취소될 수 있다는 시나리오를 들었다.
둘째, 목표가가 줄줄이 내려갔다. UBS는 "반도체 투자자들 사이에서 공급망 전체가 수요 대비 과잉 공급이라는 인식이 공유되고 있다"며 AMD·브로드컴·마벨 등 20개 종목의 목표주가를 한꺼번에 낮췄다. BNP파리바는 마이크론 투자의견을 '시장수익률 상회'에서 '중립'으로 내리고 목표가를 1,700달러에서 775달러로 반토막 냈다. 마이크론의 11% 급락은 이 리포트에 대한 반응이다.
셋째, 실적이 좋아도 팔렸다. 아날로그 디바이스(ADI)는 실적 발표 다음 날 17.37% 빠지며 S&P 500 하락률 1위였다. HPE는 시장 예상을 웃도는 실적과 상향 가이던스를 냈는데도 16.31% 급락했다. 앰바렐라는 19.96% 내렸다. 전날 델이 20% 오르며 기대를 미리 반영한 것과 같은 이유로, 이번엔 '다음 분기'가 문제가 됐다.
넷째, 추가 관세가 겹쳤다. 로이터에 따르면 미 무역대표부(USTR)는 한국·EU·일본·중국 등 16개 경제주체의 '과잉생산'에 대한 301조 조사 결과를 곧 발표하고, 기존 관세에 더해지는 새 관세를 제안할 예정이다. 전직 상무부 고위 관계자는 15~25%의 관세율과 단계적 인상 조항 가능성을 언급했다. EU·일본·한국은 15%, 중국은 20% 상한이 유지될 전망이지만, 관세가 인플레이션을 밀어 올리면 연준의 인상 기조가 길어진다는 우려가 붙는다.

3. 오늘의 화제 AI주 — 엔비디아·마이크론·델
엔비디아(NVDA) 155.38달러(−5.86%). 전날 31.48% 오른 것의 일부를 반납했다. 시가총액은 3조7,520억 달러로 4조 달러 아래로 내려왔고, 10월 6일 기록한 종가 고점보다 35% 낮다. 시간외에서는 153달러대로 더 밀렸다. 52주 최고 243.37달러, 애널리스트 평균 목표가 244.71달러와의 거리는 오히려 벌어졌다.
마이크론(MU) 629.79달러(−11.01%). 이틀 전 594.51달러에서 11/23 707.70달러까지 올랐던 종목이다. BNP파리바의 목표가 반토막이 결정적이었고, SK하이닉스 ADR(−9.90%)과 메모리 ETF(DRAM, −9.22%)가 함께 밀렸다. 메모리는 이번 조정에서 가장 먼저, 가장 크게 빠지는 자리다.
델(DELL) 295.28달러(−11.83%). 그런데 장 마감 뒤 실적이 나오자 시간외에서 4.8%대(309달러)로 돌아섰다. 3분기(10/30 마감) 매출은 549.4억 달러로 1년 전보다 103% 늘었고, 조정 EPS는 9.45달러로 컨센서스 6.59달러를 크게 넘었다. AI 서버 매출은 220억 달러(+291%), AI 서버 수주잔고는 1,323억 달러, 분기 신규 수주는 602억 달러다. 회사는 2027회계연도 매출 가이던스를 1,920억 달러에서 2,020억 달러로 올렸고, AI 서버 매출 전망도 780억 달러로 높였다. 자사주 매입 한도는 250억 달러 추가됐다. 좋은 실적이 'AI 하드웨어 조정'을 이기지 못한 정규장과, 실적이 그 조정을 되돌린 몇 시간이 같은 날 겹쳤다.
앤트로픽(ANT)은 81.91달러(−6.54%)로 상장 4거래일 만에 공모가 83달러를 밑돌았다. 첫날 111달러에 열었고 장중 115.10달러까지 갔던 종목이다. 같은 날 오펜하이머는 '아웃퍼폼·목표가 150달러'로 커버리지를 시작했다. 내년으로 예정된 오픈AI 상장을 가늠할 첫 번째 지표가 이 주가라는 점에서, 83달러선은 당분간 시장의 기준선이 될 전망이다.

4. 월가와 국내 증권가의 시각
세테라 파이낸셜의 진 골드먼 CIO는 "수개월 만에 가장 큰 랠리가 끝난 뒤에는 어느 정도 차익실현을 예상할 수 있다. 결국 하나의 뉴스가 AI 투자에 관한 투자자들의 의문을 해소해주지는 않는다"고 말했다. 지난주 조정은 장기 투자자에게 매수 기회였을 수 있지만 "당분간은 매우 울퉁불퉁한 길"이라고 덧붙였다.
UBS 글로벌자산운용의 마크 헤펠레는 기술주 변동성이 "구조적 AI 투자 스토리가 깨졌다는 신호"라고 보지 않는다면서도, "수익화가 보이는 플랫폼과 부채·희소 용량·투기적 성장에 의존하는 기업 사이의 차별화는 커질 것"이라고 썼다. 골드만삭스 유럽 주식 수석 전략가 샤론 벨은 "AI 관련주 향방은 기업들이 설비 투자에 상응하는 수익을 거둘 수 있느냐에 달려 있다"고 짚었다.
한국 증권가는 반등의 성격을 '기술적 반등'으로 규정하면서도 확인할 조건을 길게 남겼다. 키움증권 한지영 연구원은 황 CEO 복귀로 AI 투자 지속성 불안이 완화됐다면서도 "증시 불안이 온전히 소멸되지 못한 만큼 변동성 확대에 대비해야 하고, 주중 증안펀드의 실제 가동을 위한 구체적 조치가 나오는지가 관건"이라고 말했다. 신한투자증권 김성환 연구원은 "기술적·가격적 매력 이상의 강세 근거가 아직 쌓이지 않았다"고 했고, iM증권 고의영 연구원은 "GPU 우회 수출 규제와 데이터센터 지연 같은 정책 불확실성이 풀려야 주가가 회복된다"고 봤다. 대신증권 이경민 연구원은 엔비디아 중심의 순환금융 구조(엔비디아가 고객에 투자→고객이 GPU 구매→엔비디아가 메모리 장기 계약)를 짚으며 "실적 훼손 없이도 리더십 공백만으로 주가가 무너진 이유"라고 설명했다.

5. 오늘 아침 — 한국 시장과 남은 관문
한국은 전날(11/24) 뉴욕의 반등을 하루 늦게, 크게 받았다. 코스피는 297.49포인트(6.32%) 오른 5,006.03, 코스닥은 30.43포인트(4.79%) 오른 665.88에 마감했다. 3거래일 만에 5,000선을 되찾았고, 장중 5,065.74까지 올랐다. 외국인은 8거래일 만에 순매수(7,391억원)로 돌아섰고 기관은 8,692억원을 샀다. 개인은 2조430억원을 순매도했고, 양대 시장에 매수 사이드카가 발동됐다. 삼성전자는 6.70% 오른 18만9,400원, SK하이닉스는 6.73% 오른 115만8,000원. 삼성SDI +13.64%, 현대차 +11.11%, 기아 +10.65%, LG에너지솔루션 +7.89%, 삼성전기 +10.28%가 함께 올랐다. 원·달러는 1,342.4원으로 3.5원 내렸다.
문제는 그다음 밤이다. 오늘 오전 9시 개장을 앞두고 반도체에는 갭하락 압력이 걸린다. SK하이닉스 ADR −9.90%, 마이크론 −11.01%, 필반 −7.88%가 그대로 넘어오는 자리다. 반면 다우 +0.85%, 러셀2000 +0.57%, 헬스케어 +2.9%는 'AI가 아닌 쪽'이 버틴 하루였다는 신호로, 어제 외국인 순매수가 오늘도 이어지는지가 첫 관문이 된다.
오늘 밤 22시 30분(한국시간)에는 미국 10월 PCE 물가지수와 3분기 GDP 잠정치, 실업수당 청구건수가 한꺼번에 나온다. 헤드라인 PCE는 3.8%, 근원은 3.2% 상승이 예상된다. 12월 9일 연방공개시장위원회(FOMC)를 앞두고 연준이 마지막으로 보는 물가 지표이고, 금리선물 시장은 25bp 인상 확률을 90~97%로 반영하고 있다. 현재 기준금리는 3.75~4.00%로, 9월에 인상했고 10월 회의는 10대 2로 동결했다(두 명은 인상 선호). 골드만삭스는 12월·3월 두 차례, 뱅크오브아메리카는 12월·1월·3월 세 차례 인상을 전망한다. 근원 PCE가 전월 대비 0.4% 이상으로 나오면 2027년 초 인상 기대가 더 붙는다. 11월 26일은 추수감사절 휴장, 11월 27일은 블랙프라이데이 반일장(13시 ET 마감)이다. 12월 9일 브로드컴, 12월 17일 마이크론 실적이 AI 설비투자 논쟁의 다음 답이 된다.

한 줄 정리
이틀 동안 시장이 한 것은 'AI 투자에 대한 의심'을 사고파는 일이었다. 월요일에는 CEO 한 명의 복귀가 그 의심을 6.5%만큼 지웠고, 화요일에는 애널리스트 세 명의 전망 하향이 그만큼 되살렸다. 지수가 사상 최고에서 8% 남짓 떨어진 자리에 있지만, 반도체 실적과 설비투자 사이의 간격은 여전히 숫자로 확인되지 않았다. 오늘 밤 PCE와 12월 하이퍼스케일러들의 설비투자 가이던스가 그 간격을 재는 자가 될 것이다."""

EN_DESC = """Tuesday, November 24 was not a one-way day in New York. The Dow rose 423.39 points (0.85%) to 50,018.70 and the Russell 2000 added 0.57%. The S&P 500 fell 36.08 points (0.50%) to 7,201.09 and the Nasdaq Composite lost 356.02 points (1.48%) to 23,733.54. On the same session the Philadelphia Semiconductor Index dropped 7.88% to 8,832.50. What broke was not the market but AI hardware.

A day earlier, Jensen Huang's reinstatement as Nvidia CEO had lifted the Nasdaq 6.51% and the SOX 14.03%. The market read the same news two different ways in two sessions.

1. The numbers: chips -7.88%, the Dow +0.85%
S&P 500 information technology fell 2.8%, the worst of 11 sectors, while healthcare rose 2.9%, the best. Eight sectors declined, but the damage to the index was concentrated in one place.
Inside semiconductors the losses were uneven. Nvidia -5.86% to $155.38, Micron -11.01% to $629.79, AMD -8.86% to $413.27, Marvell -9.10%, Arm -8.55%, Intel -8.15%, SK hynix's ADR -9.90%, Broadcom -3.98% and TSMC's ADR -3.96%. The iShares Semiconductor ETF (SOXX) fell 8.27% and the Roundhill Memory ETF (DRAM) 9.22%. Neoclouds gave back Monday entirely: CoreWeave -11.85%, Iren -11.54%, Nebius -10.73%.
Rates and the dollar were quiet. The 10-year Treasury yield closed at 4.904%, a hair below Monday's 4.918%, and the dollar index eased 0.45% to 103.85. Gold futures fell 2.49% to $3,560.50, WTI rose 1.78% to $81.60 and bitcoin slipped 2.06% to $59,948. The VIX ended at 26.36, essentially unchanged: this was not a market-wide scare but money leaving one crowded trade.
The gainers were retail, consumer and healthcare names: Abercrombie & Fitch +19.69%, Kohl's +19.48%, Dick's Sporting Goods +14.59%, Dollar Tree +11.18%, Nike +5.89%, Amgen +5.54% and Salesforce +4.21%. Apple added 1.43%. Retail earnings the same morning gave the rotation somewhere to go.

2. Why chips alone: forecasts were sold, not results
First, capex forecasts were cut. Mizuho lowered its 2027 global AI capex estimate to $1.4 trillion from $1.5 trillion and 2028 to $1.8 trillion from $2.0 trillion, citing a scenario in which 5 gigawatts of data centre projects are delayed or cancelled over the next two years.
Second, targets fell in a row. UBS, saying investors widely see the supply chain as oversupplied relative to demand, cut price targets on about 20 semiconductor names including AMD, Broadcom and Marvell. BNP Paribas downgraded Micron to neutral from outperform and halved its target to $775 from $1,700 — the direct trigger for Micron's 11% slide.
Third, good results were sold too. Analog Devices fell 17.37% the day after reporting, the worst in the S&P 500; HPE dropped 16.31% even after beating estimates and raising guidance; Ambarella lost 19.96%. Dell had risen 20% the day before on expectations, and this time the next quarter was the problem.
Fourth, tariffs added to it. Reuters reported that the U.S. Trade Representative is poised to release the findings of a Section 301 probe into excess industrial capacity in 16 partners including Korea, the EU, Japan and China, and to propose duties stacked on existing tariffs. A former senior Commerce official floated rates of 15-25% with escalation clauses. Caps of 15% for the EU, Japan and Korea and 20% for China are expected to hold, but tariffs feed inflation, and inflation keeps the Fed hiking.

3. The AI names that mattered: Nvidia, Micron, Dell
Nvidia (NVDA) $155.38, -5.86%, giving back part of Monday's 31.48% surge. Its market value slipped back below $4 trillion to $3.752 trillion and sits 35% under its October 6 record close. It traded near $153 after hours. The gap to its 52-week high of $243.37 and to the $244.71 average analyst target widened rather than closed.
Micron (MU) $629.79, -11.01%, after running from $594.51 on November 20 to $707.70 on Monday. BNP's halved target did the damage, and SK hynix's ADR (-9.90%) and the memory ETF (-9.22%) fell with it. Memory is the first and furthest thing to fall in this correction.
Dell (DELL) $295.28, -11.83% in the regular session — then up about 4.8% to $309 after the close when the numbers landed. Fiscal third-quarter revenue was $54.94 billion, up 103% year on year, and adjusted EPS $9.45 against a $6.59 consensus. AI-optimised server revenue was $22.0 billion (+291%), AI backlog a record $132.3 billion after $60.2 billion of orders in the quarter. Dell raised full-year revenue guidance to $202 billion from $192 billion, lifted its AI server forecast to $78 billion and added $25 billion to its buyback authorisation.
Anthropic (ANT) closed at $81.91, down 6.54%, breaking below its $83 IPO price on its fourth trading day. It opened at $111, peaked at $115.10, and Oppenheimer started coverage the same day at outperform with a $150 target. With an OpenAI listing expected next year, this price is the first read on how public markets will treat frontier AI, and $83 is the line to watch.

4. What Wall Street and Korean brokers said
Cetera Financial's Gene Goldman: "After the biggest rally in months, you would expect some profit-taking. At the end of the day, one headline doesn't really resolve investor questions about the AI trade." Last week's correction may be a buying opportunity for long-term investors, he added, but the path "can be a very bumpy" one for some time.
UBS Global Wealth Management's Mark Haefele wrote that the volatility is not "a signal that the structural AI investment story has broken," while expecting "greater differentiation between established platforms with visible monetization and strong balance sheets, and companies dependent on debt, scarce capacity, or continued speculative growth." Goldman Sachs' European equity strategist Sharon Bell put it simply: the direction of AI stocks depends on whether companies can earn returns that match their capex.
Korean brokers called the rebound technical and listed what still needs confirming. Kiwoom's Han Ji-young said Huang's return eased doubts about AI spending but that volatility could widen and that concrete steps toward actually deploying the market stabilisation fund would be the key. Shinhan's Kim Seong-hwan said the case for a trend reversal beyond technical and price appeal has not been built. iM's Ko Ui-young said stocks recover only when policy uncertainty — GPU export rules and data centre delays — clears. Daishin's Lee Kyung-min described Nvidia's circular financing, where Nvidia invests in customers who buy its GPUs and sign long-term memory contracts, as the reason the stock collapsed on a leadership vacuum without any damage to earnings.

5. This morning: Seoul and the next gates
Korea took Monday's U.S. rebound a day late and took it hard. The KOSPI closed at 5,006.03, up 297.49 points (6.32%), and the KOSDAQ at 665.88, up 30.43 points (4.79%), reclaiming 5,000 for the first time in three sessions after touching 5,065.74 intraday. Foreigners turned net buyers for the first time in eight sessions (+739.1 billion won) and institutions bought 869.2 billion won, while individuals sold 2.04 trillion won. Buy-side sidecars triggered in both markets. Samsung Electronics rose 6.70% to 189,400 won and SK hynix 6.73% to 1,158,000 won, with Samsung SDI +13.64%, Hyundai +11.11%, Kia +10.65%, LG Energy Solution +7.89% and Samsung Electro-Mechanics +10.28%. The won closed at 1,342.4 per dollar, down 3.5.
Now the other side. Ahead of today's 9 a.m. open, chips face a gap down: SK hynix's ADR -9.90%, Micron -11.01% and the SOX -7.88% all arrive at once. The Dow +0.85%, Russell 2000 +0.57% and healthcare +2.9% show the non-AI side held, so whether yesterday's foreign buying continues is the first test.
At 22:30 KST tonight the U.S. releases October PCE, the second estimate of third-quarter GDP and jobless claims together. Headline PCE is expected at 3.8% year on year and core at 3.2%. It is the last inflation reading before the December 9 FOMC, with futures pricing a 25bp hike at 90-97%. The fed funds rate is 3.75-4.00% after a September hike and a 10-2 hold in October, with two dissenters preferring an increase. Goldman Sachs expects hikes in December and March; Bank of America sees December, January and March. A core reading of 0.4% or more would feed expectations for early 2027. U.S. markets close for Thanksgiving on November 26 and trade a half session on Black Friday, November 27, until 1 p.m. ET. Broadcom on December 9 and Micron on December 17 are the next answers on AI capex.

Bottom line
For two sessions the market did one thing: trade its doubts about AI spending. On Monday a CEO's return removed 6.5% of that doubt; on Tuesday three analysts' downgrades put it back. The index sits about 8% below its record, while the distance between semiconductor earnings and capital spending is still not settled by numbers. Tonight's PCE and December's hyperscaler capex guidance are the rulers."""

JA_DESC = """11月24日火曜日のニューヨークは一方向には動かなかった。ダウは423.39ポイント（0.85％）高の50,018.70、ラッセル2000も0.57％上昇。一方でS&P500は36.08ポイント（0.50％）安の7,201.09、ナスダック総合は356.02ポイント（1.48％）安の23,733.54で引けた。同じ日にフィラデルフィア半導体指数（SOX）は7.88％急落して8,832.50。壊れたのは市場全体ではなく「AIハードウェア」だった。

前日、ジェンセン・フアンのCEO復帰でナスダックが6.51％、SOXが14.03％上昇したことを思えば、方向は正反対である。市場は同じニュースを二日間で二度、違う読み方をした。

1. 数字 — SOX −7.88％、ダウ ＋0.85％
S&P500の情報技術セクターは2.8％安で11業種中最悪、ヘルスケアは2.9％高で最高だった。11業種中8業種が下落したが、指数への打撃は一箇所に集中した。
半導体の中でも落差は大きい。エヌビディア −5.86％（155.38ドル）、マイクロン −11.01％（629.79ドル）、AMD −8.86％（413.27ドル）、マーベル −9.10％、アーム −8.55％、インテル −8.15％、SKハイニックスADR −9.90％、ブロードコム −3.98％、TSMC ADR −3.96％。半導体ETF（SOXX）は8.27％、米上場のメモリーETF（DRAM）は9.22％下落した。ネオクラウドもコアウィーブ −11.85％、アイレン −11.54％、ネビウス −10.73％と前日の上昇分をそのまま返した。
金利とドルは静かだった。米10年債利回りは4.904％で前日（4.918％）をわずかに下回り、ドル指数は0.45％安の103.85。金先物は2.49％安の3,560.50ドル、WTIは1.78％高の81.60ドル、ビットコインは2.06％安の59,948ドル。VIXは26.36でほぼ横ばいだった。恐怖が広がったのではなく、半導体に偏っていた資金が抜けた一日である。
上昇したのは小売・消費・ヘルスケアだった。アバクロンビー＆フィッチ ＋19.69％、コールズ ＋19.48％、ディックス ＋14.59％、ダラーツリー ＋11.18％、ナイキ ＋5.89％、アムジェン ＋5.54％、セールスフォース ＋4.21％。アップルも1.43％高。同日の小売決算が、資金の移動先を用意した。

2. なぜ半導体だけが崩れたのか — 売られたのは業績ではなく「見通し」
第一に、設備投資の見通しが引き下げられた。みずほは2027年の世界AI設備投資を1兆5,000億ドルから1兆4,000億ドルへ、2028年を2兆ドルから1兆8,000億ドルへ下方修正した。根拠は、今後2年間に5GW規模のデータセンターが延期・中止される可能性というシナリオだ。
第二に、目標株価が相次いで下がった。UBSは「サプライチェーン全体が需要に対して供給過剰だという認識が投資家に広がっている」として、AMD・ブロードコム・マーベルなど約20銘柄の目標株価を一斉に引き下げた。BNPパリバはマイクロンの投資判断を「アウトパフォーム」から「中立」へ下げ、目標株価を1,700ドルから775ドルへ半減。マイクロンの11％安はこれへの反応である。
第三に、好決算でも売られた。アナログ・デバイセズは決算発表の翌日に17.37％下落してS&P500の下落率首位、HPEは市場予想を上回りガイダンスも引き上げたのに16.31％安、アンバレラは19.96％安だった。前日にデルが20％上げて期待を先取りしたのと同じ理由で、今回は「次の四半期」が問題になった。
第四に、追加関税が重なった。ロイターによれば、米通商代表部（USTR）は韓国・EU・日本・中国など16の経済主体の「過剰生産能力」に関する通商法301条調査の結果を近く公表し、既存関税に上乗せする新たな関税を提案する見通しだ。元商務省高官は15〜25％の税率と段階的引き上げ条項の可能性に言及した。EU・日本・韓国は15％、中国は20％の上限が維持される見込みだが、関税はインフレを押し上げ、FRBの利上げ基調を長引かせる。

3. 話題のAI銘柄 — エヌビディア、マイクロン、デル
エヌビディア（NVDA）155.38ドル（−5.86％）。前日の31.48％高の一部を返上した。時価総額は3兆7,520億ドルへ下がり4兆ドルを割り込み、10月6日の終値高値から35％低い。時間外では153ドル台へ一段下げた。52週高値243.37ドル、アナリスト平均目標株価244.71ドルとの距離はむしろ広がった。
マイクロン（MU）629.79ドル（−11.01％）。11月20日の594.51ドルから23日には707.70ドルまで上げた銘柄だ。BNPの目標株価半減が決定的で、SKハイニックスADR（−9.90％）とメモリーETF（−9.22％）も共に下げた。メモリーは今回の調整で最初に、最も大きく落ちる場所である。
デル（DELL）295.28ドル（−11.83％）。ところが引け後に決算が発表されると、時間外で4.8％高の309ドル台へ戻した。第3四半期（10月30日締め）売上高は549.4億ドルで前年比103％増、調整後EPSは9.45ドルで市場予想6.59ドルを大きく上回った。AIサーバー売上高は220億ドル（＋291％）、AIサーバー受注残は1,323億ドル、四半期の新規受注は602億ドル。通期売上高ガイダンスを1,920億ドルから2,020億ドルへ引き上げ、AIサーバー見通しも780億ドルへ。自社株買い枠は250億ドル追加された。
アントロピック（ANT）は81.91ドル（−6.54％）で、上場4日目にして公開価格83ドルを割り込んだ。初日は111ドルで寄り付き、取引中に115.10ドルまで上げた銘柄だ。同日オッペンハイマーは「アウトパフォーム・目標株価150ドル」でカバレッジを開始した。来年予定されるOpenAI上場を占う最初の指標として、83ドルは当面の基準線になる。

4. ウォール街と韓国証券会社の見方
セテラ・フィナンシャルのジーン・ゴールドマンCIOは「数カ月ぶりの大きなラリーの後には利益確定があって当然だ。結局、一つの見出しがAI投資への疑問を解消するわけではない」と述べ、先週の調整は長期投資家には買い場かもしれないが「当面はかなり凸凹した道」になり得ると付け加えた。
UBSグローバル・ウェルス・マネジメントのマーク・ヘフェレは、この変動性は「構造的なAI投資ストーリーが壊れた兆し」ではないとしつつ、「収益化が見えるプラットフォームと、負債・希少な容量・投機的成長に依存する企業との差別化は進む」と書いた。ゴールドマン・サックスの欧州株ストラテジスト、シャロン・ベルは「AI関連株の行方は、企業が設備投資に見合う利益を上げられるかにかかっている」と指摘した。
韓国証券会社は反発を「テクニカル」と規定し、確認すべき条件を並べた。キウム証券のハン・ジヨン研究員はフアン氏復帰でAI投資継続への不安は和らいだものの、変動性拡大に備える必要があり、市場安定化ファンドの実際の稼働に向けた具体的措置がカギだと述べた。新韓投資証券のキム・ソンファン研究員は「テクニカル・価格面の魅力以上の強気根拠はまだ積み上がっていない」、iM証券のコ・ウィヨン研究員は「GPU迂回輸出規制やデータセンター遅延といった政策不確実性が解消してこそ株価は回復する」と見た。大信証券のイ・ギョンミン研究員は、エヌビディアが顧客に投資し顧客がGPUを買いメモリーの長期契約を結ぶ循環金融構造を挙げ、「業績悪化なしにリーダーシップの空白だけで株価が崩れた理由」と説明した。

5. 今朝 — 韓国市場と残された関門
韓国は前日（11月24日）のニューヨークの反発を一日遅れで大きく受け取った。コスピは297.49ポイント（6.32％）高の5,006.03、コスダックは30.43ポイント（4.79％）高の665.88で引け、3営業日ぶりに5,000台を回復した（取引中は5,065.74まで上昇）。外国人は8営業日ぶりに買い越し（7,391億ウォン）、機関は8,692億ウォンを買い越し、個人は2兆430億ウォンを売り越した。両市場で買いサイドカーが発動。サムスン電子は6.70％高の18万9,400ウォン、SKハイニックスは6.73％高の115万8,000ウォン、サムスンSDI ＋13.64％、現代自動車 ＋11.11％、起亜 ＋10.65％、LGエナジーソリューション ＋7.89％。ウォンは1,342.4ウォンで3.5ウォン高かった。
問題はその次の夜だ。今日午前9時の寄り付きを前に、半導体にはギャップダウン圧力がかかる。SKハイニックスADR −9.90％、マイクロン −11.01％、SOX −7.88％がそのまま越えてくる。一方でダウ ＋0.85％、ラッセル2000 ＋0.57％、ヘルスケア ＋2.9％は「AI以外」が持ちこたえた一日だったというシグナルで、昨日の外国人の買い越しが今日も続くかが最初の関門になる。
今夜22時30分（韓国時間）には米10月PCE物価指数、第3四半期GDP改定値、新規失業保険申請件数が同時に発表される。PCEは前年比3.8％、コア3.2％の上昇が見込まれる。12月9日のFOMCを前にFRBが見る最後の物価指標で、金利先物は25bp利上げを90〜97％織り込む。政策金利は3.75〜4.00％、9月に利上げし、10月会合は10対2で据え置き（2人は利上げを支持）。ゴールドマン・サックスは12月と3月、バンク・オブ・アメリカは12月・1月・3月の利上げを予想する。コアPCEが前月比0.4％以上なら2027年初の利上げ観測が強まる。11月26日は感謝祭で米国休場、27日はブラックフライデーの半日取引（東部時間13時終了）。12月9日のブロードコム、12月17日のマイクロンの決算がAI設備投資論争の次の答えになる。

まとめ
二日間、市場がやっていたのは「AI投資への疑い」を売買することだった。月曜にはCEO一人の復帰が疑いを6.5％分消し、火曜にはアナリスト三人の見通し引き下げがそれを戻した。指数は最高値から8％ほど下の水準にあるが、半導体の業績と設備投資の間の距離はまだ数字で確認されていない。今夜のPCEと12月のハイパースケーラーの設備投資ガイダンスが、その距離を測る物差しになる。"""

ZH_DESC = """11月24日周二，纽约并未走出单一方向。道指上涨423.39点（0.85%）至50,018.70，罗素2000上涨0.57%；标普500下跌36.08点（0.50%）至7,201.09，纳斯达克综合指数下跌356.02点（1.48%）至23,733.54。同一天费城半导体指数（SOX）暴跌7.88%至8,832.50。崩掉的不是整个市场，而是"AI硬件"。

前一天，黄仁勋回归CEO曾让纳斯达克上涨6.51%、SOX上涨14.03%。方向完全相反——市场在两个交易日里对同一条新闻给出了两种解读。

1. 数字：SOX −7.88%，道指 +0.85%
标普500信息技术板块下跌2.8%，在11个板块中最差；医疗保健上涨2.9%，表现最好。11个板块中有8个下跌，但指数的失分集中在一个位置。
半导体内部跌幅并不均匀：英伟达−5.86%（155.38美元）、美光−11.01%（629.79美元）、AMD −8.86%（413.27美元）、迈威尔−9.10%、Arm −8.55%、英特尔−8.15%、SK海力士ADR −9.90%、博通−3.98%、台积电ADR −3.96%。半导体ETF（SOXX）下跌8.27%，美国上市的内存ETF（DRAM）下跌9.22%。neocloud同样回吐：CoreWeave −11.85%、Iren −11.54%、Nebius −10.73%。
利率与美元则很安静。美国10年期国债收益率收于4.904%，较前一日（4.918%）低0.014个百分点；美元指数下跌0.45%至103.85。黄金期货跌2.49%至3,560.50美元，WTI涨1.78%至81.60美元，比特币跌2.06%至59,948美元。VIX收于26.36，几乎持平——这不是全面恐慌，而是拥挤在半导体里的资金撤出。
上涨的是零售、消费与医疗：Abercrombie & Fitch +19.69%、Kohl's +19.48%、Dick's +14.59%、Dollar Tree +11.18%、耐克+5.89%、安进+5.54%、Salesforce +4.21%，苹果也涨1.43%。当天早晨的零售财报给资金提供了去处。

2. 为什么只有半导体崩：卖的是"预期"而非业绩
第一，资本开支预期被下调。瑞穗将2027年全球AI资本开支预测从1.5万亿美元下调至1.4万亿美元，2028年从2万亿下调至1.8万亿美元，理由是未来两年可能有5GW规模的数据中心延期或取消。
第二，目标价接连下调。UBS称"投资者普遍认为整条供应链相对需求供过于求"，一次性下调AMD、博通、迈威尔等约20只半导体股的目标价。BNP巴黎银行将美光评级从"跑赢大盘"下调至"中性"，目标价从1,700美元腰斩至775美元——这是美光暴跌11%的直接触发因素。
第三，业绩好也照卖。亚德诺（ADI）在发布财报次日下跌17.37%，为标普500跌幅第一；HPE业绩超预期并上调指引仍跌16.31%；安霸跌19.96%。戴尔前一天因预期上涨20%，而这次"下一季度"成了问题。
第四，新增关税叠加。据路透社，美国贸易代表办公室（USTR）即将公布针对韩国、欧盟、日本、中国等16个经济体"产能过剩"的301条款调查结果，并拟提出在现有关税之上叠加的新关税。一位前商务部高级官员提到15%~25%的税率及逐步上调条款。欧盟、日本、韩国预计维持15%上限，中国维持20%，但关税会推高通胀，从而延长美联储的加息周期。

3. 焦点AI个股：英伟达、美光、戴尔
英伟达（NVDA）155.38美元（−5.86%），回吐了前一日31.48%涨幅的一部分。市值回落至3.752万亿美元、跌回4万亿下方，比10月6日的收盘纪录低35%。盘后再跌至153美元附近。与52周高点243.37美元、分析师平均目标价244.71美元的距离反而拉大。
美光（MU）629.79美元（−11.01%），11月20日还在594.51美元，23日冲到707.70美元。BNP腰斩目标价是关键，SK海力士ADR（−9.90%）与内存ETF（−9.22%）同步下挫。内存是这轮调整中跌得最早、最深的板块。
戴尔（DELL）295.28美元（−11.83%），但收盘后财报公布，盘后回升约4.8%至309美元。第三财季（截至10月30日）营收549.4亿美元，同比增长103%；调整后EPS 9.45美元，远超市场预期的6.59美元。AI服务器营收220亿美元（+291%），AI服务器在手订单达1,323亿美元，单季新订单602亿美元。公司将2027财年营收指引从1,920亿美元上调至2,020亿美元，AI服务器收入指引上调至780亿美元，并追加250亿美元回购授权。
Anthropic（ANT）收于81.91美元（−6.54%），上市第四个交易日即跌破83美元发行价。首日开盘111美元，盘中最高115.10美元。同日奥本海默以"跑赢大盘、目标价150美元"启动覆盖。鉴于OpenAI预计明年上市，这一价格是公开市场如何对待前沿AI的第一个读数，83美元将成为一段时间的基准线。

4. 华尔街与韩国券商的看法
Cetera Financial首席投资官吉恩·戈德曼表示："在数月来最大的一轮反弹之后，出现获利了结是意料之中。归根结底，一条新闻并不能真正解答投资者对AI交易的疑问。"他补充说，上周的调整对长期投资者或许是买点，但"未来一段时间仍可能非常颠簸"。
UBS全球财富管理的马克·海费勒认为这轮波动并非"结构性AI投资逻辑破裂的信号"，但预期"可见变现的平台与依赖债务、稀缺产能和投机性增长的公司之间的分化会加大"。高盛欧洲股票策略师莎伦·贝尔指出："AI相关股票的走向，取决于企业能否获得与资本开支相匹配的回报。"
韩国券商将反弹定性为"技术性反弹"，并列出了待确认的条件。Kiwoom的韩志英表示，黄仁勋回归缓解了AI投资持续性的疑虑，但仍需防范波动扩大，市场稳定基金是否实际启动的具体措施是关键。新韩投资的金石焕认为"超出技术面与估值吸引力的看涨依据尚未积累"，iM证券的高义英认为"只有GPU绕道出口管制、数据中心延期等政策不确定性解除，股价才会恢复"。大信证券的李京民指出英伟达主导的循环金融结构（英伟达投资客户、客户购买GPU、再签内存长约），"这正是业绩未受损、仅因领导层空缺就令股价崩塌的原因"。

5. 今晨：首尔市场与剩余的关口
韩国在11月24日迟一天、且以更大力度承接了纽约的反弹。KOSPI收于5,006.03，上涨297.49点（6.32%）；科斯达克收于665.88，上涨30.43点（4.79%），三个交易日后重回5,000点（盘中最高5,065.74）。外国投资者在连续8个交易日后转为净买入（7,391亿韩元），机构净买入8,692亿韩元，个人净卖出2兆430亿韩元，两大市场均触发买入熔断。三星电子涨6.70%至189,400韩元，SK海力士涨6.73%至1,158,000韩元；三星SDI +13.64%、现代汽车+11.11%、起亚+10.65%、LG新能源+7.89%。韩元收于1,342.4，升值3.5。
关键在接下来的这个夜晚。今天上午9时开盘前，半导体面临跳空低开压力：SK海力士ADR −9.90%、美光−11.01%、SOX −7.88%会原样传导。相反，道指+0.85%、罗素2000 +0.57%、医疗保健+2.9%说明"非AI"一侧撑住了，昨天外国资金的净买入今天是否延续是第一个关口。
今晚22时30分（韩国时间），美国10月PCE物价指数、三季度GDP修正值与初请失业金人数将同时公布。PCE同比预计3.8%、核心3.2%。这是12月9日FOMC前美联储看到的最后一份通胀数据，利率期货已计入90%~97%的25个基点加息概率。当前政策利率为3.75%~4.00%，9月已加息一次，10月会议以10比2维持（两位委员倾向加息）。高盛预计12月与3月各加一次，美国银行预计12月、1月、3月三次。若核心PCE环比达到0.4%或以上，2027年初的加息预期会进一步增强。11月26日美国因感恩节休市，27日黑色星期五为半日交易（美东13时收盘）。12月9日博通、12月17日美光的财报将成为AI资本开支争论的下一个答案。

一句话总结
两个交易日里，市场只做了一件事：交易对AI投资的怀疑。周一，一位CEO的回归抹去了其中6.5%；周二，三位分析师的 downgrade 又把它加了回来。指数仍在历史高点下方约8%处，而半导体业绩与资本开支之间的差距还没有被数字确认。今晚的PCE与12月超大规模云厂商的资本开支指引，将是衡量这一差距的尺子。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "postType": "report",
    "store": "K-Trend Market",
    "priceKrw": 0,
    "releaseDate": "2026-11-25",
    "rating": 5,
    "imageUrl": C,
    "images": [G1, G2, G3, G4, G5],
    "affiliateUrl": "https://stock.naver.com/",
    "affiliatePlatform": "Coupang",
    "i18n": {
        "ko": {
            "title": "젠슨 황 랠리 하루 만에 반납…반도체 −7.88% vs 다우 +0.85%, 같은 날 두 시장이 갈린 이유",
            "summary": "S&P 500 7,201.09(−0.50%), 나스닥 23,733.54(−1.48%), 다우 50,018.70(+0.85%). 필라델피아 반도체는 −7.88%였습니다. 미즈호의 AI 설비투자 하향과 UBS·BNP의 목표가 줄하향, 추가 관세가 겹친 하루. 델 실적과 앤트로픽 공모가 이탈, 오늘 밤 PCE까지 숫자로 정리했습니다.",
            "description": KO_DESC,
            "tasteReview": [
                "필라델피아 반도체 −7.88%(8,832.50) vs 다우 +0.85%(50,018.70) — 같은 날 반대 방향",
                "엔비디아 155.38달러(−5.86%), 마이크론 629.79달러(−11.01%), 앤트로픽 81.91달러로 공모가 83달러 이탈",
                "델 3분기 매출 549.4억 달러(+103%)·AI 서버 220억 달러(+291%)·수주잔고 1,323억 달러, 정규장 −11.83% → 시간외 +4.8%",
                "전날 코스피 +6.32%(5,006.03)로 하루 늦게 반영, 오늘 밤 22:30 KST 미국 10월 PCE가 다음 관문",
            ],
            "tips": "본 글은 공개된 시세·보도·리포트를 정리한 정보 기록이며, 특정 종목의 매수·매도를 권유하지 않습니다.",
        },
        "en": {
            "title": "Nvidia's Relief Rally Lasted One Day: Chips −7.88%, the Dow +0.85%",
            "summary": "S&P 500 7,201.09 (−0.50%), Nasdaq 23,733.54 (−1.48%), Dow 50,018.70 (+0.85%) and the Philadelphia Semiconductor Index −7.88%. Mizuho's capex cut, UBS and BNP target cuts and new tariffs hit one corner of the market. Dell's blowout quarter, Anthropic below its IPO price, and tonight's PCE — all in numbers.",
            "description": EN_DESC,
            "tasteReview": [
                "SOX −7.88% to 8,832.50 while the Dow rose 0.85% to 50,018.70 — opposite directions in one session",
                "Nvidia $155.38 (−5.86%), Micron $629.79 (−11.01%), Anthropic $81.91 below its $83 IPO price",
                "Dell: revenue $54.94bn (+103%), AI servers $22.0bn (+291%), backlog $132.3bn — fell 11.83% then rose 4.8% after hours",
                "Korea's KOSPI had risen 6.32% a day earlier; U.S. October PCE at 22:30 KST tonight is the next gate",
            ],
            "tips": "This is a summary of public market data, reporting and broker research, not investment advice.",
        },
        "ja": {
            "title": "エヌビディアの安堵ラリーは1日で終了——半導体−7.88％、ダウ＋0.85％",
            "summary": "S&P500 7,201.09（−0.50％）、ナスダック 23,733.54（−1.48％）、ダウ 50,018.70（＋0.85％）、フィラデルフィア半導体は−7.88％。みずほの設備投資引き下げ、UBS・BNPの目標株価引き下げ、追加関税が一箇所に重なりました。デルの好決算、公開価格を割ったアントロピック、今夜のPCEまで数字で整理します。",
            "description": JA_DESC,
            "tasteReview": [
                "SOX −7.88％（8,832.50）に対しダウ＋0.85％（50,018.70）——同じ日の逆方向",
                "エヌビディア155.38ドル（−5.86％）、マイクロン629.79ドル（−11.01％）、アントロピック81.91ドルで公開価格83ドル割れ",
                "デル第3四半期: 売上549.4億ドル（＋103％）、AIサーバー220億ドル（＋291％）、受注残1,323億ドル。通常取引−11.83％→時間外＋4.8％",
                "前日のコスピは＋6.32％（5,006.03）で一日遅れの反映、今夜22:30（韓国時間）の米10月PCEが次の関門",
            ],
            "tips": "本記事は公開された相場データ・報道・リポートの整理であり、個別銘柄の売買を推奨するものではありません。",
        },
        "zh": {
            "title": "英伟达的宽慰行情只维持一天：半导体−7.88%，道指+0.85%",
            "summary": "标普500 7,201.09（−0.50%）、纳斯达克23,733.54（−1.48%）、道指50,018.70（+0.85%），费城半导体指数−7.88%。瑞穗下调AI资本开支、UBS与BNP下调目标价、新增关税叠加，打击集中在一处。戴尔亮眼财报、Anthropic跌破发行价，以及今晚的PCE，全部以数字整理。",
            "description": ZH_DESC,
            "tasteReview": [
                "SOX −7.88%（8,832.50）对道指+0.85%（50,018.70）——同一交易日方向相反",
                "英伟达155.38美元（−5.86%）、美光629.79美元（−11.01%）、Anthropic 81.91美元跌破83美元发行价",
                "戴尔：营收549.4亿美元（+103%）、AI服务器220亿美元（+291%）、在手订单1,323亿美元；正股−11.83%后盘后+4.8%",
                "韩国KOSPI前一日已上涨6.32%至5,006.03；今晚22:30（韩国时间）美国10月PCE是下一道关口",
            ],
            "tips": "本文仅整理公开行情、报道与研报，不构成任何个股买卖建议。",
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
