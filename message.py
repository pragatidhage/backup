import pyautogui as pg
import time

print("Program will run in 5 sec")
time.sleep(5)

for i in range(100):
    pg.write("hllo")
    time.sleep(0.5)
    pg.press("Enter")
