#if this tab is fullscreen, this program will restore it down

##### this is an example of using pyautogui to drag cursor from one point to another

import pyautogui as p

x = 1220
y = 15

p.mouseDown(x=x, y=y, button='left')
x -= 600
y += 125
p.moveTo(x,y)
p.mouseUp(x=x, y=y, button='left')
