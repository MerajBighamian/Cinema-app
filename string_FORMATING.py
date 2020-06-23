#this display scorse
scores=[
        ["meraj",12,15,4,7,2],
        ["mehdi",19,19,19,20],
        ["maryam",15,18,18,17]] 
for person in scores:
    for item in person:
        if type(item) == str:
            print(" {0:12s} |".format(item),end="")
        else:
            print(" {0:7.2f} |".format(item),end="")
        
    print()
