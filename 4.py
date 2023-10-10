ans = 100

for i in range(999 , 99 , -1) :
    for j in range(999 , 99 , -1) : 
        a = i * j 
        if str(a) == str(a)[::-1] :
            if a > ans :
                ans = a 

print(ans)