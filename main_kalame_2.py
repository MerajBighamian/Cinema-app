m="""The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship. 
This video was captured by one of our heroes who wishes peace."""
char=0
counter=int(m.count("."))
for i in range(0,counter):
    #print(i)
    print("char is ------>",char)
    char=m.find(".")
    print("char is ------>",char)
    m=m[char].replace("."," ")
    print("char is ------>",char)
    m=m[char].lower()
    print("char is ------>",char)
    char+=2
    print("char is ----------------->",char)
