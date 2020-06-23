def zarib3or5(x):
    sum_number=0
    for i in range (1,x):
        #print("i is : -->",i)
        if i % 3 == 0 or i % 5 == 0:
           
            sum_number+=i
            #print(i," sum number is ---> ",sum_number)
            
    return sum_number