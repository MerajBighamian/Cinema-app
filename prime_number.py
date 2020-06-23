#Module of prime number
#prime number of 1 to 1000
def prime_number(x):
    primenumber=True
    for i in range(2,x):
        if x%i==0:
            primenumber=False
            break
    # return primenumber
    if(primenumber):
        print("this is a prime number")
    else:
        print("this is not prime number")
        
      