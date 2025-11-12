# 버전 관리 전략

이 프로젝트는 [Semantic Versioning (SemVer)](https://semver.org/lang/ko/) 을 따릅니다.

형식: MAJOR.MINOR.PATCH

- MAJOR: 하위 호환이 깨지는 변경 (예: 공개 API 시그니처 변경)
- MINOR: 하위 호환을 유지하는 기능 추가 (예: 새로운 ADB 명령 추가)
- PATCH: 버그 수정, 문서/내부 개선 등 기능 변화 없음

## 예시

- 0.1.0 — 초기 개발 버전 (API 불안정, 내부용)
- 0.2.0 — 기능 추가(호환성 유지)
- 1.0.0 — 안정화 릴리스(외부 공개 가능)
- 1.0.1 — 버그 수정(기능 변화 없음)
- 1.1.0 — 하위 호환 기능 추가(ADB 명령 추가 등)
- 2.0.0 — 하위 호환성 파괴 변경(API 구조 변경)

## 버전 소스

- `pyproject.toml`의 `project.version`
- `src/sshadb/__init__.py`의 `__version__`

두 곳의 버전은 항상 동기화해야 합니다.

## 릴리스 체크리스트

1. 변경사항 정리: `docs/changelog.md` 업데이트
2. 버전 동기화: `pyproject.toml` 과 `src/sshadb/__init__.py`의 `__version__` 동일하게 업데이트
3. 테스트 통과 확인: `pytest -q`
4. 태그 생성(반드시 PyPI 버전과 동일):
   ```bash
   git add -A
   git commit -m "chore(release): vX.Y.Z"
   git tag -a vX.Y.Z -m "Release vX.Y.Z"
   git push && git push --tags
   ```
5. 배포:
   ```bash
   python -m pip install -U build twine
   python -m build
   twine check dist/*
   twine upload dist/*
   ```

## 가이드라인

- 공개 API에 영향이 없는 내부 리팩터링/문서/테스트만 변경: PATCH
- 새로운 커맨드(예: `install/uninstall`, `logcat`, `forward/reverse`) 추가: MINOR
- API 파괴적 변경(시그니처/모듈 구조 변경 등): MAJOR
- Git 태그(`vX.Y.Z`)와 PyPI 버전은 반드시 일치해야 하며, CI/CD에서 태그 기반으로 배포 자동화를 구성하는 것을 권장합니다.
