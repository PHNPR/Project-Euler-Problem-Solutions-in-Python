from utils import isprime 

ans = 5 ; i = 5 ; c = 2 

while i < 2 *(10**6) :
    if isprime(i) :
        ans += i 
        c += 1 
    if isprime(i+2) :
        ans += i+2
        c += 1 
    i += 6 

print(ans , c) 