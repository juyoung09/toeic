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
