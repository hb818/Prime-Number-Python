def prime_checker(number):
    is_prime = True
    i=2
    while(is_prime==True and i<number):
        if(number%i==0):
            is_prime=False
        i+=1
    if(is_prime==True):
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
