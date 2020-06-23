def primenumber(n):
        is_prime_number = True
        for counter in range(2,n):
            if(n%counter==0):
                is_prime_number = False
                break
        if(is_prime_number):
            return True
        elif(is_prime_number==False):
            return False
            
