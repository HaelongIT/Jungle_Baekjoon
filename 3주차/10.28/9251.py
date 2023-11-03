# 9251 LCS
S1 = list(input())
S2 = list(input())
# 문자열을 입력받아서 각 문자별로 리스트에 저장

len1 = len(S1)
len2 = len(S2)
# 각 길이를 저장

dp = [[0]*(len2 + 1) for _ in range(len1+1)]
# 메모이제이션할 공간 만들기(하나씩 더 공간을 만드는 이유 : 처음 시작하는 0000으로 시작하는 세로와 가로를 세팅하기 위해서)
# print(dp)

for i in range(1,len1 + 1) :
    for j in range(1,len2 + 1) :
        if S1[i-1] == S2[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
# 표로 설명

# print(dp)

print(dp[len1][len2])