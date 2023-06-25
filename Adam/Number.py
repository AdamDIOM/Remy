import math
import turtle

from PIL import Image, ImageDraw

class Number:
    def __init__(self, apiNum):
        newNum = apiNum
        print(newNum* math.pi )
        newNum = newNum * math.pi * math.pi * math.pow(newNum,5) * math.pi * math.pi
        #print(newNum)
        newNum = int(newNum * 1000)#000)
        binNum = f"{newNum:b}"
        print(newNum)
        print(binNum)
        binNum = binNum + "0" * (5-(len(binNum) % 5))
        if(len(binNum) < 5):
            binNum = binNum + "0" * (5-len(binNum))
        #print(f'{newNum} = {binNum} (len: {len(binNum)})')
        self.binary = binNum
        
class Turtle:
    
    def turtle(binStr):
        colourDict = {
            "00" : "hotpink",
            "01" : "limegreen",
            "10" : "skyblue",
            "11" : "orange"
        }
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
            t.color(colourDict[colour])
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

        print(frames)
        frames[0].save('image.gif', save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)
        return frames
        #t.forward(100)
        #turtle.done()

class Draw:
    colourDict = {
        "00" : "hotpink",
        "01" : "limegreen",
        "10" : "skyblue",
        "11" : "orange"
    }
    def __init__(self, binStr):
        n = int(binStr, 2)
        nstr = str(n)
        frames = []
        img = Image.new("RGBA", (1000,1000), "white")
        draw = ImageDraw.Draw(img)       

        for i in range(0, int(len(binStr)), 5):
            #print(binStr[i:i+5])
            print(f"{int(i/5)+1}/{int(len(binStr)/5)}")
            colour = binStr[i:i+2]
            size = int(binStr[i+2:i+5],2)
            shape = int(binStr[i+1:i+3],2)
            if size==0:
                size = 1
            pos1 = int(nstr[int(i/5):int(i/5)+3])
            pos2 = int(nstr[int(i/5)+2:int(i/5)+5])
            pos3 = int(nstr[int(i/5)+1:int(i/5)+4])
            
            print(f"1:{pos1} 2:{pos2} 3:{pos3} size:{size} shape:{shape}")
            if shape == 0 or shape == 2:
                draw.rectangle((int(pos1),int(pos2),int(pos1)*size,int(pos2)*size), outline=self.colourDict[colour], width=size*3)
            elif shape == 1 or shape==3:
                draw.ellipse((int(pos1),int(pos2),int(pos1)+50,int(pos2)+50), outline=self.colourDict[colour], width=size*3)

            #draw.rectangle((0,100,100,100),outline="red",width=5)
            frames.append(img.copy())
            #img.show()
            
        #img.show()
        frames[0].save('image.gif', format='GIF', save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)

# n = Number(623242.22423)
# print(n.binary)
# #t = Turtle.turtle(n.binary)
# d = Draw(n.binary)
