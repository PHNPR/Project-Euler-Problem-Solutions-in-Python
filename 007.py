from utils import isprime

primes = 2 

num = 5 

while True :
    if isprime(num) :
        primes += 1 
        if primes == 1e4 + 1 :
            print(num)
            break  
    if isprime(num + 2):
        primes += 1 
        if primes == 1e4 + 1 :
            print(num + 2)
            break 
    num += 6 