import pyautogui
import time
import pyperclip  # To handle clipboard text


def capture_ui():
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'l')  
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')  
    time.sleep(0.5)

    url = pyperclip.paste()
    return url

if __name__ == "__main__" :
    super_url = capture_ui()
    print(super_url)


