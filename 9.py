# p^2 - q^2 , 2pq , p^2 + q^2 . sum = 1000
# p*(p+q) = 500 

for i in range(1 , 25) :
    if 500 % i == 0 : 
        p = min(i , 500//i)
        q = max(i , 500//i) - p 

        if p > q : 
            print(p ,q)
            print((p**4 - q**4)*2*p*q)