import math
import turtle
import pyautogui
from PIL import Image, ImageDraw


class Number:
    def __init__(self, apiNum):
        newNum = apiNum
        #print(newNum)
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
        img = Image.new("RGBA", (500,500))
        draw = ImageDraw.Draw(img)       

        for i in range(0, int(len(binStr)), 5):
            #print(binStr[i:i+5])
            print(f"{int(i/5)}/{int(len(binStr)/5)}")
            colour = binStr[i:i+2]
            size = int(binStr[i+2:i+5],2)
            shape = int(binStr[i+1:i+3],2)
            if size==0:
                size = 1
            pos1 = int(nstr[int(i/5):int(i/5)+3])/2
            pos2 = int(nstr[int(i/5)+2:int(i/5)+5])/2
            pos3 = int(nstr[int(i/5)+1:int(i/5)+4])/2
            
            print(f"1:{pos1} 2:{pos2} 3:{pos3} size:{size} shape:{shape}")
            if shape == 0 or shape == 2:
                draw.rectangle((int(pos1),int(pos2),int(pos1)*size,int(pos2)*size), outline=self.colourDict[colour], width=size*3)
            elif shape == 1 or shape==3:
                draw.ellipse((int(pos1),int(pos2),int(pos1)+50,int(pos2)+50), outline=self.colourDict[colour], width=size*3)

            #draw.rectangle((0,100,100,100),outline="red",width=5)
            frames.append(img)
            img.show()
            
        #img.show()
        frames[0].save('image.gif', save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)

n = Number(6)
print(n.binary)
#t = Turtle(n.binary)
d = Draw(n.binary)