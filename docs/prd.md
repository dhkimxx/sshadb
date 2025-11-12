# 🧩 Project Requirements Document (PRD)

## 📘 프로젝트 개요

- **프로젝트명:** `sshadb`
- **Python 버전:** `3.11.14`
- **목표:** SSH를 통해 **원격 서버에서 ADB 명령을 실행**하고 결과를 로컬에서 다룰 수 있도록 하는 Python 유틸리티 라이브러리.
- **핵심 개념:**
  - 로컬 PC → SSH 연결 → 원격 서버에서 adb 실행
  - adb 결과를 로컬 Python API 형태로 반환

---

## 🧠 주요 기능 명세

### 1️⃣ `devices`

- **설명:** 원격 서버에서 `adb devices` 명령을 실행해 연결된 단말 리스트를 반환
- **예상 API:**
  ```python
  sshadb.devices()
  # 반환 예시:
  # [{"serial": "123456F", "state": "device"}, {"serial": "emulator-5554", "state": "offline"}]
  ```

---

### 2️⃣ `shell`

- **설명:** 특정 단말에서 원격 `adb shell` 명령 실행
- **예상 API:**

  ```python
  sshadb.shell("123456F", "ls /data/local/tmp")
  # 반환 예시: "test_file.txt\nlogcat_output.txt"
  ```

---

### 3️⃣ `push`

- **설명:** 로컬 → 원격 서버 → 단말로 파일 업로드

- **내부 동작:**

  1. 로컬 파일을 SSH SFTP로 원격 서버에 임시 업로드
  2. 원격에서 `adb push` 실행
  3. 성공 시 원격 임시 파일 삭제

- **예상 API:**

  ```python
  sshadb.push("123456F", "./local.apk", "/data/local/tmp/app.apk")
  ```

---

### 4️⃣ `pull`

- **설명:** 단말 → 원격 서버 → 로컬 PC로 파일 다운로드

- **내부 동작:**

  1. 원격에서 `adb pull` → 서버 임시 경로
  2. SSH SFTP로 로컬로 전송
  3. 원격 임시 파일 삭제

- **예상 API:**

  ```python
  sshadb.pull("123456F", "/data/local/tmp/app.log", "./logs/app.log")
  ```

---

### 5️⃣ `get-state`

- **설명:** 단말 상태 조회 (`adb get-state`)
- **예상 API:**

  ```python
  sshadb.get_state("123456F")
  # 반환 예시: "device"
  ```

---

## ⚙️ 환경 설정 및 연결

- SSH 접속 정보는 다음 두 가지 방식 지원 예정:

  1. **키 기반**

     ```python
     from sshadb import SSHAdb

     client = SSHAdb(host="192.168.0.10", user="ubuntu", key_path="~/.ssh/id_rsa")
     client.devices()
     ```

  2. **패스워드 기반**

     ```python
     from sshadb import SSHAdb

     client = SSHAdb(host="192.168.0.10", user="ubuntu", password="password")
     client.devices()
     ```

---

## 🧰 내부 구조 (초기 설계)

```
sshadb/
 ├── __init__.py
 ├── core/
 │   ├── ssh_client.py       # paramiko 기반 SSH/SFTP 래퍼
 │   ├── adb_executor.py     # adb 명령 실행 로직
 │   └── file_transfer.py    # push/pull 지원
 ├── commands/
 │   ├── devices.py
 │   ├── shell.py
 │   ├── push.py
 │   ├── pull.py
 │   └── get_state.py
 ├── utils/
 │   └── parser.py           # adb 출력 파서
 └── exceptions.py
```

---

## 🧪 향후 확장 계획 (추가 예정 기능)

| 기능                | 설명                        |
| ------------------- | --------------------------- |
| `install/uninstall` | APK 설치 및 제거            |
| `logcat`            | 실시간 로그 스트리밍        |
| `forward/reverse`   | 포트 포워딩 제어            |
| `reboot`, `root`    | 단말 제어 기능              |
| `exec_async`        | 비동기 명령 실행            |
| `config profiles`   | SSH 프로파일 관리 (YAML 등) |
