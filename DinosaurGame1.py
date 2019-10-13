import time
import pyautogui
 
print('PLAYING')
time.sleep(5)
pyautogui.press('space')
 
while True:
    if pyautogui.pixelMatchesColor(545, 223, (83, 83, 83)):
        pyautogui.press('space')