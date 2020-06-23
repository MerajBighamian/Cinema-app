#calculate scores
scores = [["hasan",18,12,13],["mahdi",20,19,18],["meraj",17,18,10]]

for person in scores:
    total=0
    for value in range(1,len(person)):
        total+=person[value]
    avg=total/(len(person)-1)
    print(person[0],avg)
    
    