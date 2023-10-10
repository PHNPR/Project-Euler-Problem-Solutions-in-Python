def collatz(n) :
    if n % 2 : 
        return 3 * n + 1
    return n // 2 

dic = {}

for i in range(2 , 1000001) : 
    count = 1 ; num = i 
    while num != 1 :
        count += 1 
        num = collatz(num)
        if num in dic : 
            count += dic[num] - 1 
            num = 1 
    dic[i] = count 

a = max(dic.values())

for k , v in dic.items() : 
    if v == a :
        print(k)
        break 