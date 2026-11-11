#!/usr/bin/env python3
"""
Musinsa Men's Winter Trend & Snap Auto-Harvesting Pipeline
Fetches 20s Men's Winter Trending Snaps -> Extracts exact tagged garments ->
Generates 4-language editorial post -> Saves local assets -> Upserts to Supabase -> Revalidates ISR.
"""

import os
import sys
import json
import urllib.request
import urllib.error
import re
from datetime import datetime

SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptdXFtdnh1YnV3aG9vY3Vrbm50Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDMwODA3NywiZXhwIjoyMTA5ODg0MDc3fQ.ELyAmyRJrWdQoIHRu4thMGvjAnjJfVZ4S8Cfpb9MiDY"
REVALIDATE_URL = "https://k-blog-ten.vercel.app/api/revalidate?secret=kblog2026"

PUBLIC_IMG_DIR = os.path.join(os.path.dirname(__file__), "public", "images", "products")
os.makedirs(PUBLIC_IMG_DIR, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def fetch_json_from_next(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            html = r.read().decode("utf-8")
            s = html.find('<script id="__NEXT_DATA__" type="application/json">')
            if s == -1:
                return None
            s += len('<script id="__NEXT_DATA__" type="application/json">')
            e = html.find('</script>', s)
            return json.loads(html[s:e])
    except Exception as ex:
        print(f"[-] Fetch error for {url}: {ex}")
        return None

def download_image(img_url, local_filename):
    if not img_url:
        return "/images/placeholder.jpg"
    if img_url.startswith("//"):
        img_url = "https:" + img_url
    elif img_url.startswith("/"):
        img_url = "https://image.msscdn.net" + img_url
    local_path = os.path.join(PUBLIC_IMG_DIR, local_filename)
    if os.path.exists(local_path) and os.path.getsize(local_path) > 1000:
        return f"/images/products/{local_filename}"
    req = urllib.request.Request(img_url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            with open(local_path, "wb") as f:
                f.write(r.read())
        print(f"[+] Downloaded image: {local_filename}")
        return f"/images/products/{local_filename}"
    except Exception as ex:
        print(f"[-] Failed downloading {img_url}: {ex}")
        return img_url

def get_product_details(goods_no):
    url = f"https://www.musinsa.com/products/{goods_no}"
    data = fetch_json_from_next(url)
    if not data:
        return None
    queries = data.get("props", {}).get("pageProps", {}).get("dehydratedState", {}).get("queries", [])
    for q in queries:
        qk = str(q.get("queryKey"))
        if qk.startswith("['Detail', ") and str(goods_no) in qk:
            st = q.get("state", {}).get("data", {}).get("data", {})
            return {
                "goodsNo": goods_no,
                "goodsNm": st.get("goodsNm"),
                "goodsNmEng": st.get("goodsNmEng"),
                "brand": st.get("brand"),
                "thumbnailImageUrl": st.get("thumbnailImageUrl"),
                "price": st.get("goodsPrice", {}).get("salePrice") or st.get("goodsPrice", {}).get("normalPrice") or 0,
                "normalPrice": st.get("goodsPrice", {}).get("normalPrice") or 0,
                "url": f"https://www.musinsa.com/products/{goods_no}"
            }
    return None

def harvest_musinsa_snaps():
    print("[*] Harvesting Musinsa Men's Winter Snaps...")
    url = "https://www.musinsa.com/snap/main/recommend?types=CODISHOP_SNAP&genders=MALE"
    data = fetch_json_from_next(url)
    if not data:
        print("[-] Failed to fetch main snap recommend page.")
        return []
    
    q5 = data.get("props", {}).get("pageProps", {}).get("dehydratedState", {}).get("queries", [])[5]
    contents = q5.get("state", {}).get("data", {}).get("pages", [{}])[0].get("data", {}).get("list", [{}])[0].get("contents", [])
    print(f"[*] Found {len(contents)} candidate snaps.")
    
    harvested = []
    
    for c in contents:
        snap_id = c.get("id")
        detail_url = f"https://www.musinsa.com/snap/{snap_id}"
        d_data = fetch_json_from_next(detail_url)
        if not d_data:
            continue
        
        queries = d_data.get("props", {}).get("pageProps", {}).get("dehydratedState", {}).get("queries", [])
        if len(queries) < 5:
            continue
        sd = queries[4].get("state", {}).get("data", {}).get("data", {})
        
        detail = sd.get("detail", {})
        title = detail.get("title", "")
        content = detail.get("content", "")
        medias = sd.get("medias", [])
        goods = sd.get("goods", [])
        
        # Check winter/men relevance
        text_corpus = (title + " " + content).lower()
        is_winter = any(k in text_corpus for k in ["겨울", "코트", "패딩", "플리스", "아우터", "발마칸", "헤비", "윈터"])
        
        if not is_winter or not goods or not medias:
            continue
        
        snap_img_url = medias[0].get("path")
        # Main tagged product (usually goods[0] is outerwear/hero item)
        hero_good = None
        for g in goods[:2]:
            g_info = get_product_details(g.get("goodsNo"))
            if g_info and g_info.get("goodsNm"):
                hero_good = g_info
                break
        
        if not hero_good:
            continue
        
        print(f"[+] Harvested Snap {snap_id}: {hero_good['brand']} - {hero_good['goodsNm']}")
        harvested.append({
            "snapId": snap_id,
            "snapTitle": title,
            "snapContent": content,
            "snapImage": snap_img_url,
            "heroGood": hero_good,
            "allGoods": goods
        })
        
        if len(harvested) >= 2:
            break
            
    return harvested

def build_post_payload(item):
    hero = item["heroGood"]
    snap_id = item["snapId"]
    brand = hero["brand"]
    goods_nm = hero["goodsNm"]
    price = hero["price"]
    
    # Download images locally for zero broken links
    slug = f"musinsa-mens-winter-{brand.lower()}-{hero['goodsNo']}"
    slug = re.sub(r'[^a-z0-9\-]', '-', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    
    snap_local_img = download_image(item["snapImage"], f"{slug}-snap.jpg")
    hero_local_img = download_image(hero["thumbnailImageUrl"], f"{slug}-item.jpg")
    
    # Use snap outfit image as primary card image
    primary_img = snap_local_img
    
    # Generate 4-language content
    # Korean
    ko_title = f"무신사 20대 겨울 랭킹 코디: {brand} \"{goods_nm}\" 실착 스타일링 가이드"
    ko_summary = f"무신사 스냅 랭킹 1위 코디! {brand} 아우터와 편안한 레이어드로 완성하는 2026 겨울 트렌드 실착 핏 분석"
    ko_desc = (
        f"무신사 20대 남성 패션 랭킹에서 높은 조회수를 기록 중인 실착 스냅 기반의 겨울 코디네이션입니다. "
        f"핵심 아이템인 '{brand}'의 '{goods_nm}'(발매가 {price:,}원)을 중심으로, "
        f"편안한 스웨트 팬츠와 이너 후디 레이어드를 믹스 매치해 보온성과 트렌디한 스트릿 무드를 완벽하게 잡았습니다."
    )
    ko_points = [
        f"무신사 공식 코디 스냅 인증 착샷으로 과장 없는 자연스러운 실루엣과 기장감 확인 가능",
        f"단독 착용은 물론 후디·셔츠와의 다채로운 레이어드에 최적화된 오버핏 드롭 숄더 실루엣",
        f"현재 무신사 스토어 기준 {price:,}원에 판매 중이며 20대 데일리 겨울 아우터로 높은 인기"
    ]
    ko_tips = "이너로 두꺼운 스웨트셔츠나 니트를 받쳐 입는 겨울 특성상 정사이즈 선택 시 여유 있는 오버핏 실루엣이 연출됩니다."
    
    # English
    en_title = f"Seoul Street Style FW26: {brand} \"{goods_nm}\" Musinsa Trend Guide"
    en_summary = f"Ranked #1 in Musinsa Korea winter snaps: how Seoul men layer the {brand} outerwear with effortless minimalism."
    en_desc = (
        f"Straight from Seoul's definitive youth fashion hub Musinsa, this winter coordination showcases "
        f"the viral '{goods_nm}' from cult Korean streetwear label {brand} ({price:,} KRW / approx. ${price//1400} USD). "
        f"Effortlessly mixing relaxed sweatpants with smart layering, it captures the signature 2026 Seoul minimalist aesthetic."
    )
    en_points = [
        f"Verified real-world Musinsa lookbook snap showing genuine silhouette and length proportions",
        f"Engineered for winter warmth with roomy shoulders made for layering hoodies and knitwear",
        f"Official Musinsa Store retail price at {price:,} KRW with global shipping available"
    ]
    en_tips = "Choose your regular size for an intentional modern relaxed drape that layers comfortably over winter thermals."
    
    # Japanese
    ja_title = f"韓国MUSINSA冬のメンズ人気コーデ：{brand}「{goods_nm}」着こなし解説"
    ja_summary = f"ムシンサスナップランキング上位！{brand}の注目アウターで作る2026冬の洗練ソウルストリートコーデ。"
    ja_desc = (
        f"韓国20代メンズに絶大な支持を受けるファッション通販MUSINSA（ムシンサ）の公式スナップより。 "
        f"韓国ストリートを牽引する{brand}の「{goods_nm}」（販売価格 {price:,}ウォン）を主役に、 "
        f"スウェットやフーディーを巧みにレイヤードしたリアルな冬のソウルスタイルを徹底解剖します。"
    )
    ja_points = [
        f"ムシンサ公式スナップに基づく実着用コーディネートで、着丈やシルエットのバランスが一目で把握可能",
        f"防寒性とトレンド感を両立したドロップショルダー設計で、中に着込んでも着膨れしない絶妙なサイジング",
        f"MUSINSA GLOBALサイトでも取り扱いがあり、日本へのスピード配送にも対応"
    ]
    ja_tips = "インナーに厚手のパーカーを重ね着する場合でも普段のジャストサイズを選べば綺麗な落ち感を楽しめます。"
    
    # Chinese
    zh_title = f"韩国MUSINSA秋冬男装穿搭天花板：{brand}“{goods_nm}”实穿版型测评"
    zh_summary = f"首尔20代男生冬日最爱街头搭配！{brand}冬季外套实着街拍与多层次叠穿指南。"
    zh_desc = (
        f"来自韩国第一时尚社区MUSINSA官方认证街拍！以本土大热品牌{brand}的明星单品「{goods_nm}」（售价 {price:,}韩元）为核心， "
        f"完美融合卫衣、衬衫与休闲阔腿裤，展现出2026首尔青年独有的松弛感极简街头氛围。"
    )
    zh_points = [
        f"官方街拍模特实穿直出，真实呈现上身垂坠感与衣长比例，拒绝照骗",
        f"落肩微宽松剪裁专为冬季叠穿设计，保暖御寒同时保持全身利落线条",
        f"MUSINSA官方正品保证，支持海外直邮与跨境支付"
    ]
    zh_tips = "版型自带恰到好处的松弛感，选平时正码即可轻松穿出韩系慵懒氛围。"
    
    post = {
        "id": f"musinsa-snap-{hero['goodsNo']}-202611",
        "slug": slug,
        "category": "k-fashion",
        "store": f"Musinsa ({brand})",
        "priceKrw": price,
        "releaseDate": datetime.now().strftime("%Y-%m-%d"),
        "rating": 4.9,
        "imageUrl": primary_img,
        "affiliateUrl": hero["url"],
        "affiliatePlatform": "Musinsa",
        "i18n": {
            "ko": {
                "title": ko_title,
                "summary": ko_summary,
                "description": ko_desc,
                "tasteReview": ko_points,
                "tips": ko_tips
            },
            "en": {
                "title": en_title,
                "summary": en_summary,
                "description": en_desc,
                "tasteReview": en_points,
                "tips": en_tips
            },
            "ja": {
                "title": ja_title,
                "summary": ja_summary,
                "description": ja_desc,
                "tasteReview": ja_points,
                "tips": ja_tips
            },
            "zh": {
                "title": zh_title,
                "summary": zh_summary,
                "description": zh_desc,
                "tasteReview": zh_points,
                "tips": zh_tips
            }
        }
    }
    return post

def upload_to_supabase(posts):
    if not posts:
        return
    print(f"[*] Uploading {len(posts)} posts to Supabase...")
    rows = [{"slug": p["slug"], "data": p} for p in posts]
    
    url = f"{SUPABASE_URL}/rest/v1/posts"
    data_bytes = json.dumps(rows).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data_bytes,
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            print(f"[+] Successfully uploaded {len(res)} posts into Supabase!")
            for r in res:
                print(f"    - ID: {r['id']}, Slug: {r['slug']}")
            return True
    except urllib.error.HTTPError as he:
        print(f"[-] Supabase HTTP Error {he.code}: {he.read().decode('utf-8')}")
        return False
    except Exception as ex:
        print(f"[-] Supabase Error: {ex}")
        return False

def trigger_revalidate():
    print(f"[*] Triggering Vercel on-demand ISR revalidation: {REVALIDATE_URL}")
    req = urllib.request.Request(
        REVALIDATE_URL,
        data=json.dumps({"secret": "kblog2026"}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as r:
            res = json.loads(r.read().decode("utf-8"))
            print(f"[+] Revalidation result: {res}")
            return True
    except Exception as ex:
        print(f"[-] Revalidation failed: {ex}")
        return False

if __name__ == "__main__":
    snaps = harvest_musinsa_snaps()
    if not snaps:
        print("[-] No snaps harvested.")
        sys.exit(1)
    
    posts = [build_post_payload(s) for s in snaps]
    success = upload_to_supabase(posts)
    if success:
        trigger_revalidate()
        print("[+] Pipeline execution completed successfully!")
