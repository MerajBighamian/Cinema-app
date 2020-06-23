principal=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))
def program_wam(principal, annual_interest_rate, duration):
    def wam(principal, annual_interest_rate, duration):
        if annual_interest_rate == 0:
            return principal/(duration*12)
        r=(annual_interest_rate/100.0)/12.0
        n=duration*12.0
        monthly_payment= principal*(r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
        return monthly_payment
    monthly_payment=float(wam(principal, annual_interest_rate, duration))

    def wam_balnced(principal, annual_interest_rate, duration , number_of_payments):
        p=float(number_of_payments)
        if annual_interest_rate == 0:
            return principal*((n/n)-(p/(duration*12.0)))
        r=(annual_interest_rate/100.0)/12.0
        n=duration*12.0
        remainingloanbalance= principal*((1+r)**n-(1+r)**p)/(float((1.0+r)**n)-1.0)
        return remainingloanbalance
    print("LOAN AMOUNT:",int(principal),"INTEREST RATE (PERCENT):",int(annual_interest_rate))
    print("DURATION (YEARS):",int(duration),"MONTHLY PAYMENT:",int(monthly_payment))
    count=float(principal/(monthly_payment*12))
    i=0
    x=0
    number_of_payments=12.0
    while count+1>i:
        x=x+(monthly_payment*12.0)
        baghi_mande_wam=float(wam_balnced(principal, annual_interest_rate, duration , number_of_payments))
        number_of_payments=number_of_payments+12.0
        i=i+1.0
        print("YEAR:",int(i),"BALANCE:",int(baghi_mande_wam),"TOTAL PAYMENT",int(x))
program_wam(principal, annual_interest_rate, duration)
