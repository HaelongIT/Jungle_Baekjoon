import sys

def is_primeN(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def Gold(N):
    I = 0
    J = 0
    for i in range(2,int(N/2)+1):
        j = N - i
    if is_primeN(i) and is_primeN(j):
        I = i
        J = j
    print(I, J)

N = int(sys.stdin.readline())
    

# for i in range(N):
#     G = int(sys.stdin.readline())
#     # print(G)

#     # 주어진 G라는 변수에 들어있는 정수에 대해 '골드바흐 파티션'을 추측해야 함
#     Gold(G)

list = [input() for _ in range(N)]
# print(list)

for M in list:

    M = int(M)
    I = 0
    J = 0

    for i in range(2,int(M/2)+1):
        
        j = M - i

        if is_primeN(i) and is_primeN(j):
            I = i
            J = j

    print(I, J)