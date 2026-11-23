#!/usr/bin/env python3
"""2026-11-23 증시 심층 리포트 (4개국어) → Supabase posts + ISR revalidate.

모든 수치는 2026-11-23 17:00 KST 기준으로 확인한 값:
 - 국내: 한국거래소 마감(연합뉴스·뉴스핌·서울경제), 네이버 금융 화면
 - 미장: 2026-11-20(금) 마감(연합뉴스·한국경제·뉴스1·KB증권 리포트)
 - 리포트: 네이버 금융 리서치 2026-11-23 발행분(신한·유안타·iM·대신·KB·유진)
 - 해외 IB: 블룸버그 보도(골드만삭스 패닉지수·CTA), 아시아경제(야데니)
"""

import json
import urllib.request
from urllib.parse import quote

SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJvbGUiOiJzZXJ2aWNlX3JvbGUiLCJpYXQiOjE3OTQzMDgwNzcsImV4cCI6MjEwOTg4NDA3N30.ELyAmyRJrWdQoIHRu4thMGvjAnjJfVZ4S8Cfpb9MiDY"
REVALIDATE_URL = "https://www.k-trand.store/api/revalidate?secret=kblog2026"
SLUG = "kospi-4700-line-ai-bubble-market-report-2026-11-23"

C = "/images/products/market-kospi-cover-2026-11-23.png"
G1 = "/images/products/market-kospi-numbers-2026-11-23.png"
G2 = "/images/products/market-kospi-reports-2026-11-23.png"
G3 = "/images/products/market-us-close-2026-11-23.png"

KO_DESC = """검은 금요일 다음에 온 월요일도 검었다. 코스피는 장중 4,586.80까지 밀리며 5.8% 넘게 빠졌고, 오전 11시 33분에는 2거래일 연속 매도 사이드카가 발동됐다. 종가 기준 1월 13일(4,692.64) 이후 가장 낮은 자리다. 그런데 오후에는 분위기가 달라졌다. 정부가 증안펀드 가동 준비에 착수했다는 소식과 금융위의 자사주 매입 한도 완화 결정이 나오자 낙폭을 절반 가까이 되돌렸다. 4,700선은 지켰다. 숫자를 순서대로 뜯어보면, 이 하루가 'AI 투자'라는 하나의 이야기에 얼마나 쏠려 있던 시장인지가 보인다.

1. 오늘의 숫자 — 코스피 4,708.54(−3.31%), 코스닥은 2년 만의 최저
코스피는 전 거래일보다 161.42포인트(3.31%) 내린 4,708.54에 마감했다. 시가 4,734.90으로 2.77% 갭 하락 출발한 뒤 4,700선과 4,600선을 차례로 내줬고, 장중 저점은 4,586.80이었다. 코스닥은 10.23포인트(1.58%) 내린 635.45로 2024년 12월 9일 이후 가장 낮은 종가를 기록했고, 장중에는 618.74까지 밀렸다. 코스피200은 730.83(−3.24%)이다.
수급은 외국인 −2,472억원(7거래일 연속 매도), 개인 −3,669억원, 기관 +1,872억원. 지난 6거래일 하루 평균 순매도가 7,851억원이었던 것과 비교하면 외국인 매도 강도는 오히려 줄었다. 코스닥도 기관만 +1,975억원을 사고 외국인 −354억원, 개인 −1,740억원으로 팔았다. 거래대금은 유가증권 15조3,216억원, 코스닥 4조3,539억원.
업종은 전부 내렸다. 건설 −6.91%, 보험 −5.12%, 제약 −4.89%, 운송·창고 −4.73%가 낙폭 상위다. 상승 종목은 71개, 하락 종목은 824개. 삼성전자 17만7,500원(−3.06%), SK하이닉스 108만5,000원(−2.52%), 삼성바이오로직스 −4.94%, KB금융 −5.71%, 현대차 −2.94%가 밀렸고, SK스퀘어(+0.44%)와 삼성전기(+0.52%)는 장중 방향을 바꿔 올랐다. 원·달러 환율은 9.7원 오른 1,345.9원(오후 3시30분 기준). 장중 1,351.6원까지 올라 2주 만에 1,350원대를 터치했다.

2. 왜 이렇게 빠졌나 — 한 주에 몰아친 다섯 가지 악재
첫째, 엔비디아 회계처리에 대한 미국 증권거래위원회(SEC) 조사 보도다. 로이터가 사안에 정통한 관계자 두 명을 인용해 전하면서, 보도 전 6%대 하락하던 엔비디아는 장중 14%까지 밀렸다. 둘째, AMD의 대중국 수출통제 위반 의혹(공매도 보고서 제기, 회사는 부인). 셋째, 구글의 2027년 TPU 8i 출하 계획 축소 전망에 따른 브로드컴 수요 둔화 우려. 넷째, 트럼프 대통령의 "미국 기업이 해외에 데이터센터를 지으면 큰 세금을 물리겠다"는 발언과, 리사 쿡 연준 이사의 매파 발언(12월 25bp 인상 확률이 94%까지 반영됐다). 다섯째, 역대 최대 IPO라는 앤트로픽 상장이 오히려 시장 자금을 빨아들이며 기존 AI주에서 차익실현을 유발한 점이다.
앤트로픽(ANT)은 공모가 83달러로 상장 첫날 17.1% 올랐지만, 이틀째인 20일 8.50% 내린 88.91달러에 마감하며 장중 공모가(83달러)까지 밀렸다. 총조달액 1,195억달러(약 161조원), 상장 첫날 시가총액 1조2,700억달러. 시장이 기대했던 2조달러와는 거리가 있었다.

3. 직전 미국장 — S&P 500 7거래일 연속 하락, VIX 35.89
11월 20일 뉴욕에서 S&P 500은 3.70% 내린 6,910.39, 나스닥은 5.28% 내린 22,617.73, 다우는 1.93% 내린 48,147.33에 마감했다. S&P 500은 2020년 2월 이후 가장 긴 7거래일 연속 하락이었고, 나스닥은 올해 상승분을 전부 반납했다(연초 이후 −2.69%). 주간 기준으로는 나스닥 −10.0%, S&P 500 −8.6%, 다우 −8.0%로 2025년 4월 관세 쇼크 이후 최대 낙폭이다. 필라델피아 반도체지수는 10.73% 폭락했고, VIX는 26.20% 급등한 35.89로 2025년 4월 이후 최고치를 찍었다. 미 10년물 금리는 4.909%로 14bp 내렸고, 비트코인은 장중 6만달러를 아래로 이탈했다가 6만1,000달러대를 회복 중이다.
개별 종목은 반도체가 전부 두 자릿수로 무너졌다. 엔비디아 −14.01%(125.53달러, 10월 6일 고점 대비 −48%, 시가총액 4위로 추락), AMD −13.25%, 마이크론 −13.89%, 브로드컴 −12.19%, 샌디스크 −16.05%, SK하이닉스 ADR −13.11%. 빅테크도 예외는 아니었다. 마이크로소프트 −2.77%, 알파벳 −2.70%, 아마존 −4.10%, 메타 −5.93%, 테슬라 −7.64%, 팔란티어 −6.63%, 오라클 −8.48%다. 반대로 월마트(+1.52%), 코스트코(+0.75%), 존슨앤드존슨(+1.28%) 같은 방어주로는 돈이 옮겨 갔다.
참고로 23일 오후 5시15분 현재 미국 선물은 S&P 500 +2.2%, 나스닥 +2.9%로 반등 출발했다. 낙폭이 컸던 만큼 저가 매수세가 먼저 움직이는 모습이다.

4. 오늘 발행된 리포트가 가리키는 숫자
신한투자증권은 「마켓레이더 — 증안펀드 카드에도 싸늘, 정책과 시장의 온도 차(11월 23일)」에서 코스피 12개월 선행 PBR이 0.91배로 역사적 평균 1.04배를 밑돈다고 짚었다. 유안타증권 「AI 미국 주식시장 주간 시황」은 나스닥 주간 −10.02%를 'AI 트레이드 되돌림'으로 규정하고, 이번 주 키워드로 AI 버블 논쟁·광범위한 디레버리징·PCE를 꼽았다. iM증권 「Market Time」은 증안펀드가 실제로 집행된 해가 1990·2003·2008년 세 차례뿐이며 2020·2022년은 자금 조성에 그쳤다고 정리했다. 대신증권 이경민 연구원은 "고점 대비 약 50% 하락으로 1997년 외환위기, 2008년 금융위기, 닷컴버블 이후 가장 큰 충격"이라며 "이미 언더슈팅 국면에 진입한 만큼 추가 하락 폭은 제한되며 4,700선은 지켰다"고 평가했다. KB증권은 금리선물 시장이 12월 동결 확률을 8.6%로 반영하고 있다고 전했다.
해외는 더 직접적이다. 블룸버그에 따르면 골드만삭스의 '패닉 지수'는 10점 만점에 9점까지 올랐고, 추세 추종형(CTA) 투자자들은 최근 한 달간 570억달러를 순매도한 데 이어 주가가 현 수준에 머물러도 658억달러, 하락이 이어지면 최대 806억달러를 더 팔 수 있다. 야데니리서치는 S&P 500 연말 목표를 7,900에서 7,500으로 낮추면서도, 내년 말 8,500~9,000을 제시하며 "장기 약세장 가능성은 낮다"고 봤다.

5. 지금 봐야 할 세 가지
첫째, 11월 25일 미국 3분기 GDP 잠정치와 10월 PCE 물가지수. 리사 쿡 이사의 발언대로 물가가 내려오지 않으면 12월 인상이 기정사실화되고, 그 순간 AI 인프라 투자의 자금 조달 비용이 다시 뛴다. 둘째, 11월 26일 금통위와 미국 휴장(추수감사절) 구간의 수급 공백. 환율이 1,350원을 넘어서면 외국인 이탈 압력이 커지는 구조다. 셋째, 증안펀드가 '준비'에서 '실제 집행'으로 넘어가는지 여부와 외국인 순매도 규모의 축소. 오늘 외국인 매도가 직전 6거래일 평균의 3분의 1 수준으로 줄어든 점은 긍정적이지만, 7거래일 연속 매도라는 방향은 아직 바뀌지 않았다.
한 줄로 정리하면 이렇다. 지수는 4,700선을 지켰고 밸류에이션은 역사적 하단에 가까워졌지만, 하락의 원인이 'AI 투자 수익성'이라는 구조적 질문인 만큼 단기 반등과 추세 전환은 다른 문제다. 다음 실적 시즌의 하이퍼스케일러 설비투자 가이던스가 이 질문에 대한 첫 답이 될 것이다."""

EN_DESC = """Monday in Seoul was as dark as the Friday before it. The KOSPI fell as much as 5.8% intraday to 4,586.80, triggering a second straight sell-side circuit breaker at 11:33 a.m., and closed at its lowest level since January 13. Then the afternoon changed the mood: news that the government had begun preparations to deploy the market stabilization fund, plus a decision to relax daily share buyback limits, pulled the index back above 4,700. Here is what the numbers actually say.

1. Today's numbers: KOSPI 4,708.54 (-3.31%), KOSDAQ at a two-year low
The KOSPI closed at 4,708.54, down 161.42 points (3.31%), after opening 2.77% lower at 4,734.90 and giving up the 4,700 and then 4,600 lines. The intraday low was 4,586.80. The KOSDAQ lost 1.58% to 635.45, its lowest close since December 9, 2024, and touched 618.74 during the session. The KOSPI 200 finished at 730.83 (-3.24%).
Foreign investors sold a net 247.2 billion won, a seventh straight session of selling, while retail sold 366.9 billion won and institutions bought 187.2 billion won. That foreign outflow is actually smaller than the 785.1 billion won daily average of the previous six sessions. Trading value was 15.32 trillion won on the main board and 4.35 trillion won on the KOSDAQ. Every sector fell: construction -6.91%, insurance -5.12%, pharmaceuticals -4.89%, transport and warehousing -4.73%. Only 71 stocks rose against 824 decliners. Samsung Electronics fell 3.06% to 177,500 won and SK hynix 2.52% to 1,085,000 won. The won weakened 9.7 to 1,345.9 per dollar, touching 1,351.6 intraday for the first time in two weeks.

2. Why it broke: five shocks in one week
First, a Reuters report that the U.S. SEC is examining Nvidia's accounting pushed the stock from a 6% loss to a 14% collapse. Second, allegations that AMD violated China export controls, which the company denies. Third, expectations that Google will cut 2027 TPU 8i shipments, feeding demand concerns for Broadcom. Fourth, President Trump's threat to tax U.S. companies heavily for building data centers abroad, alongside Fed Governor Lisa Cook's hawkish comments; futures now price a 94% chance of a 25bp December hike. Fifth, Anthropic's record IPO, which drained liquidity and triggered profit-taking in existing AI names. ANT closed its second session at $88.91 (-8.50%) after pricing at $83 and popping 17.1% on day one; it raised $119.5 billion in total and was valued at $1.27 trillion, well short of the $2 trillion some had expected.

3. The U.S. session before: S&P 500 down seven days straight, VIX at 35.89
On November 20 the S&P 500 lost 3.70% to 6,910.39, the Nasdaq 5.28% to 22,617.73 and the Dow 1.93% to 48,147.33. It was the S&P's longest losing streak since February 2020, and the Nasdaq erased its entire 2026 gain (now -2.69% year to date). Weekly losses were 10.0% for the Nasdaq and 8.6% for the S&P 500, the worst since the April 2025 tariff shock. The Philadelphia Semiconductor Index fell 10.73% and the VIX jumped 26.20% to 35.89, its highest since April 2025. The 10-year Treasury yield dropped 14bp to 4.909%.
Semiconductors were hit across the board: Nvidia -14.01% ($125.53, down 48% from its October 6 peak and now the fourth-largest U.S. company), AMD -13.25%, Micron -13.89%, Broadcom -12.19%, SanDisk -16.05%, SK hynix ADR -13.11%. Big tech fell too: Microsoft -2.77%, Alphabet -2.70%, Amazon -4.10%, Meta -5.93%, Tesla -7.64%, Palantir -6.63%, Oracle -8.48%. Money moved into defensives such as Walmart (+1.52%), Costco (+0.75%) and Johnson & Johnson (+1.28%). By 5:15 p.m. KST on November 23, S&P 500 futures were up 2.2% and Nasdaq futures 2.9%.

4. What the research says
Shinhan Investment's market note points out that the KOSPI's 12-month forward PBR is 0.91x versus a historical average of 1.04x. Yuanta describes the week as an "AI trade unwind" with the Nasdaq down 10.02%, and lists AI bubble debate, broad deleveraging and PCE as this week's keywords. iM Securities notes that the stabilization fund has only been deployed three times, in 1990, 2003 and 2008. Daishin's Lee Kyung-min calls the market oversold after a roughly 50% drop from its peak. KB Securities notes futures pricing only an 8.6% chance of a December hold.
Overseas, Goldman Sachs' panic index hit 9 out of 10 and its CTA model sees up to $80.6 billion of additional selling if the decline continues, after $57 billion of trend-following sales in the past month. Yardeni Research cut its S&P 500 year-end target to 7,500 from 7,900 but still sees 8,500-9,000 by the end of next year.

5. Three things to watch
U.S. Q3 GDP and October PCE on November 25 decide whether a December hike is locked in. The Bank of Korea meeting on November 26 and the U.S. Thanksgiving holiday create a liquidity gap, and a won above 1,350 adds pressure on foreign flows. Finally, watch whether the stabilization fund moves from preparation to actual buying, and whether the foreign selling streak ends."""

JA_DESC = """金曜日の「黒い一日」の次に来た月曜日もまた黒かった。コスピは取引中に4,586.80まで下落して5.8％を超える下げとなり、午前11時33分には2営業日連続で売りサイドカーが発動した。終値ベースでは1月13日以来の安値。しかし午後、政府が証券市場安定ファンド（証安ファンド）の稼動準備に着手し、金融委員会が自社株買いの1日当たり上限を緩和すると発表すると、下げ幅はほぼ半分まで戻り、4,700線は守られた。数字を順に追うと、この一日が「AI投資」という一つの物語にどれだけ偏っていたかが見えてくる。

1. 今日の数字 — コスピ4,708.54（−3.31％）、コスダックは2年ぶり安値
コスピは前日比161.42ポイント（3.31％）安の4,708.54で引けた。4,734.90と2.77％のギャップ安で寄り付き、4,700線と4,600線を順に割り込み、安値は4,586.80。コスダックは1.58％安の635.45で、2024年12月9日以来の安値終値となり、取引中には618.74まで下げた。コスピ200は730.83（−3.24％）。
需給は外国人−2,472億ウォン（7営業日連続売り越し）、個人−3,669億ウォン、機関+1,872億ウォン。直前6営業日の1日平均売り越し7,851億ウォンと比べると、外国人の売り圧力はむしろ弱まった。全業種が下落し、建設−6.91％、保険−5.12％、製薬−4.89％、運輸・倉庫−4.73％。上昇71銘柄に対し下落824銘柄。サムスン電子−3.06％、SKハイニックス−2.52％、サムスンバイオロジクス−4.94％、KB金融−5.71％、現代自動車−2.94％。ウォン・ドル相場は9.7ウォン高の1,345.9ウォン、取引中には1,351.6ウォンまで上がり2週間ぶりに1,350ウォン台を付けた。

2. なぜここまで下がったのか — 一週間に集中した5つの悪材料
第1に、米証券取引委員会（SEC）がエヌビディアの会計処理を調査しているというロイター報道。第2に、AMDの中国輸出規制違反疑惑（会社は否定）。第3に、グーグルの2027年TPU 8i出荷計画縮小観測によるブロードコム需要鈍化懸念。第4に、トランプ大統領の「海外データセンター建設には高率課税」発言とリサ・クックFRB理事のタカ派発言（12月25bp利上げ確率は94％まで織り込み）。第5に、史上最大のIPOであるアントロピック上場が資金を吸い上げ、既存AI株の利益確定を誘ったこと。アントロピック（ANT）は公開価格83ドルで初日17.1％高となったが、2日目の20日は8.50％安の88.91ドルで引け、取引中には公開価格まで下落した。調達総額1,195億ドル（約161兆ウォン）、初日の時価総額1兆2,700億ドル。

3. 前の米国市場 — S&P500は7日続落、VIXは35.89
11月20日のNY市場でS&P500は3.70％安の6,910.39、ナスダックは5.28％安の22,617.73、ダウは1.93％安の48,147.33。S&P500は2020年2月以来最長の7日続落、ナスダックは今年の上昇分をすべて返上した（年初来−2.69％）。週間ではナスダック−10.0％、S&P500−8.6％、ダウ−8.0％で、2025年4月の関税ショック以来の大きさ。フィラデルフィア半導体指数は10.73％急落し、VIXは26.20％高の35.89と2025年4月以来の高値。米10年債利回りは14bp低下の4.909％。エヌビディア−14.01％（125.53ドル、10月6日高値から−48％）、AMD−13.25％、マイクロン−13.89％、ブロードコム−12.19％、サンディスク−16.05％、SKハイニックスADR−13.11％。マイクロソフト−2.77％、アルファベット−2.70％、アマゾン−4.10％、メタ−5.93％、テスラ−7.64％。一方でウォルマート（+1.52％）、コストコ（+0.75％）などディフェンシブ銘柄には買いが入った。23日午後5時15分時点の米株先物はS&P500が+2.2％、ナスダックが+2.9％と反発して始まっている。

4. 今日発行されたリポートが示す数字
新韓投資証券の「マーケットレーダー」は、コスピの12カ月先PBRが0.91倍で過去平均1.04倍を下回ると指摘。ユアンタ証券はナスダック週間−10.02％を「AIトレードの巻き戻し」と規定し、AIバブル論争・広範なデレバレッジ・PCEを今週のキーワードに挙げた。iM証券は証安ファンドが実際に執行されたのが1990・2003・2008年の3回だけだと整理。大信証券のイ・ギョンミン研究員は「高値から約50％下落し、IMF危機・金融危機・ドットコムバブル崩壊以来の衝撃。すでにアンダーシューティング局面で、4,700線は守った」と評価した。KB証券によれば、金利先物は12月の据え置き確率を8.6％しか織り込んでいない。
海外はより直接的だ。ブルームバーグによると、ゴールドマン・サックスの「パニック指数」は10点満点中9点まで上昇。トレンドフォロー型（CTA）は直近1カ月で570億ドルを売り越し、下落が続けば最大806億ドルの追加売りが出る。ヤーデニ・リサーチはS&P500の年末目標を7,900から7,500へ引き下げつつ、来年末には8,500〜9,000を見込む。

5. いま見るべき3点
11月25日の米3Q GDPと10月PCEが12月利上げを確定させるか。11月26日の韓国銀行金融通貨委員会と米感謝祭休場による需給の空白、そして1,350ウォン超えのウォン安。最後に、証安ファンドが「準備」から「実際の買い」に移るか、外国人の売り越しが止まるかどうかだ。"""

ZH_DESC = """黑色星期五之后的周一同样惨淡。韩国综合股价指数（KOSPI）盘中一度跌至4,586.80点，跌幅超过5.8%，上午11时33分连续第二个交易日触发卖出熔断（sidecar）。收盘点位为1月13日以来最低。但午后气氛转变：政府着手准备证券市场稳定基金（维稳基金），金融委员会决定放宽上市公司每日回购上限，指数跌幅收窄近半，4,700点得以守住。按顺序梳理数据，就能看出这个市场此前对"AI投资"这一叙事依赖得有多深。

1. 今日数据——KOSPI 4,708.54（−3.31%），科斯达克创两年新低
KOSPI收于4,708.54点，下跌161.42点（3.31%）。开盘即跌2.77%至4,734.90点，随后接连失守4,700点和4,600点，盘中低点4,586.80点。科斯达克下跌1.58%至635.45点，为2024年12月9日以来最低收盘，盘中曾跌至618.74点。KOSPI200收于730.83点（−3.24%）。
资金面上，外资净卖出2,472亿韩元（连续7个交易日净卖出），个人净卖出3,669亿韩元，机构净买入1,872亿韩元。与之前6个交易日日均净卖出7,851亿韩元相比，外资抛压实际上有所减弱。全部行业下跌：建设−6.91%、保险−5.12%、制药−4.89%、运输仓储−4.73%。上涨个股仅71只，下跌824只。三星电子跌3.06%，SK海力士跌2.52%，三星生物−4.94%，KB金融−5.71%，现代汽车−2.94%。韩元对美元汇率上涨9.7韩元至1,345.9韩元，盘中一度触及1,351.6韩元，两周来首次突破1,350关口。

2. 为何暴跌——一周内集中爆发的五大利空
第一，路透社报道美国证券交易委员会（SEC）正在调查英伟达的会计处理，股价跌幅从6%扩大至14%。第二，AMD被指违反对华出口管制（公司否认）。第三，市场预期谷歌下调2027年TPU 8i出货计划，引发博通需求担忧。第四，特朗普威胁对在海外建设数据中心的美国企业征收高额税款，以及美联储理事库克的鹰派表态（12月加息25个基点概率升至94%）。第五，史上最大IPO安特罗匹克上市反而吸走流动性，引发既有AI股获利了结。ANT首日上涨17.1%，次日（20日）下跌8.50%至88.91美元，盘中一度回到发行价83美元。总募资1,195亿美元（约161万亿韩元），首日市值1.27万亿美元。

3. 前一个美股交易日——标普500七连跌，VIX 35.89
11月20日，标普500下跌3.70%至6,910.39点，纳斯达克下跌5.28%至22,617.73点，道指下跌1.93%至48,147.33点。标普500创2020年2月以来最长的七连跌，纳斯达克回吐今年全部涨幅（年内−2.69%）。一周内纳斯达克−10.0%、标普500−8.6%，为2025年4月关税冲击以来最大跌幅。费城半导体指数暴跌10.73%，VIX大涨26.20%至35.89，为2025年4月以来最高。英伟达−14.01%（125.53美元，较10月6日高点下跌48%）、AMD−13.25%、美光−13.89%、博通−12.19%、闪迪−16.05%、SK海力士ADR−13.11%；微软−2.77%、亚马逊−4.10%、Meta−5.93%、特斯拉−7.64%。资金转向沃尔玛（+1.52%）、好市多（+0.75%）等防御性资产。23日下午5时15分，标普500与纳斯达克期货分别上涨2.2%和2.9%。

4. 今日研报给出的数字
新韩投资证券指出，KOSPI的12个月远期PBR为0.91倍，低于历史均值1.04倍。Yuanta证券将纳斯达克周跌幅10.02%定义为"AI交易回吐"，并把AI泡沫争论、全面去杠杆、PCE列为本周关键词。iM证券梳理称，维稳基金历史上仅在1990、2003、2008年三次实际执行。大信证券李京民研究员认为，指数已较峰值下跌约50%，进入超跌区间，4,700点得以守住。KB证券称，利率期货仅计入8.6%的12月按兵不动概率。
海外方面，据彭博社报道，高盛"恐慌指数"升至满分10分中的9分；趋势跟踪型基金（CTA）近一个月净卖出570亿美元，若跌势延续，最多可能再卖出806亿美元。亚德尼研究将标普500年末目标从7,900下调至7,500，但仍预计明年底可达8,500~9,000点。

5. 现在该看的三件事
11月25日美国三季度GDP与10月PCE，将决定12月是否加息。11月26日韩国央行金融货币委员会会议与美国感恩节休市带来的流动性空窗，以及突破1,350的汇率。最后是维稳基金能否从"准备"走向"实际买入"，以及外资连续净卖出是否结束。"""

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
    "images": [G1, G2, G3],
    "affiliateUrl": "https://stock.naver.com/",
    "affiliatePlatform": "Coupang",
    "i18n": {
        "ko": {
            "title": "코스피 4,700선 사수, 나스닥 −5.28%…'AI 버블' 논쟁을 숫자로 해부했다",
            "summary": "코스피 4,708.54(−3.31%) 마감, 장중 −5.8%·매도 사이드카. 나스닥 −5.28%·엔비디아 −14%가 만든 '검은 금요일' 이후 첫 거래일을 수급·환율·리포트 숫자로 정리했습니다.",
            "description": KO_DESC,
            "tasteReview": [
                "코스피는 4,708.54(−3.31%)로 4,700선 사수, 코스닥은 635.45(−1.58%)로 2년 만의 최저 종가",
                "외국인 7거래일 연속 순매도(−2,472억원)지만 직전 6일 평균(−7,851억원)보다 규모는 축소",
                "골드만삭스 패닉지수 9/10, CTA 최대 806억달러 추가 매도 여지 — 수급 발 변동성은 아직 진행 중",
            ],
            "tips": "본 글은 공개된 시세·리포트를 정리한 정보 기록이며, 특정 종목의 매수·매도를 권유하지 않습니다.",
        },
        "en": {
            "title": "KOSPI Holds 4,700 as Nasdaq Falls 5.28%: The AI Bubble Debate in Numbers",
            "summary": "KOSPI closed at 4,708.54 (-3.31%) after falling as much as 5.8% intraday and triggering a sell-side circuit breaker. A data-first look at the session, the flows and the research behind the AI selloff.",
            "description": EN_DESC,
            "tasteReview": [
                "KOSPI held 4,700 at 4,708.54 (-3.31%); KOSDAQ closed at a two-year low of 635.45",
                "Foreign investors sold a seventh straight session, but 247.2bn won is far below the 785.1bn won daily average of the prior six",
                "Goldman's panic index hit 9/10 and CTA models point to up to $80.6bn of further selling",
            ],
            "tips": "This is a summary of public market data and broker research, not investment advice.",
        },
        "ja": {
            "title": "コスピ4,700線死守、ナスダック−5.28％…「AIバブル」論争を数字で読み解く",
            "summary": "コスピは4,708.54（−3.31％）で引け、取引中は5.8％安まで下落し売りサイドカーが発動。ナスダック−5.28％、エヌビディア−14％が作った「黒い金曜日」後の最初の取引日を需給・為替・リポートの数字で整理しました。",
            "description": JA_DESC,
            "tasteReview": [
                "コスピは4,708.54（−3.31％）で4,700線を死守、コスダックは635.45（−1.58％）で2年ぶり安値",
                "外国人は7営業日連続売り越しだが、規模は直前6日平均（7,851億ウォン）より縮小",
                "ゴールドマンのパニック指数9/10、CTAは最大806億ドルの追加売り余地",
            ],
            "tips": "本記事は公開された相場データとリポートの整理であり、個別銘柄の売買を推奨するものではありません。",
        },
        "zh": {
            "title": "KOSPI守住4,700点、纳斯达克暴跌5.28%：用数字拆解“AI泡沫”之争",
            "summary": "KOSPI收于4,708.54点（−3.31%），盘中一度跌5.8%并触发卖出熔断。本文用资金流、汇率与研报数据，复盘纳斯达克−5.28%、英伟达−14%之后的第一个交易日。",
            "description": ZH_DESC,
            "tasteReview": [
                "KOSPI守住4,700点，收于4,708.54（−3.31%）；科斯达克635.45（−1.58%），创两年新低",
                "外资连续7个交易日净卖出，但2,472亿韩元远低于此前6日日均7,851亿韩元",
                "高盛恐慌指数升至9/10，CTA模型显示最多还有806亿美元卖压",
            ],
            "tips": "本文仅为公开行情与研报的整理，不构成任何个股买卖建议。",
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
