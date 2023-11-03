import sys
sys.stdin=open("test.txt")
input = sys.stdin.readline

T=int(input())
for _ in range(T):
    N=int(input())
    L=[ [0,0] for i in range(N) ]
    for i in range(N):
       L[i][0],L[i][1] = map(int,sys.stdin.readline().split())
    L.sort()

    new_worker=0
    max_rank=L[0][1]
    
    for i in range(N):
        if L[i][1] <= max_rank:
            new_worker += 1
            max_rank=L[i][1]
    print(new_worker)