import os
import time
import procmonitor_module
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

log_path = input("please input log path = ") + "\\" + time.strftime('%Y-%m-%d %H-%M-%S') + ".txt"
print(log_path)
f = open(log_path, 'w')
f.close()
monitor_path = input("please input monitoring path = ")
username = os.getlogin()
patterns = [".pdf", ".img", ".png"]

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            print(f"Directory created: {event.src_path}")
            with open(log_path, "a", encoding="utf-8") as file:
                file.write(f"User: {username} &&& Directory created path: {event.src_path} &&& Directory created time: {time.strftime('%Y-%m-%d %H-%M-%S')}\n")
        else:
            print(f"File created: {event.src_path}")
            with open(log_path, "a", encoding="utf-8") as file:
                file.write(f"User: {username} &&& File created: {event.src_path} &&& File created time: {time.strftime('%Y-%m-%d %H-%M-%S')}\n")
                for pattern in patterns:
                    pass  # 추후 워터마크 기능 추가 예정

    def on_modified(self, event):
        if event.is_directory:
            print(f"Directory modified: {event.src_path}")
            with open(log_path, "a", encoding="utf-8") as file:
                file.write(f"User: {username} &&& Directory modified: {event.src_path} &&& Directory modified time: {time.strftime('%Y-%m-%d %H-%M-%S')}\n")
        else:
            print(f"File modified: {event.src_path}")
            with open(log_path, "a", encoding="utf-8") as file:
                file.write(f"User: {username} &&& File modified: {event.src_path} &&& File modified time: {time.strftime('%Y-%m-%d %H-%M-%S')}\n")
                for pattern in patterns:
                    pass  # 추후 워터마크 기능 추가 예정

    def on_deleted(self, event):
        if event.is_directory:
            print(f"Directory deleted: {event.src_path}")
            with open(log_path, "a", encoding="utf-8") as file:
                file.write(f"User: {username} &&& Directory deleted: {event.src_path} &&& Directory deleted time: {time.strftime('%Y-%m-%d %H-%M-%S')}\n")
        else:
            print(f"File deleted: {event.src_path}")
            with open(log_path, "a", encoding="utf-8") as file:
                file.write(f"User: {username} &&& File deleted: {event.src_path} &&& File deleted time: {time.strftime('%Y-%m-%d %H-%M-%S')}\n")

def start_watchdog(monitor_path):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, monitor_path, recursive=True)
    observer.start()

    try:
        while True:
            # 스크린샷 프로그램이 실행중인지 & 실행중이라면 process 죽이기
            procmonitor_module.proc_monitor()
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

start_watchdog(monitor_path)

