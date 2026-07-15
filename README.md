# TOEIC Master — 산타 스타일 학습 앱 + Daily Study Automation

## 📱 아이패드에서 앱으로 쓰기 (PWA)

`index.html`은 산타(Santa)를 모델로 한 학습 앱입니다. AI 예상 점수, 취약 유형 진단, 맞춤 문제 추천을 제공하며, 아이패드 홈 화면에 설치하면 전체화면 앱처럼 실행되고 오프라인에서도 동작합니다.

### 1회 설정: GitHub Pages 켜기

1. GitHub에서 이 저장소의 **Settings → Pages** 로 이동
2. **Source**를 `GitHub Actions`로 선택
3. 이 브랜치를 `main`에 머지하면 `.github/workflows/pages.yml`이 자동으로 배포
4. 배포 주소: `https://juyoung09.github.io/toeic/`

### 아이패드에 설치

1. 아이패드 **Safari**에서 위 주소 접속
2. 공유 버튼(⬆️) → **홈 화면에 추가**
3. 홈 화면의 `TOEIC` 아이콘으로 실행 → 주소창 없는 전체화면 앱으로 구동

### 주요 기능 (산타 스타일)

- **📊 AI 분석 탭**: 풀이 기록 기반 예상 RC 점수(5~495) + 신뢰 구간, 파트별 정답률, 유형별 취약점 진단, 최근 7일 추이
- **🎯 AI 맞춤 학습**: 취약 유형·이전 오답·미출제 문제를 우선 조합한 12문제 세트를 자동 구성
- **📚 요일별 미션**: Part 5~7 기출 유형 학습 (기존 기능)
- **📖 단어장 · 🃏 플래시카드 · ❓ OX퀴즈 · 📝 오답노트** (기존 기능)
- 모든 기록은 기기(localStorage)에 저장 — 서버 불필요, 오프라인 동작

---

# TOEIC Daily Study Automation

이 저장소는 GitHub Actions로 매일 TOEIC 학습 결과를 생성하고 GitHub에 커밋합니다.

## 지금 안 됐던 이유

저장소는 GitHub에 연결되어 있었지만, 실제로 매일 실행할 `.github/workflows` 파일과 결과 생성 스크립트가 없었습니다. 그래서 GitHub Actions가 실행될 트리거가 없었고, 결과 파일도 만들어질 수 없었습니다.

## 자동 실행

- 실행 시각: 매일 21:00 UTC, 한국 시간 06:00 KST
- Workflow: `.github/workflows/daily-toeic.yml`
- 생성 스크립트: `scripts/generate_daily_toeic.py`

## 결과 위치

매일 실행되면 아래 파일이 생성되거나 갱신됩니다.

- `reports/YYYY-MM-DD.md`: 사람이 읽는 학습 결과
- `reports/README.md`: 생성된 리포트 목록
- `data/results/YYYY-MM-DD.json`: 구조화된 결과 데이터
- `data/results/latest.json`: 가장 최근 결과 데이터

## 수동 실행

GitHub에서 바로 실행할 수 있습니다.

1. 저장소의 Actions 탭으로 이동
2. `Daily TOEIC Study Result` 선택
3. `Run workflow` 클릭
4. 필요하면 `YYYY-MM-DD` 형식의 날짜 입력

로컬에서도 실행할 수 있습니다.

```bash
python scripts/generate_daily_toeic.py
python scripts/generate_daily_toeic.py --date 2026-06-07
```

## 동작 방식

1. GitHub Actions가 매일 스케줄에 맞춰 실행됩니다.
2. Python 스크립트가 해당 날짜의 TOEIC 문제, 정답, 단어장을 생성합니다.
3. 결과가 `reports/`와 `data/results/`에 저장됩니다.
4. 변경 사항이 있으면 `github-actions[bot]`이 자동으로 커밋하고 푸시합니다.

## 참고

현재 버전은 외부 API나 비밀키 없이 동작하는 기본 자동화입니다. 나중에 실제 오답 기록, 개인 단어장, 난이도 조정, Telegram 알림을 붙일 수 있습니다.
