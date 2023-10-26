def count_connected_components(graph):
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    num_nodes = len(graph)
    num_components = 0

    for node in range(num_nodes):
        if not visited[node]:
            dfs(node)
            num_components += 1

    return num_components

def create_graph(rows, cols):
    graph = []

    for _ in range(rows):
        line = input()
        row = []
        for char in line:
            if char == '-':
                row.append(0)  # 가로(-)를 0로 매핑
            elif char == '|':
                row.append(1)  # 세로(|)를 1로 매핑
        graph.append(row)

    return graph

# 입력 받기
rows, cols = map(int, input().split())
visited = [False] * (rows * cols)  # visited 초기화
graph = create_graph(rows, cols)

# 연결된 그래프 수 세기
num_components = count_connected_components(graph)
print("Number of connected components:", num_components)
