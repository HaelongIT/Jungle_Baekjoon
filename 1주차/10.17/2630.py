import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

data = []

def sol(x,y,N):
    start = paper[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if start != paper[i][j]:
                sol(x, y, N//2)
                sol(x+N//2, y, N//2)
                sol(x, y+N//2, N//2)
                sol(x+N//2, y+N//2, N//2)
                return

    if start == 1:
        data.append(1)
    else:
        data.append(0)
    
sol(0,0,N)

print(data.count(0))
print(data.count(1))