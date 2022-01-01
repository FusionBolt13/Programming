def isPrime(number):
    
    for divisor in range(2, number - 1):
        if number % divisor == 0:
            return False
        else:
            divisor = divisor + 1
    return True

for x in range(1000000):
    if isPrime(x):
        print(x)