#!/usr/bin/env python3
"""
Upload 2-post humidifier cluster (heated humidifier winter season) to Supabase + ISR revalidate.
Keyword: 가열식 가습기 (Naver monthly search ~165,500, 2026-11-20)
 - Post A: heated vs ultrasonic vs hybrid + electricity cost
 - Post B: limescale / citric acid cleaning routine
"""

import json
import urllib.request

SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptdXFtdnh1YnV3aG9vY3Vrbm50Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDMwODA3NywiZXhwIjoyMTA5ODg0MDc3fQ.ELyAmyRJrWdQoIHRu4thMGvjAnjJfVZ4S8Cfpb9MiDY"
REVALIDATE_URL = "https://www.k-trand.store/api/revalidate?secret=kblog2026"

K = "https://www.coupang.com/np/search?q="
TAG = "&lptag=AF9412775"


def q(s):
    from urllib.parse import quote
    return K + quote(s) + TAG


POSTS = [
    {
        "id": "heated-vs-ultrasonic-humidifier-power-cost-2026",
        "slug": "heated-vs-ultrasonic-humidifier-power-cost-2026",
        "category": "tech",
        "store": "쿠팡",
        "priceKrw": 319690,
        "releaseDate": "2026-11-23",
        "rating": 4.8,
        "imageUrl": "/images/products/real-humidifier-cuckoo-steam-room.jpg",
        "images": [
            "/images/products/real-humidifier-lg-hydrotower-room.jpg",
            "/images/products/real-humidifier-zojirushi-nursery.jpg",
            "/images/products/real-humidifier-cuckoo-tank.jpg",
        ],
        "exampleItems": [
            {
                "name": "조지루시 가열식 가습기 EE-TAH60K 4L",
                "brand": "조지루시",
                "priceKrw": 319690,
                "imageUrl": "/images/products/item-zojirushi-ee-tah60k.jpg",
                "url": q("조지루시 가열식 가습기 EE-TAH60K"),
                "category": "Heated Humidifier",
            },
            {
                "name": "쿠쿠전자 스팀 100 가열식 가습기 CH-MS301FW",
                "brand": "쿠쿠전자",
                "priceKrw": 197390,
                "imageUrl": "/images/products/item-cuckoo-ch-ms301fw.jpg",
                "url": q("쿠쿠 스팀100 가열식 가습기 CH-MS301FW"),
                "category": "Heated Humidifier",
            },
            {
                "name": "르젠 플러스 IH 5세대 가열식 가습기 LPL-IH600S",
                "brand": "르젠",
                "priceKrw": 187490,
                "imageUrl": "/images/products/item-lezen-lpl-ih600s.jpg",
                "url": q("르젠 플러스 IH 가열식 가습기 LPL-IH600S"),
                "category": "Heated Humidifier",
            },
            {
                "name": "LG전자 퓨리케어 오브제컬렉션 하이드로타워 HY705RSUA",
                "brand": "LG전자",
                "priceKrw": 1034000,
                "imageUrl": "/images/products/item-lg-hydrotower-hy705rsua.jpg",
                "url": q("LG 퓨리케어 하이드로타워 HY705RSUA"),
                "category": "Hybrid Humidifier",
            },
        ],
        "affiliateUrl": q("가열식 가습기 4L"),
        "affiliatePlatform": "Coupang",
        "i18n": {
            "ko": {
                "title": "가열식 가습기 전기요금, 한 달에 얼마 더 나올까? 초음파·복합식과 숫자로 비교",
                "summary": "겨울 가습기 선택의 마지막 갈림길은 위생과 전기요금입니다. 가열식·초음파·복합식의 소비전력과 월 예상 전기료, 가습량, 관리 난이도를 제조사 스펙과 판매 데이터로 정리했습니다.",
                "description": """난방을 켜기 시작하면 실내 습도는 하루 만에 30% 아래로 떨어집니다. 11월 들어 다나와의 가습기 거래액은 한 달 새 279% 늘었고, 그중 절반 이상이 50만 원 이상 제품이었습니다. 소비자가 가격보다 위생을 먼저 본다는 뜻입니다. 문제는 가열식이 초음파보다 전기를 훨씬 많이 쓴다는 점인데, 막상 얼마인지 계산해 둔 자료는 드뭅니다.

1. 세 방식의 구조는 이렇게 다릅니다
가열식은 물을 100℃ 가까이 끓여 수증기를 내보냅니다. 물통 안에서 세균이 증식할 시간이 없고, 물때가 히터에 눌어붙기 전까지만 관리하면 위생 부담이 적습니다. 초음파식은 진동자로 물방울을 잘게 부숴 뿌리기 때문에 소비전력이 30~40W 수준입니다. 대신 물통을 자주 씻지 않으면 세균과 곰팡이가 그대로 방 안으로 날아갑니다. 복합식은 정수 필터를 거친 물을 가열해 내보내며, 가열과 정화를 함께 가져가는 상위 모델입니다.

2. 전기요금은 숫자로 계산해야 합니다
소비전력만 보면 차이가 작아 보이지만, 하루 8시간, 한 달 30일로 계산하면 결과가 달라집니다. 가열식 400W는 월 96kWh, 600W는 144kWh입니다. kWh당 130원(주택용 저압 1단계 수준)으로 계산하면 각각 12,500원과 18,700원이고, 누진 구간에 걸려 200원대가 되면 19,200원과 28,800원까지 올라갑니다. 초음파 35W는 월 8.4kWh로 1,100~1,700원 수준입니다. 즉 가열식은 초음파보다 한 달에 1만~2만 7천 원 정도를 더 쓰는 셈입니다. 다만 히터는 목표 온도에 도달하면 스스로 쉬기 때문에 실제 고지서는 이 계산치보다 20~30% 낮게 나옵니다.

3. 가습량과 습도 관리
가열식 4L 모델은 최대 600ml/h, 초음파 소형 모델은 200~300ml/h입니다. 같은 방이라면 가열식이 40~60% 구간에 더 빨리 도달합니다. 다만 지나친 가습은 결로와 곰팡이를 부르므로 습도계를 두고 50% 전후로 맞추는 편이 안전합니다.

4. 어떤 집에 어떤 방식이 맞을까
아기방, 반려동물과 함께 사는 집, 물통 세척이 부담스러운 사람에게는 가열식이 맞습니다. 전기요금이 먼저라면 살균 기능이 붙은 초음파, 넓은 거실과 정수까지 원한다면 복합식입니다. 정답은 하나가 아니라 사용 시간과 관리 성향에 따라 갈립니다.

5. 구매 전 확인할 다섯 가지
용량(침실 3~4L, 거실 5L 이상), 자동세척이나 분리세척 구조, 상부급수 여부, 소음(25~35dB), 뜨거운 증기가 나오는 제품의 안전 장치(버튼 잠금, 전도 차단)입니다. 이 다섯 가지만 맞으면 브랜드 차이는 생각보다 크지 않습니다.""",
                "tasteReview": [
                    "가열식은 위생 관리 부담이 낮은 대신 월 1만~2만 7천 원의 전기료를 더 씁니다",
                    "초음파는 전력이 10분의 1 수준이지만 물통 세척 주기를 짧게 잡아야 합니다",
                    "복합식은 정수·가열·청정을 한 번에 처리하지만 본체 가격이 두 배 이상입니다",
                ],
                "tips": "가열식을 고른다면 자동세척과 상부급수 두 가지만 먼저 확인하세요. 매일 쓰는 피로도를 결정하는 건 이 두 가지입니다.",
            },
            "en": {
                "title": "Heated Humidifier Power Cost: How Much More Per Month Than Ultrasonic?",
                "summary": "The last decision in a winter humidifier purchase is hygiene versus electricity. Here is what heated, ultrasonic and hybrid models actually cost to run, with wattage, mist output and maintenance compared.",
                "description": """Once the heating comes on, indoor humidity drops below 30% within a day. In November, transaction value for humidifiers on Danawa rose 279% month over month, and more than half of that came from units over 500,000 KRW. Buyers are choosing hygiene first. The catch is that heated models draw far more power than ultrasonic ones, and few guides actually do the math.

1. How the three types differ
A heated humidifier boils water to near 100°C and releases steam. Bacteria have little time to multiply inside the tank, and hygiene stays manageable as long as scale is cleaned before it bakes onto the heater. Ultrasonic models shatter water into fine droplets with a vibrating plate, drawing only 30-40W. The trade-off is that an unclean tank sends bacteria and mold straight into the room. Hybrid models pass water through a purification filter and then heat it, combining both jobs in one chassis.

2. Run the electricity numbers
Wattage alone makes the gap look small, but eight hours a day for thirty days tells a different story. A 400W heated unit uses 96 kWh a month and a 600W unit 144 kWh. At 130 KRW per kWh (roughly Korea's first-tier residential rate) that is 12,500 and 18,700 KRW; inside a higher tier at 200 KRW it becomes 19,200 and 28,800 KRW. A 35W ultrasonic unit uses 8.4 kWh, or 1,100-1,700 KRW. So a heated model costs roughly 10,000-27,000 KRW more per month. Because the heater cycles off once it reaches target temperature, real bills usually land 20-30% below these figures.

3. Mist output and humidity control
A 4L heated unit moves up to 600 ml/h, while a small ultrasonic model manages 200-300 ml/h. In the same room, the heated unit reaches the 40-60% band faster. Over-humidifying invites condensation and mold, so place a hygrometer and hold the room near 50%.

4. Which type fits which home
For a nursery, a home with pets, or anyone tired of scrubbing tanks, heated is the safer pick. If the electricity bill comes first, choose an ultrasonic unit with a sterilization feature. For a large living room that also needs purified water, a hybrid is the answer. There is no single right choice; usage hours and maintenance habits decide it.

5. Five checks before you buy
Tank capacity (3-4L for a bedroom, 5L or more for a living room), an auto-clean or fully detachable tank, top-fill design, noise level (25-35 dB), and safety features such as a button lock and tip-over cut-off on models that emit hot steam. Once these five line up, brand differences matter far less than expected.""",
                "tasteReview": [
                    "Heated models cut hygiene work but add roughly 10,000-27,000 KRW of electricity per month",
                    "Ultrasonic sips a tenth of the power yet demands a much shorter tank-cleaning cycle",
                    "Hybrid units handle purification, heating and air cleaning together at more than double the price",
                ],
                "tips": "If you go heated, check auto-clean and top-fill first. Those two decide how tiring the appliance feels every single day.",
            },
            "ja": {
                "title": "加熱式加湿器の電気代は月いくら？超音波・複合式と数字で比較",
                "summary": "冬の加湿器選びの最後の分かれ道は衛生管理と電気代です。加熱式・超音波・複合式の消費電力と月の電気代目安、加湿量、手入れの手間をメーカー仕様と販売データで整理しました。",
                "description": """暖房を入れ始めると、室内の湿度は一日で30%を下回ります。11月に入り、韓国ダナワの加湿器取引額は前月比279%増え、その半分以上が50万ウォン以上の製品でした。価格より衛生を優先する消費者が増えているということです。問題は、加熱式が超音波式より電力をはるかに多く使う点ですが、いくらになるかを実際に計算した資料はほとんどありません。

1. 三方式の構造の違い
加熱式は水を100℃近くまで沸騰させて蒸気を出します。水タンク内で細菌が増殖する時間がなく、ヒーターに水垢が固まる前に落とせば衛生面の負担は軽いままです。超音波式は振動子で水を細かい粒に砕いて噴霧するため、消費電力は30〜40W程度です。ただしタンクを頻繁に洗わないと、細菌やカビがそのまま部屋に飛びます。複合式は浄水フィルターを通した水を加熱して放出し、加熱と浄化を一台でこなす上位モデルです。

2. 電気代は数字で計算する
消費電力だけを見ると差は小さく見えますが、1日8時間・30日で計算すると話が変わります。加熱式400Wは月96kWh、600Wは144kWhです。1kWhあたり130ウォン（韓国の住宅用低圧第1段階相当）ならそれぞれ12,500ウォンと18,700ウォン、累進区間に届いて200ウォン台になると19,200ウォンと28,800ウォンまで上がります。超音波35Wは月8.4kWhで1,100〜1,700ウォン程度です。つまり加熱式は超音波式より月に約1万〜2万7千ウォン多くかかります。ヒーターは設定温度に達すると自動で休むため、実際の請求額はこの計算より20〜30%低くなります。

3. 加湿量と湿度管理
加熱式4Lモデルは最大600ml/h、小型の超音波式は200〜300ml/hです。同じ部屋なら加熱式のほうが40〜60%の範囲に早く到達します。ただし過剰な加湿は結露やカビの原因になるため、湿度計を置いて50%前後で保つのが安全です。

4. どんな家庭にどの方式が合うか
子ども部屋、ペットと暮らす家、タンク洗浄が負担な人には加熱式が向いています。電気代を優先するなら除菌機能付きの超音波式、広いリビングと浄水まで求めるなら複合式です。正解は一つではなく、使用時間と手入れの性格で決まります。

5. 購入前に確認する5項目
容量（寝室3〜4L、リビング5L以上）、自動洗浄または丸洗いできる構造、上から給水できるか、騒音（25〜35dB）、熱い蒸気が出るモデルの安全装置（ボタンロック、転倒時停止）です。この5点が合えば、ブランドによる差は思ったより小さくなります。""",
                "tasteReview": [
                    "加熱式は衛生管理が楽な代わりに月1万〜2万7千ウォンの電気代が増える",
                    "超音波は消費電力が10分の1だが、タンク洗浄の周期を短くする必要がある",
                    "複合式は浄水・加熱・空気清浄を一台でこなすが本体価格は2倍以上",
                ],
                "tips": "加熱式を選ぶなら自動洗浄と上給水の2点を先に確認してください。毎日使う負担を決めるのはこの2つです。",
            },
            "zh": {
                "title": "加热式加湿器电费一个月多花多少？与超声波、复合式的数据对比",
                "summary": "冬季选购加湿器最后的取舍是卫生与电费。本文用厂商参数和销售数据对比加热式、超声波与复合式的功耗、月均电费、加湿量和维护难度。",
                "description": """一开暖气，室内湿度一天内就会掉到30%以下。11月以来，韩国价格比较平台Danawa的加湿器交易额环比增长279%，其中一半以上来自50万韩元以上的产品，说明消费者把卫生放在了价格之前。问题在于加热式耗电远高于超声波式，但真正把电费算清楚的内容并不多。

1. 三种结构完全不同
加热式把水烧到接近100℃产生蒸汽。水箱内细菌几乎没有繁殖时间，只要在水垢烧结在加热器上之前清理，卫生负担就很低。超声波式用振动片把水打成细小水雾，功耗只有30~40W；但如果水箱不勤洗，细菌和霉菌会直接吹进房间。复合式先让水通过净水滤芯再加热喷出，把加热与净化合在一台机器里，属于高端方案。

2. 电费必须算数字
只看功率差距不大，但按每天8小时、每月30天计算就不一样了。加热式400W每月96kWh，600W为144kWh。按每kWh 130韩元（接近韩国居民低压第一档）计算分别为12,500和18,700韩元；进入阶梯电价200韩元档则会升到19,200和28,800韩元。超声波35W每月仅8.4kWh，约1,100~1,700韩元。也就是说加热式每月比超声波多花约1万~2万7千韩元。由于加热器达到设定温度后会自动间歇工作，实际账单通常比计算值低20~30%。

3. 加湿量与湿度控制
4L加热式最大加湿量600ml/h，小型超声波为200~300ml/h。同一房间内加热式更快达到40~60%的舒适区间。加湿过度会导致结露和发霉，建议放置湿度计并维持在50%左右。

4. 哪种房子适合哪种方式
婴儿房、养宠物的家庭、不愿频繁刷水箱的人适合加热式。若电费优先，可选择带除菌功能的超声波式；希望兼顾大客厅与净水，则选复合式。没有唯一答案，取决于使用时长和维护习惯。

5. 购买前必看的五项
容量（卧室3~4L，客厅5L以上）、自动清洗或可全拆洗结构、是否上加水、噪音（25~35dB），以及会喷出热蒸汽机型的按钮锁与倾倒断电等安全设计。这五项对上之后，品牌差异往往没有想象中那么大。""",
                "tasteReview": [
                    "加热式卫生管理轻松，但每月要多花约1万~2万7千韩元电费",
                    "超声波耗电仅十分之一，却需要更频繁地清洗水箱",
                    "复合式一台完成净水、加热与净化，但价格是两倍以上",
                ],
                "tips": "选加热式时先确认自动清洗和上加水这两点，它们决定了每天使用的疲惫程度。",
            },
        },
    },
    {
        "id": "heated-humidifier-limescale-cleaning-2026",
        "slug": "heated-humidifier-limescale-cleaning-2026",
        "category": "tech",
        "store": "쿠팡",
        "priceKrw": 8700,
        "releaseDate": "2026-11-23",
        "rating": 4.9,
        "imageUrl": "/images/products/real-humidifier-cuckoo-tank-wash.jpg",
        "images": [
            "/images/products/real-humidifier-zojirushi-citric-acid.jpg",
            "/images/products/real-humidifier-zojirushi-tank-wipe.jpg",
            "/images/products/real-humidifier-zojirushi-heater.jpg",
        ],
        "exampleItems": [
            {
                "name": "무수구연산 1kg 식품용 세정제",
                "brand": "구연산",
                "priceKrw": 8700,
                "imageUrl": "/images/products/item-citric-acid-1kg.jpg",
                "url": q("무수구연산 1kg 식품용"),
                "category": "Cleaning",
            },
            {
                "name": "에어메이드 가습기 전용 자동세척 브러시 AMH-4500B",
                "brand": "에어메이드",
                "priceKrw": 25290,
                "imageUrl": "/images/products/item-airmade-cleaning-brush.jpg",
                "url": q("에어메이드 가습기 자동세척 브러시 AMH-4500B"),
                "category": "Cleaning",
            },
            {
                "name": "LG전자 가습기 정품 청소용 솔 HW300BBB",
                "brand": "LG전자",
                "priceKrw": 11400,
                "imageUrl": "/images/products/item-lg-humidifier-brush.jpg",
                "url": q("LG전자 가습기 청소용 솔 HW300BBB"),
                "category": "Cleaning",
            },
            {
                "name": "에어메이드 THE 위대한가습기 2.0 AMH-4502 자동세척",
                "brand": "에어메이드",
                "priceKrw": 274550,
                "imageUrl": "/images/products/item-airmade-amh-4502.jpg",
                "url": q("에어메이드 더 위대한 가습기 2.0 AMH-4502"),
                "category": "Heated Humidifier",
            },
        ],
        "affiliateUrl": q("가열식 가습기 세척 구연산"),
        "affiliatePlatform": "Coupang",
        "i18n": {
            "ko": {
                "title": "가열식 가습기 물때·석회, 구연산 하나로 30분에 끝내는 법",
                "summary": "가열식 가습기는 끓이는 구조라 물때가 빨리 낍니다. 방치하면 가습량과 소음, 냄새까지 나빠집니다. 구연산 2% 용액으로 30분 만에 끝내는 부품별 세척 순서를 정리했습니다.",
                "description": """가열식 가습기를 두 달쯤 쓰면 물통 바닥과 히터 주변에 하얀 막이 앉습니다. 수돗물에 녹아 있던 칼슘과 마그네슘이 끓으면서 탄산칼슘으로 굳은 석회입니다. 문제는 이 막이 위생보다 성능을 먼저 갉아먹는다는 점입니다.

1. 물때를 방치하면 생기는 일
히터 표면에 석회가 두꺼워지면 열이 물로 전달되는 효율이 떨어집니다. 같은 전력을 써도 끓는 시간이 길어지고, 가습량이 줄고, 물이 끓는 소리는 커집니다. 석회가 몇 달 쌓이면 냄새까지 배어 구연산으로도 한 번에 지워지지 않습니다. 세척은 미관이 아니라 성능 관리입니다.

2. 준비물은 네 가지
식품용 구연산, 부드러운 솔, 미온수, 넉넉한 헹굼물입니다. 구연산은 물 1L에 20g, 2% 농도면 충분합니다. 1kg 제품 하나로 한 시즌을 넘기고도 남습니다. 뜨거운 물을 쓰면 자극이 강해지므로 40~50℃ 정도의 미온수가 적당합니다.

3. 30분 세척 코스
① 전원을 빼고 완전히 식힙니다. 뜨거운 상태에 찬물을 부으면 스테인리스 수조가 휩니다.
② 물통을 비우고 구연산 20g을 푼 미온수 1L를 채웁니다.
③ 10~15분 두고, 석회가 두꺼운 부위는 솔로 가볍게 문지릅니다. 자동세척 기능이 있는 모델은 세척 모드로 10분 돌리면 히터 주변까지 풀립니다.
④ 용액을 버리고 미온수로 3회 이상 헹굽니다. 헹굼이 부족하면 남은 산 성분이 플라스틱 부품과 패킹을 상하게 합니다.
⑤ 스팀 노즐과 석회 방지 필터를 분리해 같은 방법으로 담갔다가 헹굽니다. 석회 방지 필터는 1~2개월에 한 번 교체가 기준입니다.

4. 얼마나 자주 해야 할까
매일 8시간 이상 쓴다면 1~2주에 한 번, 주말만 쓴다면 한 달에 한 번이면 충분합니다. 자동세척 모델도 히터에 눌어붙은 석회까지 지워주지는 않으므로 두 달에 한 번은 손으로 닦아야 합니다. 물을 정수로 바꾸면 석회가 느는 속도가 눈에 띄게 줄어듭니다.

5. 헷갈리기 쉬운 주의사항
구연산은 반드시 식품용을 쓰고, 세척 중에는 전원을 분리하세요. 알루미늄 부품에는 산성 세척제를 쓰지 않습니다. 세척 후 첫 가동은 창문을 열고 10분 정도 돌려 잔여 냄새를 빼는 편이 좋습니다. 베이킹소다와 구연산을 섞으면 거품만 남고 세정력은 떨어지므로 따로 쓰는 것이 낫습니다.""",
                "tasteReview": [
                    "석회는 위생보다 가습량과 소음을 먼저 떨어뜨리는 성능 문제입니다",
                    "구연산 2% 용액에 10~15분이면 히터 주변 석회까지 풀립니다",
                    "자동세척 모델도 두 달에 한 번은 손세척이 필요합니다",
                ],
                "tips": "세척은 가열 직후가 아니라 완전히 식힌 뒤에 시작하세요. 스테인리스 수조 변형을 막는 가장 확실한 방법입니다.",
            },
            "en": {
                "title": "How to Remove Limescale From a Heated Humidifier in 30 Minutes",
                "summary": "Heated humidifiers boil water, so scale builds up fast. Left alone it cuts mist output, raises noise and eventually smells. Here is a 30-minute citric acid routine, part by part.",
                "description": """After roughly two months of use, a white film settles on the tank floor and around the heater of a heated humidifier. That is calcium and magnesium from tap water hardening into calcium carbonate as it boils. The problem is that the film hurts performance before it hurts hygiene.

1. What happens when you leave it
A thick scale layer blocks heat transfer from the heater to the water. The unit takes longer to boil on the same power, mist output drops, and the boiling noise grows louder. After a few months the smell sets in as well, and citric acid no longer removes it in one pass. Cleaning is performance maintenance, not cosmetics.

2. Four items to prepare
Food-grade citric acid, a soft brush, lukewarm water and plenty of rinse water. Twenty grams per liter, a 2% solution, is enough. One kilogram lasts well beyond a single season. Keep the water around 40-50°C; hotter water is more aggressive on the parts.

3. The 30-minute routine
1) Unplug and let the unit cool completely. Pouring cold water onto a hot stainless tank can warp it.
2) Empty the tank and fill it with one liter of lukewarm water mixed with 20 g of citric acid.
3) Wait 10-15 minutes, then brush the thickest deposits lightly. Models with an auto-clean cycle can run that mode for 10 minutes to loosen scale around the heater.
4) Drain the solution and rinse at least three times with lukewarm water. Leftover acid degrades plastic parts and gaskets.
5) Remove the steam nozzle and the scale-prevention filter, soak them the same way, then rinse. Replace the filter every one to two months.

4. How often
Daily use of eight hours or more calls for a clean every one to two weeks; weekend-only use can go a month. Even auto-clean models do not remove scale baked onto the heater, so a manual pass every two months is still needed. Switching to filtered water noticeably slows new buildup.

5. Common mistakes
Use food-grade citric acid only, and unplug during cleaning. Never use acid cleaners on aluminum parts. After cleaning, run the unit near an open window for ten minutes to clear residual odor. Mixing baking soda with citric acid produces fizz but weakens the cleaning power, so use them separately.""",
                "tasteReview": [
                    "Scale is a performance problem: it cuts mist output and raises noise before hygiene suffers",
                    "Ten to fifteen minutes in a 2% citric acid solution loosens scale around the heater",
                    "Even auto-clean models need a manual scrub every two months",
                ],
                "tips": "Start cleaning after the unit has fully cooled, not right after a boil. It is the surest way to keep a stainless tank from warping.",
            },
            "ja": {
                "title": "加熱式加湿器の水垢・石灰をクエン酸で30分できれいにする方法",
                "summary": "加熱式加湿器は沸騰させる構造のため水垢が早く付きます。放置すると加湿量と静音性が落ち、においも出ます。2%クエン酸液で30分で終わる部位別の洗浄手順をまとめました。",
                "description": """加熱式加湿器を2か月ほど使うと、水タンクの底とヒーター周りに白い膜が付きます。水道水に溶けていたカルシウムとマグネシウムが、沸騰によって炭酸カルシウムとして固まった石灰（スケール）です。問題は、この膜が衛生よりも先に性能を削ることです。

1. 放置すると起きること
ヒーター表面のスケールが厚くなると、熱が水に伝わる効率が落ちます。同じ電力でも沸騰までの時間が延び、加湿量は減り、沸騰音は大きくなります。数か月積もるとにおいまで染みつき、クエン酸でも一度では落ちません。洗浄は見た目の問題ではなく性能管理です。

2. 用意するものは4つ
食品用クエン酸、柔らかいブラシ、ぬるま湯、たっぷりのすすぎ水です。クエン酸は水1Lに20g、2%濃度で十分です。1kgあればシーズンを跨いで余ります。熱湯は部品への刺激が強いため、40〜50℃のぬるま湯が適しています。

3. 30分コース
① 電源を抜き、完全に冷まします。熱い状態に冷水を入れるとステンレス槽がゆがみます。
② 水を捨て、クエン酸20gを溶かしたぬるま湯1Lを入れます。
③ 10〜15分置き、厚い部分はブラシで軽くこすります。自動洗浄機能のある機種は洗浄モードで10分回すとヒーター周りまで緩みます。
④ 液を捨て、ぬるま湯で3回以上すすぎます。すすぎ不足は残った酸が樹脂部品やパッキンを傷めます。
⑤ スチームノズルと石灰防止フィルターを外して同じように浸し、すすぐ。フィルターは1〜2か月に一度の交換が目安です。

4. 頻度の目安
毎日8時間以上使うなら1〜2週間に一度、週末だけなら月に一度で十分です。自動洗浄機種でもヒーターに焼き付いたスケールは落ちないため、2か月に一度は手洗いが必要です。浄水に変えるとスケールの増える速度が目に見えて遅くなります。

5. 間違えやすい注意点
クエン酸は必ず食品用を使い、洗浄中は電源を抜いてください。アルミ部品に酸性洗剤は使いません。洗浄後の初回運転は窓を開けて10分ほど回し、残り香を飛ばすのがおすすめです。重曹とクエン酸を混ぜると泡立つだけで洗浄力は落ちるため、別々に使います。""",
                "tasteReview": [
                    "スケールは衛生より先に加湿量と静音性を落とす性能の問題です",
                    "2%クエン酸液に10〜15分でヒーター周りの石灰まで緩みます",
                    "自動洗浄モデルでも2か月に一度は手洗いが必要です",
                ],
                "tips": "洗浄は沸騰直後ではなく完全に冷めてから始めてください。ステンレス槽のゆがみを防ぐ最も確実な方法です。",
            },
            "zh": {
                "title": "加热式加湿器水垢清洗：柠檬酸30分钟彻底去除",
                "summary": "加热式加湿器要烧开水，水垢积累得特别快。放任不管会降低加湿量、加大噪音并产生异味。本文整理用2%柠檬酸溶液30分钟完成的分部件清洗流程。",
                "description": """加热式加湿器用上两个月左右，水箱底部和加热器周围就会出现一层白膜。这是自来水中溶解的钙镁在沸腾时变成碳酸钙沉积下来的水垢。问题在于，这层膜先损伤的是性能，其次才是卫生。

1. 放任水垢会发生什么
加热器表面的水垢变厚后，热量传到水中的效率下降。同样的功率下烧开时间变长、加湿量下降、沸腾声变大。积上几个月连异味都会渗进去，用柠檬酸也很难一次清除。清洗不是外观问题，而是性能维护。

2. 需要准备四样
食品级柠檬酸、软毛刷、温水以及充足的冲洗水。每升水加20克柠檬酸，2%浓度就足够。1公斤装能用完整个冬天还绰绰有余。水温控制在40~50℃，开水对部件刺激太强。

3. 30分钟流程
① 拔掉电源并完全冷却。高温时倒入冷水会让不锈钢水箱变形。
② 倒空水箱，注入溶有20克柠檬酸的温水1升。
③ 静置10~15分钟，水垢较厚处用刷子轻刷。带自动清洗模式的机型可运行10分钟，让加热器周围的水垢松动。
④ 倒掉溶液，用温水冲洗至少三次。冲洗不足时残留的酸会腐蚀塑料件和密封圈。
⑤ 取下蒸汽喷嘴与防垢滤芯，用同样方法浸泡后冲洗。防垢滤芯一般1~2个月更换一次。

4. 多久做一次
每天使用8小时以上建议1~2周一次，只在周末使用则一个月一次即可。自动清洗机型也无法清除烧附在加热器上的水垢，所以每两个月仍需手动清洁一次。改用净水后水垢增长速度会明显变慢。

5. 容易搞错的地方
务必使用食品级柠檬酸，清洗时必须断电。铝制部件不要用酸性清洁剂。清洗后第一次使用时开窗运行10分钟散去余味。小苏打和柠檬酸混用只会起泡，清洁力反而下降，应分开使用。""",
                "tasteReview": [
                    "水垢首先是性能问题：它让加湿量下降、噪音变大",
                    "2%柠檬酸溶液浸泡10~15分钟即可松动加热器周围的水垢",
                    "自动清洗机型也需要每两个月手动清洁一次",
                ],
                "tips": "清洗要在完全冷却后进行，而不是刚烧完就动手。这是防止不锈钢水箱变形最可靠的办法。",
            },
        },
    },
]

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation",
}

for post in POSTS:
    slug = post["slug"]
    check_url = f"{SUPABASE_URL}/rest/v1/posts?slug=eq.{slug}&select=id"
    req = urllib.request.Request(check_url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            existing = json.loads(resp.read().decode("utf-8"))
        if existing:
            update_url = f"{SUPABASE_URL}/rest/v1/posts?id=eq.{existing[0]['id']}"
            payload = json.dumps({"data": post}).encode("utf-8")
            urllib.request.urlopen(urllib.request.Request(update_url, data=payload, headers=headers, method="PATCH"))
            print(f"[+] Updated post: {slug}")
        else:
            payload = json.dumps({"slug": slug, "data": post}).encode("utf-8")
            r = urllib.request.urlopen(urllib.request.Request(f"{SUPABASE_URL}/rest/v1/posts", data=payload, headers=headers, method="POST"))
            print(f"[+] Inserted post: {slug} ({r.status})")
    except Exception as e:
        print(f"[-] Error on {slug}: {e}")

try:
    urllib.request.urlopen(urllib.request.Request(REVALIDATE_URL), timeout=60)
    print("[+] Revalidated Vercel cache")
except Exception as e:
    print(f"[-] Revalidate error: {e}")
