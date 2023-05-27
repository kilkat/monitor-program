import os
import time
import keyboard
import proc_monitor_module
import screenshot_monitor_module
import pdf_mark_module
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

    def on_modified(self, event):
        if event.is_directory:
            print(f"Directory modified: {event.src_path}")
            with open(log_path, "a", encoding="utf-8") as file:
                file.write(f"User: {username} &&& Directory modified: {event.src_path} &&& Directory modified time: {time.strftime('%Y-%m-%d %H-%M-%S')}\n")
        else:
            print(f"File modified: {event.src_path}")
            with open(log_path, "a", encoding="utf-8") as file:
                file.write(f"User: {username} &&& File modified: {event.src_path} &&& File modified time: {time.strftime('%Y-%m-%d %H-%M-%S')}\n")
            # print(type(event.src_path))
            # print(event.src_path)
            # print(patterns[0])
            # if any(pattern in event.src_path for pattern in patterns):
            #     print("파일 수정이 감지되었습니다")
            #     file_path = event.src_path
            #     event_time = time.strftime('%Y-%m-%d %H-%M-%S')
            #     pdf_mark_module.mark_maker(file_path, event_time)


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
            proc_monitor_module.proc_monitor()
            screenshot_monitor_module
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

start_watchdog(monitor_path)
