#!/usr/bin/env python3
"""
Populate concrete exampleItems with high-res product photos on Supabase
and trigger on-demand ISR revalidation.
"""

import json
import urllib.request

SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptdXFtdnh1YnV3aG9vY3Vrbm50Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDMwODA3NywiZXhwIjoyMTA5ODg0MDc3fQ.ELyAmyRJrWdQoIHRu4thMGvjAnjJfVZ4S8Cfpb9MiDY"
REVALIDATE_URL = "https://www.k-trand.store/api/revalidate?secret=kblog2026"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

items_post1 = [
  {
    "name": "MTR 오버사이즈 발마칸 코트 [딥 브라운]",
    "brand": "무신사 스탠다드",
    "priceKrw": 269890,
    "imageUrl": "/images/products/musinsa-mtr-balmacaan-coat.jpg",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "탑필 헤비 캐시미어 크루넥 니트 [포레스트 그린]",
    "brand": "쿠어 (COOOR)",
    "priceKrw": 108000,
    "imageUrl": "/images/products/item-green-knit.png",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "페이퍼 옥스포드 오버핏 셔츠 [스카이블루]",
    "brand": "토마스모어 (THOMAS MORE)",
    "priceKrw": 62000,
    "imageUrl": "/images/products/item-blue-shirt.png",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "와이드 히든 밴딩 테일러드 슬랙스 [차콜 그레이]",
    "brand": "무신사 스탠다드",
    "priceKrw": 43900,
    "imageUrl": "/images/products/item-charcoal-slacks.png",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "빅토리아 울 크루 넥 니트 [버터 옐로우]",
    "brand": "무신사 스탠다드",
    "priceKrw": 50310,
    "imageUrl": "/images/products/musinsa-butter-yellow-knit.jpg",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "오버핏 비건 레더 싱글 자켓 [딥 버건디]",
    "brand": "도프제이슨",
    "priceKrw": 119000,
    "imageUrl": "/images/products/item-burgundy-jacket.png",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  }
]

items_post2 = [
  {
    "name": "MTR 오버사이즈 캐시미어 코트 [차콜 그레이]",
    "brand": "무신사 스탠다드",
    "priceKrw": 249000,
    "imageUrl": "/images/products/musinsa-cashmere-coat.jpg",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "빅토리아 울 크루 넥 니트 [버터 옐로우]",
    "brand": "무신사 스탠다드",
    "priceKrw": 50310,
    "imageUrl": "/images/products/musinsa-butter-yellow-knit.jpg",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "와이드 투턱 치노 트라우저 [웜 베이지]",
    "brand": "모디파이드",
    "priceKrw": 54000,
    "imageUrl": "/images/products/item-beige-trousers.png",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "MANTECO® 울 혼방 레귤러 핏 코트 [에스프레소 브라운]",
    "brand": "자라 오리진스",
    "priceKrw": 329900,
    "imageUrl": "/images/products/zara-origins-manteco-wool-blend-coat-look-1.jpg",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "우먼즈 에센셜 라운드 넥 가디건 [체리 레드]",
    "brand": "무신사 스탠다드",
    "priceKrw": 38990,
    "imageUrl": "/images/products/musinsa-red-cardigan.jpg",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  },
  {
    "name": "쉐어링 레더 블루종 점퍼 [블랙/버건디]",
    "brand": "우라고 (urago)",
    "priceKrw": 218000,
    "imageUrl": "/images/products/musinsa-mens-winter-urago-7401165-item.jpg",
    "url": "https://www.musinsa.com/curator/s/jaenam1212"
  }
]

# Update Post 1
req1 = urllib.request.Request(f"{SUPABASE_URL}/rest/v1/posts?slug=eq.fail-proof-8-color-matching-rules-for-men", headers=headers)
with urllib.request.urlopen(req1) as resp:
    data1 = json.loads(resp.read().decode("utf-8"))[0]
    pdata1 = data1["data"]
    pdata1["exampleItems"] = items_post1
    up1 = f"{SUPABASE_URL}/rest/v1/posts?id=eq.{data1['id']}"
    urllib.request.urlopen(urllib.request.Request(up1, data=json.dumps({"data": pdata1}).encode("utf-8"), headers=headers, method="PATCH"))
    print("[+] Attached 6 exampleItems to post 1.")

# Update Post 2
req2 = urllib.request.Request(f"{SUPABASE_URL}/rest/v1/posts?slug=eq.pinterest-3-color-layering-rules-2026", headers=headers)
with urllib.request.urlopen(req2) as resp:
    data2 = json.loads(resp.read().decode("utf-8"))[0]
    pdata2 = data2["data"]
    pdata2["exampleItems"] = items_post2
    up2 = f"{SUPABASE_URL}/rest/v1/posts?id=eq.{data2['id']}"
    urllib.request.urlopen(urllib.request.Request(up2, data=json.dumps({"data": pdata2}).encode("utf-8"), headers=headers, method="PATCH"))
    print("[+] Attached 6 exampleItems to post 2.")

# Revalidate
try:
    urllib.request.urlopen(urllib.request.Request(REVALIDATE_URL))
    print("[+] Revalidated Vercel cache successfully!")
except Exception as e:
    print(f"[-] Revalidate error: {e}")
