import pyautogui
import time
import random

# pip install pyautogui
# C:\Users\user\AppData\Local\Programs\Python\Python312\Scripts
# Optional: https://docs.google.com/forms/d/e/1FAIpQLSdB0FwSjaamuLm2sV9LwzhNfWukA9QCdPj2O-vhfftmmucIAw/viewform

time.sleep(3)

for i in range(10000):
    time.sleep(2)

    pyautogui.press('tab'); time.sleep(0.1)
    pyautogui.press('tab'); time.sleep(0.1)
    pyautogui.press('tab'); time.sleep(0.1)

    pyautogui.press('down'); time.sleep(0.1)

    rand = random.randint(0, 100)

    if rand % 2 == 0:
        pyautogui.press('up'); time.sleep(0.05)

    pyautogui.press('tab'); time.sleep(0.05)

    pyautogui.press('down'); time.sleep(0.05)

    rand = random.randint(0, 100)

    if rand % 2 == 0:
        pyautogui.press('up'); time.sleep(0.05)

    for _ in range(21):
        pyautogui.press('tab'); time.sleep(0.05)

        pyautogui.press('space'); time.sleep(0.05)

        rand = random.randint(0, 2)

        for _ in range(rand):
            pyautogui.press('down'); time.sleep(0.05)

        pyautogui.press('tab'); time.sleep(0.05)

        pyautogui.press('space'); time.sleep(0.05)

        rand = random.randint(0, 3)

        for _ in range(rand):
            pyautogui.press('up'); time.sleep(0.05)

    pyautogui.press('tab'); time.sleep(0.05)

    front = random.randint(0, 9999)
    back = random.randint(0, 9999)

    phone_number = f"010-{front:04d}-{back:04d}"
    pyautogui.typewrite(phone_number); time.sleep(0.05)

    pyautogui.press('tab'); time.sleep(0.05)

    pyautogui.press('enter'); time.sleep(2)

    pyautogui.press('tab'); time.sleep(0.05)

    pyautogui.press('enter'); time.sleep(0.05)
