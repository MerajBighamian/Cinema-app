m="""The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship. 
This video was captured by one of our heroes who wishes peace."""

m=m.split(".")
m=m.split()
for item in range(0,len(m)):
    if m[item][0].isupper()and m[item] != "The" and m[item] != "This" and m[item] != "That" :
        m[item]=m[item].rstrip(".")
        print(item+1,":",m[item])
    else:
        
            
