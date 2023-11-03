N = int(input())

A = list(map(int, input().split()))

curr = A[0]
cnt = 0

# A[i]

for i in range(N):
    for j in range(i+1, N):
        if A[i] >= A[j]:
            continue
        curr = A[i]
        if curr < A[j]:
            cnt += 1
            break

print(cnt)