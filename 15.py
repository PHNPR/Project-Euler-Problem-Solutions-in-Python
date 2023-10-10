dp = [[1 for _ in range(21)] for _ in range(21)]

for i in range(1 , 21) : 
    for j in range(1 , 21) :
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1])