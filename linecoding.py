"""import flask
import time

from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
"""
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
#decode
def decode(ascilist):
    metin2 = ""
    for i in range(0,len(ascilist)):
        #print(i)
        metin2 += chr(ascilist[i])
    print(metin2)

#ascilist=coder(metin)
#decode(ascilist)


def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

s = 'ü'
b = string2bits(s)
s2 = bits2string(b)
#print(type(b))
str1 = ''.join(b)
#print(str1)
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
#unipolar(str1)
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
#print("")
#print(str1)
#NRZL(str1)

def NRZI(str1):
    state = int(str1[0])
    if int(str1[0]) == 1:
        print("|¯¯",end="")
    if int(str1[0]) == 0:
        print("__",end="")
    #print("diziboyut= ",end="")
    #print(len(str1))
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
        #print(i)
#NRZI(str1)
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
                #print(int(str1[i]))
                
    print("          ")

#Manchester(str1)

#print(str1)

def DifManchester(str1):
    #print(len(str1))
    if int(str1[0]) == 0:
        print("|_|¯",end="")
    elif int(str1[0]) == 1:
        print("¯|_",end="")
        #print("ilk rakam 1")


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
                #print(int(str1[i]))
                
    print("          ")
#+v den baslıyor 
#str3= "1011"
print(str3)
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
        
AMI(str3)
"""
app = flask.Flask(__name__)

@app.route('/yield')
def index():
    def inner():
        for x in range(100):
            time.sleep(1)
            yield '%s<br/>\n' % x
    env = Environment(loader=FileSystemLoader('templates'))
    tmpl = env.get_template('result.html')
    return flask.Response(tmpl.generate(result=inner()))

app.run(debug=True)
"""
#print(s2)
#Unipolar(non-return-to-zero)
