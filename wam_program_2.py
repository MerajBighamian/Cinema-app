def calculate_payment_wam(principal, annual_interest_rate, duration):
    if annual_interest_rate==0:
        return principal/(duration*12)
    r=(annual_interest_rate/100)/12
    n=duration*12
    montly_payment_wam=principal*(r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
    return montly_payment_wam
# Your function for calculating remaining balance goes here
def calculate_balance_wam(principal, annual_interest_rate, duration, number_of_payments):
    if annual_interest_rate==0:
        return principal-number_of_payments*(principal/(duration*12.0) )   
    r=(annual_interest_rate/100)/12.0
    n=duration*12
    balance_wam=principal*((1.0+r)**n-(1.0+r)**number_of_payments)/(float((1.0+r)**n)-1.0)
    return float(balance_wam)
# Your main program goes here
principal=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))    
monthly_payment_wam=calculate_payment_wam(principal, annual_interest_rate, duration)
print('LOAN AMOUNT:',principal,'INTEREST RATE (PERCENT):', annual_interest_rate)
print('DURATION (YEARS):',duration,'MONTHLY PAYMENT:',int(monthly_payment_wam))
for year_number in range(1,1+duration):
    count=calculate_balance_wam(principal, annual_interest_rate, duration, year_number*12)
    print('YEAR:', year_number, 'BALANCE:', int(count), 'TOTAL PAYMENT', int(monthly_payment_wam*year_number*12))
