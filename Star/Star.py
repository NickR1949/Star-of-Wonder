# Star.py
version = "0.3.0"
# Nick Rutt 05/01/2023
# MIT Licence
# For Raspberry Pi with Blinkt!

####
#Using Blinkt! to light paper star
#####

from time import sleep
from blinkt import set_all, show, clear
from random import randint

Colours = [ [155,0,0],
            [0,100,0],
            [0,0,100],
            [100,30,0],
            [50,0,100],
            [0,150,100],
            [120,30,0],
            [200,200,200]]
           


STEPS = 15
DOZE = 5
Target = [0,0,0]
Current = [0,0,0]
Control = [0,0,0]

def setColour():
    t = [0,0,0]
    rowColour = randint(0,7)
    print(rowColour)
    t = Colours[rowColour]
    return(t)
	
def doLights(steps,current,control):
    for y in range(steps):
        for x in range(3):
            current[x] = int(current[x] + control[x])
        r = current[0]
        g = current[1]
        b = current[2]
        
        set_all(r,g,b,brightness = None)
        show()
#        print("Current Array" ,r,g,b)
        sleep(0.5)

    return(current)
	

# program starts here
print ("XmasStar v:",version)
Target = setColour()
Current = setColour()

clear()

while(True):
    Control = [0,0,0]
    for x in range(3):
        Control[x] = int((Target[x] - Current[x])/STEPS)

    Current = doLights(STEPS,Current,Control)


    sleep(DOZE)
    while True:
        Target = setColour()
        if Target != Current:
            break
    
#   End of Program