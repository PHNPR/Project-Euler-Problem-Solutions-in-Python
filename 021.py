dic = {1 : 1 , 2 : 3 , 3 : 4 , 4 : 7}

for i in range(5 , 10001) :
    temp = 0 
    for j in range(1 , int(i ** 0.5 + 1.5)) : 
        if i % j == 0 :
            temp += (j + i //j) if j != i // j else j 
    dic[i] = temp - i  

ans = 0 

for k , v in dic.items() :
    if v in dic and v != k:
        if dic[v] == k :
            ans += k + v 

print(ans // 2)