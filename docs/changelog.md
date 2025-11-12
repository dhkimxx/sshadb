# Changelog

모든 눈에 띄는 변경사항은 이 파일에 기록합니다. 버전 표기는 [SemVer](https://semver.org/lang/ko/)를 따릅니다. 최신 항목이 가장 위에 위치합니다.

## [0.1.0] - 2025-11-12
### Added
- 초기 공개 버전(Alpha)
- `SSHAdb` API: `devices`, `shell`, `push`, `pull`, `get_state`
- 코어 모듈: `core/ssh_client.py`, `core/adb_executor.py`, `core/file_transfer.py`
- 커맨드 레이어: `commands/` 하위 기능 모듈
- 유틸: `utils/parser.py` (`adb devices` 출력 파서)
- 예외 계층: `exceptions.py`
- 패키징 설정: `pyproject.toml` (PEP 621), `py.typed`
- 테스트: `pytest` 기반 통합 테스트 및 `.env` 로드 지원(`python-dotenv`)
- 문서: 초기 `README`, 버전 전략 문서(`docs/versioning.md`), 변경 기록(`docs/changelog.md`)

### Notes
- Python 3.11+ 지원
- 원격 서버에 SSH 접근 가능 및 ADB 설치 필요
- Git 태그(`vX.Y.Z`)와 PyPI 버전을 반드시 일치시킬 것

<!-- 템플릿 예시
## [X.Y.Z] - YYYY-MM-DD
### Added
- 
### Changed
- 
### Fixed
- 
### Deprecated
- 
### Removed
- 
-->
