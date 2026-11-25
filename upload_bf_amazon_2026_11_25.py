#!/usr/bin/env python3
"""아마존 미국 직구 200달러 면세 컷 실측 (2026) → Supabase posts + ISR revalidate.

근거
 - 가격: 아마존 상품 페이지 2026-11-25 12:30~12:40 KST 직접 확인
   AirTag 2세대 4팩 B0GJTXVN9Z $79.00(정가 $99) / Kindle Paperwhite 16GB B0CFPJYX7P $129.99(정가 $199.99)
   Kindle Colorsoft B0CGVSKR1G $169.99 / Fire TV Stick 4K B0G4XRP464 $19.99(정가 $59.99)
 - 환율: USD/KRW 1,344.73 (2026-11-25 확인)
 - 관세: 관세청 안내(미국발 특송 목록통관 200달러 이하 면세, 그 외 150달러), 2026-11-22 기준 정리 보도(150달러/200달러 유지,
   2026-10-26 해외직구 전용 통관플랫폼 개통·일회용 인증번호, 개인통관고유부호 유효기간 1년)
 - 사진: 아마존 제품 이미지 4장 (AI 생성 0장)
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
SLUG = "amazon-blackfriday-under-200-duty-free-2026"

K = "https://www.coupang.com/np/search?q="
TAG = "&lptag=AF9412775"


def q(s):
    return K + quote(s) + TAG


C = "/images/products/bf-amazon-airtag-4pack.jpg"
G1 = "/images/products/bf-amazon-kindle-paperwhite.jpg"
G2 = "/images/products/bf-amazon-kindle-colorsoft.jpg"
G3 = "/images/products/bf-amazon-firetv-stick-4k.jpg"

KO_DESC = """아마존 블랙프라이데이는 11월 19일부터 30일까지다. 미국 직구에서 가장 중요한 숫자는 할인율이 아니라 200달러다. 이 선을 넘으면 넘은 금액만이 아니라 물품가격 전체에 관세와 부가세가 붙기 때문이다. 11월 25일 아마존에서 실제로 확인한 네 개를 200달러 컷에 맞춰 계산했다. 환율은 1달러 1,344.73원이다.

1. 200달러의 정확한 조건 — 다 맞지는 않는다
미국에서 특송으로 들어오는 목록통관 대상 자가사용 물품은 물품가격 200달러 이하까지 관세와 부가세가 면제된다. 미국이 아닌 나라에서 오면 150달러다. 여기에 예외가 붙는다. 의약품·건강기능식품·식품류처럼 목록통관에서 빠지는 품목은 미국에서 와도 150달러 기준이 적용된다. 전자기기·생활용품은 대부분 200달러 기준을 받는다.
기준이 되는 '물품가격'은 상품값에 미국 내 세일즈택스와 미국 내 배송비를 더한 금액이다. 한국까지 오는 국제배송비는 명백히 구분되면 빠진다. 즉 배송비가 비싸다고 면세 한도가 줄지는 않는다. 반대로 한도를 넘으면 그때는 국제배송비까지 과세가격에 들어간다.

2. 실측 네 개 — 200달러 안쪽과 바깥쪽
애플 에어태그 2세대 4팩은 79.00달러(정가 99달러)다. 원화로 10만6,234원. 리뷰 1만3,500개, 최근 한 달 1만 개 이상 팔렸다. 4개들이라 하나당 2만6,558원 꼴이다.
킨들 페이퍼화이트 16GB(2024)는 129.99달러(정가 199.99달러), 17만4,800원이다. 리뷰 2만4,200개. 블랙프라이데이 딜 표기가 붙어 있다.
킨들 컬러소프트는 169.99달러, 22만8,600원이다. 컬러 전자잉크 모델이라 단독으로는 200달러 안쪽이지만 여유가 30달러뿐이다. 케이스나 충전기를 함께 담으면 바로 선을 넘는다.
파이어 TV 스틱 4K(최신형)는 19.99달러(정가 59.99달러), 2만6,885원이다. 67% 할인이다. HD 모델은 15.99달러다. 이 가격이면 두 개를 담아도 40달러다.

3. 조합을 짜면 200달러가 갈린다
에어태그(79.00) + 파이어 TV 스틱 4K(19.99) = 98.99달러. 원화 13만3,116원. 200달러까지 100달러가 남는다.
에어태그(79.00) + 킨들 페이퍼화이트(129.99) = 208.99달러. 원화 28만1,050원. 200달러를 9달러 넘는다. 이 경우 넘은 9달러만이 아니라 208.99달러 전체에 관세와 부가세가 붙는다. 전자기기 관세율이 0%라 해도 부가세 10%만 2만8,000원 안팎이다. 9달러(약 1만2,000원)를 아끼려다 2만8,000원을 더 내는 구조다.
킨들 컬러소프트(169.99) + 케이스(20~30달러)도 위험하다. 199.99달러와 189.99달러는 겉보기에 비슷하지만, 후자는 면세, 전자는 전체 과세다.
같은 판매자(아마존)에서 같은 날 산 물품을 면세 범위 안으로 나눠 들여오는 경우에는 합산해 과세한다. 에어태그와 킨들을 따로 주문해 각각 200달러 아래로 맞춰도, 같은 날 같은 판매자에서 샀다면 합산 대상이 될 수 있다는 뜻이다. 날짜를 나누거나 판매자를 바꾸는 게 안전하다.

4. 대형 가전은 애초에 구간이 다르다
55인치 TV나 모니터처럼 부피와 금액이 큰 물건은 200달러 컷 논의 대상이 아니다. 물품가격이 기준을 넘으면 일반 수입신고로 넘어가고, 관세율이 붙는다. TV 관세율은 8% 안팎, 여기에 부가세 10%가 더해진다. 배송비와 파손 위험까지 생각하면 국내 정품과의 차액이 크지 않은 경우가 많다. 직구는 '작고 가벼운 IT 기기'에서 이득이 나는 구조다.

5. 2026년에 달라진 통관 절차
관세청은 2026년 10월 26일 해외직구 전용 통관플랫폼을 열고 일회용 인증번호 제도를 도입했다. 주문할 때나 주문 뒤에 6자리 인증번호를 요청받을 수 있고, 개인통관고유부호 유효기간은 2026년부터 1년이다. 부호가 만료되면 통관이 멈추므로 아마존 결제 전에 관세청 앱이나 홈페이지에서 유효기간을 확인하는 게 좋다.
또 하나, 면세 한도를 넘겨 과세된 물건을 반품하면 낸 세금은 환급받을 수 있다. 다만 반품 배송비와 환급 절차를 따로 챙겨야 하므로, 애매한 금액이면 처음부터 200달러 아래로 조합을 짜는 편이 낫다.

결제 전 확인 세 가지
첫째, 카트 합계가 200달러를 넘지 않는지 본다. 배송비가 아니라 상품값 합계다.
둘째, 같은 판매자에게 같은 날 사는지 확인한다. 나눠 사도 합산될 수 있다.
셋째, 목록통관 배제 품목이 섞이지 않았는지 본다. 영양제·식품을 함께 담으면 그 화물 전체가 150달러 기준으로 내려간다.

한 줄 정리
이번 아마존 블프에서 200달러 컷에 가장 잘 맞는 조합은 에어태그 4팩(79달러)과 파이어 TV 스틱 4K(19.99달러)로 98.99달러다. 킨들 페이퍼화이트를 더하면 208.99달러가 되어 9달러 초과로 전체 과세, 부가세만 2만8,000원이 붙는다. 200달러는 넘지 않는 선에서 조합을 짜는 것이 이번 주 직구에서 돈을 지키는 방법이다."""

EN_DESC = """Amazon's Black Friday runs from November 19 to 30. For US direct purchases the number that matters is not the discount but 200 dollars. Cross that line and duty and VAT apply to the entire value, not just the excess. Here are four items checked on Amazon on November 25, calculated against the $200 cut at 1,344.73 won per dollar.

1. What the $200 actually covers
Personal-use goods arriving by express from the US are exempt from duty and VAT up to $200 under list clearance. From anywhere else the limit is $150. There are exceptions: medicines, health supplements and foods are excluded from list clearance and fall back to the $150 limit even from the US. Most electronics and household goods get the $200 limit.
The "goods value" counted is the price plus US sales tax and US domestic shipping; the international leg is excluded when it is clearly separated. So expensive shipping does not shrink the allowance — but once you exceed it, shipping joins the taxable value.

2. Four items, inside and outside the line
Apple AirTag (2nd generation) 4-pack is $79.00 against a $99 list, or 106,234 won. It carries 13,500 reviews and sold 10,000+ in the past month; that is 26,558 won per tag.
Kindle Paperwhite 16GB (2024) is $129.99 against a $199.99 list, or 174,800 won, with 24,200 reviews and a Black Friday badge.
Kindle Colorsoft is $169.99, or 228,600 won. Alone it stays under $200, but only by $30 — add a case or a charger and it crosses.
Fire TV Stick 4K (newest) is $19.99 against a $59.99 list, or 26,885 won, a 67% discount. The HD model is $15.99; two of those are still $40.

3. The combination decides it
AirTag ($79.00) plus Fire TV Stick 4K ($19.99) is $98.99, or 133,116 won, leaving $100 of headroom.
AirTag plus Kindle Paperwhite is $208.99, or 281,050 won — $9 over. Then duty and VAT apply to all $208.99, not the $9. Even with a 0% electronics duty, the 10% VAT alone is about 28,000 won. Saving $9 costs 28,000 won.
Kindle Colorsoft ($169.99) plus a $20-30 case is the same trap: $199.99 and $189.99 look alike, but the latter is exempt and the former is taxed on everything.
Buying from the same seller (Amazon) on the same day and splitting the shipment to stay under the limit triggers combined assessment. Splitting the order does not help if the seller and date are the same; split the date or the seller instead.

4. Big appliances are a different bracket
A 55-inch TV or monitor is not a $200-cut question. Above the limit it moves to a formal import declaration with duty — around 8% for TVs — plus 10% VAT, before shipping and damage risk. Direct purchase pays off on small, light IT devices.

5. What changed in 2026
Korea Customs opened a dedicated cross-border shopping clearance platform on October 26, 2026, with a one-time verification number: you may be asked for a 6-digit code at or after ordering. The personal customs code is valid for one year from 2026, and an expired code stops clearance — check it before paying.
If a taxed parcel is returned, the duty can be refunded, but the return shipping and refund steps are yours; for borderline amounts, build the cart under $200 instead.

Three checks before paying
First, the cart's goods value, not shipping, must stay under $200. Second, check whether you are buying from the same seller on the same day; splitting can still be combined. Third, keep excluded categories out: one supplement or food item drops the whole shipment to the $150 rule.

Bottom line
The combination that fits the $200 cut best is the AirTag 4-pack ($79) plus Fire TV Stick 4K ($19.99) at $98.99. Adding the Kindle Paperwhite takes it to $208.99 — $9 over, taxed on the full amount, with about 28,000 won of VAT alone. Staying under $200 is how you keep your money on this week's Amazon order."""

JA_DESC = """アマゾンのブラックフライデーは11月19日から30日まで。米国直球で最も重要な数字は割引率ではなく200ドルです。この線を超えると、超えた分だけでなく商品価格全体に関税と付加価値税がかかります。11月25日にアマゾンで確認した4点を、1ドル1,344.73ウォンで200ドルの線に当てはめて計算しました。

1. 200ドルの正確な条件
米国から特送で届くリスト通関対象の自家使用品は、商品価格200ドル以下まで関税と付加価値税が免除されます。米国以外からは150ドル。例外もあります。医薬品・健康機能食品・食品類などリスト通関から外れる品目は、米国発でも150ドル基準です。電子機器や生活用品はほとんどが200ドル基準の対象です。
基準となる「商品価格」は、商品代金に米国内の売上税と米国内配送料を足した額です。韓国までの国際送料は明確に区別できれば除きます。送料が高くても免税枠は減りませんが、超えた場合は国際送料も課税価格に入ります。

2. 実測4点——線の内側と外側
Apple AirTag第2世代4パックは79.00ドル(定価99ドル)、10万6,234ウォン。レビュー1万3,500件、過去1か月に1万個以上販売。1個あたり2万6,558ウォンです。
Kindle Paperwhite 16GB(2024)は129.99ドル(定価199.99ドル)、17万4,800ウォン。レビュー2万4,200件、ブラックフライデー表示付き。
Kindle Colorsoftは169.99ドル、22万8,600ウォン。単体なら200ドル以内ですが余裕は30ドルだけ。ケースや充電器を足すと超えます。
Fire TV Stick 4K(最新)は19.99ドル(定価59.99ドル)、2万6,885ウォンで67%引き。HDモデルは15.99ドル、2台でも40ドルです。

3. 組み合わせで200ドルが分かれる
AirTag(79.00)＋Fire TV Stick 4K(19.99)＝98.99ドル、13万3,116ウォン。200ドルまで100ドル残ります。
AirTag＋Kindle Paperwhite＝208.99ドル、28万1,050ウォン。200ドルを9ドル超えます。この場合、超えた9ドルではなく208.99ドル全体に関税と付加価値税。電子機器の関税率が0%でも付加価値税10%だけで約2万8,000ウォンです。9ドル(約1万2,000ウォン)を節約して2万8,000ウォンを払う構造です。
Kindle Colorsoft(169.99)＋ケース(20〜30ドル)も同じ罠。199.99ドルと189.99ドルは似て見えますが、前者は全額課税、後者は免税です。
同じ販売者(アマゾン)から同じ日に買った商品を免税範囲内に分けて持ち込むと合算課税されます。注文を分けても販売者と日付が同じなら合算対象になり得るので、日付か販売者を分けるのが安全です。

4. 大型家電は土俵が違う
55型テレビやモニターは200ドルの話ではありません。基準を超えると一般輸入申告になり、テレビは関税8%前後＋付加価値税10%、さらに送料と破損リスクが乗ります。直球が得になるのは小さく軽いIT機器です。

5. 2026年に変わった通関手続き
関税庁は2026年10月26日に海外直球専用の通関プラットフォームを開設し、使い捨て認証番号制度を導入しました。注文時や注文後に6桁の認証番号を求められることがあります。個人通関固有符号の有効期間は2026年から1年で、期限切れは通関が止まるため支払い前に確認を。
課税された荷物を返品すれば税金は還付されますが、返送料と手続きは自己負担です。微妙な金額なら最初から200ドル以下に組むほうが確実です。

支払い前の確認3点
第一に、カートの商品価格合計(送料ではなく)が200ドル以下か。第二に、同じ販売者から同じ日に買っていないか。分けても合算され得ます。第三に、リスト通関除外品目が混ざっていないか。サプリや食品を1点でも入れると荷物全体が150ドル基準になります。

まとめ
今回のアマゾンで200ドルの線に最も合う組み合わせはAirTag 4パック(79ドル)＋Fire TV Stick 4K(19.99ドル)の98.99ドル。Kindle Paperwhiteを足すと208.99ドルで9ドル超過、全額課税となり付加価値税だけで約2万8,000ウォンです。200ドルを超えない組み合わせを作ることが、今週の直球でお金を守る方法です。"""

ZH_DESC = """亚马逊黑色星期五从11月19日持续到30日。美国直购最关键的數字不是折扣率，而是200美元。超过这条线，关税与增值税按商品全额计征，而非仅对超出部分。本文把11月25日在亚马逊上确认的四件商品按200美元线、汇率1,344.73韩元/美元计算。

1. 200美元的准确条件
从美国以特快方式寄送的清单通关自用商品，商品价格200美元以下免征关税与增值税；美国以外为150美元。也有例外：药品、健康功能食品、食品等不属于清单通关，即使来自美国也适用150美元标准。电子产品与生活用品大多适用200美元。
作为基准的「商品价格」= 商品货款 + 美国境内销售税与境内运费；到韩国的国际运费若能明确区分则可扣除。因此运费高不会缩小免税额度，但一旦超额，国际运费也计入课税价格。

2. 实测四件——线内与线外
Apple AirTag第二代4件装79.00美元（定价99美元），合106,234韩元，评论1.35万条、近一个月售出1万件以上，每件约26,558韩元。
Kindle Paperwhite 16GB（2024）129.99美元（定价199.99美元），174,800韩元，评论2.42万条，标注黑五优惠。
Kindle Colorsoft为169.99美元，228,600韩元。单独购买在200美元以内，但只余30美元，加保护套或充电器就超标。
Fire TV Stick 4K（最新）19.99美元（定价59.99美元），26,885韩元，折扣67%；HD版15.99美元。

3. 组合决定200美元
AirTag（79.00）+ Fire TV Stick 4K（19.99）= 98.99美元，133,116韩元，距200美元还有100美元空间。
AirTag + Kindle Paperwhite = 208.99美元，281,050韩元，超出9美元。此时对208.99美元全额征税，电子类关税即使0%，仅10%增值税就约2.8万韩元。为省9美元（约1.2万韩元）反而多付2.8万韩元。
Kindle Colorsoft（169.99）+保护套（20~30美元）同理：199.99美元与189.99美元看似相近，前者全额课税、后者免税。
从同一卖家（亚马逊）在同一天购买、为控制在限额内而分单寄送，会被合并课税。因此分开下单也可能被合并，最好分开日期或卖家。

4. 大型家电是另一档
55英寸电视或显示器不是200美元的问题。超过限额转入一般进口申报，电视关税约8%再加10%增值税，还要考虑运费与破损风险。直购的收益来自小而轻的IT设备。

5. 2026年通关变化
韩国关税厅于2026年10月26日开通海外直购专用通关平台，并引入一次性认证번호：下单时或下单后可能要求6位认证码。个人通关固有编号自2026年起有效期1年，过期会中断通关，付款前请确认。
被课税的包裹退货可申请退税，但退运费与手续需自行处理；金额接近限额时，不如一开始就组合到200美元以内。

付款前三项确认
第一，购物车商品价格合计（不是运费）是否在200美元以内；第二，是否同一卖家同一天购买；第三，是否混入清单通关排除品目（一件保健品或食品就会把整票货物降到150美元标准）。

一句话总结
本次亚马逊最贴合200美元线的组合是AirTag 4件装（79美元）+ Fire TV Stick 4K（19.99美元）= 98.99美元。加上Kindle Paperwhite会到208.99美元，超9美元即全额课税，仅增值税就约2.8万韩元。把组合压在200美元以下，才是本周直购守住钱包的方法。"""

POST = {
    "id": SLUG,
    "slug": SLUG,
    "category": "tech",
    "store": "아마존",
    "priceKrw": 106234,
    "releaseDate": "2026-11-25",
    "rating": 4.6,
    "imageUrl": C,
    "images": [G1, G2, G3],
    "affiliateUrl": q("애플 에어태그 4팩"),
    "affiliatePlatform": "Coupang",
    "exampleItems": [
        {
            "name": "Apple AirTag 2세대 4팩 (아마존 $79.00)",
            "brand": "Apple",
            "priceKrw": 106234,
            "imageUrl": "/images/products/bf-amazon-airtag-4pack.jpg",
            "url": "https://www.amazon.com/dp/B0GJTXVN9Z",
            "category": "트래커",
        },
        {
            "name": "Kindle Paperwhite 16GB 2024 (아마존 $129.99)",
            "brand": "Amazon",
            "priceKrw": 174800,
            "imageUrl": "/images/products/bf-amazon-kindle-paperwhite.jpg",
            "url": "https://www.amazon.com/dp/B0CFPJYX7P",
            "category": "전자책",
        },
        {
            "name": "Kindle Colorsoft (아마존 $169.99)",
            "brand": "Amazon",
            "priceKrw": 228600,
            "imageUrl": "/images/products/bf-amazon-kindle-colorsoft.jpg",
            "url": "https://www.amazon.com/dp/B0CGVSKR1G",
            "category": "전자책",
        },
        {
            "name": "Fire TV Stick 4K 최신형 (아마존 $19.99)",
            "brand": "Amazon",
            "priceKrw": 26885,
            "imageUrl": "/images/products/bf-amazon-firetv-stick-4k.jpg",
            "url": "https://www.amazon.com/dp/B0G4XRP464",
            "category": "스트리밍",
        },
    ],
    "i18n": {
        "ko": {
            "title": "아마존 직구 200달러 컷 — 실측 4종과 넘으면 2만8천 원 더 내는 조합",
            "summary": "아마존 블프는 11/19~30. 미국발 특송은 200달러까지 면세인데, 넘으면 전체 과세입니다. 11/25 실측: 에어태그 4팩 $79(10만6,234원), 킨들 페이퍼화이트 $129.99, 컬러소프트 $169.99, 파이어TV 4K $19.99. 에어태그+킨들은 $208.99로 9달러 초과, 부가세만 2만8,000원입니다.",
            "description": KO_DESC,
            "tasteReview": [
                "미국발 특송 목록통관 200달러 이하 면세, 건강기능식품·식품은 150달러 기준, 초과 시 전체 과세",
                "실측(환율 1,344.73원): 에어태그 2세대 4팩 $79.00 / 킨들 페이퍼화이트 $129.99 / 컬러소프트 $169.99 / 파이어TV 4K $19.99",
                "안전 조합: 에어태그+파이어TV = $98.99 (13만3,116원)",
                "위험 조합: 에어태그+킨들 = $208.99 (28만1,050원) → 9달러 초과로 전체 과세, 부가세 약 2만8,000원",
                "2026-10-26 통관플랫폼 개통·일회용 인증번호, 개인통관고유부호 유효기간 1년",
            ],
            "tips": "가격은 2026-11-25 12:30~12:40 KST 아마존 표시가, 환율은 USD/KRW 1,344.73 기준입니다. 이 글은 쿠팡 파트너스 활동의 일환으로 수수료를 받을 수 있으며 아마존 링크는 상품 원문 링크입니다.",
        },
        "en": {
            "title": "Amazon's $200 Duty-Free Cut: 4 Items Measured, and the Combination That Costs 28,000 Won",
            "summary": "Amazon Black Friday runs November 19-30. US express shipments are duty-free to $200, and above that the whole value is taxed. Checked on November 25: AirTag 4-pack $79 (106,234 won), Kindle Paperwhite $129.99, Colorsoft $169.99, Fire TV Stick 4K $19.99. AirTag plus Kindle is $208.99 — $9 over, adding about 28,000 won in VAT alone.",
            "description": EN_DESC,
            "tasteReview": [
                "US express list clearance is duty-free to $200; supplements and foods fall back to $150; crossing the line taxes the full value",
                "Checked at 1,344.73 won per dollar: AirTag 2nd gen 4-pack $79.00, Kindle Paperwhite $129.99, Colorsoft $169.99, Fire TV Stick 4K $19.99",
                "Safe pairing: AirTag + Fire TV Stick = $98.99 (133,116 won)",
                "Risky pairing: AirTag + Kindle = $208.99 (281,050 won) — $9 over, whole value taxed, about 28,000 won VAT",
                "2026 changes: clearance platform with one-time verification number (Oct 26), personal customs code valid one year",
            ],
            "tips": "Prices are Amazon listings at 12:30-12:40 KST on 25 November 2026 at USD/KRW 1,344.73. This post contains affiliate links and may earn a commission; Amazon links go to the product pages.",
        },
        "ja": {
            "title": "アマゾン直球200ドルの線——実測4点と、超えると2万8千ウォン余計に払う組み合わせ",
            "summary": "アマゾンのブラックフライデーは11/19〜30。米国発特送は200ドルまで免税、超えると全額課税です。11/25実測: AirTag 4パック79ドル(10万6,234ウォン)、Kindle Paperwhite 129.99ドル、Colorsoft 169.99ドル、Fire TV Stick 4K 19.99ドル。AirTag＋Kindleは208.99ドルで9ドル超過、付加価値税だけで約2万8千ウォン。",
            "description": JA_DESC,
            "tasteReview": [
                "米国発特送のリスト通関は200ドル以下免税、健康機能食品・食品は150ドル基準、超過時は全額課税",
                "実測(1ドル1,344.73ウォン): AirTag第2世代4パック79.00ドル、Kindle Paperwhite 129.99ドル、Colorsoft 169.99ドル、Fire TV Stick 4K 19.99ドル",
                "安全な組み合わせ: AirTag＋Fire TV Stick＝98.99ドル(13万3,116ウォン)",
                "危険な組み合わせ: AirTag＋Kindle＝208.99ドル(28万1,050ウォン)、9ドル超過で全額課税・付加価値税約2万8千ウォン",
                "2026年10月26日通関プラットフォーム開設・使い捨て認証番号、個人通関固有符号は有効期間1年",
            ],
            "tips": "価格は2026-11-25 12:30〜12:40 KSTのアマゾン表示価格、為替は1ドル1,344.73ウォン基準です。本記事はアフィリエイトリンクを含み手数料を受け取る場合があり、アマゾンのリンクは商品ページです。",
        },
        "zh": {
            "title": "亚马逊直购200美元线——实测4件与超线多付2.8万韩元的组合",
            "summary": "亚马逊黑五为11/19~30。美国发特快200美元以内免税，超出则全额课税。11/25实测：AirTag 4件装79美元（106,234韩元）、Kindle Paperwhite 129.99美元、Colorsoft 169.99美元、Fire TV Stick 4K 19.99美元。AirTag+Kindle为208.99美元，超9美元，仅增值税就约2.8万韩元。",
            "description": ZH_DESC,
            "tasteReview": [
                "美国发特快清单通关200美元以内免税；健康功能食品·食品适用150美元；超额则全额课税",
                "实测（1,344.73韩元/美元）：AirTag二代4件装79.00、Kindle Paperwhite 129.99、Colorsoft 169.99、Fire TV Stick 4K 19.99美元",
                "安全组合：AirTag+Fire TV Stick=98.99美元（133,116韩元）",
                "风险组合：AirTag+Kindle=208.99美元（281,050韩元），超9美元即全额课税，增值税约2.8万韩元",
                "2026-10-26通关平台开通与一次性认证码，个人通关编号有效期1年",
            ],
            "tips": "价格为2026-11-25 12:30~12:40 KST亚马逊显示价，汇率为1,344.73韩元/美元。本文含联盟链接，可能获得佣金；亚马逊链接为商品页。",
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
except Exception as e:
    print(f"[-] Revalidate error: {e}")
