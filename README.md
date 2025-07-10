# 🗺️ My Court Auction Web

**맞춤형 법원 경매 토지 정보 웹 어플리케이션**

Flask 기반의 웹 앱으로, 필터링된 토지 경매 정보를 Kakao 지도를 통해 시각적으로 제공합니다.

---
## 🏗️ 프로젝트 구조
```
court_auction_map/
├── app.py # 앱 실행 진입점
├── .env # 🔐 카카오 API 키 (.gitignore 처리)
├── .gitignore # Git 무시 파일 설정
├── routes/
│ ├── views.py # 화면 렌더링 라우트
│ └── api/
│ └── lands.py # 토지 관련 API 라우트
├── templates/
│ └── index.html # Kakao 지도 포함 HTML 템플릿
