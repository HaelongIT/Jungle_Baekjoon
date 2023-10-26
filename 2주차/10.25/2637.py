# N : 1~(N-1)까지 기본부품과 중간부품의 번호, N은 완제품의 번호
# M : M번 부품의 관계가 반복문
# 부품의 관계(X, Y, K) : X를 만드는데 부품(Y)이 K개 필요함

N = int(input())
M = int(input())

graph = []
for _ in range(N+1):
    graph.append([0] * (N + 1))

for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[Y][X] = K

print(graph)