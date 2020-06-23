def even(arr):
    count=0
    for i in range(0,len(arr)):
        element=arr[i]
        
        if(element%2!=0):
            count=count+element
    return count
a=[2,4,6]
even(a)
