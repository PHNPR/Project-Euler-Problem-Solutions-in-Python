i = 30 

while True :
    num = (i * i + i) // 2 
    count = 0 
    for j in range(1 , int(num ** 0.5 + 0.5) + 1) : 
        if num % j == 0 : 
            count += 1 
    if count >= 250 :
        print(num , count , i)
        break 
    i += 1 

# num = 76576500
# divs = []

# for i in range(1 , num + 1) : 
#     if num % i == 0 :
#         divs.append(i)

# print(len(divs) , divs)