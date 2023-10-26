# Version 0.0.1

import requests
import json
import asyncio
from datetime import datetime

#log 설정
filename = f'{datetime.now().strftime("%Y%m%d %H%M%S")} log.txt'
file1 = open(filename, 'a') 

async def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")

# 사용자로부터 시작할 인덱스 번호를 입력받음
start_index = int(input("시작할 인덱스 번호를 입력하세요: "))
file1.write(f"시작할 인덱스 번호를 입력하세요: {start_index}\n")
file1.flush()

# 마지막 확인한 인덱스 번호를 입력한 값으로 설정
last_checked_index = start_index - 1

print("=============================================")
file1.write("=============================================\n")
file1.flush()

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
                        current_time = await get_current_time()
                        print("LAST_MODF_DT:", item.get("LAST_MODF_DT")) # 출력
                        file1.write(f"LAST_MODF_DT: {item.get("LAST_MODF_DT")}\n")
                        print("BBS_NO:", item.get("BBS_NO"))
                        file1.write(f"BBS_NO: {item.get("BBS_NO")}\n")
                        print("FRST_REGIST_DT:", item.get("FRST_REGIST_DT"))
                        file1.write(f"FRST_REGIST_DT: {item.get("FRST_REGIST_DT")}\n")
                        print("BBS_ORDR:", item.get("BBS_ORDR"))
                        file1.write(f"BBS_ORDR: {item.get("BBS_ORDR")}\n")
                        print("SJ:", item.get("SJ"))
                        file1.write(f"SJ: {item.get("SJ")}\n")
                        print("IDX_NO:", item.get("IDX_NO"))
                        file1.write(f"IDX_NO: {item.get("IDX_NO")}\n")
                        print("QRY_CNT:", item.get("QRY_CNT"))
                        file1.write(f"QRY_CNT: {item.get("QRY_CNT")}\n")
                        print("CN:", item.get("CN"))
                        file1.write(f"CN: {item.get("CN")}\n")
                        print("title:", item.get("title"))
                        file1.write(f"title: {item.get("title")}\n")
                        print("USR_NM:", item.get("USR_NM"))
                        file1.write(f"USR_NM: {item.get("USR_NM")}\n")
                        print("USR_EXPSR_AT:", item.get("USR_EXPSR_AT"))
                        file1.write(f"USR_EXPSR_AT: {item.get("USR_EXPSR_AT")}\n")
                        print("USR_EXPSR_AT:", item.get("USR_EXPSR_AT"))
                        file1.write(f"USR_EXPSR_AT: {item.get("USR_EXPSR_AT")}\n")
                        print(f"{current_time} 수신")
                        file1.write(f"{current_time} 수신\n")
                        print("=============================================")
                        file1.write("=============================================\n")
                        file1.flush()
                        new_data_found = True  # 새로운 데이터를 찾았음을 표시
                break  # 데이터를 찾았으므로 while 루프 종료

            except requests.exceptions.RequestException as e:
                current_time = await get_current_time()
                if '500' in str(e):
                    print(f"{current_time} {index}번 확인 결과 새로운 데이터가 없거나 권한이 없음. 갱신 주기 재시작\n")
                    file1.write(f"{current_time} {index}번 확인 결과 새로운 데이터가 없거나 권한이 없음. 갱신 주기 재시작\n")
                    file1.flush()
                    await asyncio.sleep(1) # 1초에 여러번 실행 방지용, 하드코딩이라 언젠간 고쳐야할듯
                else:
                    print(f"{current_time} HTTP 에러 {e} 발생.\n")
                    file1.write(f"{current_time} HTTP 에러 {e} 발생.\n")
                    file1.flush()
                    await asyncio.sleep(1) # 1초에 여러번 실행 방지용, 하드코딩이라 언젠간 고쳐야할듯
                while int(datetime.now().strftime("%S")) != 1 and int(datetime.now().strftime("%S")) != 31:
                    await asyncio.sleep(1) # 정확한 초에 실행되도록 하는 방법이 복잡해서 임시방편으로

if __name__ == "__main__":
    asyncio.run(main())
