import psutil
import subprocess
import ctypes
import os

def proc_monitor():
    f = open('monitor-program\proc_list.txt', 'r')
    list_array = []

    for line in f:
        list_array.append(line.strip())

    f.close()

    # 실행 중인 모든 프로세스 목록 가져오기
    process_list = psutil.process_iter()

    # 각 프로세스에 대한 정보 출력
    for process in process_list:
        if process.name() in list_array:
            print("PID:", process.pid)
            print("이름:", process.name())
            print("blacklist process")
            print("==========================")
            subprocess.call(["taskkill", "/F", "/PID", str(process.pid)])
            ctypes.windll.user32.MessageBoxW(None, f"{process.name()}는 실행할 수 없는 프로그램입니다.", '경고', 0x30)
