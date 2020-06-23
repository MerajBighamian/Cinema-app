def int_number(a):
    new=[]
    max = a[0]
    for i in range (0,len(a)):
        if a[i]>max:
            max=a[i]
            new.append(max)
    return max
print("done")