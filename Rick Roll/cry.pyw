from time import sleep
import win32gui
import win32con
import threading
def cry():
    win32gui.MessageBox(
        None,
        'QwQ',
        'Cry',
        win32con.MB_OK
    )
threads = []
for i in range(30):
    msgbox = threading.Thread(target=cry)
    threads.append(msgbox)
    sleep(0.05)
    threads[i].start()