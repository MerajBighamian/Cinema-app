n=int(input())
n1=(n//3)-1
n2=(n//3)
n3=(n//3)+1
count=1
valid=True
if n <= 90000 and n >= 1:
    if n1+n2+n3 == n:
        if ((n1**2)+(n2**2)) == (n3**2):
            print(n1,n2,n3)
        elif valid:
            while count<2:
               n1=n1+3
               n2=n2//2
               n3=n3+2
               count+=1
            if ((n1**2)+(n2**2)) == (n3**2):
                print(n2,n1,n3)
            else:
                print('Impossible')
                
        else:
            print('Impossible')
    else:
        print('Impossible')
            

            
