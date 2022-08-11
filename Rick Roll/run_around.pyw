from time import sleep
from math import *
import win32gui
hwnd = win32gui.FindWindow(None, "Plain Craft Launcher 2　")
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
r = 80
for i in range(0, 360, 6):
    x = r * cos((i + 90) * pi / 180.0)
    y = r * sin((i + 90) * pi / 180.0)
    win32gui.MoveWindow(
        hwnd,
        left + round(x),
        top - r + round(y),
        right - left,
        bottom - top,
        False
    )
    sleep(0.001)
win32gui.MoveWindow(
    hwnd,
    left,
    top,
    right - left,
    bottom - top,
    False
)