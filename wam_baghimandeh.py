def wam(principal, annual_interest_rate, duration , number_of_payments):
    p=float(number_of_payments)
    if annual_interest_rate == 0:
        return principal*((n/n)-(p/(duration*12)))
    r=(annual_interest_rate/100.0)/12.0
    n=duration*12
    remainingloanbalance= principal*((1+r)**n-(1+r)**p)/(float((1.0+r)**n)-1.0)
    return remainingloanbalance
