#!/usr/bin/env python3
"""
가열식 가습기 2편의 AI 생성 이미지를 실제 참고 페이지(공식 제품 상세/세척 가이드)에서
가져온 실물 사진으로 교체한다.

출처
 - 쿠쿠 CH-MS301FW 스팀100 : cuckoo.co.kr 공식몰 제품 상세 (productNo=8839)
 - LG 퓨리케어 하이드로타워 HY705RSUA : lge.co.kr 공식 제품 갤러리
 - 조지루시 EE-TAH60K : zojirushi.co.kr 공식 제품 상세 / '가습기 세척 및 장기 보관 가이드'
"""

import json
import urllib.request

SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptdXFtdnh1YnV3aG9vY3Vrbm50Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDMwODA3NywiZXhwIjoyMTA5ODg0MDc3fQ.ELyAmyRJrWdQoIHRu4thMGvjAnjJfVZ4S8Cfpb9MiDY"
REVALIDATE_URL = "https://www.k-trand.store/api/revalidate?secret=kblog2026"

UPDATES = {
    "heated-vs-ultrasonic-humidifier-power-cost-2026": {
        "imageUrl": "/images/products/real-humidifier-cuckoo-steam-room.jpg",
        "images": [
            "/images/products/real-humidifier-lg-hydrotower-room.jpg",
            "/images/products/real-humidifier-zojirushi-nursery.jpg",
            "/images/products/real-humidifier-cuckoo-tank.jpg",
        ],
    },
    "heated-humidifier-limescale-cleaning-2026": {
        "imageUrl": "/images/products/real-humidifier-cuckoo-tank-wash.jpg",
        "images": [
            "/images/products/real-humidifier-zojirushi-citric-acid.jpg",
            "/images/products/real-humidifier-zojirushi-tank-wipe.jpg",
            "/images/products/real-humidifier-zojirushi-heater.jpg",
        ],
    },
}

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation",
}

for slug, change in UPDATES.items():
    url = f"{SUPABASE_URL}/rest/v1/posts?slug=eq.{slug}&select=id,data"
    rows = json.loads(
        urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read().decode("utf-8")
    )
    if not rows:
        print(f"[-] Not found: {slug}")
        continue
    row = rows[0]
    data = row["data"]
    data["imageUrl"] = change["imageUrl"]
    data["images"] = change["images"]
    patch = f"{SUPABASE_URL}/rest/v1/posts?id=eq.{row['id']}"
    body = json.dumps({"data": data}).encode("utf-8")
    urllib.request.urlopen(
        urllib.request.Request(patch, data=body, headers=headers, method="PATCH")
    ).read()
    print(f"[+] Updated {slug}: {change['imageUrl']} (+{len(change['images'])} images)")

try:
    urllib.request.urlopen(urllib.request.Request(REVALIDATE_URL), timeout=60)
    print("[+] Revalidated Vercel cache")
except Exception as e:
    print(f"[-] Revalidate error: {e}")
