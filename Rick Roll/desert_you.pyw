from time import sleep
import win32gui
import win32api
import win32con
import random
hwnd = win32gui.FindWindow(None, 'Plain Craft Launcher 2　')
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
screenx, screeny = win32api.GetSystemMetrics(win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
for i in range(0, 50, 1):
    win32gui.MoveWindow(
        hwnd,
        random.randint(50, screenx - (right - left) - 50),
        random.randint(50, screeny - (bottom - top) - 50),
        right - left,
        bottom - top,
        False
    )
    sleep(0.01)
win32gui.MoveWindow(
    hwnd,
    left,
    top,
    right - left,
    bottom - top,
    False
)