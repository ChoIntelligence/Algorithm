import pyautogui
import time
import random

# Optional: Add a short delay to ensure you switch to the target window
time.sleep(5)

for i in range(10000):
    time.sleep(2)

    pyautogui.press('tab'); time.sleep(0.05)
    pyautogui.press('tab'); time.sleep(0.05)
    pyautogui.press('tab'); time.sleep(0.05)

    pyautogui.press('down'); time.sleep(0.05)

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

        rand = random.randint(0, 4)

        for _ in range(rand):
            pyautogui.press('down'); time.sleep(0.05)

        pyautogui.press('tab'); time.sleep(0.05)

        pyautogui.press('space'); time.sleep(0.05)

        for _ in range(4 - rand):
            pyautogui.press('down'); time.sleep(0.05)

    pyautogui.press('tab'); time.sleep(0.05)

    front = random.randint(0, 9999)
    back = random.randint(0, 9999)

    phone_number = f"010-{front:04d}-{back:04d}"
    pyautogui.typewrite(phone_number); time.sleep(0.05)

    pyautogui.press('tab'); time.sleep(0.05)

    pyautogui.press('enter'); time.sleep(2)

    pyautogui.press('tab'); time.sleep(0.05)

    pyautogui.press('enter'); time.sleep(0.05)
