def show_jazr(number):
    error = 0.01
    guess = number/2
    iteration = 0

    while(abs(number-guess**2)>error):
        iteration=iteration+1
        taghsim = number/guess
        guess = (taghsim+guess)/2
    print("The square root of",number,"is",guess)
