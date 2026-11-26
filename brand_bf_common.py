#!/usr/bin/env python3
"""브랜드 자체 블프 시리즈 공통 발행 헬퍼 (2026-11-26)."""
import json
import os
import urllib.request
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))


def _env_local(name):
    try:
        for line in open(os.path.join(HERE, ".env.local"), encoding="utf-8"):
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip()
    except OSError:
        pass
    return ""


def require_env(name):
    value = os.environ.get(name) or _env_local(name)
    if not value:
        raise SystemExit(f"{name} is not set. Set it in the environment or in .env.local.")
    return value


def bearer_header(key):
    """Legacy JWT keys ride on Authorization; new sb_ keys must not (Invalid JWT)."""
    return {"Authorization": f"Bearer {key}"} if key.startswith("eyJ") else {}


SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or _env_local("SUPABASE_SERVICE_ROLE_KEY")
REVALIDATE_URL = ("https://www.k-trand.store/api/revalidate?secret=" + require_env("REVALIDATE_SECRET"))

COUPANG = "https://www.coupang.com/np/search?q="
TAG = "&lptag=AF9412775"
CREATOR_SHOP = "https://cshop.naver.com/jaenam"


def q(term):
    return COUPANG + quote(term) + TAG


def publish(POST):
    slug = POST["slug"]
    headers = {
        "apikey": SUPABASE_KEY,
        **bearer_header(SUPABASE_KEY),
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }
    check_url = f"{SUPABASE_URL}/rest/v1/posts?slug=eq.{slug}&select=id"
    req = urllib.request.Request(check_url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        existing = json.loads(resp.read().decode("utf-8"))

    if existing:
        upd = f"{SUPABASE_URL}/rest/v1/posts?id=eq.{existing[0]['id']}"
        payload = json.dumps({"data": POST}).encode("utf-8")
        urllib.request.urlopen(urllib.request.Request(upd, data=payload, headers=headers, method="PATCH"))
        print(f"[+] Updated: {slug}")
    else:
        payload = json.dumps({"slug": slug, "data": POST}).encode("utf-8")
        r = urllib.request.urlopen(
            urllib.request.Request(f"{SUPABASE_URL}/rest/v1/posts", data=payload, headers=headers, method="POST"))
        print(f"[+] Inserted: {slug} ({r.status})")

    try:
        urllib.request.urlopen(urllib.request.Request(REVALIDATE_URL), timeout=180)
        print("[+] Revalidated")
    except Exception as e:  # noqa: BLE001
        print(f"[-] Revalidate error: {e}")
