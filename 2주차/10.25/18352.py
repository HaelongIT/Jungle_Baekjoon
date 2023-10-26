from collections import deque

N, M, K, X = map(int, input().split())
# 입력 ; 도시 갯수 : N개, 도로 갯수 : M개, 거리정보 : K, 출발 도시 번호 : X도시
# 출력 ; X에서 출발하여 거리가 K인 도시들의 번호를 출력

graph = []

for _ in range(N+1):
    graph.append([])

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

# print(graph)

visited = [False] * (N + 1)

distance = [0] * (N + 1)

###################################

def bfs(graph, start, visited):
    need = deque([start])
    visited[start] = True

    answer = []

    while need:
        v = need.popleft()
        # print(v)

        for i in graph[v]:
            if not visited[i]:
                need.append(i)
                visited[i] = True

                distance[i] = distance[v] + 1
                if distance[i] == K:
                    answer.append(i)
    
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in range(len(answer)):
            print(answer[i])

bfs(graph, X, visited)