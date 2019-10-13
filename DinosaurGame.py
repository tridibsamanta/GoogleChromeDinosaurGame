import pyautogui as p
print("Playing")
y = 1
while True:
    x = p.pixel(480,220)
    if x!=y:
        p.press('space')
        y = x  