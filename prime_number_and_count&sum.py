#code by Meraj Bighamian
#prime number of 2 to 1000
#function for check prime numbers
def prime_number(x):
    #the variable of count prime number
    prime_count=0
    #the variable of sum all prime number
    prime_sum=0
    #the loop is counter 2 to 1000
    for j in range(2,x+1):
        primenumber=True
        #print("--->",j) //unit test
        #loop for counter number 2 to square root variable j
        for i in range(2,int(j**0.5)):
            #check of prime number
            if j%i==0:
                #print("number not prime -->",j,"i : ",i)
                primenumber=False
                break
        #print("result --> ",primenumber) //unit test
        #if number we is prime number run bottom code
        if(primenumber):
            print(j,"is prime number")
            prime_count+=1
            prime_sum+=j
        #if number we is not prime number run bottom code
        else:
            print(j,"is not prime number")
    # out put of my code
    print("sum of count",prime_count," ","sum of value prime ",prime_sum)
    
    
#code by Meraj Bighamian