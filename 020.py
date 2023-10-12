pro = 1 

for i in range(2 , 101) :
    pro *= i 
    while not pro % 10  :
        pro //= 10 

a = str(pro)

ans = 0 

for i in a :
    ans += int(i)

print(ans)