# DisasterMessage

Requests를 사용한 간단한 [K-CBS](https://www.dgovkorea.go.kr/service1/g2c_03/cbs) 파서.

# Cons and Pros

### Pros
* [Requests](https://pypi.org/project/requests/)를 제외하고는 파이썬 내부 라이브러리로 만듬.

### Cons
* 끔찍한 퀄리티
* 메모리 누수
* ~~그냥 직접 만들어 쓰세요~~

# Updates

### 0.0.1
* 최초 버전

### 0.0.2
* HTTP 상태 코드 500에 대한 메시지 표출여부 설정가능
* 로그 기록 과정에서 매번 파일을 열고 닫음으로써 메모리 누수 완화(아마도)
