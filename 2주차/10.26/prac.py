N, M = map(int, input().split())

# 그래프를 인접행렬로 만들기
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

print(graph)
print(visited)