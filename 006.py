def solve(n) :
    return ((n*n +n)//2) ** 2 - (n*(n+1)*(2*n+1))//6

print(solve(10))
print(solve(100))