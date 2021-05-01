import pyautogui
import time
import keyboard
from random import randint

red = (255, 0, 0)
green = (0, 150, 100)
rad = 150

print("- Iterations? -")
itr = int(input())

o = i = 0
while True:
    if keyboard.is_pressed("`") or i >= itr: break

    mon = pyautogui.screenshot()
    pixR = mon.getpixel((1050-1, 900-1))
    pixD = mon.getpixel((660-1, 1053-1))

    if pixR == red:
        print("Work...")
        pyautogui.click(1920/2 + randint(-rad, rad)/2, 1080/2 + randint(-rad, rad)/2, duration=0.16)
        for ii in range(randint(4, 8)): pyautogui.click()
    else: print("wait...", pixR, i, "/", itr)

    ver = 1 - (abs(green[0]-pixD[0])+abs(green[1]-pixD[1])+abs(green[2]-pixD[2]))/3/255
    if ver > 0.93 and o == 0:
        print("+ Fish!")
        pyautogui.press('i')
        pyautogui.click(1760, 380, duration=0.5)
        pyautogui.click(1760, 450, duration=0.5)
        
        i += 1
        o += 1
        time.sleep(5)
    else: o = 0

    time.sleep(0.1)

print("-- Work Ower --")
print(i, "Fish Caught")
