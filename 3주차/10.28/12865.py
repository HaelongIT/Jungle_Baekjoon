N, K = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]

dict = {}

for i in range(1, N+1):
    W, V = map(int, input().split())
    dict[i] = [W, V]

# print(dict)

# N는 물품 관련, K는 무게 관련
for l in range(1, N+1):
    for m in range(1, K+1):

        weight = dict[l][0]
        value = dict[l][1]

        if m < weight:
            dp[l][m] = dp[l-1][m]
        else:
            dp[l][m] = max(value + dp[l - 1][m - weight], dp[l-1][m])

print(dp[N][K])