a = b = 1 
eves = 0

while b < 4e6 :
    a , b = b , a + b
    eves += b if b % 2 == 0 else 0

print(eves)