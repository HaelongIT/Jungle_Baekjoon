from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M = list(map(int, input().split()))

graph = []
for _ in range(N+1):
    graph.append([])

for i in range(M):
    s, e = list(map(int, input().split()))
    graph[s].append(e)
    graph[e].append(s)

count = 0 # 연결 노드의 수
visited = [False] * (N+1)

for i in range(1, N+1):
    if not visited[i]:
        bfs(graph, i, visited) # bfs 한 번 끝날 때마다 count+1
        count += 1

print(count)