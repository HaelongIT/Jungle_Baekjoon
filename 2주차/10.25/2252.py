from collections import deque

N, M = map(int, input().split())
# N은 정점의 갯수, M은 간선의 갯수

need = deque()

graph = []
for _ in range(N+1):
    graph.append([])

inD = [0] * (N + 1)
inD[0] = -1

##################################
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    inD[end] = inD[end] + 1

for i in range(1, N+1):
    if inD[i] == 0:
        need.append(i)

while need:
    v = need.popleft()
    print(v, end=' ')

    for j in graph[v]:
        inD[j] = inD[j] - 1

        if inD[j] == 0:
            need.append(j)