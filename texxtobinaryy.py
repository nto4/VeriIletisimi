metin ='abc'
def coder(list):
    list = [] 
    list[:0] = metin
    ascilist = []
    #print(ord(metin[0]))
    #print(len(list))
    for i in range(0,len(list)):
        ascilist.append(ord(metin[i]))
    print(ascilist)
    return ascilist

print(coder(metin))