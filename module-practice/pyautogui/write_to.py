#this opens a python shell and makes it print 'hi'
#(i wanted to see if it would actually run things using this)

##### example of how to write to a thing

import pyautogui as p

x = 225
y = 1052
b = 'left'
l = ['p','r','i','n','t','(','"','h','i','"',')','enter']

p.click(x,y,1,1,b)
p.typewrite('python',0.2)
y = 370
p.click(x,y,1,1,b)
p.typewrite(l,0.2)
