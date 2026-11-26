#!/usr/bin/env python3
"""2026-11-24 아침 증시 리포트: 2026-11-23(월) 미국장 마감 → Supabase posts(4개국어) + ISR revalidate.

모든 수치는 2026-11-24 08:20~08:35 KST 확인:
 - 야후 파이낸스 일별 종가/시세(quotes.json), 야후 파이낸스 실화면 캡처
 - CNBC 라이브 블로그(11/23), CNBC 애널리스트 업그레이드 기사(11/23)
 - 로이터(11/23 두 건: 복귀 속보·분석), 블룸버그(11/23), AP·포춘(11/23), 뉴스핌·조선비즈·중앙일보(11/24 06시 보도)
 - 네이버 증권 리서치 데일리 11/24 게시분(신한 11/23 마감시황, KB 11/23 장마감코멘트)
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
SLUG = "nvidia-huang-return-nasdaq-best-day-2026-11-24"

C = "/images/products/market-nvidia-cover-2026-11-24.png"
G1 = "/images/products/market-nvidia-index-board-2026-11-24.png"
G2 = "/images/products/market-nvidia-movers-2026-11-24.png"
G3 = "/images/products/market-nvidia-chart-2026-11-24.png"
G4 = "/images/products/market-nvidia-timeline-2026-11-24.png"

KO_DESC = """11월 20일 금요일, 뉴욕은 AI 투매로 무너졌다. 나스닥 −5.28%, S&P 500 −3.70%, 다우 −1.93%. 세 지수 모두 고점 대비 10% 넘게 빠져 조정 국면에 들어섰고, 나스닥100은 약세장 문턱(고점 대비 −20%)까지 갔다. 엔비디아는 하루에 14% 밀렸고, 시가총액 순위는 4위로 내려앉았다. 주말 동안 시장을 덮은 이야기는 "AI 투자는 끝났는가"였다.
사흘 뒤인 11월 23일 월요일, 방향은 정반대로 뒤집혔다. 뉴욕 정규장 개장 전인 오전 9시 무렵, 엔비디아 이사회가 젠슨 황을 CEO로 복귀시킨다고 발표했다. 사임 11일 만이었다. 나스닥은 6.51% 오른 24,089.56, S&P 500은 4.73% 오른 7,237.17, 다우는 3.01% 오른 49,595.31에 마감했다. S&P 500과 나스닥 모두 2025년 4월 8일 이후 가장 큰 하루 상승폭이다. 엔비디아는 31.48% 폭등했고, 시가총액은 하루 만에 약 9,600억 달러 늘어 4조100억 달러가 됐다. 단일 기업의 하루 시가총액 증가액으로는 사상 최대다.
이 글은 그 하루를 숫자로 정리한다. 무엇이 얼마나 올랐는지, 그 상승이 무엇을 근거로 했는지, 그리고 무엇이 아직 해결되지 않았는지.

1. 숫자 — 나스닥 +6.51%, 2025년 4월 8일 이후 최대
S&P 500은 326.78포인트(4.73%) 오른 7,237.17, 나스닥 종합지수는 1,471.82포인트(6.51%) 오른 24,089.56, 다우존스는 1,447.98포인트(3.01%) 오른 49,595.31에 마감했다. 나스닥100은 6.86% 올랐고, 이날 하루 시가총액이 2조 달러 넘게 늘었다. 러셀2000도 3.40% 올라 대형주만의 반등은 아니었다.
변동성은 빠르게 꺼졌다. VIX는 전일 35.89에서 26.62로 25.83% 내렸다. 다만 20을 크게 웃도는 수준이라, 공포가 사라진 것이 아니라 한 단계 낮아진 정도다.
업종은 필수소비재와 에너지만 내렸다. S&P 500 정보기술 업종은 9.03% 올랐고, 반도체 ETF(SMH)는 15.03%, 기술주 ETF(XLK)는 8.97% 상승했다. 필라델피아 반도체지수는 14.03% 뛴 9,588.05로 마감했다.
주목할 것은 금리다. 미 10년물 국채 금리는 4.918%로 전일(4.912%)과 거의 같았다. 위험자산이 급등하는 날 채권 금리가 움직이지 않았다는 뜻은, 이 상승이 "금리 인하 기대"가 아니라 "AI 리스크 프리미엄 축소"로 설명된다는 것이다. 로이터에 따르면 단기물(2년) 금리는 위험 선호가 살아나며 10bp 올라 4.72%를 기록했다.
원유는 반대로 움직였다. 서부텍사스산 원유(WTI)는 80.28달러로 4.41% 하락했다. 주식이 오르고 유가가 빠진 조합은, 이날 상승이 경기 기대가 아니라 AI 종목의 되돌림이었다는 점을 다시 확인시켜 준다.
엔비디아는 금요일 종가 125.53달러에서 165.05달러로 올랐다. 시가 167.04달러(전일 대비 +33%)로 갭 상승했고, 장중 171.50달러까지 찍은 뒤 종가는 시가보다 2달러 낮았다. 하루 7억7,600만 주가 거래됐다.

2. 무엇이 바뀌었나 — 11일 만의 복귀
젠슨 황은 11월 12일 엔비디아 CEO직에서 물러났다. 혼외 관계 보도 때문이었고, 그중 한 명이 중국 스파이 의혹을 받는 인물이었다. AP에 따르면 그는 며칠 뒤 복귀 의사를 밝혔지만 이사회는 거절했고, 이후 이사회는 그를 다시 영입하지 않겠다는 입장을 공개적으로 밝혔다.
11월 23일 이사회는 만장일치로 그를 사장·CEO·이사로 복귀시켰다. 성명에서 이사회는 "일련의 논의와 회의"를 거쳤고 "미국 정부 고위층의 의견(input)을 받았다", 그의 복귀가 "국가안보 위협이 되지 않는다"고 확신한다고 밝혔다. CNBC는 정부 고위 관계자들이 지난주 이사회에 "국가안보법 위반이 없다"고 브리핑한 것이 결정적이었다고 전했다.
트럼프 대통령은 CNBC '스쿼크 온 더 스트리트'에 나와 "내가 개입했다. 개입하지 않았다면 엔비디아는 오랫동안 슬펐을 것"이라고 말했고, "그는 중국 스파이 문제 등과 관련해 판단을 잘못했지만, 잘못한 것은 없다. 값으로 따질 수 없는 칩을 만들었을 뿐"이라고 덧붙였다. 트루스소셜에는 "정확하고 적절한 결정"이라고 적었다(로이터).
끝난 것은 아니다. 이사회가 선임한 독립위원회(법무법인 Wachtell, Lipton, Rosen & Katz)의 조사는 "끝까지 진행"된다. 캘리포니아 법무장관실은 이날 "그의 복귀가 엔비디아의 중국 관련 공시에 대한 조사 필요성을 줄이지 않는다"고 밝혔다(로이터). 로이터가 인용한 미 SEC의 회계처리 조사 보도도 그대로 남아 있다.
한국 시간으로 보면 이 순서다. 11월 12일 사임 → 11월 13일부터 20일까지 엔비디아 −27.7%(11월 11일 종가 173.73달러 → 11월 20일 125.53달러) → 11월 20일 3대 지수 조정 진입 → 11월 23일 개장 전 복귀 발표 → 같은 날 +31.48%.

3. 오늘의 화제 AI주 — 엔비디아·마이크론·코어위브·델
첫째, 엔비디아(NVDA) 165.05달러(+31.48%). 하루에 39.52달러가 올랐다. 시가총액은 4조100억 달러로 다시 4조 달러를 넘었다. 사임 전일(11월 11일) 종가 173.73달러의 95%까지 되돌린 셈이다. 다만 52주 최고가 243.37달러와 비교하면 여전히 32% 낮다.
둘째, 마이크론(MU) 707.70달러(+19.04%). 하루에 113.19달러 올랐다. 메모리 종목이 이날 상승을 주도했다. SK하이닉스 ADR +20.00%, 웨스턴디지털 +13.84%, 샌디스크 +10.69%가 함께 뛰었고, 미국 상장 메모리 ETF(DRAM)는 19% 넘게 올라 상장(2026년 4월) 이후 최대 일간 상승을 기록했다(CNBC). 마이크론은 11월 20일 하루에만 13.89% 빠졌던 종목이다. 씨티는 이날 마이크론 목표가 1,300달러를 유지했다.
셋째, 코어위브(CRWV) 48.33달러(+22.32%). 네오클라우드·서버·네트워킹 쪽이 함께 움직였다.
넷째, 델(DELL) 334.91달러(+20.46%). 오늘(11월 24일) 미국장 마감 후 실적을 발표한다. 시장에서는 AI 서버 수주잔고가 950억 달러 수준으로 전해지고 있다. 같은 날 서버 기업 HPE는 정규장에서 17.4% 올랐다가 시간외에서 6%대 하락했다. 마벨 +18.37%, 인텔 +16.34%, 슈퍼마이크로 +13.30%, 오라클 +12.34%도 함께 올랐다.
반대로 앤트로픽(ANT)은 87.64달러로 1.43% 내렸다. AI 랠리에서 유일하게 하락 마감한 대형 AI주다. 공모가 83달러 위에서 버티고는 있지만, 지난 19일 상장 이후 시장이 기대했던 2조 달러대 밸류에이션과는 거리가 있다. CNBC는 "대표적인 AI 주식이 오늘 오르지 못한다면 뭔가 잘못된 것"이라는 자산운용사 코멘트를 전했다.

4. 월가 리포트와 외신이 본 이날
가장 빠르게 움직인 것은 애널리스트 목표가다. CNBC에 따르면 멜리어스 리서치는 투자의견을 '보유'에서 '매수'로 올리고 목표가 220달러를 제시했다(금요일 종가 대비 75% 상승 여력). 번스타인도 '시장수익률'에서 '아웃퍼폼'으로 상향하며 목표가 200달러를 냈다. 스톤엑스는 목표가 270달러, 오펜하이머는 250달러, 씨티는 225달러에서 240달러로 올렸다. LSEG 집계로 65명의 애널리스트 중 48명이 엔비디아를 매수 이상으로 평가한다.
단서도 함께 붙었다. 번스타인의 스테이시 라스곤은 "젠슨의 복귀는 단기 성장에 대한 신뢰를 회복시킨다"면서도 "이번 사태가 남긴 물음과 오버행은 당분간 멀티플을 제한할 것"이라고 썼다. 멜리어스의 벤 라이치스는 "새 젠슨은 순환 거래, 네오클라우드 매출의 실체, 컴플라이언스, 승계 계획을 서둘러 설명해야 한다"고 지적했다.
블룸버그는 이번 일을 "기업 역사상 가장 놀라운 복귀 중 하나"로 표현했다. 로이터는 복귀가 "AI 생태계 전반에 안도"를 줬지만, 근본 질문은 남는다고 정리했다. 오션파크 자산운용의 제임스 세인트오빈은 "안도 랠리가 끝나면 매도가 다시 나올 수 있다. 젠슨의 복귀는 AI 설비투자의 수익성(ROI)에 대한 큰 질문에 답하지 않는다"고 말했다. 기업지배구조 전문가들 사이에서는 비판도 나왔다. 헨리경영대학원의 나다 카카바체 교수는 "11일 만의 두 번의 만장일치가 서로 반대 방향이었다. 둘 중 하나는 틀렸다"고 지적했고, 포춘은 경영대행사 임원의 "이사회의 무능을 광고한 셈"이라는 비판을 전했다.
시장 심리에 대한 판단도 갈린다. 바클레이즈의 베뉴 크리슈나는 "밸류에이션이 이미 상당한 악재를 반영하고 있다"며 매도가 과도했다는 쪽에 섰다. BTIG의 조너선 크린스키는 "7,250~7,350까지 단기 반등 후 다시 하락할 것"이라고 봤는데, 이날 S&P 500은 7,237.17에 마감해 그의 반등 목표 구간 하단에 걸쳐 있다. 모건스탠리 인베스트먼트 매니지먼트의 앤드루 슬리먼은 "반등이 끝났다고 보지 않는다. 이 수준에서 기술주 비중을 점진적으로 늘리기에 늦지 않았다"고 말했다(뉴스핌). 글로벌트 인베스트먼츠의 토머스 마틴은 "황이 엔비디아와 AI 거래에 독보적이라는 점이 오늘 입증됐다. 다만 나머지 문제가 어떻게 전개될지는 지켜봐야 한다"고 했다.
국내 증권사 시각도 참고할 만하다. KB증권 김민규 연구원은 11월 24일자 장마감코멘트에서 "연말은 높은 변동성 속에서 의미 있는 반등보다 더듬더듬 바닥을 찾아가는 장세"로 전망했다. 신한투자증권은 코스피 12개월 선행 PBR이 0.91배로 역사적 평균(1.04배)을 밑돈다고 짚었다. iM증권은 증안펀드가 실제 집행된 해가 1990·2003·2008년 세 차례뿐이라고 정리했고, 유안타증권은 지난주 나스닥 −10.02%를 'AI 트레이드 되돌림'으로 규정했다.

5. 오늘 아침 한국 시장 — 조건은 좋아졌고, 관문은 남았다
한국은 미국보다 하루 먼저 급락을 맞았다. 11월 23일 코스피는 3.31% 내린 4,708.54, 코스닥은 1.58% 내린 635.45에 마감했다. 코스피는 2거래일 연속 매도 사이드카가 발동됐고, 외국인은 7거래일 연속 순매도(−2,472억원)를 이어갔다. 삼성전자 17만7,500원(−3.06%), SK하이닉스 108만5,000원(−2.52%)이었다. 원·달러는 서울에서 1,345.9원에 마감했지만, 뉴욕 시간대에는 1,341원대까지 내려왔다.
오늘(11월 24일) 오전 9시 개장을 앞둔 조건은 간밤 뉴욕의 반등, 필라델피아 반도체지수 +14.03%, SK하이닉스 ADR +20.00%, 원·달러 1,341원대다. 지난주 내내 눌렸던 반도체 대형주에 갭 상승 출발 여지가 생긴 셈이지만, 방향은 개장 뒤 수급이 정한다.
남은 일정은 이렇다. 오늘(11월 24일) 미국장 마감 후 델 실적, 11월 25일 미국 3분기 GDP 잠정치와 10월 PCE 물가지수, 11월 26일 미국 휴장(추수감사절)과 한국은행 금융통화위원회, 11월 27일 블랙프라이데이. 12월 9일 브로드컴, 12월 17일 마이크론 실적이 AI 투자 수익성 논쟁의 다음 답이 될 전망이다.

한 줄 정리
이날 상승은 "실적이 좋아졌다"가 아니라 "가장 큰 불확실성 하나가 사라졌다"에 가깝다. 엔비디아 한 회사의 CEO 자리가 나스닥 6.5%를 움직였다는 사실 자체가, 지금 시장이 얼마나 좁은 곳에 기대 서 있는지를 보여준다. 지수가 사상 최고에서 4% 남짓 떨어진 자리로 돌아왔지만, 조사와 소송, 그리고 AI 설비투자의 수익성이라는 질문은 그대로다. 11월 25일 PCE와 12월 하이퍼스케일러들의 설비투자 가이던스가 다음 숫자가 될 것이다."""

EN_DESC = """On Friday, November 20, New York broke. The Nasdaq fell 5.28%, the S&P 500 3.70% and the Dow 1.93%, leaving all three in correction territory, with the Nasdaq 100 within a whisker of a bear market. Nvidia lost 14% in a day and dropped to the fourth-largest U.S. company. The weekend's question was whether the AI trade was over.

Three days later, on Monday, November 23, the answer was the opposite. Around 9 a.m., before the opening bell, Nvidia's board announced it had reinstated Jensen Huang as CEO, eleven days after he resigned. The Nasdaq closed up 6.51% at 24,089.56, the S&P 500 up 4.73% at 7,237.17 and the Dow up 3.01% at 49,595.31 — the best day for both the S&P 500 and the Nasdaq since April 8, 2025. Nvidia surged 31.48%, adding roughly $960 billion in market value in a single session to reach $4.01 trillion, the largest one-day gain in market capitalization any company has ever recorded.

1. The numbers: best day since April 8, 2025
The S&P 500 added 326.78 points (4.73%), the Nasdaq 1,471.82 points (6.51%) and the Dow 1,447.98 points (3.01%). The Nasdaq 100 rose 6.86% and gained more than $2 trillion in market value in one day. The Russell 2000 rose 3.40%, so this was not a megacap-only move.
Volatility collapsed: the VIX fell 25.83% from 35.89 to 26.62, still well above 20. Within the S&P 500 only energy and consumer staples fell; information technology rose 9.03%. The VanEck Semiconductor ETF (SMH) gained 15.03%, the Technology Select Sector SPDR (XLK) 8.97%, and the Philadelphia Semiconductor Index closed up 14.03% at 9,588.05.
The tell is in rates. The 10-year Treasury yield closed at 4.918%, essentially unchanged from 4.912% the day before. Risk assets ripped while long yields stood still, which points to a compression of the AI risk premium rather than a rate-cut rally. Reuters noted short-dated yields rose 10bp to 4.72% as risk appetite returned.
Oil moved the other way: WTI fell 4.41% to $80.28, a combination that underlines this was an AI-specific rebound rather than a growth rally.
Nvidia opened at $167.04, a 33% gap from Friday's $125.53 close, traded as high as $171.50 and settled at $165.05 — $2 below its open — on 776 million shares.

2. What changed: a return in eleven days
Huang stepped down on November 12 after reports of extramarital affairs, one of them with a woman suspected of spying for China. According to the AP he offered to return days later and the board declined, then publicly ruled out reinstatement.
On November 23 the board unanimously reinstated him as president, CEO and director. Its statement cited "a series of discussions and meetings," said it had "received input from senior levels of the United States government," and expressed confidence that his return "poses no national security risk." CNBC reported that senior government officials briefed the board late last week that no national security laws had been violated, which prompted the reversal.
President Trump told CNBC he had spoken with the board "directly and indirectly" and "convinced" them. "He did nothing wrong other than he created a chip that's invaluable," Trump said, calling the decision "correct and proper" on Truth Social.
It is not over. The independent committee the board formed, with law firm Wachtell, Lipton, Rosen & Katz, will "proceed to conclusion." California's attorney general said the reinstatement "does not diminish the need for a probe" into what Nvidia told investors about its China ties, and Reuters' report that the SEC is examining Nvidia's accounting still stands.
The sequence, in Korean time: resignation on November 12; a 27.7% decline from the November 11 close of $173.73 to $125.53 on November 20; all three indexes entering correction on November 20; reinstatement before the November 23 open; then +31.48% the same day.

3. The AI names that moved
Nvidia (NVDA) $165.05, +31.48%. It recovered 95% of its pre-resignation close of $173.73 but remains 32% below its 52-week high of $243.37, with a $4.01 trillion market cap.
Micron (MU) $707.70, +19.04%, up $113.19. Memory led: SK hynix's ADR rose 20.00%, Western Digital 13.84% and SanDisk 10.69%. The U.S.-listed Roundhill Memory ETF (DRAM) gained more than 19%, its best day since launching in April 2026, per CNBC. Micron had fallen 13.89% on Friday alone, and Citi kept its $1,300 target on the stock.
CoreWeave (CRWV) $48.33, +22.32%. Dell rose 20.46% to $334.91 ahead of its earnings after today's close, with AI server backlog reported around $95 billion; HPE gained 17.4% in the regular session before falling about 6% after hours. Marvell added 18.37%, Intel 16.34%, Super Micro 13.30% and Oracle 12.34%.
Anthropic (ANT) was the exception, down 1.43% to $87.64 — the only large AI name to close lower. It remains above its $83 IPO price but far from the $2 trillion valuation hoped for.

4. What Wall Street said
Analysts moved fast. Melius Research upgraded Nvidia to buy from hold with a $220 target (75% upside from Friday's close); Bernstein went to outperform from market perform with $200; StoneX set $270, Oppenheimer $250 and Citigroup raised its target to $240 from $225. LSEG data shows 48 of 65 analysts rate the stock a buy or strong buy.
The caveats came with the upgrades. Bernstein's Stacy Rasgon said the return restores near-term confidence but "will leave some overhangs in place that may limit NVDA's multiple for now." Melius's Ben Reitzes said the "new Jensen" should quickly address circular deals, how much revenue goes to neoclouds that ultimately serve China, compliance and a succession plan.
Bloomberg called it "one of the most startling corporate comebacks in history." Reuters captured the relief and the doubt: BakerAvenue's King Lip called the episode "one of those pieces of uncertainty" now removed, while Ocean Park's James St. Aubin warned that "we very well may see more selling pressure after this relief rally runs its course" and that the return "doesn't answer the big questions investors were grappling with" about AI returns. Governance experts were harsher: Nada Kakabadse of Henley Business School said two unanimous votes in eleven days pointing opposite ways means "one of them was wrong."
On direction, views split. Barclays' Venu Krishna thinks valuations already price in substantial adverse outcomes. BTIG's Jonathan Krinsky expects a short-term rally to 7,250-7,350 before turning lower again; the S&P closed at 7,237.17. Morgan Stanley Investment Management's Andrew Slimmon said it is not too late to add tech gradually, while Globalt's Thomas Martin said Huang's unique importance was proven but much remains unsettled.
Korean brokers remain cautious: KB Securities expects a year-end of high volatility and a slow search for a bottom rather than a meaningful rebound; Shinhan notes the KOSPI's 12-month forward PBR of 0.91x against a 1.04x historical average; iM Securities notes the stabilization fund has only actually been deployed in 1990, 2003 and 2008.

5. What it means for Seoul this morning
Korea took its hit a day earlier: the KOSPI closed at 4,708.54 (-3.31%) and the KOSDAQ at 635.45 (-1.58%) on November 23, with sell-side sidecars on two consecutive sessions and a seventh straight day of foreign net selling (-247.2 billion won). Samsung Electronics fell 3.06% to 177,500 won and SK hynix 2.52% to 1,085,000 won. The won closed at 1,345.9 per dollar in Seoul but traded near 1,341 overnight.
Ahead of the 9 a.m. open on November 24, the setup is friendlier: a 6.51% Nasdaq session, a 14.03% gain in the Philadelphia Semiconductor Index, SK hynix's ADR up 20% and the won near 1,341. What happens after the open depends on flows.
The calendar: Dell's earnings after today's close; U.S. Q3 GDP and October PCE on November 25; U.S. markets closed for Thanksgiving and the Bank of Korea decision on November 26; Black Friday on November 27; then Broadcom on December 9 and Micron on December 17.

Bottom line
This was not a day about better earnings. It was a day about one large uncertainty being removed, and the fact that one company's CEO seat moved the Nasdaq 6.5% shows how narrowly the market is standing. The investigations, the lawsuits and the question of returns on AI capex are all still open. October PCE on November 25 and hyperscaler capex guidance in December will be the next numbers that matter."""

JA_DESC = """11月20日金曜日、ニューヨークはAI売りに崩れた。ナスダック−5.28％、S&P500−3.70％、ダウ−1.93％。3指数そろって高値から10％以上下落して調整局面入りし、ナスダック100は弱気相場の入り口（高値比−20％）まで下げた。エヌビディアは1日で14％下落し、時価総額ランキングは4位に後退。週末の市場を覆った問いは「AI投資は終わったのか」だった。
3日後の11月23日月曜日、方向は正反対に反転した。ニューヨーク市場の寄り付き前、午前9時ごろ、エヌビディアの取締役会がジェンセン・フアンをCEOに復帰させると発表した。辞任から11日ぶりだった。ナスダックは6.51％高の24,089.56、S&P500は4.73％高の7,237.17、ダウは3.01％高の49,595.31で取引を終えた。S&P500とナスダックはいずれも2025年4月8日以来の大幅高。エヌビディアは31.48％急騰し、時価総額は1日で約9,600億ドル増えて4兆100億ドルになった。1社の1日当たり時価総額増加額としては史上最大である。
本稿はその1日を数字で整理する。

1. 数字 — ナスダック＋6.51％、2025年4月8日以来の大幅高
S&P500は326.78ポイント（4.73％）高の7,237.17、ナスダック総合は1,471.82ポイント（6.51％）高の24,089.56、ダウは1,447.98ポイント（3.01％）高の49,595.31。ナスダック100は6.86％上昇し、この日の時価総額増加は2兆ドルを超えた。ラッセル2000も3.40％高で、大型株だけの反発ではなかった。
変動性は急速にしぼんだ。VIXは前日35.89から26.62へ25.83％下落。ただし20を大きく上回る水準で、恐怖が消えたのではなく一段下がっただけだ。
業種別では生活必需品とエネルギーだけが下落。S&P500の情報技術セクターは9.03％高、半導体ETF（SMH）は15.03％、テックETF（XLK）は8.97％上昇した。フィラデルフィア半導体指数は14.03％高の9,588.05で引けた。
注目は金利だ。米10年債利回りは4.918％で前日（4.912％）とほぼ同じ。リスク資産が急騰した日に長期金利が動かなかったのは、この上昇が利下げ期待ではなく「AIリスクプレミアムの縮小」によるものだということを示す。ロイターによれば短期債（2年）利回りはリスク選好の回復で10bp上昇し4.72％。
原油は逆方向に動いた。WTIは80.28ドルへ4.41％下落。株高と原油安の組み合わせは、この上昇が景気期待ではなくAI銘柄の戻りであることを示す。
エヌビディアは金曜日終値125.53ドルから165.05ドルへ上昇。始値167.04ドル（前日比＋33％）でギャップアップし、取引中171.50ドルまで上げた後、終値は始値より2ドル低かった。出来高は7億7,600万株。

2. 何が変わったのか — 11日ぶりの復帰
フアン氏は11月12日、婚外関係の報道（うち1人は中国のスパイと疑われる人物）を受けてCEOを辞任した。AP通信によれば、数日後に復帰の意向を示したが取締役会は拒否し、その後、再登用しない方針を公表していた。
11月23日、取締役会は全会一致で彼を社長・CEO・取締役に復帰させた。声明では「一連の議論と会合」を経て「米国政府高官の意見（input）を得た」とし、復帰が「国家安全保障上の脅威にならない」と確信していると明らかにした。CNBCは、政府高官が先週取締役会に対し「国家安全保障法違反はない」と説明したことが決定的だったと伝えた。
トランプ大統領はCNBCの番組で「私が説得した。介入しなければエヌビディアは長く悲しむことになった」と述べ、「彼は婚外関係などで判断を誤ったが、違法行為はない。代価のつけられないチップを作っただけだ」と語った。トゥルース・ソーシャルには「正確かつ適切な決定」と投稿した（ロイター）。
終わったわけではない。取締役会が設置した独立委員会（法律事務所Wachtell, Lipton, Rosen & Katz）の調査は「最後まで続ける」としている。カリフォルニア州司法長官室は、復帰が「中国関連の開示に関する調査の必要性を減らすものではない」と述べた（ロイター）。SECがエヌビディアの会計処理を調べているというロイター報道も残っている。
韓国時間で並べると、11月12日辞任 → 11月13日〜20日にエヌビディア−27.7％（11月11日終値173.73ドル→11月20日125.53ドル）→ 11月20日に3指数が調整局面入り → 11月23日寄り付き前に復帰発表 → 同日＋31.48％。

3. 話題のAI銘柄 — エヌビディア・マイクロン・コアウィーブ
エヌビディア（NVDA）165.05ドル（＋31.48％）。時価総額は4兆100億ドルで再び4兆ドル台へ。辞任前日（11月11日）終値173.73ドルの95％まで戻したが、52週高値243.37ドル相比では依然32％低い。
マイクロン（MU）707.70ドル（＋19.04％）。この日はメモリが主導し、SKハイニックスADR＋20.00％、ウエスタンデジタル＋13.84％、サンディスク＋10.69％。米上場のメモリETF（DRAM）は19％超上昇し、2026年4月上場以来の最大の1日上昇（CNBC）。マイクロンは11月20日に13.89％下落した銘柄だ。
コアウィーブ（CRWV）48.33ドル（＋22.32％）。デルは＋20.46％の334.91ドル。本日（11月24日）の米国市場引け後に決算を発表する予定で、AIサーバーの受注残は950億ドル規模と伝わる。HPEは通常取引で17.4％上昇した後、時間外で6％台下落した。マーベル＋18.37％、インテル＋16.34％、スーパーマイクロ＋13.30％、オラクル＋12.34％も上昇した。
一方、アントロピック（ANT）は87.64ドルで1.43％安。AIラリーで唯一下落した大型AI株だ。公開価格83ドルは上回っているが、市場が期待した2兆ドル台の評価には遠い。

4. ウォール街の見方
アナリストは素早く動いた。メリウス・リサーチは投資判断を「保有」から「買い」に引き上げ目標株価220ドル（金曜日終値比75％上昇余地）。バーンスタインも「アウトパフォーム」に格上げし200ドル。ストーンエックス270ドル、オッペンハイマー250ドル、シティは225ドルから240ドルへ引き上げた。LSEG集計では65人中48人が買い以上と評価する。
ただし留保も付く。バーンスタインのステイシー・ラスゴンは「短期的な成長への信頼は回復する」としつつ「今回の騒動が残した懸念は当面バリュエーションを制限する」と書いた。メリウスのベン・ライツェスは「新しいフアンは循環取引、ネオクラウド向け売上の実態、コンプライアンス、後継者計画を早急に説明すべきだ」と指摘した。
ブルームバーグは「企業史上最も驚くべき復帰の一つ」と表現。ロイターは安堵と疑問の両方を伝えた。オーシャンパーク・アセット・マネジメントのジェームズ・セントオービンは「安堵ラリーが終われば売りが再び出る可能性がある。フアンの復帰はAI設備投資の収益性という大きな問いに答えてはいない」と述べた。ガバナンス専門家からは批判も出た。ヘンリー・ビジネススクールのナダ・カカバッツェ教授は「11日間の2度の全会一致が正反対を向いた。どちらかは間違っていた」と指摘した。
方向感は分かれる。バークレイズのベヌ・クリシュナはバリュエーションがすでに悪材料を相当織り込んでいるとみる。BTIGのジョナサン・クリンスキーは「7,250〜7,350まで短期反発した後、再び下げる」と予想した（この日のS&P500終値は7,237.17）。モルガン・スタンレー・インベストメント・マネジメントのアンドリュー・スリモンは「この水準でハイテク比率を段階的に増やすのに遅くない」と述べた。
韓国証券会社は慎重だ。KB証券は「年末は高い変動性のなか、意味のある反発よりも底を探る展開」と展望し、新韓投資証券はコスピの12カ月先PBRが0.91倍で歴史的平均1.04倍を下回ると指摘。iM証券は安定化ファンドが実際に執行されたのは1990・2003・2008年の3回だけだと整理した。

5. 今朝のソウル市場
韓国は米国より1日早く急落した。11月23日のコスピは3.31％安の4,708.54、コスダックは1.58％安の635.45。コスピは2営業日連続で売りサイドカーが発動し、外国人は7営業日連続の売り越し（−2,472億ウォン）。サムスン電子は3.06％安の17万7,500ウォン、SKハイニックスは2.52％安の108万5,000ウォン。ウォンはソウルで1,345.9ウォン、ニューヨーク時間帯には1,341ウォン台まで下がった。
11月24日午前9時の寄り付き前の条件は改善している。ナスダック＋6.51％、フィラデルフィア半導体指数＋14.03％、SKハイニックスADR＋20.00％、ウォン1,341ウォン台。ただし方向は寄り付き後の需給が決める。
日程は、本日（11月24日）米国市場引け後にデルの決算、11月25日に米3Q GDP速報値と10月PCE、11月26日に米国休場（感謝祭）と韓国銀行金融通貨委員会、11月27日にブラックフライデー。12月9日のブロードコム、12月17日のマイクロンの決算がAI投資収益性議論の次の答えになる。

まとめ
この日の上昇は「業績が良くなった」ではなく「最大の不確実性が一つ消えた」に近い。1社のCEOの座がナスダックを6.5％動かしたという事実そのものが、今の市場がどれほど狭い場所に立っているかを示す。調査も訴訟も、AI設備投資の収益性という問いも残ったままだ。11月25日のPCEと12月のハイパースケーラーの設備投資ガイダンスが次の数字になる。"""

ZH_DESC = """11月20日周五，纽约因AI抛售而崩跌。纳斯达克−5.28%、标普500−3.70%、道指−1.93%，三大指数全部进入调整区间，纳斯达克100距熊市门槛（较峰值−20%）仅一步之遥。英伟达单日下跌14%，市值排名跌至第四。整个周末市场都在问："AI交易结束了吗？"

三天后的11月23日周一，方向彻底反转。开盘前的上午9时许，英伟达董事会宣布让黄仁勋回归担任CEO——距其辞职仅11天。纳斯达克收涨6.51%至24,089.56点，标普500涨4.73%至7,237.17点，道指涨3.01%至49,595.31点，标普500与纳斯达克均创2025年4月8日以来最大单日涨幅。英伟达暴涨31.48%，单日市值增加约9,600亿美元至4.01万亿美元，创下任何公司单日市值增幅的历史最高纪录。

1. 数字：2025年4月8日以来最大单日涨幅
标普500上涨326.78点（4.73%），纳斯达克上涨1,471.82点（6.51%），道指上涨1,447.98点（3.01%）。纳斯达克100上涨6.86%，单日市值增加逾2万亿美元。罗素2000也上涨3.40%，说明并非只有超大盘股反弹。
波动率迅速回落：VIX从35.89降至26.62，跌25.83%，但仍远高于20。标普500中仅能源与必需消费品下跌，信息技术板块上涨9.03%；半导体ETF（SMH）涨15.03%，科技ETF（XLK）涨8.97%，费城半导体指数涨14.03%收于9,588.05点。
关键线索在利率：美国10年期国债收益率收于4.918%，与前一日（4.912%）几乎持平。风险资产暴涨而长端利率不动，说明这轮上涨不是"降息预期"，而是"AI风险溢价收缩"。据路透社，短端（2年期）收益率因风险偏好回升上升10个基点至4.72%。
英伟达从周五收盘125.53美元涨至165.05美元，开盘跳空至167.04美元（+33%），盘中最高171.50美元，收盘较开盘低2美元，成交7.76亿股。

2. 什么变了：11天后的回归
黄仁勋于11月12日辞去CEO职务，此前有报道称其存在多段婚外关系，其中一人被怀疑为中国间谍。据美联社，他数日后提出回归意愿，但董事会拒绝，并公开表示不会让其复职。
11月23日，董事会一致决定恢复其总裁、CEO及董事职务。声明称经过"一系列讨论与会议"，并"听取了美国政府高层意见"，确信其回归"不构成国家安全威胁"。据CNBC，政府高级官员上周向董事会通报"未违反国家安全法"，成为转折点。
特朗普对CNBC表示，他与董事会"直接和间接"沟通并"说服"了他们，称黄"没有做错任何事，只是造出了无价的芯片"，并在Truth Social上称这是"正确而恰当的决定"（路透社）。
事情并未结束。董事会设立的独立委员会（律师事务所Wachtell, Lipton, Rosen & Katz）的调查将"进行到底"。加州总检察长办公室表示，复职"并不减少就英伟达对华业务披露展开调查的必要性"。路透社关于SEC调查英伟达会计处理的报道依然有效。
按韩国时间排列：11月12日辞职 → 11月13日至20日英伟达−27.7%（11月11日收盘173.73美元→11月20日125.53美元）→ 11月20日三大指数进入调整 → 11月23日盘前宣布回归 → 当日+31.48%。

3. 今日焦点AI个股
英伟达（NVDA）165.05美元，+31.48%，市值4.01万亿美元，重回4万亿关口；已收复辞职前一日（11月11日）收盘173.73美元的95%，但仍较52周高点243.37美元低32%。
美光（MU）707.70美元，+19.04%，单日上涨113.19美元。内存板块领涨：SK海力士ADR+20.00%、西部数据+13.84%、闪迪+10.69%；美国上市的内存ETF（DRAM）涨超19%，为2026年4月上市以来最大单日涨幅（CNBC）。美光11月20日单日曾下跌13.89%。
CoreWeave（CRWV）48.33美元，+22.32%；戴尔+20.46%至334.91美元，将于今日（11月24日）美股盘后发布财报，市场传其AI服务器在手订单约950亿美元；HPE常规交易时段上涨17.4%，盘后回落6%左右。迈威尔+18.37%、英特尔+16.34%、超微电脑+13.30%、甲骨文+12.34%。
相反，Anthropic（ANT）收跌1.43%至87.64美元，是AI行情中唯一收跌的大型AI股。虽仍高于83美元发行价，但距离市场期待的2万亿美元估值仍远。

4. 华尔街怎么说
分析师动作迅速：Melius Research将评级从"持有"上调至"买入"，目标价220美元（较周五收盘有75%空间）；伯恩斯坦上调至"跑赢大盘"，目标价200美元；StoneX给出270美元，奥本海默250美元，花旗从225美元上调至240美元。LSEG数据显示65位分析师中有48位给予买入或强力买入。
但附带了保留意见。伯恩斯坦的Stacy Rasgon表示回归恢复了对近期增长的信心，但"这整件事留下的疑问将在短期内限制估值"。Melius的Ben Reitzes称"新黄仁勋"应尽快说明循环交易、面向最终服务中国的neocloud的真实销售额、合规与继任计划。
彭博社称之为"企业史上最令人震惊的回归之一"。路透社同时记录了宽慰与疑虑：Ocean Park的James St. Aubin警告"宽慰性反弹结束后可能还会有抛压"，且回归"并未回答投资者关于AI投资回报的核心问题"。治理专家批评更直接：亨利商学院教授Nada Kakabadse称"11天内两次一致表决方向相反，其中一次必然是错的"。
方向判断分歧明显。巴克莱的Venu Krishna认为估值已计入大量负面情形；BTIG的Jonathan Krinsky预计短线反弹至7,250–7,350后再度回落（标普500当日收于7,237.17）；摩根士丹利投资管理的Andrew Slimmon认为现在逐步加仓科技股并不算晚。
韩国券商依旧谨慎：KB证券预计年末将在高波动中"逐步寻找底部"而非有意义的反弹；新韩投资证券指出KOSPI 12个月远期PBR为0.91倍，低于历史均值1.04倍；iM证券指出稳定基金历史上仅在1990、2003、2008年三次实际执行。

5. 今晨首尔市场
韩国比美国早一天下跌：11月23日KOSPI收于4,708.54（−3.31%），科斯达克635.45（−1.58%），连续两个交易日触发卖出熔断，外资连续7个交易日净卖出（−2,472亿韩元）。三星电子跌3.06%至177,500韩元，SK海力士跌2.52%至1,085,000韩元。韩元在首尔收于1,345.9，纽约时段跌至1,341附近。
11月24日上午9时开盘前条件改善：纳斯达克+6.51%、费城半导体指数+14.03%、SK海力士ADR+20.00%、韩元1,341附近。但方向仍取决于开盘后的资金流。
日程：今日（11月24日）美股盘后戴尔财报；11月25日美国三季度GDP初值与10月PCE；11月26日美国休市（感恩节）与韩国银行金融货币委员会；11月27日黑色星期五；此后12月9日博通、12月17日美光财报。

一句话总结
这天的上涨不是"业绩变好"，而是"最大的不确定性之一消失"。一家公司的CEO之位能推动纳斯达克6.5%，正说明当前市场站得有多窄。调查、诉讼以及AI资本开支回报的问题都还在。11月25日的PCE与12月超大规模云厂商的资本开支指引，将是下一组关键数字。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "postType": "report",
    "store": "K-Trend Market",
    "priceKrw": 0,
    "releaseDate": "2026-11-24",
    "rating": 5,
    "imageUrl": C,
    "images": [G1, G2, G3, G4],
    "affiliateUrl": "https://stock.naver.com/",
    "affiliatePlatform": "Coupang",
    "i18n": {
        "ko": {
            "title": "하루에 9,600억 달러…젠슨 황 복귀가 만든 나스닥 +6.51%를 숫자로 뜯었다",
            "summary": "나스닥 24,089.56(+6.51%), S&P 500 7,237.17(+4.73%). 엔비디아 CEO 복귀 발표 하나로 금요일의 투매를 하루에 되돌렸습니다. 지수·종목·리포트 숫자와 아직 남은 조사 리스크를 정리했습니다.",
            "description": KO_DESC,
            "tasteReview": [
                "나스닥 +6.51%·S&P 500 +4.73%로 2025년 4월 8일 이후 최대 일간 상승, VIX는 35.89 → 26.62",
                "엔비디아 +31.48%(165.05달러), 시총 하루 +9,600억 달러로 4조100억 달러 — 단일 기업 사상 최대",
                "마이크론 +19.04%·코어위브 +22.32%, 반면 앤트로픽은 −1.43%로 홀로 하락",
                "이사회 조사·캘리포니아 법무장관 조사는 그대로, 11/25 미국 PCE가 다음 관문",
            ],
            "tips": "본 글은 공개된 시세·보도·리포트를 정리한 정보 기록이며, 특정 종목의 매수·매도를 권유하지 않습니다.",
        },
        "en": {
            "title": "One Day, $960 Billion: How Jensen Huang's Return Lifted the Nasdaq 6.51%",
            "summary": "Nasdaq 24,089.56 (+6.51%), S&P 500 7,237.17 (+4.73%). A single board decision undid Friday's rout in one session. The numbers, the analysts, and the investigations that are still open.",
            "description": EN_DESC,
            "tasteReview": [
                "Best day for the S&P 500 and Nasdaq since April 8, 2025; VIX fell from 35.89 to 26.62",
                "Nvidia +31.48% to $165.05, adding about $960bn in a day to a $4.01tn market cap — the largest single-day gain ever",
                "Micron +19.04%, CoreWeave +22.32%, while Anthropic was the only large AI name to close lower (-1.43%)",
                "The board's independent review and California's probe continue; U.S. PCE on Nov 25 is the next test",
            ],
            "tips": "This is a summary of public market data, reporting and broker research, not investment advice.",
        },
        "ja": {
            "title": "1日で9,600億ドル…ジェンセン・フアン復帰が作ったナスダック＋6.51％を数字で解体",
            "summary": "ナスダック24,089.56（＋6.51％）、S&P500 7,237.17（＋4.73％）。エヌビディアCEO復帰の一報が金曜日の投げ売りを1日で取り戻しました。指数・銘柄・リポートの数字と、残された調査リスクを整理します。",
            "description": JA_DESC,
            "tasteReview": [
                "ナスダック＋6.51％・S&P500＋4.73％で2025年4月8日以来の大幅高、VIXは35.89→26.62",
                "エヌビディア＋31.48％（165.05ドル）、時価総額は1日で約9,600億ドル増の4兆100億ドル — 1社として史上最大",
                "マイクロン＋19.04％・コアウィーブ＋22.32％、一方アントロピックは−1.43％で唯一の下落",
                "取締役会の独立調査とカリフォルニア州司法長官の調査は継続、11/25の米PCEが次の関門",
            ],
            "tips": "本記事は公開された相場データ・報道・リポートの整理であり、個別銘柄の売買を推奨するものではありません。",
        },
        "zh": {
            "title": "一天9,600亿美元：黄仁勋回归如何把纳斯达克推高6.51%",
            "summary": "纳斯达克24,089.56（+6.51%）、标普500 7,237.17（+4.73%）。一项董事会决定在一个交易日内抹平了周五的抛售。指数、个股、研报数字，以及仍未结束的调查风险。",
            "description": ZH_DESC,
            "tasteReview": [
                "纳斯达克+6.51%、标普500+4.73%，创2025年4月8日以来最大单日涨幅；VIX从35.89降至26.62",
                "英伟达+31.48%至165.05美元，单日市值增加约9,600亿美元至4.01万亿美元，创单一公司历史纪录",
                "美光+19.04%、CoreWeave+22.32%，而Anthropic是唯一收跌的大型AI股（−1.43%）",
                "董事会独立调查与加州总检察长调查仍在进行，11月25日美国PCE是下一道关口",
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
