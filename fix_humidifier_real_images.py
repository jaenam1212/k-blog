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
import os

def _env_local(name):
    """Read a value from the .env.local next to this script (never hardcode secrets)."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env.local")
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith(name + "="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
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
SUPABASE_KEY = _require_env("SUPABASE_SERVICE_ROLE_KEY")
REVALIDATE_URL = ("https://www.k-trand.store/api/revalidate?secret="
                  + _require_env("REVALIDATE_SECRET"))

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
