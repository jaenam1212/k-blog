#!/usr/bin/env python3
"""
Update color matching posts to standard polished editorial tone while keeping hook titles and high-res lookbook images
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

posts = [
  {
    "slug": "fail-proof-8-color-matching-rules-for-men",
    "store": "무신사 스토어 큐레이션",
    "i18n_ko": {
      "title": "옷 못 입는 사람 특징: 옷장에 검정·회색만 있음 (실패 없는 8가지 색 조합 치트키)",
      "summary": "옷장에 검정 롱패딩과 회색 후드티만 가득하다면 주목해보세요. 비싼 명품을 사지 않아도, 컬러 조합만 제대로 맞추면 누구나 세련된 인상을 남길 수 있습니다.",
      "description": "평소 옷 입을 때 옷장을 열어보면 검정 패딩, 검정 슬랙스, 회색 후드티만 가득한 분들이 많습니다.\n무난하고 깔끔하다는 이유로 무채색만 고집하다 보면 자칫 인상이 칙칙해 보이거나 밋밋한 느낌을 주기 쉽습니다.\n\n그렇다고 과한 원색이나 형광색을 매치하는 것은 부담스러울 수 있습니다.\n이럴 때 가장 좋은 방법은 평소 즐겨 입던 검정·회색 기본 아이템에, 서로 자연스럽게 어우러지는 '포인트 컬러' 한 가지를 더하는 것입니다.\n\n최근 SNS에서 큰 반응을 얻은 '무채색에서 벗어나는 실패 없는 8가지 컬러 매치 공식'을 실전에 맞게 정리해 드립니다.\n\n1. 브라운 + 그레이 (Brown + Grey)\n따뜻하고 묵직한 브라운과 차분한 그레이가 서로의 단점을 보완해 줍니다. 캐시미어 니트에 울 코트를 매치할 때 가장 추천하는 고급스러운 조합입니다.\n\n2. 그린 + 네이비 (Green + Navy)\n클래식한 네이비 슬랙스나 자켓에 딥한 포레스트 그린 니트를 매치해 보세요. 튀지 않으면서도 안정감 있고 지적인 분위기를 연출할 수 있습니다.\n\n3. 차콜 + 블루 (Charcoal + Blue)\n블랙 대신 묵직한 차콜 그레이 팬츠에 스카이블루나 딥블루 이너를 더하는 조합입니다. 출근 룩이나 댄디한 스타일에 가장 세련되게 어울립니다.\n\n4. 그린 + 핑크 (Green + Pink)\n카키 야상이나 올리브 컬러 패딩에 은은한 연핑크 이너를 레이어드하는 방식입니다. 투박할 수 있는 밀리터리 무드를 부드러운 핑크가 감각적으로 중화해 줍니다.\n\n5. 옐로우 + 블루 (Yellow + Blue)\n네이비 아우터에 버터나 머스타드 옐로우 이너를 매치하는 조합입니다. 뚜렷한 색 대비 덕분에 생동감이 돌고 한층 밝고 젊은 느낌을 줍니다.\n\n6. 브라운 + 레드 (Brown + Red)\n차분한 브라운 코트나 자켓에 산뜻한 레드 머플러나 가디건을 포인트로 더해 보세요. 연말 모임이나 데이트 룩으로 손색없는 프렌치 무드를 연출할 수 있습니다.\n\n7. 퍼플 + 그레이 (Purple + Grey)\n그레이 팬츠나 가디건에 은은한 라벤더 컬러 이너를 받치는 조합입니다. 과하지 않으면서도 신비롭고 감도 높은 세련미를 보여줍니다.\n\n8. 버건디 + 블랙 (Burgundy + Black)\n올블랙 스타일에 버건디 레더 자켓이나 니트 하나를 더하는 조합입니다. 가볍지 않고 묵직하며 성숙한 무드를 완성하는 최고의 공식입니다.\n\n결론:\n스타일의 완성은 비싼 옷이 아니라 '색상의 조화'에서 나옵니다.\n베이스 컬러 70%에 포인트 컬러 30%의 비율만 기억해 보세요.",
      "tasteReview": [
        "기존 검정·회색 기본 아이템에 포인트 컬러 하나를 더해 즉각적인 스타일 업그레이드",
        "부담스러운 형광색을 배제하고 무채색과 자연스럽게 어우러지는 현실적인 8대 조합",
        "무신사나 SPA 브랜드에서 단품 하나만으로 손쉽게 시도 가능한 실용적 공식"
      ],
      "tips": "베이스 컬러 70%에 포인트 컬러 30%의 황금 비율을 지키는 것이 핵심입니다. 1:1로 반반 섞기보다는 아우터나 하의는 무채색으로 단단하게 잡고, 이너나 액세서리로 색감을 더해보세요."
    }
  },
  {
    "slug": "pinterest-3-color-layering-rules-2026",
    "store": "무신사 스토어 큐레이션",
    "i18n_ko": {
      "title": "‘너 오늘 분위기 미쳤다’ 소리 듣는 법: 핀터레스트 3컬러 레이어링 치트키 5",
      "summary": "두 가지 색은 다소 밋밋하고 네 가지 이상은 자칫 산만해지기 쉽습니다. SNS에서 저장 수 급증 중인 실패 없는 '3색 삼위일체' 레이어링 공식 5가지를 정리해 드립니다.",
      "description": "스타일링을 할 때 두 가지 색상만 쓰면 단조로워 보이기 쉽고, 반대로 네 가지 이상의 색상을 섞으면 자칫 산만하고 어수선한 인상을 줄 수 있습니다.\n\n패션 피플들이 핀터레스트나 인스타그램에서 감도 높은 사진을 연출할 때 애용하는 절대 원칙이 바로 '3컬러 법칙(Three-Color Rule)'입니다.\n안정적인 베이스 컬러 2가지에 매력적인 포인트 컬러 1가지를 자연스럽게 레이어드하는 방식입니다.\n\n이번 가을·겨울 시즌, 실패 없이 세련된 분위기를 연출할 수 있는 5가지 삼위일체 컬러 조합을 정리해 드립니다.\n\n1. 그레이 & 화이트 + 옐로우 (Grey & White + Yellow)\n깔끔한 차콜이나 멜란지 그레이 아우터에 화이트 셔츠를 매치하고, 부드러운 버터 옐로우 니트나 머플러를 더하는 조합입니다. 차분하고 지적인 톤에 은은한 화사함이 돋보입니다.\n\n2. 화이트 & 네이비 + 베이지 (White & Navy + Beige)\n클래식한 네이비 자켓이나 울 코트에 화이트 이너를 입고, 베이지 팬츠나 머플러를 매치해 보세요. 단정하면서도 부드러운 '핀터레스트 무드'의 미니멀 룩이 완성됩니다.\n\n3. 브라운 & 블랙 + 네이비 (Brown & Black + Navy)\n다크 브라운 코트에 블랙 터틀넥, 그리고 네이비 슬랙스나 스카프를 한 스푼 레이어드하는 조합입니다. 톤 다운된 컬러들이 조화롭게 맞물려 절제된 시크함을 자아냅니다.\n\n4. 다크 브라운 & 화이트 + 골드 (Dark Brown & White + Gold)\n깊이감 있는 에스프레소 브라운 코트에 깨끗한 아이보리 니트를 매치하고, 벨트 버클이나 시계의 은은한 골드 디테일을 더해 보세요. 자연스러운 '올드머니 룩'의 정수를 보여줍니다.\n\n5. 버건디 & 블루 + 그레이 (Burgundy & Blue + Grey)\n깊은 와인 버건디 아우터에 생지 데님(블루)을 매치하고, 멜란지 그레이 이너로 톤을 안정시키는 조합입니다. 분위기 있으면서도 트렌디하여 모임 룩으로 강력 추천합니다.\n\n결론:\n좋은 스타일링은 고가의 옷보다 '색상의 균형'을 아는 것에서 시작됩니다.\n베이스 컬러 2가지(70%)와 포인트 컬러 1가지(30%), 이 황금 비율을 기억해 보세요.",
      "tasteReview": [
        "단조로운 2색 코디와 어수선한 다색 코디의 한계를 동시에 해결하는 3컬러 황금비",
        "핀터레스트와 인스타그램에서 가장 높은 호응을 얻는 감도 높은 5대 무드",
        "기존에 갖고 있던 기본 아이템에 단품 하나만 추가해 즉시 연출 가능"
      ],
      "tips": "포인트 컬러의 면적이 지나치게 넓어지면 부담스러울 수 있습니다. 이너의 넥라인 살짝 보이게 입거나 머플러, 비니 등의 소품으로 면적을 조절하는 것이 자연스럽습니다."
    }
  }
]

for item in posts:
    slug = item["slug"]
    check_url = f"{SUPABASE_URL}/rest/v1/posts?slug=eq.{slug}"
    req = urllib.request.Request(check_url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data:
                row = data[0]
                post_data = row["data"]
                post_data["store"] = item["store"]
                post_data["i18n"]["ko"]["title"] = item["i18n_ko"]["title"]
                post_data["i18n"]["ko"]["summary"] = item["i18n_ko"]["summary"]
                post_data["i18n"]["ko"]["description"] = item["i18n_ko"]["description"]
                post_data["i18n"]["ko"]["tasteReview"] = item["i18n_ko"]["tasteReview"]
                post_data["i18n"]["ko"]["tips"] = item["i18n_ko"]["tips"]

                update_url = f"{SUPABASE_URL}/rest/v1/posts?id=eq.{row['id']}"
                payload = json.dumps({"data": post_data}).encode("utf-8")
                urllib.request.urlopen(urllib.request.Request(update_url, data=payload, headers=headers, method="PATCH"))
                print(f"[+] Updated {slug} to clean standard editorial tone.")
    except Exception as e:
        print(f"[-] Error updating {slug}: {e}")

try:
    urllib.request.urlopen(urllib.request.Request(REVALIDATE_URL))
    print("[+] Revalidated Vercel cache successfully!")
except Exception as e:
    print(f"[-] Revalidate error: {e}")
