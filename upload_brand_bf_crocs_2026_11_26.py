#!/usr/bin/env python3
"""3편 크록스 블랙프라이데이 앵콜 (4개국어) → Supabase posts + ISR revalidate.

근거 (2026-11-26 13:20~13:35 KST crocs.co.kr 직접 확인)
 - 블랙프라이데이 앵콜 2026.11.25 09:00 ~ 11.30 09:00, 최대 70%
 - 2개 구매 15%, 3개 이상 25% 추가 할인 / 지비츠 참 5개 40% / 크록스 클럽 첫 구매 15%
 - 11/26(목) 20시 블프 앵콜 라이브: 타임특가 + 추가 할인 + 사은품 (live.crocskorea.com 11,111원 추가 할인 안내)
 - 바야 라인드 클로그 84,900→49,900(41%, 아미그린/멀티) / 올모스트 화이트 47,900(44%), 리뷰 397·4.7
 - 바야 플랫폼 퍼즈 스트랩 라인드 클로그 99,900→59,900(40%)
 - 언퍼게터블 코지 클로그 84,900→64,900(24%)
 - 멜로우 리커버리 클로그 79,900→29,900(63%)
 - 클래식 클로그 정가 69,900, 컬러에 따라 54,900(21%)·49,900(29%)·29,900(57%), 리뷰 159·4.8
 - 제품 사진: 공식몰 제품컷 5장 3:4(1200×1600) 정규화. AI 생성 0장.
"""
from brand_bf_common import publish, q

SLUG = "crocs-blackfriday-encore-2026-official-store"

G1 = "/images/products/bfb-crocs-baya-lined.jpg"
G2 = "/images/products/bfb-crocs-baya-platform-fuzz.jpg"
G3 = "/images/products/bfb-crocs-unfurgettable-cozy.jpg"
G4 = "/images/products/bfb-crocs-mellow-recovery.jpg"
G5 = "/images/products/bfb-crocs-classic.jpg"

KO = """크록스가 11월 25일 오전 9시부터 '블랙프라이데이 앵콜'을 열었다. 11월 16일 시작한 본 행사가 25일 오전 9시에 끝나자마자 바로 이어서 연 세일이다. 종료는 11월 30일 오전 9시다. 본 행사보다 할인 폭이 커진 대신 기간이 5일로 짧다.
11월 26일 오후 공식몰에서 확인한 가격과 조건을 정리했다.

1. 언제까지, 얼마나
기간은 11월 25일 오전 9시부터 11월 30일 오전 9시까지다. 마지막 날 밤 12시가 아니라 30일 아침 9시에 끝난다는 점을 먼저 기억해야 한다. 크록스는 매년 이렇게 오전 9시에 시작하고 오전 9시에 닫는다.
최대 할인율은 70%다. 다만 이 수치는 재고 정리 상품에 붙는 값이고, 오늘 확인한 대표 모델은 24~63% 구간에 퍼져 있다. 첫 화면에는 지비츠 참 최대 30% 할인 안내도 함께 걸려 있다.

2. 담을수록 싸진다 — 2개 15%, 3개 25%
이번 앵콜의 핵심은 추가 할인이다. 대상 상품을 2개 사면 15%, 3개 이상 사면 25%가 더 빠진다. 상품 상세페이지 상단에도 '블랙프라이데이 앵콜 | 2개 구매 시 15% 할인 / 3개 이상 구매 시 추가 25% 할인'이 표시돼 있다.
크록스는 원래 계절 단위로 사는 브랜드다. 여름 클로그 한 켤레, 겨울 라인드 한 켤레, 집에서 신을 한 켤레면 3개가 채워지고 25% 구간에 들어간다. 오늘 확인한 세 켤레를 그대로 계산하면 이렇다. 바야 라인드 클로그 49,900원, 바야 플랫폼 퍼즈 스트랩 라인드 클로그 59,900원, 멜로우 리커버리 클로그 29,900원을 합치면 139,700원이다. 여기에 25%가 적용되면 104,775원이 된다.
단, 추가 할인은 '대상 상품'에만 붙고 일부 프로모션·쿠폰과 중복되지 않는다. 장바구니에서 25%가 실제로 계산되는지 확인해야 한다.
지비츠 참은 따로 5개 사면 40% 할인이다. 참은 개당 5,000~7,000원대라 5개를 모아도 2만 원 후반~3만 원대다. 신발에 캐릭터를 붙이는 용도라면 이 구간을 노리는 편이 낫다.

3. 오늘 실제로 얼마인가
바야 라인드 클로그는 정가 84,900원에서 41% 내린 49,900원이다(아미 그린/멀티). 같은 모델 올모스트 화이트 컬러는 44% 내린 47,900원으로, 컬러에 따라 2,000원 차이가 난다. 리뷰 397개에 평점 4.7이다.
바야 플랫폼 퍼즈 스트랩 라인드 클로그는 99,900원에서 40% 내린 59,900원, 언퍼게터블 코지 클로그는 84,900원에서 24% 내린 64,900원이다. 가장 많이 빠진 모델은 멜로우 리커버리 클로그로, 79,900원에서 63% 내린 29,900원이다. 회복용 슬리퍼로 나온 모델이라 쿠션감이 두껍고, 집안에서 신기 좋다.
키즈 라인도 같이 내려간다. 바야 라인드 클로그 키즈는 19,900~39,900원, 언퍼게터블 클로그 키즈는 79,900원이다. 성인용과 키즈용을 함께 담아 3개 25% 구간을 채우는 방법도 있다.

4. 같은 신발인데 색에 따라 2만 원 차이
클래식 클로그는 정가 69,900원이다. 그런데 오늘 화면에서는 컬러에 따라 가격이 54,900원(21% 할인), 49,900원(29%), 29,900원(57%)으로 갈렸다. 같은 모델, 같은 사이즈인데 색만 바꿔도 2만 원 이상 차이가 난다.
블랙처럼 수요가 꾸준한 색은 할인이 거의 없고, 시즌 컬러나 재고가 남은 색은 크게 빠진다. 신발을 신발장에 넣어두고 필요할 때 꺼내 신는 품목이라면, 색을 조금 양보하고 가격을 가져오는 쪽이 합리적이다. 반대로 매일 신는 기본 색이라면 정가에 가까워도 블랙을 고르는 편이 낫다.
사이즈도 확인해야 한다. 오늘 클래식 클로그는 210~300까지 재고가 있었고, 310은 입고 알림, 320 이상은 품절이었다. 발이 큰 편이라면 원하는 색이 있어도 사이즈가 없을 수 있다.

5. 오늘 밤 8시 라이브
11월 26일 오후 8시에 '블프 앵콜 라이브'가 열린다. 라이브에서는 타임특가와 추가 할인, 사은품이 나온다. 라이브 전용 페이지에는 11,111원 추가 할인 안내도 걸려 있다. 라이브 특가는 방송 중에만 열리고 수량이 짧다.
라이브를 볼 생각이라면 미리 장바구니에 담아두는 편이 낫다. 방송 중에 사이즈가 빠지면 할인만 보고 못 사는 경우가 생긴다.

6. 11월 30일 오전 9시, 그 뒤에는 정가
앵콜은 5일짜리다. 11월 30일 오전 9시가 지나면 남은 재고는 정가로 돌아간다. 오늘 63%까지 빠진 멜로우 리커버리처럼 할인 폭이 큰 모델은 행사 후 가격 차이가 5만 원 가까이 벌어진다.
블랙프라이데이 당일인 27일에 맞춰 사려는 계획이라면, 27일은 앵콜 셋째 날이라는 점만 기억하면 된다. 굳이 27일을 기다릴 이유는 없다. 오히려 사이즈가 먼저 빠진다.

7. 사기 전에 확인할 것
첫째, 컬러별 가격을 비교해야 한다. 같은 모델이라도 색에 따라 20~30% 차이가 나는 경우가 흔하다.
둘째, 2개·3개 추가 할인이 실제로 적용되는 상품인지 확인해야 한다. 행사 대상에서 빠진 상품은 세일가만 적용된다.
셋째, 크록스 클럽 가입 첫 구매 15% 쿠폰이 별도로 있다. 이 쿠폰이 앵콜 추가 할인과 겹치는지는 상품과 결제 조건에 따라 다르다.
넷째, 사이즈 표를 봐야 한다. 크록스는 여유 있게 나오는 편이라 정사이즈보다 반 사이즈 작게 신는 사람도 많다. 신발마다 핏이 다르므로 리뷰의 '크게 나옴/작게 나옴' 비율을 확인하는 편이 좋다.

한 줄 정리
크록스 블랙프라이데이 앵콜은 11월 30일 오전 9시에 끝난다. 바야 라인드 클로그 84,900→49,900원, 바야 플랫폼 퍼즈 스트랩 라인드 99,900→59,900원, 멜로우 리커버리 79,900→29,900원이다. 3개를 담으면 25%가 더 빠지므로, 한 켤레만 필요해도 색이 다른 켤레나 키즈용을 함께 담아 구간을 맞추는 편이 유리하다."""

EN = """Crocs opened a "Black Friday Encore" at 09:00 on 25 November, the moment its main event — which started on 16 November — closed. The encore runs to 09:00 on 30 November: deeper discounts than the main event, but only five days.
Here is what the official store showed on the afternoon of 26 November.

1. Until when, and how much
The window is 09:00 on 25 November to 09:00 on 30 November. Note the 9am finish rather than midnight — Crocs starts and stops its sales at 9am every year.
The headline rate is up to 70%, which applies to clearance stock; the models we checked spread from 24% to 63%. The front page also advertises up to 30% off Jibbitz charms.

2. The more you add, the less you pay — 15% for two, 25% for three
The core of this encore is the basket discount: 15% off two qualifying pairs, 25% off three or more. Product pages carry the same notice at the top: "Black Friday Encore | 15% off when you buy two, an extra 25% off for three or more."
Crocs is a brand people buy by season. One summer clog, one lined winter pair and one pair for indoors fills the three-item tier. Today's three pairs add up like this: Baya Lined Clog 49,900 won, Baya Platform Fuzz Strap Lined Clog 59,900 won and Mellow Recovery Clog 29,900 won total 139,700 won, and 25% brings that to 104,775 won.
The extra discount applies only to qualifying items and does not stack with every promotion or coupon, so confirm in the cart that 25% is actually deducted.
Jibbitz charms have their own deal: 40% off five. Charms run 5,000-7,000 won each, so five land in the high 20,000 to low 30,000 won range — the right tier for decorating a pair.

3. Today's actual prices
The Baya Lined Clog is 49,900 won, 41% off 84,900, in army green/multi. The Almost White colour of the same model is 47,900 won, 44% off — a 2,000-won difference by colour. It carries 397 reviews at 4.7.
The Baya Platform Fuzz Strap Lined Clog is 59,900 won (40% off 99,900) and the Unfurgettable Cozy Clog is 64,900 won (24% off 84,900). The deepest cut is the Mellow Recovery Clog at 29,900 won, 63% off 79,900 — a thick-soled recovery slide that works well indoors.
Kids' lines drop too: the Kids Baya Lined Clog is 19,900-39,900 won, and the Kids Unfurgettable Clog is 79,900 won. Pairing an adult and a kids' pair is an easy way to reach the three-item tier.

4. Same shoe, 20,000 won apart by colour
The Classic Clog lists at 69,900 won, but today's page showed 54,900 won (21% off), 49,900 won (29%) and 29,900 won (57%) depending on colour. Same model, same size, more than 20,000 won between two colours.
Steady sellers like black barely discount; seasonal and leftover colours go deep. If the pair lives in a shoe cupboard and comes out occasionally, trading colour for price is reasonable. If it is the pair you wear every day, paying closer to list for black is usually the better call.
Check sizes as well. Today the Classic Clog had 210-300 in stock, 310 on restock alert and 320 and up sold out. If your feet are larger, the colour you want may not have your size.

5. Live show at 8pm tonight
A "Black Friday Encore Live" opens at 8pm on 26 November with time deals, extra discounts and gifts. The live page also advertises an additional 11,111-won discount. Live pricing runs only during the broadcast and in short quantities.
If you plan to watch, put items in the cart beforehand; sizes disappear mid-broadcast and the discount alone will not save the purchase.

6. 09:00 on 30 November, then back to list price
The encore lasts five days. After 09:00 on 30 November whatever is left returns to list price. On a model like the Mellow Recovery Clog, 63% off today, the gap afterwards is close to 50,000 won.
If you were planning to buy on Black Friday itself, the 27th is simply the third day of this encore — no reason to wait, and sizes go first.

7. Before you pay
Compare colours: a 20-30% spread across colours of one model is common. Check that the two- and three-pair discount actually applies to what you picked; excluded items take only the sale price. The Crocs Club first-purchase 15% coupon is separate, and whether it stacks with the encore discount depends on the item and payment conditions. Finally, read the size guide — Crocs run roomy, and many buyers size down half a size; check the "runs large / runs small" split in reviews for each model.

In one line
The Crocs Black Friday Encore ends at 09:00 on 30 November. Baya Lined Clog 84,900 to 49,900 won, Baya Platform Fuzz Strap Lined 99,900 to 59,900, Mellow Recovery 79,900 to 29,900. Three pairs take another 25% off, so even if you need one pair, adding a different colour or a kids' pair to reach the tier pays."""

JA = """クロックスが11月25日午前9時から「ブラックフライデー アンコール」を開いた。11月16日に始まった本行事が25日午前9時に終わると同時に続けて開いたセールだ。終了は11月30日午前9時。本行事より割引幅が大きい代わりに、期間は5日と短い。
11月26日午後に公式ストアで確認した価格と条件をまとめた。

1. いつまで、どれくらい
期間は11月25日午前9時から11月30日午前9時まで。最終日の夜12時ではなく、30日の朝9時に終わる点を先に覚えたい。クロックスは毎年こうして午前9時に始まり午前9時に閉じる。
最大割引率は70%。ただしこれは在庫整理商品に付く値で、今日確認した代表モデルは24〜63%に散っている。最初の画面にはジビッツチャーム最大30%割引の案内も出ている。

2. 入れるほど安くなる — 2足15%、3足25%
今回のアンコールの核は追加割引だ。対象商品を2足買うと15%、3足以上で25%がさらに引かれる。商品詳細ページの上部にも「ブラックフライデー アンコール｜2足購入で15%割引／3足以上で追加25%割引」と表示されている。
クロックスは季節単位で買うブランドだ。夏のクロッグ1足、冬のラインド1足、室内用1足で3足に届き、25%の帯に入る。今日確認した3足で計算するとこうなる。バヤ ラインド クロッグ49,900ウォン、バヤ プラットフォーム ファズ ストラップ ラインド クロッグ59,900ウォン、メロウ リカバリー クロッグ29,900ウォンの合計は139,700ウォン。ここに25%が適用されると104,775ウォンになる。
ただし追加割引は「対象商品」にのみ付き、一部のプロモーションやクーポンとは重複しない。カートで25%が実際に計算されるか確認したい。
ジビッツチャームは別枠で5個買うと40%割引だ。チャームは1個5,000〜7,000ウォン台なので、5個集めても2万ウォン台後半から3万ウォン台。靴にキャラクターを付ける用途ならこの帯を狙うほうがいい。

3. 今日の実際の価格
バヤ ラインド クロッグは定価84,900ウォンから41%引きの49,900ウォン（アーミーグリーン／マルチ）。同じモデルのオールモストホワイトは44%引きの47,900ウォンで、色によって2,000ウォンの差が出る。レビュー397件、評価4.7。
バヤ プラットフォーム ファズ ストラップ ラインド クロッグは99,900ウォンから40%引きの59,900ウォン、アンフォゲッタブル コージー クロッグは84,900ウォンから24%引きの64,900ウォン。最も下がったのはメロウ リカバリー クロッグで、79,900ウォンから63%引きの29,900ウォン。回復用スリッパとして出たモデルで、クッションが厚く室内使いに向く。
キッズラインも下がる。キッズ バヤ ラインド クロッグは19,900〜39,900ウォン、キッズ アンフォゲッタブル クロッグは79,900ウォン。大人用とキッズ用を一緒に入れて3足25%の帯を満たす方法もある。

4. 同じ靴なのに色で2万ウォン差
クラシック クロッグは定価69,900ウォン。ところが今日の画面では色によって54,900ウォン（21%引き）、49,900ウォン（29%）、29,900ウォン（57%）に分かれていた。同じモデル、同じサイズで、色を変えるだけで2万ウォン以上の差になる。
ブラックのように需要が安定した色はほとんど割引がなく、シーズンカラーや在庫の残った色は大きく下がる。靴箱に入れて必要時に履く品なら、色を少し譲って価格を取るほうが合理的だ。逆に毎日履く基本色なら、定価に近くてもブラックを選ぶほうがいい。
サイズも確認したい。今日のクラシック クロッグは210〜300まで在庫があり、310は入荷通知、320以上は品切れだった。足が大きい人は、欲しい色があってもサイズがないことがある。

5. 今夜8時ライブ
11月26日午後8時に「ブラックフライデー アンコール ライブ」が開く。ライブではタイム特価と追加割引、ノベルティが出る。ライブ専用ページには11,111ウォン追加割引の案内もある。ライブ特価は放送中だけ開かれ、数量は短い。
見る予定なら事前にカートへ入れておきたい。放送中にサイズが消えると、割引だけ見て買えないことが起きる。

6. 11月30日午前9時、その後は定価
アンコールは5日間だ。11月30日午前9時を過ぎると残った在庫は定価に戻る。今日63%まで下がったメロウ リカバリーのようなモデルは、終了後の価格差が5万ウォン近く開く。
ブラックフライデー当日の27日に合わせて買う計画なら、27日はアンコール3日目だということだけ覚えておけばいい。わざわざ27日を待つ理由はない。むしろサイズが先に消える。

7. 買う前に確認すること
第一に色別の価格を比べること。同じモデルでも色によって20〜30%差が出ることはよくある。第二に、2足・3足の追加割引が実際に適用される商品かどうか。対象外の商品はセール価格だけが適用される。第三に、クロックス クラブ入会の初回購入15%クーポンが別にあり、これがアンコールの追加割引と重なるかは商品と決済条件による。第四にサイズ表。クロックスはゆったり作られており、定寸より半サイズ下げる人も多い。モデルごとにフィットが違うので、レビューの「大きめ／小さめ」の比率を見るといい。

ひとことで
クロックスのブラックフライデー アンコールは11月30日午前9時に終わる。バヤ ラインド クロッグ84,900→49,900ウォン、バヤ プラットフォーム ファズ ストラップ ラインド99,900→59,900ウォン、メロウ リカバリー79,900→29,900ウォン。3足で25%がさらに引かれるので、1足だけ必要でも色違いやキッズ用を足して帯を満たすほうが得だ。"""

ZH = """卡骆驰在11月25日上午9点开启了「黑色星期五返场」。11月16日开始的正式活动在25日上午9点结束，返场紧接着开始，到11月30日上午9点结束——折扣比正场更深，但只持续5天。
以下是11月26日下午在官方商城确认的价格与条件。

1. 到什么时候，便宜多少
期间为11月25日上午9点至11月30日上午9点。注意是30日早上9点结束，而不是最后一晚12点，卡骆驰每年都在上午9点开始、上午9点结束。
最高折扣为70%，出现在清库存商品上；我们确认的代表型号分布在24%至63%。首屏还挂着智必星最高30%折扣的提示。

2. 越凑越便宜——2件15%、3件25%
这次返场的核心是数量折扣：买2件15%，3件以上25%。商品详情页顶部也写着「黑五返场｜买2件15%、3件以上再减25%」。
卡骆驰是按季节买的品牌：一双夏季洞洞鞋、一双加绒冬款、一双室内穿，正好凑满3件。按今天确认的三双计算：Baya Lined 49,900韩元、Baya Platform Fuzz Strap Lined 59,900韩元、Mellow Recovery 29,900韩元，合计139,700韩元，再减25%即104,775韩元。
但追加折扣只对「对象商品」生效，且不与部分促销和优惠券叠加，请在购物车确认25%是否真的被扣除。
智必星另有买5个40%的优惠。单件5,000至7,000韩元，5个也就2万中后段到3万韩元区间，想装饰鞋子的话这个档位更合适。

3. 今天的实际价格
Baya Lined 洞洞鞋由84,900降至49,900韩元（41%，军绿/多色）；同款Almost White色为47,900韩元（44%），颜色不同差2,000韩元。评价397条、评分4.7。
Baya Platform Fuzz Strap Lined 99,900→59,900韩元（40%），Unfurgettable Cozy 84,900→64,900韩元（24%）。降幅最大的是Mellow Recovery，79,900→29,900韩元（63%），厚底恢复拖鞋，适合室内穿。
儿童线同样下调：Kids Baya Lined 19,900～39,900韩元，Kids Unfurgettable 79,900韩元。成人款加儿童款搭配，很容易凑到3件25%。

4. 同一双鞋，颜色差2万韩元
经典洞洞鞋标价69,900韩元，但今天的页面按颜色分为54,900韩元（21%）、49,900韩元（29%）和29,900韩元（57%）。同款同码，换个颜色差价超过2万韩元。
黑色这类稳定款几乎不打折，季节色和剩货颜色降得最狠。如果这双鞋放在鞋柜里偶尔穿，牺牲颜色换价格更合理；如果是每天穿的基础款，即使接近原价也该选黑色。
尺码也要看。今天经典洞洞鞋210至300有货，310到货提醒，320以上售罄。脚大的人可能看中的颜色没有尺码。

5. 今晚8点直播
11月26日晚8点开「黑五返场直播」，有时段特价、追加折扣与赠品，直播专页还挂着再减11,111韩元的提示。直播价只在播出期间有效，数量很少。
打算看直播的话提前放进购物车；播出中尺码一旦没了，只看到折扣也买不到。

6. 11月30日上午9点，之后回到原价
返场只有5天。30日上午9点过后，剩余库存回到原价。像今天降63%的Mellow Recovery，结束后价差接近5万韩元。
若原计划在黑五当天27日买，记住27日只是返场第3天即可，没有等的必要，反而尺码先消失。

7. 购买前确认
一是比较各颜色价格，同款不同色差20%至30%很常见。二是确认所选商品是否适用2件、3件追加折扣，排除商品只享受折扣价。三是Crocs Club入会首购15%券另计，能否与返场折扣叠加取决于商品与支付条件。四是看尺码表，卡骆驰偏宽松，不少人会小半码选；各款版型不同，建议看评论里「偏大／偏小」的比例。

一句话总结
卡骆驰黑五返场在11月30日上午9点结束。Baya Lined 84,900→49,900韩元，Baya Platform Fuzz Strap Lined 99,900→59,900韩元，Mellow Recovery 79,900→29,900韩元。三件再减25%，所以即使只需要一双，添一双不同颜色或儿童款凑档更划算。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "k-fashion",
    "store": "크록스 공식몰",
    "priceKrw": 49900,
    "releaseDate": "2026-11-26",
    "rating": 4.7,
    "imageUrl": G1,
    "images": [G1, G2, G3, G4, G5],
    "affiliateUrl": q("크록스 바야 라인드 클로그"),
    "affiliatePlatform": "Coupang",
    "exampleItems": [
        {"name": "바야 라인드 클로그", "brand": "Crocs", "priceKrw": 49900, "imageUrl": G1,
         "url": q("크록스 바야 라인드 클로그"), "category": "84,900→49,900원 · 41%"},
        {"name": "바야 플랫폼 퍼즈 스트랩 라인드 클로그", "brand": "Crocs", "priceKrw": 59900, "imageUrl": G2,
         "url": q("크록스 바야 플랫폼 퍼즈 스트랩"), "category": "99,900→59,900원 · 40%"},
        {"name": "언퍼게터블 코지 클로그", "brand": "Crocs", "priceKrw": 64900, "imageUrl": G3,
         "url": q("크록스 언퍼게터블 코지 클로그"), "category": "84,900→64,900원 · 24%"},
        {"name": "멜로우 리커버리 클로그", "brand": "Crocs", "priceKrw": 29900, "imageUrl": G4,
         "url": q("크록스 멜로우 리커버리 클로그"), "category": "79,900→29,900원 · 63%"},
        {"name": "클래식 클로그", "brand": "Crocs", "priceKrw": 29900, "imageUrl": G5,
         "url": q("크록스 클래식 클로그"), "category": "69,900원 · 컬러별 29,900~54,900원"},
    ],
    "i18n": {
        "ko": {
            "title": "크록스 블프 앵콜, 30일 오전 9시까지 — 3켤레 담으면 25% 더, 29,900원 클로그 실측",
            "summary": "11월 30일 09:00 마감, 최대 70%. 바야 라인드 84,900→49,900원, 바야 플랫폼 퍼즈 99,900→59,900원, 멜로우 리커버리 79,900→29,900원. 2개 15%·3개 25% 추가 할인과 컬러별 가격차, 오늘 밤 8시 라이브까지 정리했습니다.",
            "description": KO,
            "tasteReview": [
                "기간: 2026.11.25 09:00 ~ 11.30 09:00, 최대 70%",
                "추가 할인: 대상 2개 15%, 3개 이상 25% / 지비츠 참 5개 40% / 크록스 클럽 첫 구매 15%",
                "바야 라인드 84,900→49,900원(41%), 바야 플랫폼 퍼즈 99,900→59,900원(40%), 멜로우 리커버리 79,900→29,900원(63%)",
                "클래식 클로그 정가 69,900원, 컬러별 29,900~54,900원 / 11월 26일 20시 라이브 타임특가·11,111원 추가 할인",
            ],
            "tips": "가격과 기간은 2026년 11월 26일 오후 크록스 공식몰에서 확인한 값입니다. 추가 할인은 대상 상품에만 적용되고 일부 쿠폰과 중복되지 않으니 장바구니에서 확인하세요. 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있으며, 비교 링크는 쿠팡 검색 결과로 연결됩니다.",
        },
        "en": {
            "title": "Crocs Black Friday Encore Runs to 09:00 on 30 November — 25% More Off Three Pairs, a 29,900-Won Clog",
            "summary": "Ends 09:00 on 30 November, up to 70%. Baya Lined 84,900 to 49,900 won, Baya Platform Fuzz 99,900 to 59,900, Mellow Recovery 79,900 to 29,900. The 15% for two and 25% for three stacking, colour price gaps and tonight's 8pm live show.",
            "description": EN,
            "tasteReview": [
                "Period: 25 Nov 09:00 to 30 Nov 09:00, up to 70%",
                "Basket discount: 15% for two qualifying pairs, 25% for three or more / 40% on five Jibbitz charms / 15% Crocs Club first purchase",
                "Baya Lined 84,900 to 49,900 (41%), Baya Platform Fuzz 99,900 to 59,900 (40%), Mellow Recovery 79,900 to 29,900 (63%)",
                "Classic Clog list 69,900, 29,900 to 54,900 by colour / live show 8pm on 26 November with an extra 11,111 won off",
            ],
            "tips": "Prices and dates were read at the Crocs official store on the afternoon of 26 November 2026. Extra discounts apply only to qualifying items and do not stack with every coupon; check the cart. This post contains affiliate links and may earn a commission; comparison links open Coupang search results.",
        },
        "ja": {
            "title": "クロックス ブラックフライデー アンコール、30日午前9時まで — 3足で25%追加、29,900ウォンのクロッグ実測",
            "summary": "11月30日9:00終了、最大70%。バヤ ラインド84,900→49,900ウォン、バヤ プラットフォーム ファズ99,900→59,900ウォン、メロウ リカバリー79,900→29,900ウォン。2足15%・3足25%の追加割引、色別価格差、今夜8時ライブまで整理しました。",
            "description": JA,
            "tasteReview": [
                "期間：2026.11.25 9:00〜11.30 9:00、最大70%",
                "追加割引：対象2足15%、3足以上25%／ジビッツチャーム5個40%／クロックス クラブ初回購入15%",
                "バヤ ラインド84,900→49,900ウォン（41%）、バヤ プラットフォーム ファズ99,900→59,900ウォン（40%）、メロウ リカバリー79,900→29,900ウォン（63%）",
                "クラシック クロッグ定価69,900ウォン、色別29,900〜54,900ウォン／11月26日20時ライブと11,111ウォン追加割引",
            ],
            "tips": "価格と期間は2026年11月26日午後にクロックス公式ストアで確認した値です。追加割引は対象商品のみで一部クーポンと重複しないためカートで確認してください。本記事はアフィリエイトリンクを含み手数料を受け取る場合があります。比較リンクはCoupang検索結果に移動します。",
        },
        "zh": {
            "title": "卡骆驰黑五返场到30日上午9点——三双再减25%，29,900韩元洞洞鞋实价",
            "summary": "11月30日9:00截止，最高70%。Baya Lined 84,900→49,900韩元，Baya Platform Fuzz 99,900→59,900韩元，Mellow Recovery 79,900→29,900韩元。买2件15%、3件25%的叠加规则、颜色价差与今晚8点直播一次说清。",
            "description": ZH,
            "tasteReview": [
                "期间：2026.11.25 9:00～11.30 9:00，最高70%",
                "追加折扣：对象商品2件15%、3件以上25%／智必星5个40%／Crocs Club首购15%",
                "Baya Lined 84,900→49,900韩元（41%）、Baya Platform Fuzz 99,900→59,900韩元（40%）、Mellow Recovery 79,900→29,900韩元（63%）",
                "经典洞洞鞋标价69,900韩元，按颜色29,900～54,900韩元／11月26日20点直播与再加11,111韩元优惠",
            ],
            "tips": "价格与期间为2026年11月26日下午在卡骆驰官方商城确认的数值。追加折扣仅限对象商品且不与部分优惠券叠加，请在购物车确认。本文含联盟链接，可能获得佣金；比价链接跳转至Coupang搜索结果。",
        },
    },
}

if __name__ == "__main__":
    publish(POST)
