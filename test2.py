from tkinter import *
import matplotlib.pyplot as plt 
import random 
from subprocess import call
metin = []
metin2 =[]

def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def alinanmetin():
    metin.append(giris.get())
    strmetin = metin[0]
    binary = string2bits(metin[0])
    str1 = ''.join(binary)
    yazi.config(text="Girilen metnin binary karşılığı: %s" %str1)
    return str1

def alinandatarate():
    metin2.append(giris1.get())
    strmetin = metin2[0]
    yazi1.config(text="Girilen Data Rate: %s" %strmetin)
    return strmetin

def Unipolar():
    binary = alinanmetin()
    datarate =alinandatarate()
    datarate = int(datarate)
    #binary = "01101001"   
    #datarate = 8
    w = Canvas(anapencere, width=1000, height=200)
    w.configure(background='white')
    #Bitleri çizme ekleme
    sp = 25
    for i in range (1,datarate):
        sp = sp +50
        w.create_text(sp,25,fill="red",font="Times 20 italic bold",text=binary[i-1] )
    sp += 50
    w.create_text(sp,25,fill="red",font="Times 20 italic bold",text=binary[-1] )
    #


    w.pack()
    w.create_line(0,10,1000,10, dash=(4, 2))
    w.create_line(0,100,1000,100,  dash=(4, 2))
    w.create_line(0,190,1000,190,  dash=(4, 2))
    for i in range(1,20):
        w.create_line(50*i,10,50*i,190, dash=(4,2))
    if binary[0] == "1":
        x1 = 50
        y1 = 50
        x2 = 100
        y2 = 50
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
         #,fill="#0000ff", width=3
        x1 = x2 
        y1 = y2
    elif binary[0] == "0":
        x1 = 50
        y1 = 100
        x2 = 100
        y2 = 100
        w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
        x1 = x2
        y1 = y2


    for i in range(1,datarate):
        if  binary[i-1] == "1" and binary[i] == "1":
            x2 += 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2

        elif  binary[i-1] == "0" and binary[i] == "1":
            y2 -= 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2
            y1 = y2
            x2 += 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2

        elif  binary[i-1] == "1" and binary[i] == "0":
            y2 += 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2 
            x2 += 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2
 
        elif binary[i-1] == "0" and binary[i] == "0":
            x2 +=50
            w.create_line(x1,y1,x2,y2,fill="#0000ff", width=3)
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
    datarate =alinandatarate()
    datarate = int(datarate)
    #binary = "110011"

    w = Canvas(anapencere, width=1000, height=200)
    w.configure(background='white')
    #Bitleri çizme ekleme
    sp = 25
    for i in range (1,datarate):
        sp = sp +50
        w.create_text(sp,25,fill="red",font="Times 20 italic bold",text=binary[i-1] )
    sp += 50
    w.create_text(sp,25,fill="red",font="Times 20 italic bold",text=binary[-1] )
    #
    w.pack()
    w.create_line(0,10,1000,10, dash=(4, 2))
    w.create_line(0,100,1000,100,  dash=(4, 2))
    w.create_line(0,190,1000,190,  dash=(4, 2))
    for i in range(1,20):
        w.create_line(50*i,10,50*i,190, dash=(4,2))
    if binary[0] == "0":
        x1 = 50
        y1 = 75
        x2 = 100
        y2 = 75
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
         #,fill="#0000ff", width=3
        x1 = x2 
        y1 = y2
    elif binary[0] == "1":
        x1 = 50
        y1 = 125
        x2 = 100
        y2 = 125
        w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
        x1 = x2
        y1 = y2


    for i in range(1,datarate):
        if  binary[i-1] == "0" and binary[i] == "0":
            x2 += 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2

        elif  binary[i-1] == "1" and binary[i] == "0":
            y2 -= 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2
            y1 = y2
            x2 += 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2

        elif  binary[i-1] == "0" and binary[i] == "1":
            y2 += 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2 
            x2 += 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2
 
        elif binary[i-1] == "1" and binary[i] == "1":
            x2 +=50
            w.create_line(x1,y1,x2,y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2

    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

def NRZI():
    #İlk bit 0 sa +v dan başla // ilk bit 1 se -v den başla
    binary = alinanmetin()
    datarate =alinandatarate()
    datarate = int(datarate)
    #binary = "01001110" 
    bayrak = True    
    w = Canvas(anapencere, width=1000, height=200)
    w.configure(background='white')
    #Bitleri çizme ekleme
    sp = 25
    for i in range (1,datarate):
        sp = sp +50
        w.create_text(sp,25,fill="red",font="Times 20 italic bold",text=binary[i-1] )
    sp += 50
    w.create_text(sp,25,fill="red",font="Times 20 italic bold",text=binary[-1] )
    #
    w.pack()
    w.create_line(0,10,1000,10, dash=(4, 2))
    w.create_line(0,100,1000,100,  dash=(4, 2))
    w.create_line(0,190,1000,190,  dash=(4, 2))
    for i in range(1,20):
        w.create_line(50*i,10,50*i,190, dash=(4,2))
   # true ust 
   # fasle alt
    if binary[0] == "1":
        x1 = 50 
        y1 = 75
        x2 = 50
        y2 = 125
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        x1 = 50
        y1 = 125
        x2 = 100
        y2 = 125
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
         #,fill="#0000ff", width=3
        x1 = x2 
        y1 = y2
        bayrak = False
    elif binary[0] == "0":
        x1 = 50
        y1 = 75
        x2 = 100
        y2 = 75
        w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
        x1 = x2
        y1 = y2
        bayrak = True


    for i in range(1,datarate):
        if  binary[i] == "1" and bayrak == True:
          
            y2 += 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2
            x2 += 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2
            bayrak = False

        elif binary[i] == "1" and bayrak == False:
           
            y2 -= 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2
            x2 += 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2
            bayrak = True

        elif binary[i] == "0":
            x2 +=50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2
            y1 = y2


    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

def Manchester():
    binary = alinanmetin()
    datarate =alinandatarate()
    datarate = int(datarate)
    w = Canvas(anapencere, width=1000, height=200)
    w.configure(background='white')
    #Bitleri çizme ekleme
    sp = 25
    for i in range (1,datarate):
        sp = sp +50
        w.create_text(sp,25,fill="red",font="Times 20 italic bold",text=binary[i-1] )
    sp += 50
    w.create_text(sp,25,fill="red",font="Times 20 italic bold",text=binary[-1] )
    #
    w.pack()
    w.create_line(0,10,1000,10, dash=(4, 2))
    w.create_line(0,100,1000,100,  dash=(4, 2))
    w.create_line(0,190,1000,190,  dash=(4, 2))
    for i in range(1,20):
        w.create_line(50*i,10,50*i,190, dash=(4,2))
    bayrak = True
  
    if binary[0] == "0":
        #üst
        x1 = 50
        y1 = 75
        x2 = 75
        y2 = 75
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
         #,fill="#0000ff", width=3
        x1 = x2 
        y1 = y2
        #üstten alta dik
        y2 = y1 + 50
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        y1 = y2
        #alt
        x2 = x1 + 25
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        x1 = x2
    elif binary[0] == "1":
        #alt
        x1 = 50
        y1 = 125
        x2 = 75
        y2 = 125
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        x1 = x2 
        y1 = y2
        #alttan üste dik
        y2 = y1 - 50
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        y1 = y2
        #üst
        x2 = x1 + 25
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        x1 = x2

    for i in range(1,datarate):
        if  binary[i-1] == "0" and binary[i] == "0":
            #alttan üste dik
            y2 = y1 - 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2
            #üst
            x2 = x1 + 25
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2
            #üstten alta dik
            y2 = y1 + 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            y1 = y2
            #alt
            x2 = x1 +25
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 

        elif binary[i-1] == "1" and binary[i] == "1":
            #üstten alta dik
            y2 = y1 + 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            y1 = y2
            #alt
            x2 = x1 +25
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2
            #alttan üste dik
            y2 = y1 - 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2
            #üst
            x2 = x1 + 25
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2
            

        elif  binary[i-1] == "1" and binary[i] == "0":
            #üst
            x2 = x1 + 25
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2
            #üstten alta dik
            y2 = y1 + 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            y1 = y2
            #alt
            x2 = x1 +25
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 

        elif  binary[i-1] == "0" and binary[i] == "1":
            #alt
            x2 = x1 +25
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2
            #alttan üste dik
            y2 = y1 - 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2
            #üst
            x2 = x1 + 25
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2
 


    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

def DifMacnhester():
    binary = alinanmetin()
    datarate =alinandatarate()
    datarate = int(datarate)
    # Bit 0 için değişim //  Bit 1 için değişim yok 
    #binary = "010011"  
    w = Canvas(anapencere, width=1000, height=200)
    w.configure(background='white')
    #Bitleri çizme ekleme
    sp = 25
    for i in range (1,datarate):
        sp = sp +50
        w.create_text(sp,25,fill="red",font="Times 20 italic bold",text=binary[i-1] )
    sp += 50
    w.create_text(sp,25,fill="red",font="Times 20 italic bold",text=binary[-1] )
    #


    #
    w.pack()
    w.create_line(0,10,1000,10, dash=(4, 2))
    w.create_line(0,100,1000,100,  dash=(4, 2))
    w.create_line(0,190,1000,190,  dash=(4, 2))
    for i in range(1,20):
        w.create_line(50*i,10,50*i,190, dash=(4,2))
   # true ust 
   # fasle alt
    if binary[0] == "1":
        #baslangıc çizgisi
        x1 = 25
        y1 = 100
        x2 = 50
        y2 = 100
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        x1 = x2 
        y1 = y2
        #orta üst yarım dik
        y2 = y1 - 25
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        y1 = y2
        #üst
        x1 = 50
        y1 = 75
        x2 = 75
        y2 = 75
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
         #,fill="#0000ff", width=3
        x1 = x2 
        y1 = y2
        #üstten alta dik
        y2 = y1 + 50
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        y1 = y2
        #alt
        x2 = x1 + 25
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        x1 = x2
    elif binary[0] == "0":
        #üstten alta dik
        x1 = 50
        y1 = 75
        x2 = 50
        y2 = 125
        w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
        x1 = x2
        y1 = y2
        #alt
        x1 = 50
        y1 = 125
        x2 = 75
        y2 = 125
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        x1 = x2 
        y1 = y2
        #alttan üste dik
        y2 = y1 - 50
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        y1 = y2
        #üst
        x2 = x1 + 25
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        x1 = x2



    for i in range(1,datarate):
        if  binary[i] == "0" and y1 == 125:#curser aşağıda 1 den sonra 0 gelince
            #aşağıdan yukarıya dik
            y2 -= 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2
            #üst
            x2 = x1 + 25
            w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
            x1 = x2
            #üstten alt  dik
            y2 = y1 + 50
            w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
            y1 = y2
            #alt
            x2 +=25
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2
            y1 = y2

        elif binary[i] == "0" and y1 == 75:#curser yukarda 0dan sonra 0 gelince
            #yukardan aşağı dik
            y2 += 50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2 
            y1 = y2
            #alt
            x2 +=25
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2
            y1 = y2
            #alttan üste dik
            y2 = y1 - 50
            w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
            y1 = y2
            #üst
            x2 = x1 + 25
            w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
            x1 = x2

        elif binary[i] == "1" and y1 == 125: # curser altta
            #alt
            x2 +=25
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2
            y1 = y2
            #alttan üste dik
            y2 = y1 - 50
            w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
            y1 = y2
            #üst
            x2 = x1 + 25
            w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
            x1 = x2
        elif binary[i] == "1" and y1 == 75: # curser üstte
            #üst
            x2 = x1 + 25
            w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
            x1 = x2
            #üstten alt  dik
            y2 = y1 + 50
            w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
            y1 = y2
            #alt
            x2 +=25
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
            x1 = x2
            y1 = y2




    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

def AMI():
    # ilk 1 +v den başlar
    binary = alinanmetin()
    datarate =alinandatarate()
    #binary = "010010" 
    bayrak = True    
    w = Canvas(anapencere, width=1000, height=200)
    w.configure(background='white')
    #Bitleri çizme ekleme
    sp = 25
    for i in range (1,datarate):
        sp = sp +50
        w.create_text(sp,25,fill="red",font="Times 20 italic bold",text=binary[i-1] )
    sp += 50
    w.create_text(sp,25,fill="red",font="Times 20 italic bold",text=binary[-1] )
    #
    w.pack()
    w.create_line(0,10,1000,10, dash=(4, 2))
    w.create_line(0,100,1000,100,  dash=(4, 2))
    w.create_line(0,190,1000,190,  dash=(4, 2))
    for i in range(1,20):
        w.create_line(50*i,10,50*i,190, dash=(4,2))
    bayrak = True
   # true ust 
   # fasle alt
    if binary[0] == "1":
        #baslangıc çizgisi
        x1 = 25
        y1 = 100
        x2 = 50
        y2 = 100
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        x1 = x2 
        y1 = y2
        #ortadan üste yarım dik
        y2 = y1 -25
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        y1 = y2
        #soldan sağa 50
        x2 = x1 + 50
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        x1 = x2
        #üstten ortaya yarım dik
        y2 = y1 +25
        w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
        y1 = y2
        bayrak = False
 

    elif binary[0] == "0":
        x1 = 50
        y1 = 100
        x2 = 100
        y2 = 100
        w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
        x1 = x2
        y1 = y2



    for i in range(1,datarate):
        if  binary[i] == "1" and bayrak == True:
            #ortadan üste yarım dik
            y2 = y1 -25
            w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
            y1 = y2
            #soldan sağa 50
            x2 = x1 + 50
            w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
            x1 = x2
            #üstten ortaya yarım dik
            y2 = y1 +25
            w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
            y1 = y2
            bayrak = False

        elif binary[i] == "1" and bayrak == False:
            #ortadan aşağı yarım dik
            y2 = y1 + 25
            w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
            y1 = y2
            #soldan sağa 50
            x2 = x1 + 50
            w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
            x1 = x2
            #aşağodan ortaya yarım dik
            y2 = y1 - 25
            w.create_line(x1, y1, x2, y2 ,fill="#0000ff", width=3 )
            y1 = y2
            bayrak = True

        elif binary[i] == "0":
            x2 +=50
            w.create_line(x1, y1, x2, y2,fill="#0000ff", width=3)
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
anapencere.geometry('1000x801')

yazi=Label(anapencere)
yazi.config(text="Buraya girilen metin gelecek.")
yazi.pack()

giris=Entry(anapencere)
giris.pack()

yazi1=Label(anapencere)
yazi1.config(text="Buraya girilen data rate gelecek data rate girilen metin boyutundan büyük olamaz")
yazi1.pack()

giris1=Entry(anapencere)
giris1.pack()

buton=Button(anapencere)
buton.config(text="Unipolar")
buton.config(command=Unipolar)
buton.pack()

buton2=Button(anapencere)
buton2.config(text="NRZL")
buton2.config(command=NRZL)
buton2.pack()


buton3=Button(anapencere)
buton3.config(text="NRZI")
buton3.config(command=NRZI)
buton3.pack()

buton4=Button(anapencere)
buton4.config(text="Manchester")
buton4.config(command=Manchester)
buton4.pack()

buton5=Button(anapencere)
buton5.config(text="Dif Manchester")
buton5.config(command=DifMacnhester)
buton5.pack()

buton6=Button(anapencere)
buton6.config(text="AMI")
buton6.config(command=AMI)
buton6.pack()
anapencere.mainloop()