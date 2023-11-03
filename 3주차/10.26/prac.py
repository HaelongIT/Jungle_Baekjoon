dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for index in range(3, 1001):
    dp[index] = dp[index - 1] + dp[index - 2]
print (dp[2] % 10007)
print (dp[9] % 10007)