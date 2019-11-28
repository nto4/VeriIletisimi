"""
from tkinter import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
window.mainloop()

metin ='abc'

def coder(list):
    list = [] 
    list[:0] = metin
    ascilist = []
    #print(ord(metin[0]))
    #print(len(list))
    for i in range(0,len(list)):
        ascilist.append(ord(metin[i]))
        #print(i)
       

    print(ascilist)
    return ascilist

def decode(ascilist):
    metin2 = ""
    for i in range(0,len(ascilist)):
        #print(i)
        metin2 += chr(ascilist[i])
    print(metin2)



def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

s = 'ü'
b = string2bits(s)
s2 = bits2string(b)
str1 = ''.join(b)
def unipolar(str1):
    state = 0
    for i in str1:
        if int(i) == 1:
            if state == 0:
                print("|",end ="")
                state = 1
            print("¯¯",end="")
        if int(i) == 0:
            if state == 1:
                print("|",end ="")
                state = 0
            print("--",end="")

def NRZL(str1):
    state = 0
    for i in str1:
        if int(i) == 1:
            if state == 0:
                print("|",end ="")
                state = 1
            print("¯¯",end="")
        if int(i) == 0:
            if state == 1:
                print("|",end ="")
                state = 0
            print("__",end="")


def NRZI(str1):
    state = int(str1[0])
    if int(str1[0]) == 1:
        print("|¯¯",end="")
    if int(str1[0]) == 0:
        print("__",end="")
    for i in range(1,len(str1)):
       
        if int(str1[i]) == 1 and state == 1:
            print("¯¯",end="")
        elif int(str1[i]) == 0 and state == 1:
            print("|",end="")
            print("__",end="")
            state = 0
        elif int(str1[i]) == 0 and state == 0:
            print("__",end="")
        elif int(str1[i]) == 1 and state == 0:
            print("|",end="")
            print("¯¯",end="")
            state = 1

str3 = "010010"
def Manchester(str1):
    #print(len(str1))
    if int(str1[0]) == 1:
        print("*_|¯",end="")
        #print("ilk rakam 1")
    elif int(str1[0]) == 0:
        print("*¯|_",end="")

    for i in range(1,len(str1)):
        #print("")
        if int(str1[i]) == 1:
            #print((int(str1[i-1])==1))
            if (int(str1[i-1]) == 1):
                    print("|",end="")
            print("_|¯",end="")
                
        elif int(str1[i]) == 0:
            if (int(str1[i-1]) == 0):
                    print("|",end="")
            print("¯|_",end="")
             
                
    print("          ")



def DifManchester(str1):
  
    if int(str1[0]) == 0:
        print("|_|¯",end="")
    elif int(str1[0]) == 1:
        print("¯|_",end="")
    for i in range(1,len(str1)):
        if int(str1[i]) == 1:
            if (int(str1[i-1]) == 1):
                    print("|",end="")
            print("_|¯",end="")
        elif int(str1[i]) == 0:
            if (int(str1[i-1]) == 0):
                    print("|",end="")
            print("¯|_",end="")
    print("          ")
def AMI(str1):
    state = 0
    if int(str1[0]) == 1:
        print("|¯|",end="")
        if state == 0:
            state = 1
        else:
            state =0
    #print("ilk rakam 1")
    elif int(str1[0]) == 0:
        print("-",end="")
    #print("loop")
    for i in range(1,len(str1)):
        #print(i)
        if int(str1[i]) == 1:
            if state == 0:
                print("|¯|",end ="")
                state = 1
            elif state == 1:
                print("|_|",end ="")
                state = 0
           
        if int(str1[i]) == 0:
            print("-",end ="")
            
"""     
"""
from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.geometry('1366x1024')
img = ImageTk.PhotoImage(Image.open("bir.gif"))
#img2 = ImageTk.PhotoImage(Image.open("sifir.gif"))
panel = Label(root, image = img)
#panel = Label(root, image = img2)
panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()
"""
"""
import numpy as np
from matplotlib import pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
"""

# importing the required module 
import tkinter as tk
import matplotlib.pyplot as plt 
import random    
from tkinter import Label
def quit():
    global root
    root.quit()
def ciz():
   
    x = [1, 2, 2,3, 4, 5, 6, 7, 8, 9, 10] 
    y = [-1,-1,1,1,1,0,0,1,1,-1,-1]   
    plt.plot(x, y) 
    plt.xlabel('x - axis')
    plt.ylabel('y - axis') 
    plt.title('My first graph!') 
    plt.show() 

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
e1 =tk.Entry(root)
e1.pack(side='top')
yazi = Label(root)
yazi.pack(side='bottom')
button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Çiz",
                   command=ciz)
slogan.pack(side=tk.LEFT)

root.mainloop()



#ciz()

"""
from scipy import signal

import matplotlib.pyplot as plot

import numpy as np

 

# Sampling rate 1000 hz / second

t = np.linspace(0, 1, 1000, endpoint=True)

 

# Plot the square wave signal

plot.plot(t, signal.square(2 * np.pi * 5 * t))

 

# Give a title for the square wave plot

plot.title('Sqaure wave - 5 Hz sampled at 1000 Hz /second')

 

# Give x axis label for the square wave plot

plot.xlabel('Time')

 

# Give y axis label for the square wave plot

plot.ylabel('Amplitude')

 

plot.grid(True, which='both')

 

# Provide x axis and line color

plot.axhline(y=0, color='k')

 

# Set the max and min values for y axis

plot.ylim(-2, 2)

 

# Display the square wave drawn

plot.show()
"""