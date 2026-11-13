#!/usr/bin/env python3
"""
Upload Deskterior Monitor Arm 3-Post Cluster to Supabase and trigger ISR revalidation
"""

import json
import urllib.request
import urllib.error

SUPABASE_URL = "https://jmuqmvxubuwhoocuknnt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptdXFtdnh1YnV3aG9vY3Vrbm50Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDMwODA3NywiZXhwIjoyMTA5ODg0MDc3fQ.ELyAmyRJrWdQoIHRu4thMGvjAnjJfVZ4S8Cfpb9MiDY"
REVALIDATE_URL = "https://www.k-trand.store/api/revalidate?secret=kblog2026"

posts = [
    {
        "id": "monitor-arm-desk-thickness-installation-guide-2026",
        "slug": "monitor-arm-desk-thickness-installation-guide-2026",
        "category": "tech",
        "store": "쿠팡",
        "priceKrw": 28900,
        "releaseDate": "2026-11-13",
        "rating": 4.9,
        "imageUrl": "/images/products/deskterior-monitor-arm-setup-1.png",
        "images": [
            "/images/products/deskterior-monitor-arm-setup-1.png",
            "/images/products/item-camel-mpk1.jpg",
            "/images/products/item-nb-f80.jpg"
        ],
        "exampleItems": [
            {
                "name": "카멜마운트 MPK1 고중량 모니터암 보강판",
                "brand": "카멜마운트",
                "priceKrw": 7200,
                "imageUrl": "/images/products/item-camel-mpk1.jpg",
                "url": "https://www.coupang.com/np/search?q=%EC%B9%B4%EB%A9%9C%EB%A7%88%EC%9A%B4%ED%8A%B8+MPK1+%EB%B3%B4%EA%B0%95%ED%8C%90&lptag=AF9412775",
                "category": "Accessory"
            },
            {
                "name": "노스바유 NB F80 싱글 모니터암 (17~32인치)",
                "brand": "노스바유 (NorthBayou)",
                "priceKrw": 28900,
                "imageUrl": "/images/products/item-nb-f80.jpg",
                "url": "https://www.coupang.com/np/search?q=%EB%85%B8%EC%8A%A4%EB%B0%94%EC%9C%A0+NB+F80+%EC%8B%B1%EA%B8%80+%EB%AA%A8%EB%8B%88%ED%84%B0%EC%95%94&lptag=AF9412775",
                "category": "Monitor Arm"
            }
        ],
        "affiliateUrl": "https://www.coupang.com/np/search?q=%EB%AA%A8%EB%8B%88%ED%84%B0%EC%95%94+%EC%84%A4%EC%B9%98+%EB%B3%B4%EA%B0%95%ED%8C%90&lptag=AF9412775",
        "affiliatePlatform": "Coupang",
        "i18n": {
            "ko": {
                "title": "모니터암 설치 조건: 책상 두께 몇 cm부터 가능할까? (상판 프레임 걸릴 때 해결법)",
                "summary": "모니터암 구매 전 책상 상판 두께와 하부 철제 프레임 간섭 여부를 확인하지 않으면 반품하기 십상입니다. 클램프 규격과 보강판 활용 해결법을 완벽 정리합니다.",
                "description": "책상 위를 넓게 쓰려고 모니터암을 샀는데, 막상 설치하려다 책상에 안 들어가서 당근에 그대로 되파는 분들이 정말 많습니다.\n\n모니터암은 모니터 인치수보다 '내 책상에 물릴 수 있는지'를 먼저 확인해야 돈과 시간을 날리지 않습니다.\n\n구매 전 딱 3분 만에 확인하는 모니터암 책상 설치 조건과 상판 프레임 간섭 해결법을 정리해 드립니다.\n\n1. 책상 상판 두께: 몇 cm까지 지원할까?\n시중에 판매되는 대부분의 클램프형 모니터암(카멜마운트, NB, 루나랩 등)의 표준 규격은 최소 10mm(1cm)에서 최대 50mm~85mm(5cm~8.5cm) 내외입니다. 이케아 린몬 등 속이 빈 허니콤 상판은 압력을 못 견디므로 반드시 보강판을 대거나 원목 상판을 써야 합니다.\n\n2. 두께보다 더 중요한 뒤쪽 여유 공간과 철제 프레임\n두께가 맞아도 설치에 실패하는 90%의 원인은 책상 하부 프레임입니다. 클램프가 물리기 위해 최소 40~60mm 이상의 깊이가 확보되어야 하며, 상판 테두리에 사각 철제 프레임이 바짝 붙어 있다면 클램프 턱이 걸려 조여지지 않습니다.\n\n3. 철제 프레임에 걸릴 때 3가지 실전 해결법\n가장 깔끔한 방법은 카멜마운트 MPK1 같은 '모니터암 전용 보강판'을 덧대어 고정 면적을 넓히고 단차를 메우는 것입니다. 또는 책상 케이블 홀에 볼트를 통과시키는 그로밋(타공) 방식을 쓰면 프레임 간섭 없이 바로 튼튼하게 고정됩니다.",
                "tasteReview": [
                    "구매 전 상판 두께 10~80mm 및 하부 프레임 깊이 5cm 여유 확인 필수",
                    "두닷 등 철제 프레임 책상은 모니터암 보강판 하나로 단차와 상판 휨 동시 해결",
                    "2~3만 원대 가성비 싱글암만 제대로 설치해도 데스크 공간이 2배로 넓어짐"
                ],
                "tips": "상판 두께가 얇거나 약한 압축목 책상이라면 모니터암을 조이기 전에 상하판 스틸 보강판을 반드시 덧대세요. 상판 파손과 타건 시 모니터 흔들림을 동시에 잡아줍니다."
            },
            "en": {
                "title": "Monitor Arm Desk Requirements: Minimum Tabletop Thickness & Cable Management Guide",
                "summary": "Avoid returning your monitor arm by verifying desk clamp clearance, tabletop thickness (10-85mm), and under-desk frame interference beforehand.",
                "description": "Upgrading to a clean floating monitor setup is one of the most effective deskterior improvements. However, 90% of installation failures stem from under-desk steel frames and improper tabletop thickness.\n\n1. Tabletop Thickness Specifications\nStandard C-clamps accommodate desks between 10mm and 85mm. Avoid hollow honeycomb desks (such as IKEA Linnmon) unless paired with heavy-duty reinforcement plates.\n\n2. Clearance & Steel Frame Interference\nA minimum overhang depth of 50mm behind the desk is required. If perimeter steel rails block the clamp jaw, a mounting reinforcement kit is essential.\n\n3. Practical Fixes\nUsing a dedicated steel reinforcement plate like the Camel Mount MPK1 bridges height gaps and distributes clamping force evenly, eliminating wobble.",
                "tasteReview": [
                    "Guarantees stable clamp fit across standing desks and standard office tables",
                    "Prevents surface dents and wobble with steel reinforcement plates",
                    "Frees up 60% of usable desk real estate beneath the display"
                ],
                "tips": "Always measure rear overhang depth before purchasing. Grommet hole mounting is an ideal backup if perimeter frame clearance is under 40mm."
            },
            "ja": {
                "title": "モニターアーム取り付け条件：天板の厚みとフレーム干渉の完全対策ガイド",
                "summary": "モニターアーム購入前に天板の厚さ（10〜85mm）と裏面フレームの干渉をチェック。クランプ式設置の失敗を防ぐ必須ポイントを徹底解説。",
                "description": "デスク周りを劇的に広くするモニターアームですが、天板の厚みや裏面の補強フレームに干渉して設置できないトラブルが後を絶ちません。\n\n1. 天板の厚み規格：10mm〜85mm対応が主流ですが、内部が空洞のハニカム天板は補強プレートなしでは破損の恐れがあります。\n2. 背面の奥行きクリアランス：クランプ金具を差し込むため、最低でも5cmの平らな奥行きが必要です。\n3. フレーム干渉の解決策：段差を解消するスチール製補強プレートを使用するか、配線穴を利用するグロメット固定を選択するのが確実です。",
                "tasteReview": [
                    "天板の厚みと裏面構造を確認するだけで失敗リスクをゼロに",
                    "補強プレート併用で天板の凹みやタイピング時の揺れを大幅軽減",
                    "3千円台の定番シングルアームでも圧倒的なデスクスペースを確保"
                ],
                "tips": "天板が薄いデスクやMDF素材の場合は、上下に挟む補強プレートを必ず併用してください。"
            },
            "zh": {
                "title": "显示器支架桌面安装指南：桌板厚度要求与底部钢架干涉避坑技巧",
                "summary": "购买显示器支架前必看的桌面尺寸核对：夹持厚度（10-85mm）、桌底钢架避让以及使用加固板解决受力不均的实战方法。",
                "description": "安装显示器支架是打造极简桌搭的核心步骤，但不少人因未提前测量桌面厚度和桌底横梁而导致无法安装。\n\n1. 桌面厚度与材质：标准夹桌款通常支持10~85mm厚度，空心蜂窝板（如宜家部分桌面）严禁裸装，必须配合金属加固垫片。\n2. 桌下边缘深度：桌子边缘至少需预留5cm无遮挡深度供夹具咬合。\n3. 钢架干涉解决法：使用卡美特MPK1等专用加固钢板填平高低差，或直接改用穿孔（Grommet）安装方式。",
                "tasteReview": [
                    "彻底解决桌底横梁卡死无法上螺丝的常见困扰",
                    "搭配加固钢板有效分散压强，防止木质桌面凹陷变形",
                    "瞬间释放显示器下方60%以上的宝贵桌面空间"
                ],
                "tips": "如遇桌后紧贴墙壁且无下沉空间，建议优先考虑穿孔安装或选择带短力臂结构的型号。"
            }
        }
    },
    {
        "id": "dual-vs-two-single-monitor-arms-comparison-2026",
        "slug": "dual-vs-two-single-monitor-arms-comparison-2026",
        "category": "tech",
        "store": "쿠팡",
        "priceKrw": 57800,
        "releaseDate": "2026-11-13",
        "rating": 4.9,
        "imageUrl": "/images/products/deskterior-monitor-arm-setup-2.png",
        "images": [
            "/images/products/deskterior-monitor-arm-setup-2.png",
            "/images/products/item-nb-f80.jpg",
            "/images/products/item-camel-mpk1.jpg"
        ],
        "exampleItems": [
            {
                "name": "노스바유 NB F80 싱글 모니터암 (2세트 구성)",
                "brand": "노스바유 (NorthBayou)",
                "priceKrw": 57800,
                "imageUrl": "/images/products/item-nb-f80.jpg",
                "url": "https://www.coupang.com/np/search?q=%EB%85%B8%EC%8A%A4%EB%B0%94%EC%9C%A0+NB+F80+%EC%8B%B1%EA%B8%80+%EB%AA%A8%EB%8B%88%ED%84%B0%EC%95%94&lptag=AF9412775",
                "category": "Monitor Arm"
            },
            {
                "name": "카멜마운트 MPK1 보강판 (2개 세트)",
                "brand": "카멜마운트",
                "priceKrw": 14050,
                "imageUrl": "/images/products/item-camel-mpk1.jpg",
                "url": "https://www.coupang.com/np/search?q=%EC%B9%B4%EB%A9%9C%EB%A7%88%EC%9A%B4%ED%8A%B8+MPK1+%EB%B3%B4%EA%B0%95%ED%8C%90+2%EA%B0%9C&lptag=AF9412775",
                "category": "Accessory"
            }
        ],
        "affiliateUrl": "https://www.coupang.com/np/search?q=%EC%8B%B1%EA%B8%80+%EB%AA%A8%EB%8B%88%ED%84%B0%EC%95%94+2%EA%B0%9C&lptag=AF9412775",
        "affiliatePlatform": "Coupang",
        "i18n": {
            "ko": {
                "title": "모니터 2대 쓸 때 듀얼 모니터암 1개 vs 싱글 2개, 왜 다들 싱글 2개로 갈아탈까?",
                "summary": "듀얼 모니터 구성 시 일체형 듀얼 모니터암을 샀다가 벽 밀착 불가와 높이 불일치로 후회하는 이유와, 싱글 2개 조합이 종결인 이유를 비교 분석합니다.",
                "description": "듀얼 모니터 세팅을 결심했을 때 대부분 '모니터 2대니까 듀얼 모니터암 하나 사면 되겠지'라고 생각합니다.\n\n하지만 실제 개발자나 디자이너 데스크테리어 유저들은 얼마 못 가 듀얼 모니터암을 처분하고 '싱글 모니터암 2개'로 갈아탑니다.\n\n1. 일체형 듀얼 모니터암의 치명적 한계\n첫째, 벽 밀착이 불가능합니다. 두 모니터 각도를 안쪽으로 모으려면 암 관절이 뒤로 꺾여야 하는데, 벽에 부딪혀 모니터가 앞으로 15~20cm 튀어나와 책상이 좁아집니다.\n둘째, 인치수가 다른 모니터(예: 32인치 메인 + 27인치 세로 피벗)를 쓸 때 높낮이를 미세하게 일치시키기 어렵습니다.\n셋째, 기둥 하나에 두 모니터 하중이 집중되어 한쪽으로 당길 때 책상 휨과 흔들림이 심해집니다.\n\n2. 싱글 모니터암 2개 조합의 장점\n책상 좌우 원하는 모서리에 클램프를 각각 배치할 수 있어 벽 밀착 세팅이 완벽합니다. 가성비 싱글암(NB F80 등) 2대를 사도 5만 원대 중반으로 일체형 듀얼암보다 오히려 저렴하며, 모니터 교체나 배치 변경 시 스트레스가 전혀 없습니다.",
                "tasteReview": [
                    "벽 밀착과 모니터 간격 조절에서 싱글 2개 조합이 압도적 우위",
                    "메인 가로 + 서브 세로 피벗 구성에 가장 최적화된 독립 관절 구조",
                    "가격 면에서도 가성비 싱글암 2개가 브랜드 일체형 듀얼암보다 경제적"
                ],
                "tips": "책상이 벽에 바짝 붙어 있다면 일체형 듀얼암은 무조건 피하세요. 싱글 모니터암 2개를 좌우로 나누어 설치해야 책상 깊이를 온전히 살릴 수 있습니다."
            },
            "en": {
                "title": "Dual Monitor Arm vs Two Single Arms: Why Power Users Prefer Dual Singles",
                "summary": "Comparing integrated dual monitor arms with two independent single arms: solving wall clearance constraints and mismatched screen heights.",
                "description": "When setting up two monitors, an integrated dual-arm mount seems intuitive. However, power users invariably switch to two independent single monitor arms.\n\n1. The Hidden Flaws of Dual Mounts\nIntegrated poles require arm joints to protrude backwards to create an inward ergonomic curve, pushing screens 6 to 8 inches forward on desks placed against walls. Furthermore, aligning mixed displays (e.g., a 32-inch landscape with a 27-inch portrait) is notoriously difficult.\n\n2. Why Two Single Arms Reign Supreme\nTwo separate single mounts allow placing base clamps at optimal desk corners, achieving flush wall alignment. With budget champions like the NB F80, two single arms often cost less while delivering unmatched flexibility.",
                "tasteReview": [
                    "Full wall-flush capability without sacrificing viewing ergonomics",
                    "Effortless vertical pivot adjustments for coding and multi-tasking",
                    "Reduces focused torque stress on a single desktop contact point"
                ],
                "tips": "If your workstation rests directly against a wall, opt for two independent single arms to reclaim valuable front desk depth."
            },
            "ja": {
                "title": "デュアルモニターアーム1台 vs シングル2台：なぜ多くの人がシングル2台を選ぶのか？",
                "summary": "2画面環境で一体型デュアルアームから独立型シングル2台へ乗り換える人が多い理由。壁際設置のクリアランスと高さ調整の自由度を比較。",
                "description": "デュアルディスプレイ構築時、一体型デュアルアームを選ぶと「壁にぶつかって画面が手前に出すぎる」「左右のモニターサイズが違うと高さが合わない」といった壁に直面します。\n\n独立したシングルモニターアームを2台設置することで、左右のクランプ位置を自由に決められ、壁ピタ設置が可能になります。NB F80のような高コスパアームを2本揃えれば、費用も一体型より安く抑えられます。",
                "tasteReview": [
                    "デスクを壁際に密着させたまま最適な内向きアングルを実現",
                    "メイン横画面＋サブ縦画面（ピボット）の高さ合わせが自由自在",
                    "将来的なモニター入れ替えやレイアウト変更にも柔軟に対応"
                ],
                "tips": "横幅120〜140cm前後のデスクでは、両端近くにシングルアームを配置すると中央の作業スペースが劇的にスッキリします。"
            },
            "zh": {
                "title": "双屏选一体式双臂还是一对单臂？老玩家都换成两根单臂支架的真相",
                "summary": "双显示器桌面实测对比：一体式双屏支架靠墙受阻、高低对齐困难的痛点，以及为什么两根独立单臂是更终极的性价比方案。",
                "description": "搭建双屏桌面时，很多人第一反应是一体式双屏支架。但实际使用后，绝大多数用户都会转投“双单臂”阵营。\n\n一体式支架为了形成环抱夹角，连杆关节必须向后探出，遇到靠墙书桌时会被迫让屏幕向前移15-20厘米，严重挤占键鼠空间。而两根独立单臂支架可以分别固定在桌子两侧，真正实现屏幕平贴墙面，并且一横一竖（副屏竖屏编程阅读）的微调体验远超一体式。",
                "tasteReview": [
                    "彻底解决靠墙桌面屏幕前凸压抑的结构硬伤",
                    "主屏横屏＋副屏竖屏代码流的最佳搭档",
                    "两套高性价比单臂总价甚至低于品牌一体式双臂支架"
                ],
                "tips": "如果使用的两台显示器尺寸或重量不同，强烈建议选择两根独立单臂支架分别调节气压张力。"
            }
        }
    },
    {
        "id": "budget-vs-heavy-duty-32inch-monitor-arm-guide-2026",
        "slug": "budget-vs-heavy-duty-32inch-monitor-arm-guide-2026",
        "category": "tech",
        "store": "쿠팡",
        "priceKrw": 109000,
        "releaseDate": "2026-11-13",
        "rating": 5.0,
        "imageUrl": "/images/products/deskterior-monitor-arm-setup-3.png",
        "images": [
            "/images/products/deskterior-monitor-arm-setup-3.png",
            "/images/products/item-nb-f80.jpg",
            "/images/products/item-camel-pma2x.jpg"
        ],
        "exampleItems": [
            {
                "name": "노스바유 NB F80 싱글 모니터암 (24~27형 & 경량 32형)",
                "brand": "노스바유",
                "priceKrw": 28900,
                "imageUrl": "/images/products/item-nb-f80.jpg",
                "url": "https://www.coupang.com/np/search?q=%EB%85%B8%EC%8A%A4%EB%B0%94%EC%9C%A0+NB+F80+%EC%8B%B1%EA%B8%80+%EB%AA%A8%EB%8B%88%ED%84%B0%EC%95%94&lptag=AF9412775",
                "category": "Monitor Arm"
            },
            {
                "name": "카멜마운트 PMA2X 초고중량 싱글 모니터암 (~57형, 27kg)",
                "brand": "카멜마운트",
                "priceKrw": 109000,
                "imageUrl": "/images/products/item-camel-pma2x.jpg",
                "url": "https://www.coupang.com/np/search?q=%EC%B9%B4%EB%A9%9C%EB%A7%88%EC%9A%B4%ED%8A%B8+PMA2X+%EA%B3%A0%EC%A4%91%EB%9F%89+%EB%AA%A8%EB%8B%88%ED%84%B0%EC%95%94&lptag=AF9412775",
                "category": "Monitor Arm"
            }
        ],
        "affiliateUrl": "https://www.coupang.com/np/search?q=%EA%B3%A0%EC%A4%91%EB%9F%89+%EB%AA%A8%EB%8B%88%ED%84%B0%EC%95%94+32%EC%9D%B8%EC%B9%98&lptag=AF9412775",
        "affiliatePlatform": "Coupang",
        "i18n": {
            "ko": {
                "title": "3만 원대 가성비 모니터암 vs 10만 원대, 32인치 올리면 고개 숙일까?",
                "summary": "32인치 대화면 및 커브드 모니터 거치 시 발생하는 고개 숙임 현상의 원인과, 가성비 모델(NB F80)과 고하중 헤비급 모델(카멜 PMA2X)의 실체적 차이를 규명합니다.",
                "description": "24인치나 27인치 모니터라면 2~3만 원대 가성비 모니터암으로도 차고 넘칩니다. 하지만 32인치 대형 화면이나 커브드 모니터를 올리는 순간 화면이 서서히 아래로 떨어지는 '고개 숙임' 현상이 발생합니다.\n\n1. 고개 숙임이 일어나는 진짜 원인\n화면 높낮이를 버티는 가스 스프링과 별개로, 화면 상하 각도를 지탱하는 '틸트 힌지 마찰력'이 중력을 이기지 못하기 때문입니다. 특히 32인치 이상 커브드 모니터는 곡률 때문에 무게 중심이 앞으로 10cm 이상 튀어나와 실질적인 모멘트 하중이 1.5배 이상 증가합니다.\n\n2. 3만 원대 vs 10만 원대 실사용 차이\n2~3만 원대 가성비 라인(NB F80 등)은 평면 32인치까지 장력을 꽉 조여 버틸 수 있지만, 커브드나 고중량 모니터에서는 장기 사용 시 틸트 볼트 마모가 생깁니다. 반면 카멜마운트 PMA2X 같은 10만 원대 초고중량 라인은 베어링 틸팅 구조와 알루미늄 다이캐스팅 관절로 최대 57인치 27kg까지 고개 숙임 없이 미동조차 없습니다.\n\n결론적으로 24~27인치는 2만 원대 싱글암, 32인치 커브드 및 대형 게이밍 모니터는 10만 원대 고중량 전용 모델로 가는 것이 중복 투자를 피하는 정답입니다.",
                "tasteReview": [
                    "32인치 커브드 및 울트라와이드 모니터의 고개 숙임 스트레스 완벽 해결",
                    "베어링 틸팅 구조 탑재로 손가락 하나로도 부드러운 각도 조절 가능",
                    "타건 시 모니터 미세 진동을 묵직한 알루미늄 암이 완벽 흡수"
                ],
                "tips": "커브드 32인치 이상 모델을 쓰고 계시다면 일반 규격 대신 반드시 최대 지지 무게 15kg 이상의 '고중량(Heavy-Duty)' 표기 모델을 선택하세요."
            },
            "en": {
                "title": "$25 Budget vs $80 Heavy-Duty Monitor Arm: Will a 32-Inch Screen Sag?",
                "summary": "Analyzing the causes of screen tilt drooping on 32-inch and curved monitors, comparing entry-level gas springs with premium geared bearing tilt hinges.",
                "description": "While budget monitor arms easily handle 24 to 27-inch displays, mounting a 32-inch curved screen often causes unwanted downward tilt sagging over time.\n\n1. Why Tilt Drooping Occurs\nEven when the vertical gas strut holds, the forward center of gravity on curved screens multiplies rotational torque, overcoming standard friction washers.\n\n2. The Engineering Difference\nBudget models (like the NB F80) max out near 9kg and require maximum bolt tightening. High-end heavy-duty solutions like the Camel Mount PMA2X feature geared bearing tilt mechanisms supporting up to 27kg (57-inch ultrawides) with zero droop.",
                "tasteReview": [
                    "Eliminates tilt slippage on heavy 32-inch curved gaming monitors",
                    "Industrial-grade die-cast aluminum frame dampens typing vibrations",
                    "Finger-touch articulation despite extreme display mass"
                ],
                "tips": "For curved displays, always calculate effective load as 1.5x nominal panel weight due to the forward center of gravity."
            },
            "ja": {
                "title": "3千円の高コスパアーム vs 1万円超の高耐荷重アーム：32インチで「お辞儀」するのか？",
                "summary": "32インチや湾曲ディスプレイで発生するモニターアームの「お辞儀（チルト下垂）」現象を検証。高コスパ定番機とヘビー級専用機の決定的な違い。",
                "description": "24〜27インチなら3千円前後の定番アームで十分ですが、32インチや湾曲ウルトラワイドを載せると、時間が経つにつれ画面が下を向いてしまう「お辞儀問題」が発生しがちです。\n\n湾曲モニターは画面中央が前方にせり出しているため、チルト関節にかかる負荷が通常の1.5倍近く跳ね上がります。カメールPMA2Xのような高耐荷重モデル（最大27kg対応）はベアリング内蔵のチルト機構を採用しており、超大型画面でも指一本で角度調節ができ、びくともしません。",
                "tasteReview": [
                    "重量級湾曲モニターでもお辞儀せず強固に姿勢をキープ",
                    "ベアリングチルト構造によりスムーズな無段階アングル調整が可能",
                    "激しいキーボード入力時にも揺れを瞬時に抑え込む圧倒的な剛性"
                ],
                "tips": "湾曲32インチ以上の画面をお使いの場合は、耐荷重15kg以上の「高耐荷重（ヘビーデューティー）」モデル一択です。"
            },
            "zh": {
                "title": "百元平价支架 vs 五百元重型支架：挂32寸显示器真的会点头下垂吗？",
                "summary": "实测32寸大屏与带鱼屏曲面显示器“点头下垂”的力学根源，对比入门气压臂与重型轴承云台支架的核心性能差异。",
                "description": "对于24-27寸普通显示器，百元出头的入门支架完全够用。但一旦换上32寸以上或曲面大屏，俯仰角关节承受不住重心前移，往往会出现自动“点头下垂”的尴尬。\n\n普通支架依靠垫片摩擦力锁紧俯仰角，曲面屏的前倾力矩极易导致滑丝下垂。而像卡美特PMA2X这类重型支架（支持至57寸、27kg）采用工业级轴承云台结构，不仅彻底告别点头，单手推动依然轻盈丝滑。",
                "tasteReview": [
                    "从根源杜绝重型曲面电竞屏与带鱼屏的点头溜车痛点",
                    "内置齿轮轴承结构，实现大屏悬停随心调节",
                    "加粗铝合金力臂，大力敲击键盘桌面依然稳如磐石"
                ],
                "tips": "只要是带曲率的32寸及以上显示器，建议直接一步到位选择承重15kg以上的重型加固支架。"
            }
        }
    }
]

def upload_all_posts():
    for p in posts:
        payload = {"slug": p["slug"], "data": p}
        req = urllib.request.Request(
            f"{SUPABASE_URL}/rest/v1/posts",
            headers={
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "application/json",
                "Prefer": "resolution=merge-duplicates"
            },
            data=json.dumps(payload).encode("utf-8")
        )
        try:
            with urllib.request.urlopen(req, timeout=15) as r:
                print(f"[+] Post '{p['slug']}' upserted! Status: {r.status}")
        except urllib.error.HTTPError as e:
            print(f"[-] HTTP Error for '{p['slug']}': {e.code} {e.read().decode('utf-8')}")
        except Exception as e:
            print(f"[-] Error for '{p['slug']}': {e}")

    # Trigger revalidation
    try:
        with urllib.request.urlopen(REVALIDATE_URL, timeout=15) as r:
            print(f"[+] Revalidation triggered! Status: {r.status}, response: {r.read().decode('utf-8')}")
    except Exception as e:
        print(f"[-] Revalidation warning: {e}")

if __name__ == "__main__":
    upload_all_posts()
