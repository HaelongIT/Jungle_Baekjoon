# import sys

# # 최소 스패닝 트리
# # 유니온 파인드


# # 부모 노드 찾기
# def find(a):
#     if a == parent[a]:
#         return a
#     # 부모 찾았으면 리턴(베이스케이스)

#     parent[a] = find(parent[a])
#     # 분해

#     return parent[a]
#     # 조합

# # 베이스케이스 : 부모와 정점이 같을때 그 정점 리턴
# # 분해 : 점점 부모와 정점이 같은 곳에 가까워짐
# # 조합1 : 1개 위일 때 : 베이스케이스 리턴 받으면 그게 곧 부모
# # 조합2 : 3개 위일 때 : 베이스케이스 리턴 받으면 그게 곧 부모


# # 트리 합치기
# def union(a, b):
#     a = find(a)
#     b = find(b)
#     # 두 정점의 부모를 찾고

#     # 작은 루트 노드를 기준으로 합침
#     if b < a:
#         parent[a] = b
#     else:
#         parent[b] = a


# v, e = map(int, sys.stdin.readline().split())
# # v : 정점의 갯수
# # e : 간선의 갯수

# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(e)]
# # 간선의 갯수 만큼 돌면서 2차원으로 graph에 저장(정점1, 정점2, 가중치)

# graph.sort(key=lambda x: x[2]) 
# # 간선들을 가중치 기준으로 정렬시킨다.

# parent = [i for i in range(v+1)]
# # parent는 일단 정점의 갯수보다 하나더 만든다
# # (입력하는 사람이 정점0부터 시작하거나 1부터 시작하거나 둘다 대비)

# answer = 0

# # 반복문을 통해 간선들의 두 정점을 확인
# for s, e, w in graph:
#     # 부모 노드가 같지 않다면 스패닝 트리!
#     # (부모가 같은데 연결하면 사이클 형성)
#     if find(s) != find(e):
#         union(s, e) # 두 노드를 합친다.
#         answer += w

# print(answer)

################################################

import sys

# 베이스케이스 : p_find(a) == a 일 때
# 분해 : 부모를 타고 올라가기
# 결합 : 베이스케이스의 리턴값

def p_find(N):
    if parent[N] == N:
        return N
    
    else:
        parent[N] = p_find(parent[N])
        return parent[N]
    
def union(a, b):
    if p_find(a) > p_find(b):
        parent[p_find(a)] = p_find(b)
    else:
        parent[p_find(b)] = p_find(a)

v, e = list(map(int, sys.stdin.readline().split()))

data = []
for _ in range(e):
    N = list(map(int, input().split()))
    data.append(N)
data.sort(key= lambda x:x[2])

parent = []
for i in range(v+1):
    parent.append(i)


weight = 0
for start, end, cost in data:
    if p_find(start) != p_find(end):
        union(start, end)
        weight = weight + cost
    
print(weight)