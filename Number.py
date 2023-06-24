import math
import turtle
import pyautogui
from PIL import Image

class Number:
    def __init__(self, apiNum):
        newNum = apiNum
        #print(newNum)
        newNum = newNum * math.pi * math.pi * math.factorial(int(newNum)) * math.pi * math.pi
        #print(newNum)
        newNum = int(newNum * 1000)#000)
        binNum = f"{newNum:b}"
        binNum = binNum + "0" * (5-(len(binNum) % 5))
        if(len(binNum) < 5):
            binNum = binNum + "0" * (5-len(binNum))
        #print(f'{newNum} = {binNum} (len: {len(binNum)})')
        self.binary = binNum
        
class Turtle:
    colourDict = {
        "00" : "hotpink",
        "01" : "limegreen",
        "10" : "skyblue",
        "11" : "orange"
    }
    def __init__(self, binStr):
        t = turtle.Turtle()
        t.width = 10
        n = int(binStr, 2)
        nstr = str(n)

        frames = []
        image = pyautogui.screenshot()
        frames.append(image)
        for i in range(0, int(len(binStr)), 5):
            #print(binStr[i:i+5])
            colour = binStr[i:i+2]
            size = int(binStr[i+2:i+5],2)
            posx = nstr[int(i/5):int(i/5)+3]
            posy = nstr[int(i/5)+1:int(i/5)+4]

            print(f"x:{posx} y:{posy} size:{size}")
            t.color(self.colourDict[colour])
            t.setx((int(posx)/1000*650)-350)
            image = pyautogui.screenshot()
            frames.append(image)
            t.sety((int(posx)/1000*650)-325)
            image = pyautogui.screenshot()
            frames.append(image)
            t.pensize(size)
            t.forward(size*5)
            image = pyautogui.screenshot()
            frames.append(image)
            t.left(90)
        #self.Mouse(t, posx, posy)

        
        frames[0].save('image.gif', save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)

        #t.forward(100)
        #turtle.done()

n = Number(5.23)
print(n.binary)
t = Turtle(n.binary)