#!/usr/bin/env python3
"""ZARA 코리아 2026 블랙프라이데이 + 겨울 시즌오프 일정 총정리 (4개국어) → Supabase posts + ISR revalidate.

근거
 - 오늘의 할인 실측: zara.com/kr 여성·남성 '특가 상품' 컬렉션 (2026-11-27 09:05~09:15 KST 직접 확인)
   https://www.zara.com/kr/ko/woman-special-prices-l1314.html?v1=2419737
   https://www.zara.com/kr/ko/man-special-prices-l806.html?v1=2436823
 - 국내 보도(기간): 에스콰이어 코리아 2026-11-18 '자라 블프 11/27~12/1', 트렌드픽 2026-11-16 동일
 - 글로벌 공지: 자라 앱 2026-11-26 20시(현지) 선오픈, 선택 품목 최대 40% (Who What Wear 2026-11-26, La Razón 2026-11-26)
 - 지난 겨울 세일: 매일경제 2025-12-17 '앱·웹 12/17 20시 선오픈, 매장 12/18, 최대 50%'
 - 상품 사진: static.zara.net 공식 상품컷 원본(1920×2880)을 3:4(900×1200)로 정규화, AI 생성 0장
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


def _require_env(name):
    value = os.environ.get(name) or _env_local(name)
    if not value:
        raise SystemExit(
            f"{name} is not set. Set it in the environment or in .env.local "
            f"(see .env.example). Secrets are never stored in the repository."
        )
    return value


def _bearer_header(key):
    return {"Authorization": f"Bearer {key}"} if key.startswith("eyJ") else {}


SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or _env_local("SUPABASE_SERVICE_ROLE_KEY")
REVALIDATE_URL = ("https://www.k-trand.store/api/revalidate?secret="
                  + _require_env("REVALIDATE_SECRET"))
SLUG = "zara-black-friday-2026-korea-winter-sale-dates"

K = "https://www.coupang.com/np/search?q="
TAG = "&lptag=AF9412775"


def q(s):
    return K + quote(s) + TAG


COVER = "/images/products/zara-faux-fur-trim-jacket-women.jpg"
G1 = "/images/products/zara-belted-wool-coat-women.jpg"
G2 = "/images/products/zara-check-padded-anorak-women.jpg"
G3 = "/images/products/zara-double-face-jacket-women.jpg"
G4 = "/images/products/zara-combo-faux-fur-jacket-women.jpg"
G5 = "/images/products/zara-relaxed-faux-leather-jacket-men.jpg"
G6 = "/images/products/zara-washed-faux-suede-jacket-men.jpg"

KO_DESC = """자라 코리아 공식몰의 특가 상품 컬렉션이 오늘(11월 27일) 오전 9시 현재 열려 있다. 여성 특가 상품 페이지의 최대 할인율은 54%(체크 패딩 아노락 109,900원 → 49,900원)이고, 남성 특가 상품 페이지는 57%(릴랙스 핏 페이크 레더 재킷 139,900원 → 59,900원)까지 내려간다. 겨울 아우터와 니트, 부츠가 할인 목록 앞쪽에 올라와 있어, 블랙프라이데이에 맞춰 겨울옷을 사려는 사람이라면 오늘 확인할 가치가 충분하다.

다만 두 가지는 분명히 해두자. 첫째, 자라 코리아 공식몰 어디에도 '블랙프라이데이'라는 이름의 공지나 종료일은 적혀 있지 않다. 공식몰 첫 화면과 메뉴에서 확인되는 것은 '특가 상품' 컬렉션이다. 행사 기간은 국내 보도 기준으로 11월 27일부터 12월 1일까지다(에스콰이어 코리아 11월 18일, 트렌드픽 11월 16일). 둘째, 12월 겨울 시즌오프는 오늘 오전 9시 기준 자라 쪽 공식 발표가 없다. 아래에 정리한 12월 날짜는 지난 두 해의 실제 일정을 근거로 한 예상이고, 확정된 날짜가 아니다.

1. 오늘 자라 공식몰에서 실제로 확인한 가격
여성 특가 상품: 체크 패딩 아노락 109,900원 → 49,900원(54% 할인), 페이크 퍼 배색 재킷 149,900원 → 79,900원(46%), ZW 컬렉션 더블 페이스 재킷 149,900원 → 79,900원(46%), 벨트 장식 울 코트 89,900원 → 49,900원(44%), 스웨이드 웨지 앵클부츠 169,900원 → 89,900원(47%), 브이넥 니트 스웨터 59,900원 → 35,900원(40%).
남성 특가 상품: 릴랙스 핏 페이크 레더 재킷 139,900원 → 59,900원(57%), 워싱 페이크 스웨이드 재킷 139,900원 → 59,900원(57%), 릴렉스핏 메탈 토글 재킷 139,900원 → 79,900원(42%), 글로시 콘트라스트 퀼팅 오버셔츠 149,900원 → 89,900원(40%), 벨트 디테일 플리츠 벌룬핏 팬츠 89,900원 → 49,900원(44%).
할인율은 상품마다 다르고, 같은 품목도 색상·사이즈에 따라 재고가 다르다. 목록에 보이는 정가와 판매가를 그대로 적었으니, 실제 결제 화면에서 한 번 더 확인하는 편이 안전하다.

2. 6종을 담으면 얼마가 빠지나
여성 아우터 3종(페이크 퍼 배색 재킷 + 벨트 장식 울 코트 + 체크 패딩 아노락)은 정가 합계 349,700원에서 179,700원이 된다. 170,000원이 빠진다. 남성 3종(릴랙스 핏 페이크 레더 재킷 + 워싱 페이크 스웨이드 재킷 + 글로시 콘트라스트 퀼팅 오버셔츠)은 429,700원에서 209,700원, 220,000원이 빠진다. 두 묶음을 합치면 779,400원이 389,400원이 된다. 겨울 아우터 한 벌을 정가로 사는 값에 두 벌을 사는 셈이다.

3. 블랙프라이데이 기간, 어디까지가 확인된 것인가
확인된 것: 오늘 오전 9시 현재 특가 상품 컬렉션이 라이브이고, 위 가격이 실제로 표시된다. 자라 앱은 11월 26일 저녁 8시(현지 시각)부터 선택 품목 40% 할인을 예고했고, 매장은 11월 27일부터 시작한다는 보도가 유럽·영국 매체에 함께 나왔다. 국내 언론은 자라 블랙프라이데이를 11월 27일~12월 1일로 전했다.
확인되지 않은 것: 자라 코리아가 직접 밝힌 종료일. 글로벌 보도도 "종료일은 아직 공지되지 않았다"고 전한다. 그래서 12월 1일 이후에도 남아 있을 가능성과, 그 전에 품절될 가능성을 동시에 열어두는 게 맞다. 인기 사이즈는 첫날 오전에 빠지는 경우가 많다.

4. 12월 겨울 시즌오프는 언제인가 (예상)
자라는 정기 세일 날짜를 미리 공지하지 않는다. 지난 두 해 실제 일정은 이렇다. 2025년은 12월 17일(수) 오후 8시에 앱과 공식 홈페이지가 먼저 열렸고, 매장은 12월 18일(목)부터 시작했다. 할인율은 품목에 따라 최대 50%까지였다. 2024년도 12월 18일 전후에 시작했고, 앱이 전날 저녁 8시, 웹이 밤 9시에 먼저 열렸다. 두 해 모두 '수요일 밤 온라인 선오픈 → 목요일 매장' 순서였다.
이 패턴을 2026년에 그대로 적용하면 12월 셋째 주 목요일인 12월 17일이 매장 시작일, 그 전날인 12월 16일(수) 오후 8시가 앱 선오픈 시점이 된다. 하지만 이는 예상일 뿐이고, 자라가 12월 넷째 주 목요일(12월 24일)로 미룬 해도 있었다. 공식 공지는 보통 시작 며칠 전 앱 푸시와 사이트 배너로 뜬다.

5. 지금 살까, 12월을 기다릴까
지금 사는 게 유리한 경우는 세 가지다. 원하는 색상·사이즈가 지금 목록에 있고, 할인율이 40%를 넘고, 이번 겨울에 바로 입을 옷이라면 기다릴 이유가 적다. 위 여성 코트 49,900원, 남성 재킷 59,900원은 시즌오프 첫날에도 이보다 더 떨어지기 어려운 가격대다.
기다리는 게 나은 경우는 사이즈가 애매하거나, 목록에 없는 신상 라인을 노리는 경우다. 시즌오프는 할인 범위가 훨씬 넓고, 1월 초에 한 번 더 인하되는 구간이 있다. 대신 그때는 인기 사이즈가 이미 없다. 세일 첫날 품절된 코트를 1월에 반값으로 찾는 일은 드물다.

6. 매장과 온라인, 어디서 사나
가격은 같다. 다른 것은 재고 확인 속도다. 온라인은 상품 페이지에서 사이즈별 재고가 바로 보이고, 매장은 방문해야 안다. 반품과 교환은 구매한 채널의 기준을 따르므로, 매장에서 사면 매장 규정, 온라인에서 사면 온라인 규정이 적용된다. 온라인 주문 후 매장 수령을 고르면 배송비 없이 받을 수 있는 경우가 있으니 결제 화면에서 확인하자.

한 줄 요약
2026년 11월 27일 오늘, 자라 코리아 공식몰 특가 상품은 여성 최대 54%, 남성 최대 57%다. 6종을 담으면 77만 9,400원이 38만 9,400원이 된다. 블랙프라이데이 종료일은 공식 공지가 없고, 12월 겨울 시즌오프는 12월 16일 밤 앱 선오픈·17일 매장 시작이 지난 두 해 패턴상 가장 유력한 예상이다."""

EN_DESC = """ZARA Korea's official online store has its "special prices" collections live this morning (27 November), measured at 09:00 KST. The women's section runs to 54% off (checked padded anorak 109,900 → 49,900 won), and the men's section reaches 57% off (relaxed-fit faux leather jacket 139,900 → 59,900 won). Winter coats, knits and boots sit at the top of both lists, which makes today the moment to look if you were waiting for Black Friday to buy winter clothes.

Two things need to be separated from the discounts. First, nowhere on ZARA Korea's site is there a notice called "Black Friday", and no end date is published; what the store actually shows is a "special prices" collection. Korean press reported the promotion as running 27 November to 1 December (Esquire Korea, 18 November; Trendpick, 16 November). Second, ZARA has not announced its December winter sale as of this morning. The December dates below are a forecast built on the last two years of actual schedules, not a confirmed date.

1. Prices actually shown on ZARA Korea today
Women: checked padded anorak 109,900 → 49,900 won (54% off), faux fur-trimmed jacket 149,900 → 79,900 (46%), ZW Collection double-faced jacket 149,900 → 79,900 (46%), belted wool coat 89,900 → 49,900 (44%), suede wedge ankle boots 169,900 → 89,900 (47%), V-neck knit sweater 59,900 → 35,900 (40%).
Men: relaxed-fit faux leather jacket 139,900 → 59,900 won (57%), washed faux suede jacket 139,900 → 59,900 (57%), relaxed metal toggle jacket 139,900 → 79,900 (42%), glossy contrast quilted overshirt 149,900 → 89,900 (40%), belted pleated balloon trousers 89,900 → 49,900 (44%).
Discounts vary by item, and stock differs by colour and size. These are the struck-through and current prices as displayed, so confirm once more on the checkout screen.

2. What six pieces actually save
Three women's outerwear pieces (faux fur-trimmed jacket, belted wool coat, checked padded anorak) go from 349,700 won to 179,700 won: 170,000 won off. Three men's pieces (faux leather jacket, faux suede jacket, quilted overshirt) go from 429,700 to 209,700: 220,000 won off. Together, 779,400 won becomes 389,400 won. You pay for one coat at full price and take home two.

3. How much of the Black Friday window is confirmed
Confirmed: the special prices collection is live today and the prices above are displayed. ZARA's app announced 40% off selected items from 8 pm local time on 26 November, with stores joining on 27 November, as reported across European and UK media. Korean outlets put ZARA's Black Friday at 27 November to 1 December.
Not confirmed: an end date from ZARA Korea itself. Global coverage also notes that ZARA has not confirmed when the sale ends. Treat both possibilities as open: stock may last past 1 December, and popular sizes may sell out before it. In practice, the most-wanted sizes tend to go on the first morning.

4. The December winter sale (forecast)
ZARA does not announce its regular sale dates in advance. The last two years: in 2025 the app and website opened first at 8 pm on Wednesday 17 December, stores started Thursday 18 December, and discounts reached 50% on some items. In 2024 the sale started around 18 December, with the app at 8 pm and the website at 9 pm the evening before. Both years followed the same order: Wednesday night online, Thursday in stores.
Applied to 2026, that puts the store start on Thursday 17 December, with the app opening at 8 pm on Wednesday 16 December. It is a forecast only; ZARA has also moved the start to the fourth Thursday (24 December) in some years. Official notice usually appears in the app and as a site banner a few days before.

5. Buy now, or wait for December
Buy now if the colour and size you want are in today's list, the discount is above 40%, and you will wear the piece this winter. A 49,900-won wool coat or a 59,900-won leather jacket is already at a level the season sale rarely beats on day one.
Wait if your size is uncertain or you are after a new-season line that is not on the list. The season sale covers far more of the range and usually cuts prices again in early January, but by then the popular sizes are gone. Finding a coat that sold out on day one at half price in January is rare.

6. Store or online
Prices are the same. What differs is how fast you can see stock: online shows availability by size on the product page, while in store you have to be there. Returns and exchanges follow the channel you bought from. If the checkout offers free store pickup, take it rather than paying delivery.

In one line
On 27 November 2026, ZARA Korea's special prices reach 54% for women and 57% for men; six pieces fall from 779,400 won to 389,400 won. No official end date has been published for Black Friday, and the December winter sale is most likely to open in the app on the evening of 16 December with stores from 17 December, based on the last two years."""

JA_DESC = """ZARAコリア公式オンラインストアでは、今朝（11月27日）9時時点で「特別価格（특가 상품）」コレクションが公開されている。女性は最大54%オフ（チェック柄パデッドアノラック 109,900→49,900ウォン）、男性は最大57%オフ（リラックスフィットのフェイクレザージャケット 139,900→59,900ウォン）。冬コート、ニット、ブーツがリストの前方に並んでおり、ブラックフライデーで冬物を買う予定なら今日確認する価値がある。

ただし二点は分けて考えたい。第一に、ZARAコリアのサイトに「ブラックフライデー」という名称の告知や終了日は表示されていない。実際に開いているのは「特別価格」コレクションだ。韓国メディアは期間を11月27日〜12月1日と伝えている（エスクァイアコリア11月18日、トレンドピック11月16日）。第二に、12月の冬セールは今朝時点でZARAからの公式発表がない。以下の12月の日付は過去2年の実績に基づく予想であり、確定日ではない。

1. 今日、公式ストアで実際に確認した価格
女性：チェック柄パデッドアノラック 109,900→49,900ウォン（54%オフ）、フェイクファー切替ジャケット 149,900→79,900（46%）、ZWコレクション ダブルフェイスジャケット 149,900→79,900（46%）、ベルト付きウールコート 89,900→49,900（44%）、スエードウェッジアンクルブーツ 169,900→89,900（47%）、Vネックニット 59,900→35,900（40%）。
男性：リラックスフィット フェイクレザージャケット 139,900→59,900ウォン（57%）、ウォッシュド フェイクスエードジャケット 139,900→59,900（57%）、メタルトグルジャケット 139,900→79,900（42%）、グロッシーキルティングオーバーシャツ 149,900→89,900（40%）、ベルト付きプリーツバルーンパンツ 89,900→49,900（44%）。
割引率は商品ごとに異なり、同じ商品でも色・サイズで在庫が違う。表示されている定価と販売価格をそのまま記載しているので、決済画面でもう一度確認するとよい。

2. 6点買うといくら下がるか
女性アウター3点（フェイクファー切替ジャケット＋ベルト付きウールコート＋チェック柄パデッドアノラック）は定価合計349,700ウォンが179,700ウォンになる。170,000ウォンの節約。男性3点（フェイクレザー＋フェイクスエード＋キルティングオーバーシャツ）は429,700ウォンが209,700ウォン、220,000ウォンの節約。合計では779,400ウォンが389,400ウォンになる。コート1着の定価で2着買える計算だ。

3. ブラックフライデーの期間、どこまで確認済みか
確認済み：今朝9時時点で特別価格コレクションが公開中で、上記の価格が実際に表示されている。ZARAアプリは11月26日20時（現地時間）から対象商品40%オフを告知し、店舗は27日から開始するという報道が欧州・英国の媒体に出た。韓国メディアは11月27日〜12月1日と伝えている。
未確認：ZARAコリア自身による終了日。海外報道も「終了日は未発表」としている。12月1日以降も残る可能性と、それ以前に人気サイズが売り切れる可能性の両方を見ておくべきだ。

4. 12月の冬セール（予想）
ZARAは定例セールの日程を事前に公表しない。過去2年の実績は次の通り。2025年は12月17日（水）20時にアプリと公式サイトが先行オープンし、店舗は12月18日（木）から。一部商品は最大50%オフだった。2024年も12月18日頃に始まり、前日夜8時にアプリ、9時にウェブが開いた。どちらも「水曜夜にオンライン先行→木曜に店舗」の順番だった。
これを2026年に当てはめると、店舗開始は12月17日（木）、アプリ先行は12月16日（水）20時になる。あくまで予想で、12月第4木曜（24日）にずれた年もある。公式告知は通常、開始数日前にアプリ通知とサイトバナーで出る。

5. 今買うか、12月を待つか
今買うべきなのは、欲しい色とサイズが今日のリストにあり、割引率が40%を超え、この冬にすぐ着る場合だ。ウールコート49,900ウォン、レザージャケット59,900ウォンは、シーズンセール初日でもこれ以上下がりにくい水準である。
待つべきなのは、サイズが曖昧な場合や、リストにない新作ラインを狙う場合。シーズンセールは対象範囲が広く、1月上旬にさらに値下げされる局面がある。ただしその頃には人気サイズは残っていない。

6. 店舗かオンラインか
価格は同じ。違うのは在庫の見え方だ。オンラインは商品ページでサイズ別在庫がすぐ分かり、店舗は行かないと分からない。返品・交換は購入したチャネルの規定に従う。オンライン注文で店舗受け取りを選べば送料が無料になる場合があるので、決済画面で確認したい。

一行まとめ
2026年11月27日、ZARAコリアの特別価格は女性最大54%オフ、男性最大57%オフ。6点で779,400ウォンが389,400ウォンになる。ブラックフライデーの終了日は公式未発表、12月の冬セールは過去2年のパターンから12月16日夜のアプリ先行・17日の店舗開始が最も有力な予想だ。"""

ZH_DESC = """ZARA韩国官方商城今晨（11月27日）9时的“特价商品（특가 상품）”系列已经上架。女装最高折扣54%（格纹绗缝套头外套 109,900→49,900韩元），男装最高57%（宽松版人造皮夹克 139,900→59,900韩元）。冬季大衣、针织和靴子都排在列表前列，如果你正等黑五买冬装，今天值得先看一眼。

有两点需要分开看。第一，ZARA韩国站上并没有名为“黑色星期五”的公告，也没有公布结束日期，实际开放的是“特价商品”系列。韩国媒体报道的活动期为11月27日至12月1日（Esquire Korea 11月18日、Trendpick 11月16日）。第二，12月的冬季换季大促，截至今晨ZARA方面没有官方发布。下面的12月日期是根据过去两年实际日程做出的预测，不是确定日期。

1. 今天在官方商城实际看到的价格
女装：格纹绗缝套头外套 109,900→49,900韩元（54%）、人造毛拼接夹克 149,900→79,900（46%）、ZW系列双面夹克 149,900→79,900（46%）、系带羊毛大衣 89,900→49,900（44%）、绒面坡跟短靴 169,900→89,900（47%）、V领针织衫 59,900→35,900（40%）。
男装：宽松版人造皮夹克 139,900→59,900韩元（57%）、水洗人造麂皮夹克 139,900→59,900（57%）、金属牛角扣夹克 139,900→79,900（42%）、光泽感绗缝衬衫外套 149,900→89,900（40%）、腰带褶皱灯笼裤 89,900→49,900（44%）。
折扣按单品不同，同一单品的颜色和尺码库存也不同。以上是页面显示的划线价与现价，付款前请在结算页面再确认一次。

2. 六件一起买能省多少
女装三件外套（人造毛拼接夹克＋系带羊毛大衣＋格纹绗缝外套）原价合计349,700韩元，现为179,700韩元，省170,000韩元。男装三件（人造皮夹克＋人造麂皮夹克＋绗缝衬衫外套）从429,700韩元降到209,700韩元，省220,000韩元。两组相加，779,400韩元变成389,400韩元。相当于用一件大衣的原价买两件。

3. 黑五的时间窗口确认到哪一步
已确认：今晨9时特价系列在线，上述价格确实显示在页面上。ZARA App宣布自11月26日晚8点（当地时间）起对部分商品打四折，门店从27日开始，欧洲与英国媒体均有报道。韩国媒体则把ZARA黑五写作11月27日至12月1日。
未确认：ZARA韩国自己公布的结束日期。海外报道也提到“结束日期尚未公布”。因此要同时考虑两种情况：12月1日之后仍有库存，以及在此之前热门尺码就卖光。事实上，最抢手的尺码往往在第一天上午就没了。

4. 12月冬季大促（预测）
ZARA不会提前公布定期促销日期。过去两年的实际情况是：2025年12月17日（周三）晚8点App与官网先行开放，门店12月18日（周四）开始，部分商品最高五折；2024年同样在12月18日前后开始，前一日晚8点App、9点官网先行。两年都是“周三夜间线上先行，周四门店开始”。
套用到2026年，门店开始是12月17日（周四），App先行是12月16日（周三）晚8点。但这只是预测，ZARA也有过推迟到12月第四个周四（24日）的年份。官方通知通常在开始前几天通过App推送和网站横幅发出。

5. 现在买还是等12月
适合现在买：想要的颜色和尺码就在今天的列表里、折扣超过40%、这个冬天马上就要穿。49,900韩元的羊毛大衣、59,900韩元的皮夹克，已接近换季首日也很难再低的价格区间。
适合再等：尺码拿不准，或者想要不在列表里的新品线。换季大促覆盖范围更广，1月初还有一次再降价，但那时热门尺码已经没了。第一天售罄的大衣，1月能以半价找到的情况很少。

6. 门店还是线上
价格一样，差别在于看到库存的速度：线上在商品页直接显示各尺码库存，门店必须到场。退换货按购买渠道的规则处理。如果结算页面提供门店自提，通常可以省下运费，值得选。

一句话总结
2026年11月27日，ZARA韩国特价商品女装最高54%、男装最高57%；六件合计从779,400韩元降到389,400韩元。黑五结束日尚无官方公布，12月冬季大促按过去两年规律，最可能是12月16日晚App先行、17日门店开始。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "k-fashion",
    "store": "ZARA",
    "priceKrw": 49900,
    "releaseDate": "2026-11-27",
    "rating": 4.6,
    "imageUrl": COVER,
    "images": [G1, G2, G3, G4, G5, G6],
    "affiliateUrl": "https://www.zara.com/kr/ko/woman-special-prices-l1314.html?v1=2419737",
    "affiliatePlatform": "Zara",
    "exampleItems": [
        {
            "name": "자라 릴랙스 핏 페이크 레더 재킷 (남성)",
            "brand": "ZARA",
            "priceKrw": 59900,
            "imageUrl": G5,
            "url": q("자라 남성 페이크 레더 자켓"),
            "category": "-57% · 139,900→59,900원",
        },
        {
            "name": "자라 워싱 페이크 스웨이드 재킷 (남성)",
            "brand": "ZARA",
            "priceKrw": 59900,
            "imageUrl": G6,
            "url": q("자라 남성 스웨이드 자켓"),
            "category": "-57% · 139,900→59,900원",
        },
        {
            "name": "자라 페이크 퍼 배색 재킷 (여성)",
            "brand": "ZARA",
            "priceKrw": 79900,
            "imageUrl": COVER,
            "url": q("자라 페이크 퍼 자켓"),
            "category": "-46% · 149,900→79,900원",
        },
        {
            "name": "자라 체크 패딩 아노락 (여성)",
            "brand": "ZARA",
            "priceKrw": 49900,
            "imageUrl": G2,
            "url": q("자라 패딩 아노락"),
            "category": "-54% · 109,900→49,900원",
        },
        {
            "name": "자라 벨트 장식 울 코트 (여성)",
            "brand": "ZARA",
            "priceKrw": 49900,
            "imageUrl": G1,
            "url": q("자라 여성 울 코트"),
            "category": "-44% · 89,900→49,900원",
        },
        {
            "name": "자라 ZW 컬렉션 더블 페이스 재킷 (여성)",
            "brand": "ZARA",
            "priceKrw": 79900,
            "imageUrl": G3,
            "url": q("자라 ZW 더블 페이스 자켓"),
            "category": "-46% · 149,900→79,900원",
        },
        {
            "name": "자라 ZW 컬렉션 콤비 페이크 퍼 재킷 (여성)",
            "brand": "ZARA",
            "priceKrw": 79900,
            "imageUrl": G4,
            "url": q("자라 ZW 컬렉션 자켓"),
            "category": "-38% · 129,900→79,900원",
        },
    ],
    "i18n": {
        "ko": {
            "title": "자라 블랙프라이데이 2026 오늘 시작, 최대 57%…6종 담으면 39만 원 차이",
            "summary": "11월 27일 오전 9시 자라 코리아 공식몰 실측. 여성 최대 54%·남성 최대 57% 할인 품목과 가격, 그리고 아직 공식 발표가 없는 12월 겨울 시즌오프 예상일(12월 16일 밤 앱·17일 매장)을 확정과 예상으로 나눠 정리했습니다.",
            "description": KO_DESC,
            "tasteReview": [
                "여성 최대 54%: 체크 패딩 아노락 109,900→49,900원, 페이크 퍼 배색 재킷 149,900→79,900원, 벨트 장식 울 코트 89,900→49,900원",
                "남성 최대 57%: 릴랙스 핏 페이크 레더 재킷·워싱 페이크 스웨이드 재킷 139,900→59,900원",
                "6종 합계 779,400원 → 389,400원, 390,000원 절약",
                "블랙프라이데이 종료일은 공식 미표기(국내 보도 11/27~12/1), 겨울 시즌오프는 12/16 밤 앱·12/17 매장이 예상",
            ],
            "tips": "가격은 2026년 11월 27일 09:00~09:15 KST에 자라 코리아 공식몰(zara.com/kr) 여성·남성 '특가 상품' 목록에서 직접 확인한 표시가이며, 재고·색상·쿠폰에 따라 달라질 수 있습니다. 12월 겨울 시즌오프 날짜는 공식 발표가 아닌 과거 일정 기반 예상입니다. 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있습니다.",
        },
        "en": {
            "title": "ZARA Korea Black Friday 2026 is live: up to 57% off, and six pieces that save 390,000 won",
            "summary": "Measured on ZARA Korea's own store at 09:00 KST on 27 November: women's up to 54% off, men's up to 57% off, plus the December winter sale dates as a forecast — clearly separated from what ZARA has actually confirmed.",
            "description": EN_DESC,
            "tasteReview": [
                "Women's up to 54%: checked padded anorak 109,900→49,900 won, faux fur-trimmed jacket 149,900→79,900, belted wool coat 89,900→49,900",
                "Men's up to 57%: relaxed faux leather jacket and washed faux suede jacket both 139,900→59,900 won",
                "Six pieces: 779,400 won becomes 389,400 won, a 390,000 won saving",
                "No official end date for Black Friday (Korean press: 27 Nov–1 Dec); winter sale forecast: app on the evening of 16 Dec, stores 17 Dec",
            ],
            "tips": "Prices were read on ZARA Korea's official store (zara.com/kr) between 09:00 and 09:15 KST on 27 November 2026 and may change with stock, colour and coupons. The December winter sale date is a forecast from past schedules, not an official announcement. This post contains affiliate links and may earn a commission.",
        },
        "ja": {
            "title": "ZARA韓国ブラックフライデー2026開幕、最大57%オフ — 6点で39万ウォン差になる組み合わせ",
            "summary": "11月27日9時（韓国時間）にZARAコリア公式ストアで実測。女性最大54%オフ、男性最大57%オフの価格と、まだ公式発表のない12月ウィンターセールの予想日（12月16日夜アプリ・17日店舗）を確定と予想に分けて整理。",
            "description": JA_DESC,
            "tasteReview": [
                "女性最大54%：チェック柄パデッドアノラック109,900→49,900ウォン、フェイクファー切替ジャケット149,900→79,900、ベルト付きウールコート89,900→49,900",
                "男性最大57%：フェイクレザージャケット・フェイクスエードジャケットがいずれも139,900→59,900ウォン",
                "6点合計779,400ウォン→389,400ウォン、390,000ウォンの節約",
                "ブラックフライデーの終了日は公式未発表（韓国報道11/27〜12/1）、ウィンターセールは12/16夜アプリ・12/17店舗が予想",
            ],
            "tips": "価格は2026年11月27日9:00〜9:15（韓国時間）にZARAコリア公式ストア（zara.com/kr）の女性・男性「特別価格」リストで確認した表示価格で、在庫・色・クーポンにより変わります。12月のウィンターセール日程は公式発表ではなく過去日程に基づく予想です。本記事はアフィリエイトリンクを含み、手数料を受け取る場合があります。",
        },
        "zh": {
            "title": "ZARA韩国2026黑五开跑，最高57%折扣 — 六件一起买差39万韩元",
            "summary": "11月27日9时（韩国时间）在ZARA韩国官方商城实测：女装最高54%、男装最高57%，并把尚无官方发布的12月冬季大促预测日（12月16日晚App、17日门店）与已确认事实分开整理。",
            "description": ZH_DESC,
            "tasteReview": [
                "女装最高54%：格纹绗缝套头外套109,900→49,900韩元，人造毛拼接夹克149,900→79,900，系带羊毛大衣89,900→49,900",
                "男装最高57%：人造皮夹克与人造麂皮夹克均为139,900→59,900韩元",
                "六件合计779,400韩元→389,400韩元，省39万韩元",
                "黑五结束日官方未公布（韩国报道11/27—12/1），冬季大促预计12/16晚App、12/17门店",
            ],
            "tips": "价格为2026年11月27日9:00—9:15（韩国时间）在ZARA韩国官方商城（zara.com/kr）女装、男装“特价商品”列表中确认的显示价，可能因库存、颜色和优惠券而变化。12月冬季大促日期为依据往年日程的预测，非官方发布。本文含联盟链接，可能获得佣金。",
        },
    },
}

headers = {
    "apikey": SUPABASE_KEY,
    **_bearer_header(SUPABASE_KEY),
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
