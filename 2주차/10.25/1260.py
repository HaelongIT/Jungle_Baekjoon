from collections import deque

N, M, V = list(map(int, input().split()))

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    graph[v].sort()

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    need = deque([start])
    visited[start] = True

    while need:
        v = need.popleft()
        print(v, end=" ")
        
        graph[v].sort()

        for i in graph[v]:
            if not visited[i]:
                need.append(i)
                visited[i]= True

graph = []

for _ in range(N+1):
    graph.append([])

for i in range(M):
    s, e = list(map(int, input().split()))
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (N+1)
visited2 = [False] * (N+1)

dfs(graph, V, visited)
print()
bfs(graph, V, visited2)