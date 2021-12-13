#close four google chrome tabs
#(at least on this laptop, while < 6 tabs are open) 
#this was just a test while learning the pyautogui module

###### example of using pyautogui to click different points on screen

import pyautogui as p
from time import sleep

x = 1190
y = 20

for i in range(4):
    p.click(x,y,1,1,'left')
    sleep(1)
    x = x-300
