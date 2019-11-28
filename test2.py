from tkinter import *
import matplotlib.pyplot as plt 
import random 
from subprocess import call
metin = []

def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def alinanmetin():
    metin.append(giris.get())
    strmetin = metin[0]
    binary = string2bits(metin[0])
    str1 = ''.join(binary)
    print(str1)
    yazi.config(text="Girilen metnin binary karşılığı: %s" %str1)
    return str1

def Unipolar():
    binary = alinanmetin()
    #binary = "1011001101"   
    print(binary)
    x = [1, 2, 2,3, 4, 5, 6, 7, 8, 9, 10] 
    y = [-1,-1,1,1,1,0,0,1,1,-1,-1]   
    w = Canvas(anapencere, width=800, height=200)
    w.pack()
    w.create_line(0,10,800,10, dash=(4, 2))
    w.create_line(0,100,800,100,  dash=(4, 2))
    w.create_line(0,190,800,190,  dash=(4, 2))
    if binary[0] == "1":
        x1 = 50
        y1 = 50
        x2 = 100
        y2 = 50
        w.create_line(x1, y1, x2, y2 ,fill="#476042", width=3 )
         #,fill="#476042", width=3
        x1 = x2 
        y1 = y2
    elif binary[0] == "0":
        x1 = 50
        y1 = 100
        x2 = 100
        y2 = 100
        w.create_line(x1, y1, x2, y2,fill="#476042", width=3)
        x1 = x2
        y1 = y2


    for i in range(1,len(binary)):
        if  binary[i-1] == "1" and binary[i] == "1":
            x2 += 50
            w.create_line(x1, y1, x2, y2,fill="#476042", width=3)
            x1 = x2 
            y1 = y2

        elif  binary[i-1] == "0" and binary[i] == "1":
            y2 -= 50
            w.create_line(x1, y1, x2, y2,fill="#476042", width=3)
            x1 = x2
            y1 = y2
            x2 += 50
            w.create_line(x1, y1, x2, y2,fill="#476042", width=3)
            x1 = x2 
            y1 = y2

        elif  binary[i-1] == "1" and binary[i] == "0":
            y2 += 50
            w.create_line(x1, y1, x2, y2,fill="#476042", width=3)
            x1 = x2 
            y1 = y2 
            x2 += 50
            w.create_line(x1, y1, x2, y2,fill="#476042", width=3)
            x1 = x2 
            y1 = y2
 
        elif binary[i-1] == "0" and binary[i] == "0":
            x2 +=50
            w.create_line(x1,y1,x2,y2,fill="#476042", width=3)
            x1 = x2 
            y1 = y2

    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0



    
    """
    plt.plot(x, y) 
    plt.xlabel('x - axis')
    plt.ylabel('y - axis') 
    plt.title('Unipolar') 
    alinanmetin()
    plt.show() 
    """
    
def NRZL():
    binary = alinanmetin()
    #binary = "110011"   
    print(binary)
    x = [1, 2, 2,3, 4, 5, 6, 7, 8, 9, 10] 
    y = [-1,-1,1,1,1,0,0,1,1,-1,-1]   
    w = Canvas(anapencere, width=800, height=200)
    w.pack()
    w.create_line(0,10,800,10, dash=(4, 2))
    w.create_line(0,100,800,100,  dash=(4, 2))
    w.create_line(0,190,800,190,  dash=(4, 2))
    if binary[0] == "1":
        x1 = 50
        y1 = 75
        x2 = 100
        y2 = 75
        w.create_line(x1, y1, x2, y2 ,fill="#476042", width=3 )
         #,fill="#476042", width=3
        x1 = x2 
        y1 = y2
    elif binary[0] == "0":
        x1 = 50
        y1 = 125
        x2 = 100
        y2 = 125
        w.create_line(x1, y1, x2, y2,fill="#476042", width=3)
        x1 = x2
        y1 = y2


    for i in range(1,len(binary)):
        if  binary[i-1] == "1" and binary[i] == "1":
            x2 += 50
            w.create_line(x1, y1, x2, y2,fill="#476042", width=3)
            x1 = x2 
            y1 = y2

        elif  binary[i-1] == "0" and binary[i] == "1":
            y2 -= 50
            w.create_line(x1, y1, x2, y2,fill="#476042", width=3)
            x1 = x2
            y1 = y2
            x2 += 50
            w.create_line(x1, y1, x2, y2,fill="#476042", width=3)
            x1 = x2 
            y1 = y2

        elif  binary[i-1] == "1" and binary[i] == "0":
            y2 += 50
            w.create_line(x1, y1, x2, y2,fill="#476042", width=3)
            x1 = x2 
            y1 = y2 
            x2 += 50
            w.create_line(x1, y1, x2, y2,fill="#476042", width=3)
            x1 = x2 
            y1 = y2
 
        elif binary[i-1] == "0" and binary[i] == "0":
            x2 +=50
            w.create_line(x1,y1,x2,y2,fill="#476042", width=3)
            x1 = x2 
            y1 = y2

    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

def NRZL_Plotter():
       
    x = [1, 2, 2,3, 4, 5, 6, 7, 8, 9, 10] 
    y = [-1,-1,1,1,1,0,0,1,1,-1,-1]   
    plt.plot(x, y) 
    plt.xlabel('x - axis')
    plt.ylabel('y - axis') 
    plt.title('NRZL') 
    alinanmetin()
    plt.show() 

def cagir():
    call(["python", "drawline.py"])

anapencere=Tk()
anapencere.geometry('1000x800')
yazi=Label(anapencere)
yazi.config(text="Buraya girilen metin gelecek.")
yazi.pack()

giris=Entry(anapencere)
giris.pack()

buton=Button(anapencere)
buton.config(text="Unipolar")
buton.config(command=Unipolar)
buton.pack()

buton2=Button(anapencere)
buton2.config(text="NRZL")
buton2.config(command=NRZL)
buton2.pack()


buton3=Button(anapencere)
buton3.config(text="NRZL-Plotter")
buton3.config(command=NRZL_Plotter)
buton3.pack()
anapencere.mainloop()