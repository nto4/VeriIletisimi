from tkinter import *
import matplotlib.pyplot as plt 
import random 



def startone(x,y):

    x.extend([0,0,1])
    y.extend([0,1,1])
    return x,y

def startzero(x,y):
    print("çalıştı")
    x.extend([0,0,1])
    y.extend([1,0,0])
    return x,y


def altciz(x,y):
    if y[-1]== 0:
        y.append(0)
        tmp = x[-1]
        print(tmp)
        tmp = tmp + 1
        x.append(tmp)
    elif y[-1] == 1:
        y.append(0)
        tmp = x[-1]
        x.append(tmp)
        y.append(0)
        tmp += 1
        x.append(tmp)
    
    return x,y
          

def ustciz(x,y):
    if y[-1] == 0:
        tmp = x[-1]
        y.append(1)
        x.append(tmp)
        y.append(1)
        tmp += 1
        x.append(tmp)
   
    elif y[-1] == 1:
        y.append(1)
        tmp = x[-1]
        tmp +=1
        x.append(tmp)
    return x,y
    



def Unipolar():

    x= []
    y= []
    str1 = "01101001"
    
    print(len(str1))
    print(str1[0])
    if str1[0]=="1":
        startone(x,y)
    elif str1[0]=="0":
        startzero(x,y)
    else:
        print("WTF")
    for i in range(1,len(str1)):
        if str1[i] == "1":
            ustciz(x,y)
        elif str1[i] == "0":
            altciz(x,y)

    print(x)
    print(y)
    
    
    plt.plot(x, y) 
    #plt.axis([0, 24, 0, 2])
    plt.axis("tight")
    plt.xlabel('x - axis')
    plt.ylabel('y - axis') 
    plt.title('Unipolar') 
    plt.show() 

#startone()


Unipolar()