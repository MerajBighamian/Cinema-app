
def int_num(num):
    x=0
    for i in range(1,num):
        if num%i==0:
            x=x+i
    if x==num:
        return True
    else:
        return False
