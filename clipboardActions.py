import time
import pyperclip as pc
import pyautogui
import pygetwindow as gw
from utils import log

def copy_from_active_window():
    log("Copying text from active window")
    active_window = gw.getActiveWindow()
    if active_window is not None:
        text = active_window.title
        pc.copy(text)
        return text
    else:
        return None

def paste_value(value):
    log("Pasting value into active window")
    pc.copy(value)
    time.sleep(0.5)  # Added delay to allow focus and processing
    pyautogui.hotkey('ctrl', 'v')
