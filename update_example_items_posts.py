#!/usr/bin/env python3
"""
Add concrete recommended example items (brands, product names, price ranges)
to both color matching posts on Supabase and revalidate Vercel cache.
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


def _bearer_header(key):
    """Legacy JWT keys ride on Authorization; new sb_ keys must not (Invalid JWT)."""
    return {"Authorization": f"Bearer {key}"} if key.startswith("eyJ") else {}




SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = _require_env("SUPABASE_SERVICE_ROLE_KEY")
REVALIDATE_URL = ("https://www.k-trand.store/api/revalidate?secret="
                  + _require_env("REVALIDATE_SECRET"))

headers = {
    "apikey": SUPABASE_KEY,
    **_bearer_header(SUPABASE_KEY),
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

desc_8color_ko = """평소 옷 입을 때 옷장을 열어보면 검정 패딩, 검정 슬랙스, 회색 후드티만 가득한 분들이 많습니다.
무난하고 깔끔하다는 이유로 무채색만 고집하다 보면 자칫 인상이 칙칙해 보이거나 밋밋한 느낌을 주기 쉽습니다.

그렇다고 과한 원색이나 형광색을 매치하는 것은 부담스러울 수 있습니다.
이럴 때 가장 좋은 방법은 평소 즐겨 입던 검정·회색 기본 아이템에, 서로 자연스럽게 어우러지는 '포인트 컬러' 한 가지를 더하는 것입니다.

SNS에서 큰 반응을 얻은 실패 없는 8가지 컬러 매치 공식과, 지금 바로 무신사·SPA에서 장만해 써먹기 좋은 대표 예시 아이템을 함께 정리해 드립니다.

1. 브라운 + 그레이 (Brown + Grey)
따뜻하고 묵직한 브라운과 차분한 그레이가 서로의 단점을 완벽하게 보완해 줍니다.
• 추천 아우터: 무신사 스탠다드 MTR 오버사이즈 발마칸 코트 [딥 브라운] (269,890원)
• 추천 이너: 유니클로 프리미엄 램스울 크루넥 스웨터 [그레이] (49,900원)

2. 그린 + 네이비 (Green + Navy)
클래식한 네이비 베이스에 딥한 포레스트 그린을 얹어 지적이면서도 생동감 있는 분위기를 만듭니다.
• 추천 하의: 자라 릴랙스 핏 네이비 울 테일러드 슬랙스 (79,900원)
• 추천 상의: 쿠어(COOOR) 탑필 헤비 캐시미어 니트 [포레스트 그린] (108,000원)

3. 차콜 + 블루 (Charcoal + Blue)
블랙 대신 묵직한 차콜 슬랙스에 스카이블루나 딥블루 이너를 더하는 세련된 출근 룩 치트키입니다.
• 추천 하의: 무신사 스탠다드 와이드 히든 밴딩 슬랙스 [차콜 그레이] (43,900원)
• 추천 이너: 토마스모어(THOMAS MORE) 페이퍼 옥스포드 셔츠 [스카이블루] (62,000원)

4. 그린 + 핑크 (Green + Pink)
투박할 수 있는 카키 야상이나 올리브 패딩을 은은한 연핑크 이너가 감각적으로 중화해 줍니다.
• 추천 아우터: 유니클로 하이브리드 다운 파카 [다크 그린/카키] (129,000원)
• 추천 이너: 인스턴트펑크 모헤어 라운드 가디건 [더스티 핑크] (118,000원)

5. 옐로우 + 블루 (Yellow + Blue)
네이비 아우터에 버터 옐로우 이너를 매치해 뚜렷한 색 대비로 한층 밝고 젊은 활력을 줍니다.
• 추천 아우터: 커버낫 울 발마칸 싱글 코트 [네이비] (199,000원)
• 추천 이너: 무신사 스탠다드 빅토리아 울 크루넥 니트 [버터 옐로우] (50,310원)

6. 브라운 + 레드 (Brown + Red)
차분한 브라운 코트에 산뜻한 레드 머플러나 가디건을 더해 손쉽게 프렌치 무드를 완성합니다.
• 추천 아우터: 자라 MANTECO® 울 혼방 레귤러 핏 코트 [브라운] (329,900원)
• 추천 소품: 무신사 스탠다드 캐시미어 블렌드 머플러 [체리 레드] (39,900원)

7. 퍼플 + 그레이 (Purple + Grey)
그레이 팬츠에 은은한 라벤더 컬러를 받쳐 과하지 않으면서도 신비로운 세련미를 뽐낼 수 있습니다.
• 추천 아우터: 파사드패턴 램스울 V넥 가디건 [그레이] (138,000원)
• 추천 이너: 이에이(YEEA) 소프트 텐셀 터틀넥 [라벤더 퍼플] (38,000원)

8. 버건디 + 블랙 (Burgundy + Black)
올블랙 스타일에 버건디 레더 자켓이나 니트 하나를 걸쳐 성숙하고 묵직한 가오를 살립니다.
• 추천 아우터: 도프제이슨 오버핏 비건 레더 싱글 자켓 [딥 버건디] (119,000원)
• 추천 베이스: 스파오 베이직 울 라이크 와이드 슬랙스 [블랙] (39,900원)

결론:
스타일의 완성은 비싼 옷이 아니라 '색상의 조화'에서 나옵니다.
베이스 컬러 70%에 포인트 컬러 30%의 황금 비율을 기억해 보세요."""

desc_3color_ko = """스타일링을 할 때 두 가지 색상만 쓰면 단조로워 보이기 쉽고, 반대로 네 가지 이상의 색상을 섞으면 자칫 산만하고 어수선한 인상을 줄 수 있습니다.

패션 피플들이 핀터레스트나 인스타그램에서 감도 높은 사진을 연출할 때 애용하는 절대 원칙이 바로 '3컬러 법칙(Three-Color Rule)'입니다.
안정적인 베이스 컬러 2가지에 매력적인 포인트 컬러 1가지를 자연스럽게 레이어드하는 방식입니다.

SNS에서 저장 수 급증 중인 실패 없는 5가지 삼위일체 컬러 조합과, 실전 추천 예시 아이템을 함께 정리해 드립니다.

1. 그레이 & 화이트 + 옐로우 (Grey & White + Yellow)
깔끔한 차콜 코트에 화이트 셔츠를 매치하고, 부드러운 버터 옐로우 니트로 화사함을 더하는 조합입니다.
• 추천 베이스 코트: 무신사 스탠다드 MTR 캐시미어 싱글 코트 [차콜 그레이] (249,000원)
• 추천 이너 셔츠: 무신사 스탠다드 릴랙스 핏 옥스포드 셔츠 [화이트] (35,900원)
• 추천 포인트 니트: 빅토리아 울 크루 넥 니트 [버터 옐로우] (50,310원)

2. 화이트 & 네이비 + 베이지 (White & Navy + Beige)
클래식한 네이비 자켓에 화이트 이너, 그리고 베이지 와이드 슬랙스를 매치하는 감도 높은 미니멀 룩입니다.
• 추천 자켓: 자라 오버사이즈 울 블렌드 블레이저 [네이비] (149,900원)
• 추천 이너: 유니클로 수피마 코튼 크루넥 티 [화이트] (19,900원)
• 추천 하의: 모디파이드 와이드 투턱 치노 팬츠 [웜 베이지] (54,000원)

3. 브라운 & 블랙 + 네이비 (Brown & Black + Navy)
다크 브라운 코트에 블랙 터틀넥, 그리고 네이비 머플러를 레이어드해 절제된 시크함을 자아냅니다.
• 추천 코트: 유니클로 남성 울 블렌드 발마칸 코트 [다크 브라운] (149,000원)
• 추천 이너: 스파오 소프트 터틀넥 스웨터 [블랙] (29,900원)
• 추천 소품: 무신사 스탠다드 캐시미어 100 머플러 [네이비] (49,900원)

4. 다크 브라운 & 화이트 + 골드 (Dark Brown & White + Gold)
깊이감 있는 에스프레소 브라운 코트에 아이보리 니트를 입고, 골드 버클이나 시계로 올드머니 룩을 완성합니다.
• 추천 아우터: 자라 오리진스 MANTECO® 울 코트 [에스프레소 브라운] (329,900원)
• 추천 이너: 쿠어(COOOR) 캐시미어 라운드 니트 [아이보리] (105,000원)
• 추천 소품: 페르커 클래식 가죽 벨트 [골드 버클] (42,000원)

5. 버건디 & 블루 + 그레이 (Burgundy & Blue + Grey)
깊은 와인 버건디 아우터에 생지 데님을 매치하고, 멜란지 그레이 이너로 톤을 차분하게 안정시키는 조합입니다.
• 추천 아우터: 디스이즈네버댓 빈티지 레더 바시티 자켓 [버건디] (189,000원)
• 추천 팬츠: 모드나인(MODNINE) 크롭 와이드 생지 데님 [인디고 블루] (89,000원)
• 추천 이너: 무신사 스탠다드 헤비웨이트 스웨트셔츠 [멜란지 그레이] (39,900원)

결론:
좋은 스타일링은 고가의 옷보다 '색상의 균형'을 아는 것에서 시작됩니다.
베이스 컬러 2가지(70%)와 포인트 컬러 1가지(30%), 이 황금 비율을 기억해 보세요."""

# 1. Update 8 color matching post
check_url1 = f"{SUPABASE_URL}/rest/v1/posts?slug=eq.fail-proof-8-color-matching-rules-for-men"
req1 = urllib.request.Request(check_url1, headers=headers)
with urllib.request.urlopen(req1) as resp:
    data1 = json.loads(resp.read().decode("utf-8"))[0]
    post_data1 = data1["data"]
    post_data1["i18n"]["ko"]["description"] = desc_8color_ko
    update_url1 = f"{SUPABASE_URL}/rest/v1/posts?id=eq.{data1['id']}"
    payload1 = json.dumps({"data": post_data1}).encode("utf-8")
    urllib.request.urlopen(urllib.request.Request(update_url1, data=payload1, headers=headers, method="PATCH"))
    print("[+] Added example items to 8-color match post.")

# 2. Update 3 color layering post
check_url2 = f"{SUPABASE_URL}/rest/v1/posts?slug=eq.pinterest-3-color-layering-rules-2026"
req2 = urllib.request.Request(check_url2, headers=headers)
with urllib.request.urlopen(req2) as resp:
    data2 = json.loads(resp.read().decode("utf-8"))[0]
    post_data2 = data2["data"]
    post_data2["i18n"]["ko"]["description"] = desc_3color_ko
    update_url2 = f"{SUPABASE_URL}/rest/v1/posts?id=eq.{data2['id']}"
    payload2 = json.dumps({"data": post_data2}).encode("utf-8")
    urllib.request.urlopen(urllib.request.Request(update_url2, data=payload2, headers=headers, method="PATCH"))
    print("[+] Added example items to 3-color layering post.")

# Revalidate
try:
    urllib.request.urlopen(urllib.request.Request(REVALIDATE_URL))
    print("[+] Revalidated Vercel cache successfully!")
except Exception as e:
    print(f"[-] Revalidate error: {e}")
