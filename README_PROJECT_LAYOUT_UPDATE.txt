포트폴리오 프로젝트 영역 최종 반영 패키지
=========================================

반영 내용
---------
메인 프로젝트:
1. CHIPS MASTER PROGRAM
   - 20 nm급 BCAT DRAM MEB–Cov–GIDL 강건 설계
   - 연구 진행 중 / Run 0 검증 결과만 표시

2. 반도체집적공정
   - 423 K 고온·단채널 NMOS 공정 최적화

3. SSU 데이터톤 2025
   - 62,199건 논문 기반 반도체 연구 동향 분석

공통 변경:
- 메인 프로젝트 썸네일 이미지 제거
- 대제목을 최대한 한 줄로 표시
- PC 전체 화면에서는 3개 카드 가로 배치
- PC 절반 창과 태블릿에서는 카드가 위아래 구조로 1개씩 배치
- 모바일에서도 상단 대제목 영역과 본문 영역을 위아래로 유지
- MORE PROJECTS의 이미지 제거
- MORE PROJECTS를 PMOS / SE–X-ray / 디지털논리 프로젝트로 구성
- 각 MORE PROJECTS 카드에 과목명, 설명, 핵심 결과, 기간 표시
- CONTACT의 GitHub 주소와 이메일 글자 크기를 소폭 축소

수정 파일:
- index.html
- assets/css/style.css

실행 방법
---------
1. GitHub Desktop에서 minhosong-mse.github.io 저장소를 엽니다.
2. Repository > Show in Explorer를 누릅니다.
3. 이 ZIP의 파일 3개를 index.html이 있는 저장소 최상위 폴더에 풉니다.

   apply_project_layout_update.py
   run_project_layout_update.bat
   README_PROJECT_LAYOUT_UPDATE.txt

4. run_project_layout_update.bat을 더블클릭합니다.
5. 브라우저가 http://localhost:8010 으로 열립니다.
6. 다음 세 화면을 확인합니다.
   - PC 전체 화면
   - 브라우저 절반 너비
   - 모바일 개발자 도구 화면

배포 방법
---------
화면이 괜찮으면 GitHub Desktop에서 변경된 아래 두 파일만 확인합니다.

- index.html
- assets/css/style.css

Summary:
update image-free project portfolio layout

Commit to main
Push origin

배포 후:
https://minhosong-mse.github.io

변경 전 화면이 남으면 Ctrl + F5로 강력 새로고침합니다.

백업
----
백업은 Git 저장소 내부가 아니라 저장소와 같은 상위 폴더에 생성됩니다.

minhosong-mse.github.io-backup-YYYYMMDD-HHMMSS

도우미 파일 3개는 .git/info/exclude에 자동 등록되므로
정상적인 경우 GitHub Desktop 변경 목록에 나타나지 않습니다.
