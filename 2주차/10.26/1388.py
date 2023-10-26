from collections import deque

N, M = map(int, input().split())

# 그래프 만들기
graph = []
for _ in range(N):
    data = list(input())
    graph.append(data)

# 방문했는지 안했는지 확인용
visited = []
for _ in range(N):
    visited.append([])
for i in range(N):
    visited[i].append([False] * M)

# print(graph)
# print(visited)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    need = deque()
    need.append((x,y))
    visited[x][y] = True
    cnt = 0

    while need:
        x, y = need.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if graph[x][y] == '-':
                pass
            
            else:
                pass
        
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                bfs(i, j)
                cnt += 1

#######################################

