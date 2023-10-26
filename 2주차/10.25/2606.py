n = int(input())
m = int(input())

#################################
def dfs(graph, v, visited):
    # print(v)
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i, visited)
#################################

graph = []

for _ in range(n+1):
    graph.append([])

# print(graph)

for _ in range(m):
    s, e = map(int, input().split())

    graph[s].append(e)
    graph[e].append(s)

# print(graph)

visited = [False] * (n+1)

#####################################

dfs(graph, 1, visited)

# print(visited)

cnt = 0

for i in range(2,n+1):
    # print(visited[i])
    if visited[i] == True:
        cnt = cnt + 1
print(cnt)