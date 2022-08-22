from time import sleep
from math import *
import win32gui

def to_arc(angle):
    return pi / 180.0 * angle

hwnd = win32gui.FindWindow(None, 'Plain Craft Launcher 2　')
left, top, right, bottom = win32gui.GetWindowRect(hwnd)

r = 80
for i in range(0, 360, 6):
    x = - r * sin(to_arc(i))
    y = - r * cos(to_arc(i))
    win32gui.MoveWindow(
        hwnd,
        left + round(x),
        top - round(y) - r,
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