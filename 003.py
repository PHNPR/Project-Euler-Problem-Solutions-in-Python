from utils import isprime 

num = 600851475143 
divs = []

for i in range(2 , int(num ** 0.5 + 0.5) + 5) :
    if num % i == 0 :
        divs.append(i)
        divs.append(num // i)

divs.sort(reverse = True)

for i in divs :
    if isprime(i) :
        print(i)
        break 