import requests
import json
import asyncio
from datetime import datetime

async def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")

# 사용자로부터 시작할 인덱스 번호를 입력받음
start_index = int(input("시작할 인덱스 번호를 입력하세요: "))

# 마지막 확인한 인덱스 번호를 입력한 값으로 설정
last_checked_index = start_index - 1

async def main():
    global last_checked_index
    while True:
        new_data_found = False  # 새로운 데이터를 찾았는지 여부를 추적

        # 이전에 확인한 인덱스 번호보다 큰 새로운 데이터가 있는지 확인
        index = last_checked_index + 1
        while True:
            url = f'https://www.safekorea.go.kr/idsiSFK/neo/ext/json/disasterDataList/disasterData_{index}.json'
            try:
                response = requests.get(url)
                response.raise_for_status()  # HTTP 에러 발생 시 예외 발생
                data = json.loads(response.content.decode('utf-8'))

                if data:
                    last_checked_index = index
                    for item in data:
                        print("LAST_MODF_DT:", item.get("LAST_MODF_DT", "(없음)"))
                        print("BBS_NO:", item.get("BBS_NO", "(없음)"))
                        print("FRST_REGIST_DT:", item.get("FRST_REGIST_DT", "(없음)"))
                        print("BBS_ORDR:", item.get("BBS_ORDR", "(없음)"))
                        print("SJ:", item.get("SJ", "(없음)"))
                        print("IDX_NO:", item.get("IDX_NO", "(없음)"))
                        print("QRY_CNT:", item.get("QRY_CNT", "(없음)"))
                        print("CN:", item.get("CN", "(없음)"))
                        print("title:", item.get("title", "(없음)"))
                        print("USR_NM:", item.get("USR_NM", "(없음)"))
                        print("USR_EXPSR_AT:", item.get("USR_EXPSR_AT", "(없음)"))
                        new_data_found = True  # 새로운 데이터를 찾았음을 표시
                break  # 데이터를 찾았으므로 while 루프 종료

            except requests.exceptions.RequestException as e:
                current_time = await get_current_time()
                if '500' in str(e):
                    print(f"{current_time} {index}번 확인 결과 새로운 데이터가 없거나 권한이 없음. 갱신 주기 재시작")
                else:
                    print(f"{current_time} HTTP 에러 {e} 발생.")
                await asyncio.sleep(30)  # 30초 동안 기다린 후 다시 확인 시도

        if not new_data_found:
            current_time = await get_current_time()
            print(f"{current_time} 확인 결과 새로운 데이터 없음. 갱신 주기 재시작")
            await asyncio.sleep(30)  # 30초 대기 후 다시 확인

if __name__ == "__main__":
    asyncio.run(main())
