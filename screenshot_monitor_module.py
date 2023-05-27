import ctypes
import win32clipboard
import threading
import keyboard


def screenshot_ctrl(event):
    # 클립보드 열기
    if event.name == 'print screen':
        print("PrtSc key pressed!")
        threading.Event().wait(1)
        win32clipboard.OpenClipboard(None)
        
        try:
            # 클립보드 데이터 형식 가져오기
            data_format = win32clipboard.EnumClipboardFormats(0)
            if data_format == win32clipboard.CF_BITMAP:
                # 데이터 형식이 비트맵인 경우 데이터 가져오기
                data_handle = win32clipboard.GetClipboardData(data_format)

                # 데이터 출력
                print("Clipboard Screenshot Data:", data_handle)
                win32clipboard.EmptyClipboard()
                print("Clipboard data deleted")

            else:
                print("No screenshot data on the clipboard.")
        finally:
            # 클립보드 닫기
            win32clipboard.CloseClipboard()

# PrtSc 키 감지 이벤트 등록
keyboard.on_press(screenshot_ctrl)