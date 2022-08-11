from time import sleep
import win32gui
hwnd = win32gui.FindWindow(None, 'Plain Craft Launcher 2　')
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
for i in range(0, 500, 10):
    win32gui.MoveWindow(
        hwnd,
        left,
        top - i,
        right - left,
        bottom - top,
        False
    )
    sleep(0.001)