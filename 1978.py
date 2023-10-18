import sys

def is_primeN(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# for i in A:
#     print(i)

sum = 0
for i in range(N):
#     if A[i] == 1:
#         sum += 1

# print(sum)
    if A[i] == 1:
        continue

    if is_primeN(A[i]) == True:
        sum += 1

print(sum)