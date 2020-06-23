def wam(principal, annual_interest_rate, duration):
    if annual_interest_rate == 0:
        return principal/(duration*12)
    r=(annual_interest_rate/100.0)/12.0
    n=duration*12.0
    monthly_payment= principal*(r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
    return monthly_payment
