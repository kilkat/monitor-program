import monitor_module

def watchdog(path):
    monitor_module.start_watchdog(path)

if __name__ == "__main__":
    #아래 코드 실행전 register 값 변경을 통해 스샷 방지
    path = input("please input monitoring path = ")
    watchdog(path)
    