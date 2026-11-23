#!/usr/bin/env python3
"""2026-11-23 AI 관련주 심층 리포트 (4개국어) → Supabase posts + ISR revalidate.

모든 수치는 2026-11-23 17:00~17:55 KST에 직접 확인한 값:
 - 주가: 야후 파이낸스 종가(미장 11/20, 국장 11/23) 및 시간외·선물(11/23 17:49 KST)
 - 기업: Anthropic IPO 공시(11/20), NVIDIA FQ3 실적(11/17), 마이크론 실적·가이던스
 - 보도: 로이터(SEC 회계조사, 11/20), CNBC·WSJ·Barron's·Ming-Chi Kuo(11/20)
 - 리포트: 교보증권 반도체(11/23), 골드만삭스 메모리(11/22), 삼성증권·하나증권(11/23)
 - 국내: 한국거래소 마감(11/23), 관세청 11월 1~20일 수출입(11/23)
"""

import json
import os
import urllib.request

def _env_local(name):
    """Read a key from .env.local so no secret is hardcoded in the repo."""
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
SLUG = "ai-stocks-nvda-broadcom-micron-anthropic-deep-dive-2026-11-23"

C = "/images/products/ai-stocks-cover-2026-11-23.png"
G1 = "/images/products/ai-stocks-nvda-2026-11-23.png"
G2 = "/images/products/ai-stocks-asic-2026-11-23.png"
G3 = "/images/products/ai-stocks-ant-2026-11-23.png"
G4 = "/images/products/ai-stocks-korea-2026-11-23.png"

KO_DESC = """실물 지표는 사상 최대인데 주가는 반토막이 났다. 11월 23일 코스피는 4,708.54(−3.31%)로 마감했고, 같은 날 관세청이 발표한 11월 1~20일 반도체 수출은 385억 달러로 전년 동기 대비 294.4% 급증해 전체 수출의 49.7%를 차지했다. 시장이 판 것은 지금의 실적이 아니라 2028년의 실적이다. 엔비디아·브로드컴·마이크론·앤트로픽 네 종목을 같은 날 확인된 숫자로만 해부했다.

1. 오늘의 좌표 — 코스피 4,708.54, 반도체 수출 +294.4%
코스피는 전 거래일보다 161.42포인트(3.31%) 내린 4,708.54에 마감했다. 장중 4,586.80까지 밀려 5.8% 넘게 빠졌고, 오전 11시 33분에는 2거래일 연속 매도 사이드카가 발동됐다. 코스닥은 1.58% 내린 635.45로 2024년 12월 9일 이후 가장 낮은 종가를 기록했다. 외국인은 2,472억원을 순매도하며 7거래일 연속 팔았고, 원·달러 환율은 1,345.9원, 장중 1,351.6원까지 올랐다.
반대편 숫자도 같은 날 나왔다. 관세청의 11월 1~20일 수출입 잠정치는 수출 774억 달러(전년 동기 대비 +101.5%), 반도체 385억 달러(+294.4%)였다. 반도체 수출 비중은 1년 전보다 24.3%포인트 오른 49.7%다. 올해 누적 수출은 사상 처음 1조 달러를 넘었다. 실물은 최대로 달리는데 주가가 고점 대비 절반인 이유는, 조정의 초점이 올해 이익이 아니라 2028년 이후의 설비투자와 가격 전망으로 옮겨갔기 때문이다.

2. 엔비디아 −14.01%: 팔린 것은 실적이 아니라 '신뢰'
엔비디아는 11월 20일 20.45달러(14.01%) 내린 125.53달러에 마감했다. 10월 6일 고점 243.37달러 대비 48% 낮고, 7주 연속 하락으로 2008년 금융위기 이후 가장 긴 연속 하락을 기록했다. 8일 사이에 다섯 가지가 겹쳤다. 11월 12일 젠슨 황 CEO가 사생활 스캔들 보도로 사임했고, 17일 실적 발표에서 회계연도 3분기 매출 1,158억 달러(+100%), 주당순이익 2.68달러(예상 2.47달러)를 냈다. 데이터센터 매출은 1,076억 달러로 110% 늘었고, 회사는 2028 회계연도 매출 성장률 전망을 70%에서 75%로 올리며 금액 기준 500억 달러를 더했다. 그런데 18일 10-Q 제출을 "수 주 내"로 미뤘고, 19일 캘리포니아 법무장관이 조사 소환장을 보냈으며, 20일 로이터가 SEC 집행국이 회계 처리를 들여다본다고 보도했다.
보도의 초점은 두 갈래다. 하나는 지역별 매출 표기 방식이다. 엔비디아는 청구지 주소 대신 고객 본사 소재지 기준으로 매출을 분류하도록 바꾸면서 싱가포르를 지역별 매출에서 뺐는데, 싱가포르 매출이 전체의 22%까지 커진 시점(2026 회계연도 2분기 102억 달러, +81%)의 변경이었다는 점이 문제로 지적됐다. 다른 하나는 '순환 금융'이다. 엔비디아가 AI 기업과 클라우드 사업자에 투자하고 데이터센터 보증을 서서 고객의 자사 칩 구매를 돕는 구조가 매출의 질을 가린다는 비판이다.
확인된 것과 확인되지 않은 것을 나눠야 한다. 확인된 것은 조사 착수 보도, 소환장, 10-Q 지연이다. 확인되지 않은 것은 조사 시점과 범위, 위법 여부다. 로이터도 "조사는 위법의 증거가 아니며 많은 조사가 처분 없이 끝난다"고 명시했다. 실적 발표에서 콜레트 크레스 임시 CEO는 앞으로 AI 금융 지원을 더 선별적으로 하겠다고 밝혔고, 회계 문제에 대한 회사 입장은 아직 나오지 않았다.
같은 실적에 월가의 목표가는 174달러에서 260달러까지 갈렸다. 모건스탠리가 비중확대에 260달러(267→260), UBS가 매수 240달러(300→240), 골드만삭스 매수 220달러, 미즈호 아웃퍼폼 220달러(250→220)를 유지한 반면, 트루이스트는 투자의견을 보유로 내리고 목표가를 346달러에서 174달러로 깎았다. UBS는 "생태계가 연간 제품 사이클을 끌고 갈 것"이라며 조정을 매수 기회로 봤고, 트루이스트는 "중국 유출 리스크 때문에 매출을 예측할 신뢰가 없다"고 했다. 즉 지금의 논쟁은 밸류에이션이 아니라 신뢰 비용이다.

3. 브로드컴·AMD·마이크론: GPU 대 ASIC, 진짜 쟁점은 2028년
브로드컴은 12.19% 내린 304.41달러로 11월 6일 이후 최저 종가를 찍었고, AMD는 13.25% 내린 424.39달러, 마이크론은 13.89% 내린 594.51달러였다. 필라델피아 반도체지수는 하루 10.73%, 한 주 17.13% 빠졌다.
브로드컴 급락의 방아쇠는 11월 20일 궈밍치(TF인터내셔널)의 공급망 서베이였다. 구글이 2027년 브로드컴 설계 TPU 8i 시리즈 출하 계획을 약 100만 개(약 20%) 줄였고, 감축은 고가 모델인 8i Max(웨일피시)에 집중됐으며, 대신 미디어텍 설계 8t(학습용) 출하를 늘린다는 내용이다. 기존 500만 개가 400만 개로 줄어든다는 계산이지만 이는 서베이 추정치이고, 구글과 브로드컴은 코멘트하지 않았다. 방향 자체는 새롭지 않다. 브로드컴은 6월 실적 콜에서 구글의 TPU 소스 다변화를 이미 언급했고, 맥쿼리는 브로드컴 비중이 2026년 95%에서 2027년 80%, 2028년 65%로 내려간다고 본다. 반대로 파이퍼샌들러는 전체 TPU 출하를 2026년 450만 개에서 2027년 880만 개로 잡는다. 두 추정을 곱하면 브로드컴 물량은 427만 개에서 704만 개로 늘어난다. 비중은 줄고 절대량은 늘 수 있다는 뜻이다.
AMD는 대중 수출통제 위반 의혹을 담은 공매도 보고서가 나왔고 회사는 부인했다. 마이크론은 성격이 다르다. 2027 회계연도 컨센서스 주당순이익 176.50달러 기준 주가수익비율이 3.4배까지 내려왔고, 6월 25일 사상 최고 종가 1,213.56달러의 절반 수준이다. 회사는 2027년 물량의 75%가 이미 팔렸고, 납품을 거부해도 대금을 내는 5년 구매의무 계약을 도입했다고 밝혔다. 26건의 다년 계약이 2030년까지 매출의 35% 이상을 덮는다. 다만 트렌드포스는 낸드 계약가격이 2027년 1분기부터 최대 5% 하락할 것으로 봤고, 11월 14일에는 D램 가격 담합 소송의 기각 신청이 받아들여지지 않아 삼성전자·SK하이닉스와 함께 재판을 이어가게 됐다.
네 종목을 한 줄로 묶는 것은 2028년이다. 교보증권이 23일 리포트에서 인용한 세미애널리시스는 2028년 가속기 지출 전망을 기존 대비 28% 낮췄고, 수정 후 성장률은 21%다. 2028~2030년 지출 전망은 28~41% 하향됐고, 2028년 HBM 비트 수요 전망은 30% 깎였다. 골드만삭스는 2028년 D램 가격 하락률 전망을 기존 −5%에서 −19%로, 낸드는 −14%에서 −21%로 낮췄다. 반면 2027년은 다르다. 골드만삭스는 2027년 D램 공급 부족이 15년 만에 가장 심한 −5.1%라고 본다. 시장은 2027년의 부족과 2028년의 과잉을 동시에 가격에 넣고 있는 셈이다.

4. 앤트로픽: 1,195억 달러가 만든 유동성 진공, 그리고 오늘 밤 파생상품 9종
앤트로픽은 11월 19일 나스닥에 상장했다. 공모가는 83달러, 기본 공모 규모는 813억 달러였고 초과배정(그린슈)이 전량 행사되며 935억 달러가 됐다. 여기에 AMD·브로드컴·구글·마이크론·마이크로소프트·엔비디아·TSMC가 참여한 260억 달러 사모를 더해 총조달액은 1,195억 달러다. 상장 첫날 111.50달러에 개장해 97.17달러로 마감하며 공모가 대비 17.1% 올랐지만, 이틀째인 20일에는 8.50% 내린 88.91달러로 마감하며 장중 공모가 부근까지 밀렸다.
이 IPO가 기존 AI주에 타격이 된 이유는 두 가지다. 첫째, 사상 최대 규모의 신주가 그날의 자금을 흡수하며 기존 AI주에 차익실현을 유발했다. 둘째, 마이크론처럼 사모에 참여한 종목은 상장사의 주가 하락이 곧 투자 평가손으로 이어졌다. 마이크론은 사모에 10억 달러를 약정했고, 베타가 2.4로 시장보다 변동성이 커 낙폭이 확대됐다.
오늘 밤(11월 23일)에는 파생상품이 한꺼번에 열린다. 미국 20개 옵션거래소가 모두 앤트로픽 옵션을 상장한다. Cboe 규칙 4.3에 따라 공모가 기준 30억 달러 이상 IPO는 두 번째 영업일에 옵션을 상장할 수 있고, 11월 23일이 그날이다. 행사가는 현물가 ±50% 범위에서 5달러 단위로 설정되고, 주간물은 추수감사절 휴장 때문에 11월 25일에 추가돼 27일(반일장)에 만기가 돌아온다. Cboe는 내재변동성이 50~100% 또는 그 이상에서 형성될 수 있다고 봤다. 같은 날 레버리지·인버스 ETF 9종도 상장한다. 프로셰어스 ANTU·ANTY(나스닥, 2배·−2배, 보수 0.95%), 트레이더 ANTT·ANTZ(Cboe), 그라나이트셰어스 AIL·ANS(나스닥), 레버리지셰어스 ANUU·ANDD·ANSS(Cboe, 0.75~0.99%)다. 2배 상품은 하루에 50% 넘게 움직이면 원금 전액을 잃을 수 있고, 일간 수익률을 좇는 구조라 장기 보유 시 복리 왜곡이 생긴다.
앤트로픽 자체의 변수도 있다. 교보증권 리포트는 다리오 아모데이 CEO가 안전성과 인간 통제를 확신할 때까지 학습·배포 속도를 조절하겠다고 밝힌 점을 첫 번째 악재로 꼽았다. 모델 출시 속도는 신규 매출과 후속 투자 시점을 좌우한다.

5. 국내 밸류체인: 목표가가 갈린 이유
삼성전자는 3.06% 내린 177,500원, SK하이닉스는 2.52% 내린 1,085,000원에 마감했다. 장중에는 각각 171,500원(−6.34%), 1,044,000원(−6.20%)까지 밀렸다.
골드만삭스는 22일 보고서에서 삼성전자 목표가를 50만원에서 35만원으로, SK하이닉스를 350만원에서 200만원으로 낮췄다. 2028년 D램 가격 전망을 −19%로 낮추고 두 회사의 2028년 영업이익 추정치도 26%, 23% 깎은 결과다. 다만 투자의견 '매수'는 유지했다. 2027년 D램 공급 부족이 15년 만에 최악이고, HBM 시장은 2027년 2,000억 달러(+236%)로 커지며, 2027년 예상 PER이 2.0~2.4배, 주주환원율이 17~22%라는 점을 근거로 들었다.
삼성증권은 23일 "내년 메모리 가격 급락이 이미 선반영됐다"며 2027년 예상 PBR 1배를 바닥권으로 봤다. 현재 주가가 삼성전자는 내년 메모리 가격 46% 하락, SK하이닉스는 36% 하락을 반영하고 있다는 계산이다. 목표가는 40만원과 300만원. 반등 조건으로는 미국의 2028년 이후 데이터센터 추가 인허가, 엔비디아 새 CEO 확정, 새로운 AI 응용처 등장, 금리 인상 우려 완화 네 가지를 꼽았다. 하나증권은 2027년 실적 전망으로 삼성전자 매출 1,013조원·영업이익 624조원, SK하이닉스 매출 570조원·영업이익 465조원(HBM 매출 91조원, +138%)을 제시하며 목표가 40만원과 280만원을 유지했다.
정리하면 이렇다. 2027년의 숫자는 아직 좋다. 문제는 2028년의 가격과 설비투자다. 그 답은 12월 9일 브로드컴, 12월 17일 마이크론 실적과 내년 1월 하이퍼스케일러 설비투자 가이던스에서 나온다.

6. 오늘 밤과 이번 주 체크리스트
11월 23일 오후 5시 49분(한국시간) 기준 야후 파이낸스에서 S&P 500 선물은 7,102.00(+2.38%), 나스닥 선물은 25,907.50(+3.11%)였다. VIX는 31.30(−12.80%), 미 10년물 금리는 4.912%였다. 엔비디아는 시간외에서 135.70달러(+8.10%)로 반등을 시도했고, 앤트로픽 옵션·ETF 상장과 함께 AI주 저가 매수세가 먼저 움직이는 모습이다. 다만 선물 반등은 하루짜리 수급일 수 있다.
이번 주에는 11월 25일 미국 3분기 GDP와 10월 PCE가 나온다. 물가가 내려오지 않으면 12월 금리 인상이 굳어지고, 그 순간 AI 인프라의 자금조달 비용이 다시 뛴다. 26일에는 한국은행 금통위와 미국 추수감사절 휴장이 겹친다. 한화투자증권은 26일 금통위를 '100% 만장일치 인상'으로 전망하는 채권 리포트를 냈다. 27일은 미국 반일장이라 유동성이 얇다.
종목 쪽 일정은 12월 9일 브로드컴 실적, 12월 17일 마이크론 실적이다. 브로드컴은 구글 TPU 물량 조정의 실제 규모를, 마이크론은 2027년 완판과 2028년 가격 전망의 간극을 확인할 자리다. 2028년을 둘러싼 논쟁이 숫자로 정리되는 시점은 그때다.

본 글은 공개된 시세·공시·리포트를 정리한 정보 기록이며, 특정 종목의 매수·매도를 권유하지 않습니다."""

EN_DESC = """The physical data is at a record high and the stocks are down by half. The KOSPI closed at 4,708.54 (-3.31%) on November 23, while the same morning Korea's customs service reported that semiconductor exports for November 1-20 reached $38.5 billion, up 294.4% year over year and 49.7% of all exports. What the market sold was not this year's earnings but 2028's. Here are Nvidia, Broadcom, Micron and Anthropic, read only through numbers confirmed that day.

1. Today's coordinates: KOSPI 4,708.54, chip exports +294.4%
The KOSPI closed at 4,708.54, down 161.42 points (3.31%), after falling as much as 5.8% to 4,586.80 and triggering a second straight sell-side circuit breaker at 11:33 a.m. The KOSDAQ lost 1.58% to 635.45, its lowest close since December 9, 2024. Foreign investors sold a net 247.2 billion won, a seventh straight session, and the won weakened to 1,345.9 per dollar, touching 1,351.6 intraday.
The same day produced the opposite numbers. Customs data for November 1-20 showed exports of $77.4 billion (+101.5% year over year), with semiconductors at $38.5 billion (+294.4%) and a 49.7% share of total exports, up 24.3 percentage points. Cumulative exports passed $1 trillion for the first time. The gap exists because the selloff is no longer about this year's earnings; it is about capex and pricing beyond 2028.

2. Nvidia -14.01%: what was sold was trust, not earnings
Nvidia closed at $125.53 on November 20, down $20.45 or 14.01%. That is 48% below its October 6 peak of $243.37 and a seventh straight weekly decline, the longest since the 2008 financial crisis. Five things stacked up in eight days. On November 12 CEO Jensen Huang resigned after reports about his personal life. On the 17th the company reported fiscal third-quarter revenue of $115.8 billion (+100%) and EPS of $2.68 against $2.47 expected, with data-center revenue up 110% to $107.6 billion, and raised its fiscal 2028 revenue growth outlook to 75% from 70%, adding $50 billion. Then on the 18th it delayed its 10-Q filing to "coming weeks", on the 19th California's attorney general served an investigative subpoena, and on the 20th Reuters reported that SEC enforcement staff are examining its accounting.
The reporting has two threads. One is geographic revenue reporting: Nvidia switched from billing address to customer headquarters and dropped Singapore from its regional breakdown, a change made just as Singapore sales reached 22% of the total ($10.2 billion in fiscal Q2 2026, +81%). The other is circular financing: Nvidia invests in AI companies and cloud providers and guarantees data-center projects that buy its chips, which critics say obscures the quality of its revenue.
Confirmed and unconfirmed must be separated. Confirmed: the reports of an inquiry, the subpoena, the delayed 10-Q. Unconfirmed: when the inquiry opened, what it covers, and whether any rule was broken. Reuters itself noted that investigations are not evidence of wrongdoing and many close without action. On the earnings call, interim CEO Colette Kress said the company would be far more selective about AI financing deals; it has not commented on the accounting question.
Wall Street price targets on identical earnings now range from $174 to $260. Morgan Stanley kept Overweight at $260 (from $267), UBS kept Buy at $240 (from $300), Goldman Sachs Buy at $220, Mizuho Outperform at $220 (from $250). Truist cut its rating to hold and its target to $174 from $346. UBS called the pullback an opportunity because the ecosystem will pull the annual roadmap along; Truist said China exposure leaves it unable to forecast revenue with confidence. The argument is not about valuation multiples. It is about the cost of trust.

3. Broadcom, AMD, Micron: GPU versus ASIC, and the real fight is 2028
Broadcom fell 12.19% to $304.41, its lowest close since November 6. AMD fell 13.25% to $424.39 and Micron 13.89% to $594.51. The Philadelphia Semiconductor Index lost 10.73% in a day and 17.13% in a week.
Broadcom's trigger was a November 20 supply-chain survey from Ming-Chi Kuo of TF International: Google cut 2027 shipments of Broadcom-designed TPU 8i by about one million units, or roughly 20%, concentrated in the higher-priced 8i Max (Whalefish), while increasing MediaTek-designed 8t (training) shipments. That implies a cut from about five million to four million units, but it is a single survey estimate, and Google and Broadcom declined to comment. The direction is not new: Broadcom itself flagged Google diversifying its TPU sourcing on its June earnings call, and Macquarie sees Broadcom's share falling from 95% in 2026 to 80% in 2027 and 65% in 2028. Piper Sandler, however, sees total TPU shipments rising from 4.5 million in 2026 to 8.8 million in 2027. Multiply the two and Broadcom's units rise from 4.27 million to 7.04 million: share can fall while volume rises.
AMD is facing a short-seller report alleging violations of China export controls, which the company denies. Micron is a different story. At $594.51 it trades at about 3.4 times fiscal 2027 consensus EPS of $176.50, roughly half its record close of $1,213.56 on June 25. Management says 75% of 2027 output is already sold and that it has moved to five-year take-or-pay contracts, with 26 multi-year agreements covering more than 35% of revenue through 2030. But TrendForce expects NAND contract prices to start falling by up to 5% in the first quarter of 2027, and on November 14 a court refused to dismiss a DRAM price-fixing suit, leaving Micron, Samsung and SK hynix as co-defendants.
What ties the group together is 2028. SemiAnalysis, cited in a November 23 Kyobo Securities report, cut its 2028 accelerator spending forecast by 28%, leaving growth of 21%, reduced its 2028-2030 spending outlook by 28-41% and its 2028 HBM bit demand by 30%. Goldman Sachs cut its 2028 DRAM price forecast to -19% from -5% and NAND to -21% from -14%. Yet 2027 remains tight: Goldman sees a 5.1% DRAM supply deficit, the worst in 15 years. The market is pricing 2027 scarcity and 2028 glut at the same time.

4. Anthropic: the $119.5 billion liquidity vacuum, and nine derivatives tonight
Anthropic listed on Nasdaq on November 19 at an IPO price of $83. The base offering raised $81.3 billion; with the full greenshoe it reached $93.5 billion. Add a $26 billion concurrent private placement bought by AMD, Broadcom, Google, Micron, Microsoft, Nvidia and TSMC and total gross proceeds were $119.5 billion. The stock opened at $111.50 and closed its first day at $97.17, up 17.1% from the IPO price, then fell 8.50% to $88.91 on the second day, trading near the offer price intraday.
Two things made the IPO a hit to existing AI stocks. First, the largest new issue on record absorbed the day's money and triggered profit-taking in AI names. Second, holders that took part in the private placement, like Micron with a $1 billion commitment, saw a mark-to-market loss as the shares fell. Micron's beta of about 2.4 amplified the move.
Tonight, November 23, the derivatives open all at once. All 20 U.S. options exchanges list Anthropic options. Under Cboe Rule 4.3 an IPO of $3 billion or more may list options on its second business day, and today is that day. Strikes will be set in $5 increments roughly 50% above and below spot; weeklies arrive November 25 because of the Thanksgiving holiday and first expire November 27, a shortened session. Cboe expects implied volatility of 50-100% or higher. Nine leveraged and inverse ETFs also launch: ProShares ANTU and ANTY (Nasdaq, 2x and -2x, 0.95% net expense), Tradr ANTT and ANTZ (Cboe), GraniteShares AIL and ANS (Nasdaq), and Leverage Shares ANUU, ANDD and ANSS (Cboe, 0.75-0.99%). A 2x fund can lose all of its value in a single day if the stock moves more than 50%, and daily resetting makes long holding periods deviate sharply from the stated multiple.
Anthropic also carries its own risk. The Kyobo report lists as the first of five negatives that CEO Dario Amodei has said the company will pace training and deployment until it is confident about safety and human control, which makes model release timing a swing factor for revenue and follow-on investment.

5. Korea's value chain: why the targets split
Samsung Electronics closed at 177,500 won (-3.06%) and SK hynix at 1,085,000 won (-2.52%), after falling as much as 6.34% and 6.20% intraday.
On November 22 Goldman Sachs cut its Samsung target to 350,000 won from 500,000 and SK hynix to 2,000,000 won from 3,500,000, reflecting a 2028 DRAM price forecast of -19% and cuts of 26% and 23% to 2028 operating profit. It kept Buy. Its reasons: the 2027 DRAM deficit is the worst in 15 years, the HBM market grows to $200 billion in 2027 (+236%), 2027 P/E is 2.0-2.4x and shareholder returns run 17-22%.
Samsung Securities argued on the 23rd that next year's memory price decline is already priced in: at 2027 book value multiples near 1x, Samsung reflects a 46% drop in memory prices and SK hynix 36%. It kept targets of 400,000 and 3,000,000 won and named four conditions for a rebound: additional U.S. data-center permits from 2028, a permanent Nvidia CEO, new AI applications, and easing rate-hike fears. Hana Securities forecast 2027 revenue of 1,013 trillion won and operating profit of 624 trillion won for Samsung, and 570 trillion won and 465 trillion won for SK hynix (HBM revenue 91 trillion won, +138%), keeping targets of 400,000 and 2,800,000 won.
The summary: 2027 still looks good on paper. The problem is 2028 pricing and capex. The answers arrive with Broadcom on December 9, Micron on December 17, and next January's hyperscaler capex guidance.

6. Tonight and this week
At 5:49 p.m. KST on November 23, S&P 500 futures were at 7,102.00 (+2.38%) and Nasdaq futures at 25,907.50 (+3.11%). The VIX was 31.30 (-12.80%) and the 10-year Treasury yield 4.912%. Nvidia traded at $135.70 in the overnight session (+8.10%), suggesting dip buyers are moving first alongside the Anthropic options and ETF listings. One day of futures does not make a turn.
This week brings U.S. third-quarter GDP and October PCE on November 25. If inflation does not cool, a December hike locks in and AI infrastructure funding costs jump again. November 26 brings the Bank of Korea meeting and the U.S. Thanksgiving holiday; Hana Securities expects a unanimous BOK hike. November 27 is a half session in the U.S., so liquidity is thin.
On the corporate calendar, Broadcom reports December 9 and Micron December 17. Broadcom will show the real size of Google's TPU adjustment; Micron will show the gap between sold-out 2027 and 2028 pricing. That is when the 2028 argument turns into numbers.

This is a record of public prices, filings and research, not investment advice."""

JA_DESC = """実体指標は過去最高なのに、株価は半値になった。11月23日のコスピは4,708.54（−3.31%）で引け、同じ日の朝に関税庁が発表した11月1〜20日の半導体輸出は385億ドルで前年同期比294.4%増、全輸出の49.7%を占めた。市場が売ったのは今年の利益ではなく2028年の利益だ。エヌビディア、ブロードコム、マイクロン、アントロピックの4銘柄を、その日に確認できた数字だけで解剖した。

1. 今日の座標 — コスピ4,708.54、半導体輸出+294.4%
コスピは前日比161.42ポイント（3.31%）安の4,708.54で引けた。取引中に4,586.80まで下げて5.8%超の下落となり、午前11時33分には2営業日連続で売りサイドカーが発動した。コスダックは1.58%安の635.45で、2024年12月9日以来の安値終値。外国人は2,472億ウォンを売り越して7営業日連続の売り越しとなり、ウォン・ドルは1,345.9ウォン、取引中に1,351.6ウォンまで上がった。
同じ日に逆の数字も出た。11月1〜20日の輸出は774億ドル（前年同期比+101.5%）、半導体は385億ドル（+294.4%）で、半導体の輸出比重は24.3ポイント上がって49.7%になった。年初来の累計輸出は初めて1兆ドルを超えた。実体は過去最高なのに株価が高値から半値なのは、調整の焦点が今年の利益ではなく2028年以降の設備投資と価格見通しに移ったからだ。

2. エヌビディア−14.01% 売られたのは実績ではなく「信頼」
エヌビディアは11月20日に20.45ドル（14.01%）安の125.53ドルで引けた。10月6日の高値243.37ドルから48%低く、7週連続下落は2008年金融危機以来最長。8日の間に5つが重なった。11月12日にジェンセン・フアンCEOが辞任し、17日の決算では売上高1,158億ドル（+100%）、EPS2.68ドル（予想2.47ドル）を計上、データセンター売上は110%増の1,076億ドルだった。会社は2028会計年度の売上成長率見通しを70%から75%へ引き上げ、金額で500億ドルを上乗せした。ところが18日に10-Q提出を「数週間内」に先送りし、19日にカリフォルニア州司法長官が調査の召喚状を送り、20日にはロイターがSEC執行部が会計処理を調べていると報じた。
報道の焦点は2つ。地域別売上の表示方法と、循環金融だ。エヌビディアは請求先住所ではなく顧客本社の所在地で売上を分類する方式に変え、シンガポールを地域別売上から外した。シンガポール売上が全体の22%（2026会計年度2四半期に102億ドル、+81%）まで膨らんだ時期の変更だった点が問われている。循環金融は、エヌビディアがAI企業やクラウド事業者に出資し、データセンターの保証を提供して自社チップの購入を支える構造で、売上の質を覆い隠すという批判だ。
確認できたことと、できていないことを分ける必要がある。確認できたのは調査着手の報道、召喚状、10-Qの遅延。確認できていないのは調査の時期・範囲・違法性だ。ロイター自身も「調査は違法の証拠ではなく、多くは処分なしで終わる」と明記した。決算説明でコレット・クレス暫定CEOはAI向け金融支援をより選別的にすると述べ、会計問題については会社の見解が出ていない。
同じ決算に対する目標株価は174ドルから260ドルまで割れた。モルガン・スタンレーは268→260ドルで強気維持、UBSは300→240ドルで買い維持、ゴールドマン・サックスは220ドル、みずほは250→220ドル。一方トルーイストは投資判断を保有に下げ、目標を346ドルから174ドルへ切り下げた。UBSは「エコシステムが年次製品サイクルを引っ張る」として押し目を買い機会と見て、トルーイストは「中国流出リスクで売上を予想する信頼がない」とした。論点はバリュエーションではなく信頼のコストだ。

3. ブロードコム・AMD・マイクロン — GPU対ASIC、本当の争点は2028年
ブロードコムは12.19%安の304.41ドルで11月6日以来の安値、AMDは13.25%安の424.39ドル、マイクロンは13.89%安の594.51ドル。フィラデルフィア半導体指数は1日で10.73%、1週間で17.13%下落した。
ブロードコム急落の引き金は11月20日の郭明錤（TFインターナショナル）のサプライチェーン調査だ。グーグルが2027年のブロードコム設計TPU 8iシリーズの出荷計画を約100万個（約20%）減らし、削減は高価格の8i Max（ホエールフィッシュ）に集中、代わりにMediaTek設計の8t（学習用）を増やすという内容だ。500万個が400万個になる計算だが、これは単一調査の推計で、グーグルとブロードコムはコメントしていない。方向自体は新しくない。ブロードコムは6月の決算説明でグーグルのTPU調達先の多様化に言及しており、マッコーリーはブロードコムの比率が2026年95%から2027年80%、2028年65%へ下がると見る。逆にパイパー・サンドラーはTPU全体の出荷を2026年450万個から2027年880万個に増えると試算する。両者を掛けるとブロードコムの数量は427万個から704万個に増える。比率は下がっても数量は増え得る。
AMDは対中輸出規制違反の疑いを指摘する空売り報告書が出て、会社は否定した。マイクロンは事情が違う。2027会計年度のコンセンサスEPS176.50ドルでPERは3.4倍まで下がり、6月25日の上場来高値終値1,213.56ドルのほぼ半値だ。会社は2027年数量の75%が完売し、納品を拒否しても代金を払う5年の購買義務契約を導入したと説明する。26件の複数年契約が2030年まで売上の35%以上をカバーする。ただしトレンドフォースはNANDの契約価格が2027年1〜3月に最大5%下落すると見ており、11月14日にはDRAM価格カルテル訴訟の却下申し立てが認められず、サムスン電子・SKハイニックスとともに審理が続く。
4銘柄を結ぶのは2028年だ。11月23日の教保証券レポートが引用したセミアナリシスは、2028年のアクセラレータ支出見通しを28%下方修正し、修正後の成長率を21%とした。2028〜30年の支出見通しは28〜41%引き下げ、2028年のHBMビット需要は30%削った。ゴールドマン・サックスは2028年のDRAM価格下落率を−5%から−19%へ、NANDを−14%から−21%へ引き下げた。一方で2027年は違う。ゴールドマンは2027年のDRAM需給ギャップを−5.1%と、15年で最悪の供給不足と見る。市場は2027年の不足と2028年の過剰を同時に織り込んでいる。

4. アントロピック — 1,195億ドルが作った流動性の真空、そして今夜のデリバティブ9本
アントロピックは11月19日にナスダックへ上場した。公開価格83ドル、基本公募は813億ドル、超過割当（グリーンシュー）の全行使で935億ドル。さらにAMD・ブロードコム・グーグル・マイクロン・マイクロソフト・エヌビディア・TSMCが参加した260億ドルの私募を加え、調達総額は1,195億ドルになった。初日は111.50ドルで寄り付き97.17ドルで引けて公開価格比17.1%高。2日目の20日は8.50%安の88.91ドルで引け、取引中に公開価格付近まで下げた。
このIPOが既存AI株の重しになった理由は2つ。史上最大の新株がその日の資金を吸い、AI株の利益確定を誘ったこと。そして私募に参加したマイクロンのように、上場企業の株価下落が投資評価損に直結したことだ。マイクロンは私募に10億ドルを約定し、ベータ2.4が値動きを増幅した。
今夜（11月23日）はデリバティブが一斉に開く。米国の20のオプション取引所がすべてアントロピックのオプションを上場する。Cboe規則4.3により公開価格ベースで30億ドル以上のIPOは2営業日目に上場でき、この日がそれにあたる。権利行使価格は現物の±50%の範囲で5ドル刻み、週次は感謝祭休場のため11月25日に追加され、27日（短縮取引）が最初の満期になる。Cboeはインプライド・ボラティリティが50〜100%以上になり得るとした。同じ日にレバレッジ・インバースETF9本も上場する。プロシェアーズANTU・ANTY（ナスダック、2倍・−2倍、経費0.95%）、トレーダーANTT・ANTZ（Cboe）、グラナイトシェアーズAIL・ANS（ナスダック）、レバレッジシェアーズANUU・ANDD・ANSS（Cboe、0.75〜0.99%）。2倍の商品は1日に50%超動くと元本を全額失い得る。
アントロピック自身の変数もある。教保証券のレポートは、ダリオ・アモデイCEOが安全性と人間の統制に確信を持つまで学習・配備の速度を調整すると述べた点を5つの悪材料の1番目に挙げた。モデル発表の速度は新規売上と追加投資の時期を左右する。

5. 韓国のバリューチェーン — 目標株価が割れた理由
サムスン電子は3.06%安の177,500ウォン、SKハイニックスは2.52%安の1,085,000ウォンで引けた。取引中にはそれぞれ171,500ウォン（−6.34%）、1,044,000ウォン（−6.20%）まで下げた。
ゴールドマン・サックスは22日のレポートでサムスン電子の目標を50万ウォンから35万ウォンへ、SKハイニックスを350万ウォンから200万ウォンへ引き下げた。2028年のDRAM価格見通しを−19%に下げ、両社の2028年営業利益予想を26%、23%削った結果だ。ただし投資判断「買い」は維持した。2027年のDRAM供給不足が15年で最悪で、HBM市場が2027年に2,000億ドル（+236%）へ拡大し、2027年PERが2.0〜2.4倍、株主還元率が17〜22%である点を根拠に挙げた。
サムスン証券は23日、来年のメモリ価格急落はすでに株価に織り込まれたとし、2027年予想PBR1倍を底値圏と見た。現在の株価はサムスン電子が来年のメモリ価格46%下落を、SKハイニックスが36%下落を反映しているという計算だ。目標は40万ウォンと300万ウォン。反発の条件として、米国の2028年以降のデータセンター追加認可、エヌビディアの新CEO確定、新しいAI用途の登場、利上げ懸念の緩和の4つを挙げた。ハナ証券は2027年の業績見通しとしてサムスン電子の売上1,013兆ウォン・営業利益624兆ウォン、SKハイニックスの売上570兆ウォン・営業利益465兆ウォン（HBM売上91兆ウォン、+138%）を示し、目標40万ウォンと280万ウォンを維持した。
まとめるとこうだ。2027年の数字はまだ良い。問題は2028年の価格と設備投資だ。その答えは12月9日のブロードコム、12月17日のマイクロンの決算と、来年1月のハイパースケーラーの設備投資ガイダンスで出る。

6. 今夜と今週のチェックリスト
11月23日午後5時49分（韓国時間）時点で、S&P500先物は7,102.00（+2.38%）、ナスダック先物は25,907.50（+3.11%）。VIXは31.30（−12.80%）、米10年債利回りは4.912%だった。エヌビディアは時間外で135.70ドル（+8.10%）と反発を試み、アントロピックのオプション・ETF上場とともに押し目買いが先に動いている。ただし先物の反発は一日の需給かもしれない。
今週は11月25日に米3四半期GDPと10月PCEが出る。物価が下がらなければ12月利上げが固まり、その瞬間にAIインフラの資金調達コストが再び跳ねる。26日は韓国銀行の金融通貨委員会と米感謝祭休場が重なる。ハナ証券は26日の会合を「100%全会一致の利上げ」と予想する債券レポートを出した。27日は米国が短縮取引で流動性が薄い。
銘柄では12月9日のブロードコム、12月17日のマイクロンの決算だ。ブロードコムはグーグルのTPU調整の実規模を、マイクロンは2027年の完売と2028年の価格見通しの乖離を確認する場になる。2028年をめぐる議論が数字に変わるのはその時だ。

本記事は公開された相場・開示・レポートの整理であり、個別銘柄の売買を推奨するものではない。"""

ZH_DESC = """实体指标创下历史新高，股价却腰斩。11月23日韩国综合股价指数（KOSPI）收于4,708.54点（−3.31%），同一天上午关税厅公布的11月1日至20日半导体出口为385亿美元，同比增长294.4%，占全部出口的49.7%。市场卖出的不是今年的利润，而是2028年的利润。本文只用当天确认的数字，拆解英伟达、博通、美光、Anthropic四只股票。

1. 今日坐标——KOSPI 4,708.54，半导体出口+294.4%
KOSPI收于4,708.54点，下跌161.42点（3.31%）。盘中一度跌至4,586.80点，跌幅超过5.8%，上午11时33分连续第二个交易日触发卖出熔断（sidecar）。科斯达克下跌1.58%至635.45点，为2024年12月9日以来最低收盘。外资净卖出2,472亿韩元，连续7个交易日净卖出；韩元对美元报1,345.9，盘中一度升至1,351.6。
同一天也出现了相反的数字。11月1日至20日出口774亿美元（同比+101.5%），半导体385亿美元（+294.4%），半导体占比上升24.3个百分点至49.7%。今年以来累计出口首次突破1万亿美元。实体数据创纪录而股价只有高点的一半，原因在于调整的焦点已从今年的利润转向2028年以后的资本开支与价格展望。

2. 英伟达−14.01%：被卖出的是信任，不是业绩
英伟达11月20日收于125.53美元，下跌20.45美元（14.01%），较10月6日高点243.37美元低48%，连续7周下跌，为2008年金融危机以来最长。8天内五件事叠加：11月12日黄仁勋CEO因私生活报道辞职；17日财报营收1,158亿美元（+100%）、每股收益2.68美元（预期2.47美元），数据中心营收增长110%至1,076亿美元，公司将2028财年营收增速指引从70%上调至75%，金额上调500亿美元；18日将10-Q申报推迟至"未来数周"；19日加州总检察长发出调查传票；20日路透报道SEC执法部门正在审查其会计处理。
报道有两条主线。一是地区营收列报方式：英伟达改为按客户总部所在地而非账单地址划分营收，并将新加坡从地区明细中剔除，而当时新加坡营收已达总额的22%（2026财年第二季度102亿美元，+81%）。二是"循环融资"：英伟达投资AI企业与云厂商、为数据中心项目提供担保以支持其购买自家芯片，批评者认为这掩盖了营收质量。
必须区分已确认与未确认。已确认：调查报道、传票、10-Q推迟。未确认：调查启动时间、范围与是否违法。路透本身也指出"调查不是违法的证据，许多调查无处分结案"。电话会上临时CEO科莱特·克雷斯表示今后对AI融资将更加挑剔，公司尚未就会计问题表态。
同样的业绩，华尔街目标价从174美元到260美元不等。摩根士丹利维持增持、目标260美元（267→260），UBS维持买入240美元（300→240），高盛买入220美元，瑞穗跑赢大盘220美元（250→220）；而Truist将评级下调至持有，目标价从346美元砍至174美元。争论的不是估值倍数，而是信任的成本。

3. 博通、AMD、美光：GPU对ASIC，真正的焦点是2028年
博通下跌12.19%至304.41美元，为11月6日以来最低收盘；AMD跌13.25%至424.39美元；美光跌13.89%至594.51美元。费城半导体指数单日跌10.73%，一周跌17.13%。
博通的导火索是11月20日郭明錤（天风国际）的供应链调查：谷歌将2027年博通设计的TPU 8i系列出货计划下调约100万颗（约20%），削减集中在高价的8i Max（Whalefish），同时增加联发科设计的8t（训练用）出货。按此推算由500万颗降至400万颗，但这是单一调查的估计，谷歌与博通均未置评。方向并不新：博通在6月财报电话会上已提及谷歌TPU供应多元化，麦格理认为博通份额将从2026年的95%降至2027年的80%、2028年的65%。但Piper Sandler估计TPU总出货将从2026年的450万颗增至2027年的880万颗，两者相乘，博通出货由427万颗升至704万颗——份额下降，数量仍可增长。
AMD面对的是指控其违反对华出口管制的做空报告，公司予以否认。美光情况不同：按2027财年一致预期每股收益176.50美元计算，市盈率已降至约3.4倍，约为6月25日历史最高收盘1,213.56美元的一半。公司称2027年产量已售出75%，并采用五年照付不议合同；26份多年协议覆盖到2030年35%以上的营收。但TrendForce预计NAND合约价将从2027年第一季度起下跌最多5%，11月14日DRAM价格操纵诉讼的驳回申请未获支持，美光与三星、SK海力士继续作为共同被告应诉。
把四只股票串起来的是2028年。教保证券11月23日报告引用的SemiAnalysis将2028年加速器支出预测下调28%，修正后增速为21%；2028至2030年支出预测下调28%至41%，2028年HBM比特需求下调30%。高盛将2028年DRAM价格预测从−5%下调至−19%，NAND从−14%下调至−21%。但2027年不同：高盛认为2027年DRAM供需缺口为−5.1%，是15年来最严重的短缺。市场同时在为2027年的短缺和2028年的过剩定价。

4. Anthropic：1,195亿美元制造的流动性真空，以及今晚9种衍生品
Anthropic于11月19日在纳斯达克上市，发行价83美元，基础发行募资813亿美元，超额配售（绿鞋）全额行使后达935亿美元；加上AMD、博通、谷歌、美光、微软、英伟达、台积电参与的260亿美元私募，募资总额1,195亿美元。首日开盘111.50美元、收盘97.17美元，较发行价涨17.1%；第二日（20日）跌8.50%至88.91美元，盘中一度逼近发行价。
这次IPO冲击现有AI股有两个原因：史上最大规模新股吸走了当日资金，引发AI股获利了结；参与私募的公司（如承诺10亿美元的美光）股价下跌直接形成投资损失，美光约2.4的贝塔放大了跌幅。
今晚（11月23日）衍生品同时开闸。美国20家期权交易所全部上市Anthropic期权。按Cboe规则4.3，发行规模30亿美元以上的IPO可在第二个交易日上市期权，今天正是那一天。行权价在现价上下约50%区间内以5美元为单位；因感恩节休市，周度合约于11月25日追加，首个到期日为11月27日（半日交易）。Cboe预计隐含波动率在50%至100%甚至更高。同日还有9只杠杆与反向ETF上市：ProShares ANTU/ANTY（纳斯达克，2倍/−2倍，费率0.95%）、Tradr ANTT/ANTZ（Cboe）、GraniteShares AIL/ANS（纳斯达克）、Leverage Shares ANUU/ANDD/ANSS（Cboe，0.75~0.99%）。2倍产品若单日波动超过50%可能损失全部本金。
Anthropic自身也有变量。教保证券报告把CEO达里奥·阿莫代伊表示"在确信安全与人类可控之前将调整训练与部署速度"列为五大利空之首——模型发布节奏直接影响新增营收与后续投资时点。

5. 韩国价值链：目标价为何分化
三星电子收于177,500韩元（−3.06%），SK海力士1,085,000韩元（−2.52%），盘中分别跌至171,500韩元（−6.34%）与1,044,000韩元（−6.20%）。
高盛11月22日将三星电子目标价从50万韩元下调至35万韩元，SK海力士从350万韩元下调至200万韩元，反映2028年DRAM价格预测−19%以及两家公司2028年营业利润预测下调26%与23%。但维持"买入"：2027年DRAM缺口为15年来最严重，HBM市场2027年增至2,000亿美元（+236%），2027年市盈率仅2.0~2.4倍，股东回报率17%~22%。
三星证券11月23日认为明年的存储价格下跌已在股价中反映：2027年预期市净率约1倍，三星电子已反映存储价格下跌46%、SK海力士36%。维持目标价40万与300万韩元，并提出四个反弹条件：美国2028年以后新增数据中心许可、英伟达新CEO确定、新的AI应用出现、加息忧虑缓解。韩亚证券预测2027年三星电子营收1,013万亿韩元、营业利润624万亿韩元，SK海力士营收570万亿韩元、营业利润465万亿韩元（HBM营收91万亿韩元，+138%），维持目标价40万与280万韩元。
一句话总结：2027年的数字仍然好看，问题在2028年的价格与资本开支。答案将在12月9日博通、12月17日美光的财报，以及明年1月超大规模厂商的资本开支指引中揭晓。

6. 今晚与本周清单
11月23日下午5时49分（韩国时间），标普500期货7,102.00（+2.38%），纳斯达克期货25,907.50（+3.11%），VIX 31.30（−12.80%），美债10年期收益率4.912%。英伟达盘后报135.70美元（+8.10%），与Anthropic期权、ETF上市一道，抄底资金先行。但一天的期货反弹不代表趋势反转。
本周关注：11月25日美国三季度GDP与10月PCE——若通胀不降，12月加息将成定局，AI基础设施融资成本再度跳升；11月26日韩国银行金融货币委员会与美国感恩节休市叠加，韩亚证券预计此次会议"100%全票加息"；11月27日美股半日交易，流动性稀薄。
个股日程：12月9日博通、12月17日美光财报。博通将揭示谷歌TPU调整的真实规模，美光将显示2027年售罄与2028年价格展望之间的落差。围绕2028年的争论将在那时变成数字。

本文仅为公开行情、公告与研报的整理，不构成任何个股买卖建议。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "postType": "report",
    "store": "K-Trend Market",
    "priceKrw": 0,
    "releaseDate": "2026-11-23",
    "rating": 5,
    "imageUrl": C,
    "images": [G1, G2, G3, G4],
    "affiliateUrl": "https://stock.naver.com/",
    "affiliatePlatform": "Coupang",
    "i18n": {
        "ko": {
            "title": "실적은 사상 최대인데 주가는 −48%…AI 관련주 4종을 같은 날 숫자로 해부했다",
            "summary": "엔비디아 −14.01%($125.53), 브로드컴 −12.19%, 마이크론 −13.89%, 앤트로픽 −8.50%. SEC 회계조사·구글 TPU 감산·1,195억 달러 IPO·반도체 수출 +294.4%까지, 11월 23일 확인된 숫자만으로 네 종목의 쟁점을 정리했습니다.",
            "description": KO_DESC,
            "tasteReview": [
                "엔비디아는 7주 연속 하락·고점 대비 −48%. 실적은 매출 $1,158억(+100%)으로 예상을 웃돌았지만, SEC 회계조사 보도가 하루 낙폭을 두 배로 키웠다",
                "브로드컴 급락의 방아쇠는 구글 TPU 8i 100만 개(≈20%) 감산 서베이. 다만 이는 단일 추정치이고, TPU 전체 파이가 커지면 절대 물량은 늘 수 있다",
                "앤트로픽은 조달 총액 $1,195억으로 사상 최대 IPO. 상장 3일차인 11/23에 옵션과 레버리지·인버스 ETF 9종이 동시에 상장한다",
                "국내는 수출 +294.4%와 주가 −50%가 공존. 골드만삭스와 삼성증권 모두 '매수'는 유지하되 2028년 가격 전망을 낮췄다",
            ],
            "tips": "본 글은 공개된 시세·공시·리포트를 정리한 정보 기록이며, 특정 종목의 매수·매도를 권유하지 않습니다.",
        },
        "en": {
            "title": "Record Earnings, a 48% Drawdown: Four AI Stocks Dissected With One Day's Numbers",
            "summary": "Nvidia -14.01% ($125.53), Broadcom -12.19%, Micron -13.89%, Anthropic -8.50%. From the SEC accounting report and Google's TPU cut to a $119.5bn IPO and Korean chip exports up 294.4%, here is what the numbers confirmed on November 23.",
            "description": EN_DESC,
            "tasteReview": [
                "Nvidia has fallen seven weeks straight and sits 48% below its October peak, even after $115.8bn of quarterly revenue (+100%) beat estimates",
                "Broadcom's slide began with a survey saying Google cut 2027 TPU 8i shipments by about 20% - one estimate, while the total TPU pie is still growing",
                "Anthropic raised $119.5bn in the largest IPO on record and lists options plus nine leveraged and inverse ETFs on day three",
                "Korea shows +294.4% chip exports alongside stocks down by half; Goldman and Samsung Securities both keep Buy but cut 2028 price forecasts",
            ],
            "tips": "This is a summary of public market data, filings and research, not investment advice.",
        },
        "ja": {
            "title": "過去最高の業績、株価は−48%…AI関連4銘柄を同じ日の数字で解剖",
            "summary": "エヌビディア−14.01%（125.53ドル）、ブロードコム−12.19%、マイクロン−13.89%、アントロピック−8.50%。SEC会計調査、グーグルのTPU減産、1,195億ドルのIPO、半導体輸出+294.4%まで、11月23日に確認できた数字だけで4銘柄の論点を整理した。",
            "description": JA_DESC,
            "tasteReview": [
                "エヌビディアは7週連続下落で高値から−48%。売上1,158億ドル（+100%）は予想超えだが、SEC会計調査報道が一日の下げを倍にした",
                "ブロードコム急落の引き金はグーグルのTPU 8i約20%減という調査。単一推計であり、TPU全体のパイが広がれば数量は増え得る",
                "アントロピックは調達総額1,195億ドルで史上最大のIPO。上場3日目の11/23にオプションとレバレッジ・インバースETF9本が同時上場する",
                "韓国は輸出+294.4%と株価−50%が同居。ゴールドマンもサムスン証券も買いは維持しつつ2028年の価格見通しを下げた",
            ],
            "tips": "本記事は公開された相場・開示・レポートの整理であり、個別銘柄の売買を推奨するものではない。",
        },
        "zh": {
            "title": "业绩创历史新高、股价却腰斩：用同一天的数字拆解四只AI股",
            "summary": "英伟达−14.01%（125.53美元）、博通−12.19%、美光−13.89%、Anthropic−8.50%。从SEC会计调查、谷歌TPU减产，到1,195亿美元IPO与韩国半导体出口+294.4%，本文只用11月23日确认的数字梳理四只股票的争议点。",
            "description": ZH_DESC,
            "tasteReview": [
                "英伟达连跌7周、较高点低48%。单季营收1,158亿美元（+100%）超预期，但SEC会计调查报道令当日跌幅翻倍",
                "博通暴跌的导火索是谷歌2027年TPU 8i减产约20%的调查，但这是单一估计；若TPU整体蛋糕扩大，绝对数量仍可能增长",
                "Anthropic募资总额1,195亿美元，为史上最大IPO；上市第三天（11/23）期权与9只杠杆、反向ETF同时上市",
                "韩国半导体出口+294.4%与股价−50%并存；高盛与三星证券均维持买入，但下调2028年价格预测",
            ],
            "tips": "本文仅为公开行情、公告与研报的整理，不构成任何个股买卖建议。",
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
