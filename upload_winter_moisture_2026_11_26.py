#!/usr/bin/env python3
"""겨울철 정전기·건조함 잡는 보습템 4선 (4개국어) → Supabase posts + ISR revalidate.

근거
 - 가격·용량·후기 수·평점: 2026-11-26 08:40~08:50 KST 쿠팡 검색 결과 직접 확인
   일리윤 세라마이드 아토 집중크림 230ml 1개 22,900 → 13,300원(41%), 100ml당 5,783원, 후기 29,263, 5.0
   세타필 모이스춰라이징 로션 591ml 1개 24,500 → 13,600원(44%), 100ml당 2,301원, 후기 245,818, 5.0
   뉴트로지나 노르웨이젼 포뮬러 핸드크림 56g 1개 7,000원, 10g당 1,250원, 후기 7,457, 4.5
   바세린 립 테라피 립밤 오리지널 7g 2개 10,000 → 5,460원(45%), 10g당 3,900원, 후기 32,449, 5.0
 - 제품 사진: 쿠팡 상품 썸네일 원본 4장을 3:4(1200×1600)로 정규화. AI 생성 0장.
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
SLUG = "winter-static-dry-skin-moisture-4picks-2026"

K = "https://www.coupang.com/np/search?q="
TAG = "&lptag=AF9412775"


def q(s):
    return K + quote(s) + TAG


C = "/images/products/winter-moist-cetaphil-lotion.jpg"
G1 = "/images/products/winter-moist-illiyoon-cream.jpg"
G2 = "/images/products/winter-moist-cetaphil-lotion.jpg"
G3 = "/images/products/winter-moist-neutrogena-hand.jpg"
G4 = "/images/products/winter-moist-vaseline-lip.jpg"

KO_DESC = """11월 26일 목요일, 내일이 블랙프라이데이다. 연말 세일을 앞두고 난방을 켜는 시간이 길어지면 실내 습도가 40% 아래로 떨어진다. 습도가 낮아지면 피부 수분이 빨리 날아가고, 마른 공기는 전기를 잘 통하지 않아 정전기가 쌓인다. 손잡이를 잡을 때 따끔한 그 느낌은 피부가 건조하다는 신호다. 오늘 오전 쿠팡에서 실제로 확인한 가격으로, 겨울철 보습을 담당할 4종을 골랐다. 4개를 한 번에 사도 3만9,360원이다.

1. 왜 겨울에 정전기가 생기나
정전기는 물체에 쌓인 전하가 빠져나가지 못할 때 생긴다. 여름에는 공기 중 수분이 전하를 옮겨 주지만, 겨울에는 습도가 낮아 공기가 부도체에 가까워진다. 그래서 같은 옷을 입고 같은 문을 잡아도 겨울에만 찌릿하다. 해결은 두 가지다. 실내 습도를 40~60%로 올리고, 피부 표면에 수분 막을 만들어 두는 것. 가습기나 빨래 실내 건조로 습도를 올렸다면, 남은 절반은 보습제가 맡는다.

2. 일리윤 세라마이드 아토 집중크림 230ml — 13,300원
정가 22,900원에서 41% 내린 13,300원이다. 100ml당 5,783원으로, 오늘 고른 4종 중 용량당 단가가 가장 높다. 대신 얼굴·팔꿈치·무릎처럼 갈라지기 쉬운 곳에 국소적으로 쓰는 크림이다. 쿠팡 후기 2만9,263건에 평점 5.0이고 로켓배송으로 오늘 도착한다. 제품 겉면에 'Fragrance Free'와 '9 FREE'가 표기돼 있다. 향이 부담스러운 사람이 얼굴에 쓰기 좋다.
이렇게 쓰면 좋다. 세안 후 물기를 완전히 닦기 전에 얇게 펴 바르고, 각질이 일어난 부위에는 한 겹 더 올린다. 230ml면 얼굴에만 쓰면 두세 달, 손·팔꿈치까지 쓰면 한 달 반 정도다.

3. 세타필 모이스춰라이징 로션 591ml — 13,600원
정가 24,500원에서 44% 내린 13,600원. 100ml당 2,301원으로 4종 중 가장 싸다. 591ml 대용량이라 샤워 후 전신에 쓰기 좋다. 쿠팡 후기 24만5,818건으로 이 글에서 다룬 제품 중 압도적으로 후기가 많고, 평점 5.0이다. 쿠팡 'BEST AWARDS' 표기가 붙은 상품이다.
샤워 후 3분 안에 바르는 것이 핵심이다. 물기가 남아 있을 때 로션을 발라야 수분이 증발하지 않고 막 안에 갇힌다. 타월로 몸을 대충 훔친 상태에서 종아리·팔·허리 순으로 바르면 된다. 591ml는 하루 한 번 전신에 쓰면 두 달 남짓 간다.

4. 뉴트로지나 노르웨이젼 포뮬러 핸드크림 56g — 7,000원
할인 없이 7,000원이고 10g당 1,250원이다. 손 전용으로는 10g당 단가가 가장 높지만, 손은 하루에 열 번 넘게 씻는 부위라 자주 발라야 해서 소모가 빠르다. 56g 튜브는 가방에 넣기 좋은 크기다. 후기 7,457건, 평점 4.5. 향이 랜덤 발송되므로 특정 향을 원하면 상품 옵션을 확인해야 한다.
손 씻고 물기를 살짝 남긴 상태에서 손등부터 바르고, 손톱 주변과 손가락 사이에 남은 양을 눌러 넣는다. 자기 전에는 한 번 더 두껍게 발라 장갑을 끼면 다음 날 손등이 덜 갈라진다.

5. 바세린 립 테라피 립밤 오리지널 7g 2개 — 5,460원
정가 10,000원에서 45% 내린 5,460원. 7g 두 개들이라 10g당 3,900원이다. 후기 3만2,449건, 평점 5.0. 입술은 피지선이 없어 스스로 수분을 지키지 못하는 부위라, 겨울에는 각질이 먼저 올라온다.
립밤은 하루 세 번 이상, 얇게 여러 번 바르는 편이 좋다. 두껍게 한 번 바르는 것보다 자주 덧바르는 쪽이 각질이 덜 생긴다. 자기 전에 두껍게 바르는 것을 '립 슬리핑'처럼 쓰면 다음 날 아침 입술이 덜 거칠다. 7g 두 개면 한 개는 가방, 한 개는 책상에 두기 좋다.

6. 네 개를 다 사면 얼마인가
13,300 + 13,600 + 7,000 + 5,460 = 3만9,360원이다. 정가 합계 6만4,400원에서 2만5,040원(38.9%) 줄어든 금액이다. 같은 돈으로 손·얼굴·전신·입술을 모두 덮을 수 있다.
우선순위를 정해야 한다면 이 순서다. 겨울에 가장 먼저 갈라지는 곳은 손등과 입술이다. 손은 하루 종일 물을 만나고, 입술은 피지선이 없다. 예산이 4만 원이라면 네 개를 다 사고, 2만 원이라면 세타필 로션(전신)과 바세린 립밤을 먼저 사는 편이 낫다.

7. 사기 전에 확인할 것
가격은 11월 26일 오전 8시 40~50분 쿠팡에서 확인한 값이고, 로켓배송·판매자·쿠폰에 따라 달라진다. 특히 '오늘 도착' 표기는 재고와 시간에 따라 바뀌므로 결제 직전에 한 번 더 확인하는 편이 좋다. 세일 기간에는 같은 상품이 여러 판매자에게 다른 가격으로 올라와 있으니, 용량과 개수를 확인하고 100ml(10g)당 단가로 비교해야 속지 않는다.
립밤·핸드크림처럼 향이 있는 제품은 향의 호불호가 크다. 뉴트로지나 핸드크림은 향이 랜덤 발송되므로 무향을 원하면 다른 상품을 골라야 한다.

한 줄 정리
겨울철 정전기와 각질은 '습도'와 '보습 막' 두 가지로 잡는다. 오늘 확인한 가격 기준으로 일리윤 집중크림 13,300원, 세타필 로션 13,600원, 뉴트로지나 핸드크림 7,000원, 바세린 립밤 5,460원 — 네 개를 다 사도 3만9,360원이다. 비싼 제품보다 중요한 것은 바르는 타이밍이다. 샤워 후 3분, 손 씻은 직후, 자기 전. 이 세 번을 지키면 같은 제품으로도 결과가 달라진다."""

EN_DESC = """Thursday 26 November, the day before Black Friday. The longer the heating runs, the lower indoor humidity falls — often below 40%. Dry air pulls moisture out of skin, and because dry air is a poor conductor, static charge builds up instead of draining away. That small shock when you touch a door handle is a signal that your skin is dry. Here are four products at prices confirmed on Coupang this morning; all four together come to 39,360 won.

1. Why winter brings static
Static builds when charge cannot leave an object. In summer, moisture in the air carries charge away; in winter, low humidity makes air behave like an insulator, so the same coat and the same door handle only sting in winter. There are two fixes: keep indoor humidity at 40–60%, and put a moisture barrier on the skin. A humidifier or drying laundry indoors handles the first; a moisturiser handles the second.

2. Illiyoon Ceramide Ato Concentrate Cream 230ml — 13,300 won
41% off the 22,900-won list price. At 5,783 won per 100ml it has the highest unit price of the four, because it is a concentrated cream for problem areas — face, elbows, knees — rather than a full-body product. 29,263 Coupang reviews at 5.0, Rocket Delivery arriving today, and the tube is marked "Fragrance Free" and "9 FREE". Good for anyone who wants to use the same cream on the face without fragrance.
How to use it: after washing, apply a thin layer before the skin is fully dry, then add a second layer on flaking areas. 230ml lasts two to three months on the face alone, about six weeks if you also use it on hands and elbows.

3. Cetaphil Moisturizing Lotion 591ml — 13,600 won
44% off 24,500 won, and the cheapest per millilitre of the four at 2,301 won per 100ml. The 591ml pump size suits full-body use after a shower. 245,818 Coupang reviews at 5.0 — far more than any other product here — and a Coupang "BEST AWARDS" badge.
The timing matters more than the product: apply within three minutes of showering, while the skin is still damp, so the water is sealed in rather than evaporating. Pat yourself partly dry with a towel, then work down the calves, arms and waist. One pump session a day makes 591ml last about two months.

4. Neutrogena Norwegian Formula Hand Cream 56g — 7,000 won
7,000 won with no discount, 1,250 won per 10g. That is the highest unit price here, but hands are washed more than ten times a day, so a hand cream gets used up fast. The 56g tube fits in a bag. 7,457 reviews at 4.5. The scent is shipped at random, so check the options if you need a specific one.
Apply to slightly damp hands after washing, starting from the back of the hand and pressing the remainder into the nail edges and between the fingers. At night, a thicker layer plus cotton gloves leaves the back of your hands far less cracked by morning.

5. Vaseline Lip Therapy Original 7g, two-pack — 5,460 won
45% off 10,000 won, 3,900 won per 10g. 32,449 reviews at 5.0. Lips have no sebaceous glands, so they cannot hold moisture on their own — which is why flaking starts there first in winter.
Apply thin layers three or more times a day rather than one thick coat. Used as a night mask, a thick layer leaves lips visibly smoother in the morning. Two 7g tins: one for the bag, one for the desk.

6. The total
13,300 + 13,600 + 7,000 + 5,460 = 39,360 won, against 64,400 won at list price — 25,040 won (38.9%) saved. For that, hands, face, body and lips are all covered.
If you have to prioritise: hands and lips crack first. Hands meet water all day; lips have no oil glands. With a 40,000-won budget, buy all four. With 20,000 won, start with the Cetaphil lotion for the body and the Vaseline lip balm.

7. Before you buy
Prices were checked on Coupang between 08:40 and 08:50 on 26 November and change with seller, coupons and Rocket Delivery status; the "arrives today" badge depends on stock and time. During sale periods the same product appears from several sellers at different prices, so compare volume and unit price per 100ml (or per 10g) rather than the headline number.
Fragrance is the other split: the Neutrogena hand cream ships at random, so choose a different product if you need fragrance-free.

In one line
Winter static and flaking are handled by two things: humidity and a moisture barrier. At today's prices — Illiyoon 13,300, Cetaphil 13,600, Neutrogena 7,000, Vaseline 5,460 — all four cost 39,360 won. Timing matters more than price: within three minutes of a shower, right after washing hands, and before bed."""

JA_DESC = """11月26日木曜日、明日はブラックフライデー。暖房をつける時間が長くなると室内の湿度は40%を下回る。湿度が下がると肌の水分は早く失われ、乾いた空気は電気を通しにくいため静電気がたまる。ドアノブを触ったときのあの小さな痛みは、肌が乾いているという合図だ。今朝クーポン（クーパン）で実際に確認した価格で、冬の保湿を担当する4品を選んだ。4つ全部買っても39,360ウォンだ。

1. 冬になぜ静電気が起きるのか
静電気は、たまった電荷が逃げられないときに起こる。夏は空気中の水分が電荷を運ぶが、冬は湿度が低く空気が絶縁体に近づく。だから同じ服で同じドアノブを触っても冬だけ痛い。対策は2つ。室内湿度を40〜60%に上げること、そして肌の表面に水分の膜を作ること。加湿器や室内干しで湿度を上げたら、残りの半分は保湿剤が担う。

2. イリユン セラミドアト集中クリーム 230ml — 13,300ウォン
定価22,900ウォンから41%引きの13,300ウォン。100mlあたり5,783ウォンで、4品の中では容量単価が最も高い。全身用ではなく、顔・ひじ・ひざなど割れやすい部分に使う濃厚クリームだからだ。クーポンのレビュー29,263件、評価5.0。ロケット配送で今日到着。商品には「Fragrance Free」「9 FREE」の表示がある。香りが苦手な人が顔にも使える。
使い方：洗顔後、完全に水分を拭き取る前に薄く伸ばし、かさついた部分にはもう一層重ねる。230mlは顔だけなら2〜3か月、手やひじにも使うと1か月半ほど。

3. セタフィル モイスチャライジングローション 591ml — 13,600ウォン
定価24,500ウォンから44%引きの13,600ウォン。100mlあたり2,301ウォンで4品中最安。591mlの大容量はシャワー後の全身使いに向く。レビュー245,818件・評価5.0で、この記事の商品では圧倒的に多い。クーポンの「BEST AWARDS」表示付き。
商品よりタイミングが重要だ。シャワー後3分以内、肌がまだ湿っているうちに塗ると、水分が蒸発せず膜の内側に閉じ込められる。タオルで軽く拭いた状態で、ふくらはぎ・腕・腰の順に塗る。1日1回全身で約2か月もつ。

4. ニュートロジーナ ノルウェーフォーミュラ ハンドクリーム 56g — 7,000ウォン
割引なしの7,000ウォン、10gあたり1,250ウォン。ハンド専用としては10g単価が最も高いが、手は1日に10回以上洗う部位なので減りが早い。56gのチューブはバッグに入れやすい。レビュー7,457件・評価4.5。香りはランダム発送なので、特定の香りが必要ならオプションを確認する。
手を洗って軽く水分が残った状態で手の甲から塗り、残りを爪の周りと指の間に押し込む。夜は厚めに塗って手袋をすれば、翌朝の手の甲のひび割れが少なくなる。

5. ヴァセリン リップセラピー オリジナル 7g×2個 — 5,460ウォン
定価10,000ウォンから45%引きの5,460ウォン、10gあたり3,900ウォン。レビュー32,449件・評価5.0。唇には皮脂腺がなく自分では水分を保てないため、冬は最初にかさつく部位だ。
一度に厚く塗るより、1日3回以上薄く重ねるほうがよい。夜に厚く塗って寝ると翌朝の唇がなめらかになる。7gが2個あれば、1個はバッグ、1個は机に置ける。

6. 4つ全部でいくらか
13,300+13,600+7,000+5,460＝39,360ウォン。定価合計64,400ウォンから25,040ウォン（38.9%）安い。手・顔・全身・唇をこれでカバーできる。
優先順位をつけるなら、冬に最初に割れるのは手の甲と唇だ。手は一日中水に触れ、唇には皮脂腺がない。予算4万ウォンなら4つ全部、2万ウォンならセタフィルのローションとヴァセリンのリップを先に買うほうがよい。

7. 買う前に確認すること
価格は11月26日午前8時40〜50分にクーポンで確認した値で、販売者・クーポン・ロケット配送の状況で変わる。「今日到着」の表示も在庫と時間で変わるので、決済直前に一度確認したい。セール期間は同じ商品が複数の販売者から異なる価格で出るので、容量と個数を確認し、100ml（10g）あたりの単価で比べるのが安全だ。
香りものは好みが分かれる。ニュートロジーナのハンドクリームは香りがランダム発送なので、無香料が必要なら別の商品を選ぶ。

一行まとめ
冬の静電気とかさつきは「湿度」と「保湿の膜」で抑える。今日の価格ならイリユン13,300ウォン、セタフィル13,600ウォン、ニュートロジーナ7,000ウォン、ヴァセリン5,460ウォンで、4つ全部39,360ウォン。高い製品より大事なのは塗るタイミングだ。シャワー後3分、手洗い直後、就寝前。"""

ZH_DESC = """11月26日周四，明天就是黑色星期五。随着开暖气的时间变长，室内湿度会降到40%以下。湿度低，皮肤水分流失更快；干燥的空气不易导电，静电便容易堆积。碰到门把手时那一下刺痛，就是皮肤干燥的信号。以下是今早在Coupang实际确认的价格，挑出负责冬季保湿的四件商品，四件全买也只要39,360韩元。

1. 冬天为什么会有静电
静电产生于电荷无法释放的时候。夏天空气中的水分会带走电荷，冬天气候干燥，空气接近绝缘体，所以同一件外套、同一个门把手，只有冬天会被电。解决办法有两个：把室内湿度维持在40%—60%，并在皮肤表面形成一层保湿膜。加湿器或室内晾衣负责前者，保湿产品负责后者。

2. Illiyoon 神经酰胺Atto集中面霜 230ml — 13,300韩元
原价22,900韩元，打41%折扣后为13,300韩元。每100ml 5,783韩元，是四件中单位容量价格最高的，因为它是用于脸部、手肘、膝盖等易裂部位的浓缩面霜，而不是全身用。Coupang评价29,263条、评分5.0，火箭配送今日送达，管身标注"Fragrance Free"和"9 FREE"，适合不想在脸上用香精的人。
用法：洁面后趁水分未完全擦干，薄薄涂一层，起皮部位再叠一层。230ml只用于脸部可用两三个月，连手和手肘一起用大约一个半月。

3. Cetaphil 保湿乳液 591ml — 13,600韩元
原价24,500韩元，打44%折扣后为13,600韩元，每100ml 2,301韩元，是四件中最便宜的。591ml大容量适合洗澡后全身使用。评价245,818条、评分5.0，是本文商品中评价最多的，并带有Coupang"BEST AWARDS"标识。
比产品更重要的是时机：洗澡后3分钟内、皮肤仍潮湿时涂抹，水分才会被锁在膜内而不是蒸发。用毛巾轻拍后，依次涂小腿、手臂、腰部。每天一次全身使用，591ml大约可用两个月。

4. Neutrogena 挪威配方护手霜 56g — 7,000韩元
无折扣7,000韩元，每10g 1,250韩元。作为手部专用单品，它的单位价格最高，但手一天要洗十几次，消耗很快。56g软管便于放进包里。评价7,457条、评分4.5。香味随机发货，若需要特定香型要确认选项。
洗完手在微湿状态下从手背开始涂，剩下的按压进指甲边缘和指缝。睡前厚涂并戴上手套，第二天手背的干裂会明显减少。

5. Vaseline Lip Therapy 原味 7g 两个装 — 5,460韩元
原价10,000韩元，打45%折扣后为5,460韩元，每10g 3,900韩元。评价32,449条、评分5.0。嘴唇没有皮脂腺，无法自行锁水，所以冬天最先起皮。
与其一次厚涂，不如一天薄涂三次以上。睡前厚涂当作唇膜，第二天嘴唇会明显平滑。两个7g，一个放包里，一个放桌上。

6. 四件一共多少钱
13,300 + 13,600 + 7,000 + 5,460 = 39,360韩元。原价合计64,400韩元，省下25,040韩元（38.9%）。这笔钱同时覆盖手、脸、全身和嘴唇。
如果要排优先顺序：冬天最先裂开的是手背和嘴唇。手整天接触水，嘴唇没有皮脂腺。预算4万韩元就四件全买；预算2万韩元，先买Cetaphil乳液（全身）和Vaseline唇膏。

7. 购买前要确认
价格是11月26日上午8点40—50分在Coupang确认的，会随卖家、优惠券和火箭配送状态变化；"今日送达"也取决于库存和时间，结账前最好再看一次。促销期间同一商品会有多个卖家以不同价格上架，务必确认容量和数量，按每100ml（或每10g）的单价比较。
香味类产品因人而异。Neutrogena护手霜的香味随机发货，需要无香型请选择其他商品。

一句话总结
冬季静电和起皮靠两件事解决：湿度和保湿膜。以今天确认的价格，Illiyoon 13,300、Cetaphil 13,600、Neutrogena 7,000、Vaseline 5,460，四件共39,360韩元。比价格更重要的是时机：洗澡后3分钟、洗手后立刻、睡前。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "store": "쿠팡",
    "priceKrw": 13300,
    "releaseDate": "2026-11-26",
    "rating": 4.8,
    "imageUrl": C,
    "images": [G1, G2, G3, G4],
    "affiliateUrl": q("겨울 보습 크림"),
    "affiliatePlatform": "Coupang",
    "exampleItems": [
        {
            "name": "일리윤 세라마이드 아토 집중크림 230ml",
            "brand": "ILLIYOON",
            "priceKrw": 13300,
            "imageUrl": G1,
            "url": q("일리윤 세라마이드 아토 집중크림"),
            "category": "22,900→13,300원 · 41%",
        },
        {
            "name": "세타필 모이스춰라이징 로션 591ml",
            "brand": "Cetaphil",
            "priceKrw": 13600,
            "imageUrl": G2,
            "url": q("세타필 모이스춰라이징 로션"),
            "category": "24,500→13,600원 · 44%",
        },
        {
            "name": "뉴트로지나 노르웨이젼 포뮬러 핸드크림 56g",
            "brand": "Neutrogena",
            "priceKrw": 7000,
            "imageUrl": G3,
            "url": q("뉴트로지나 노르웨이 핸드크림"),
            "category": "7,000원 · 10g당 1,250원",
        },
        {
            "name": "바세린 립 테라피 립밤 오리지널 7g 2개",
            "brand": "Vaseline",
            "priceKrw": 5460,
            "imageUrl": G4,
            "url": q("바세린 립 테라피 립밤 오리지널"),
            "category": "10,000→5,460원 · 45%",
        },
    ],
    "i18n": {
        "ko": {
            "title": "겨울 정전기·각질, 3만9천원으로 잡는다 — 11월 26일 실측 보습템 4선",
            "summary": "일리윤 집중크림 13,300원, 세타필 로션 13,600원, 뉴트로지나 핸드크림 7,000원, 바세린 립밤 5,460원. 네 개를 다 사도 3만9,360원입니다. 정전기가 생기는 이유와 바르는 타이밍까지 숫자로 정리했습니다.",
            "description": KO_DESC,
            "tasteReview": [
                "일리윤 세라마이드 아토 집중크림 230ml: 22,900→13,300원(41%), 100ml당 5,783원, 후기 29,263·5.0",
                "세타필 모이스춰라이징 로션 591ml: 24,500→13,600원(44%), 100ml당 2,301원, 후기 245,818·5.0",
                "뉴트로지나 핸드크림 56g 7,000원(10g당 1,250원), 바세린 립 테라피 오리지널 7g 2개 5,460원(45%)",
                "4종 합계 39,360원 — 정가 64,400원 대비 25,040원(38.9%) 절약, 실내 습도 40~60% 유지가 먼저",
            ],
            "tips": "가격은 2026년 11월 26일 오전 8시 40~50분 쿠팡에서 확인한 값이며 판매자·쿠폰·재고에 따라 달라질 수 있습니다. 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있습니다.",
        },
        "en": {
            "title": "Winter Static and Flaking Skin, Covered for 39,360 Won — Four Moisture Picks Priced Today",
            "summary": "Illiyoon cream 13,300 won, Cetaphil lotion 13,600, Neutrogena hand cream 7,000, Vaseline lip balm 5,460 — all four for 39,360 won. Why winter brings static, and when to apply each one.",
            "description": EN_DESC,
            "tasteReview": [
                "Illiyoon Ceramide Ato Concentrate Cream 230ml: 22,900→13,300 won (41%), 5,783 won per 100ml, 29,263 reviews at 5.0",
                "Cetaphil Moisturizing Lotion 591ml: 24,500→13,600 won (44%), 2,301 won per 100ml, 245,818 reviews at 5.0",
                "Neutrogena hand cream 56g at 7,000 won (1,250 per 10g); Vaseline Lip Therapy Original 7g two-pack at 5,460 won (45% off)",
                "All four total 39,360 won against 64,400 at list price — 25,040 won (38.9%) saved; keep indoor humidity at 40–60% first",
            ],
            "tips": "Prices were checked on Coupang between 08:40 and 08:50 on 26 November 2026 and may change with seller, coupons and stock. This post contains affiliate links and may earn a commission.",
        },
        "ja": {
            "title": "冬の静電気とかさつきは39,360ウォンで抑える — 11月26日実測の保湿4品",
            "summary": "イリユン集中クリーム13,300ウォン、セタフィルローション13,600ウォン、ニュートロジーナハンドクリーム7,000ウォン、ヴァセリンリップ5,460ウォン。4つ全部でも39,360ウォン。静電気の理由と塗るタイミングまで整理しました。",
            "description": JA_DESC,
            "tasteReview": [
                "イリユン セラミドアト集中クリーム230ml：22,900→13,300ウォン（41%）、100mlあたり5,783ウォン、レビュー29,263件・5.0",
                "セタフィル モイスチャライジングローション591ml：24,500→13,600ウォン（44%）、100mlあたり2,301ウォン、レビュー245,818件・5.0",
                "ニュートロジーナ ハンドクリーム56g 7,000ウォン（10gあたり1,250ウォン）、ヴァセリン リップセラピー オリジナル7g×2 5,460ウォン（45%引き）",
                "4品合計39,360ウォン — 定価64,400ウォンから25,040ウォン（38.9%）節約、室内湿度40〜60%維持が先",
            ],
            "tips": "価格は2026年11月26日午前8時40〜50分にクーポンで確認した値で、販売者・クーポン・在庫により変わります。本記事はアフィリエイトリンクを含み、手数料を受け取る場合があります。",
        },
        "zh": {
            "title": "冬季静电与起皮，39,360韩元全搞定——11月26日实测四款保湿好物",
            "summary": "Illiyoon集中面霜13,300韩元、Cetaphil乳液13,600韩元、Neutrogena护手霜7,000韩元、Vaseline唇膏5,460韩元，四件全买39,360韩元。附静电成因与涂抹时机。",
            "description": ZH_DESC,
            "tasteReview": [
                "Illiyoon神经酰胺Atto集中面霜230ml：22,900→13,300韩元（41%），每100ml 5,783韩元，评价29,263条、5.0分",
                "Cetaphil保湿乳液591ml：24,500→13,600韩元（44%），每100ml 2,301韩元，评价245,818条、5.0分",
                "Neutrogena护手霜56g 7,000韩元（每10g 1,250韩元），Vaseline Lip Therapy原味7g两件5,460韩元（45%折扣）",
                "四件合计39,360韩元——较原价64,400韩元省25,040韩元（38.9%），先把室内湿度维持在40%—60%",
            ],
            "tips": "价格为2026年11月26日上午8点40—50分在Coupang确认，可能因卖家、优惠券和库存变动。本文含联盟链接，可能获得佣金。",
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
