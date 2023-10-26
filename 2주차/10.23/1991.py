# import sys

# N = int(sys.stdin.readline().strip())
# tree = {}

# for n in range(N):
#     root, left, right = sys.stdin.readline().strip().split()
#     tree[root] = [left, right]

# def preO(root):
#     if root == ".":
#         return
#     else:
#         print(root, end='')
#         preO(tree[root][0])
#         preO(tree[root][1])

# preO('A')

###########################################

# 1. 베이스케이스 : preO(.)이면 출력없음 -> (.), 루트(G) 하나만 있으면 -> G/(.)/(.)

# 2. 분해 : 점점 갈수록 탐색 범위가 줄어들게

# 3. 조합
# 3-1. 한 단계 위일 때 답을 생각해보기(preO(F)이면 -> F/(.)/G(.)(.))
# 3-2. 3단계 위일 때 답을 생각해보기(preO(C)이면 -> C/E(.)(.)/F(.)G(.)(.))
# 3-공통점 : 루트노드 출력/왼쪽재귀/오른쪽재귀

# * 베이스케이스 합치기 : 사실 '루트(G) 하나만 있으면 -> G/(.)/(.)'은 베이스케이스가 아니였음

# 코드 작성 : 베이스케이스 -> 분해/조합

import sys

N = int(sys.stdin.readline().strip())
tree = {}

for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

def preO(root):
    if root == '.':
        return
    else:
        print(root, end='')
        # preO(root.left)
        # preO(root.right)
        preO(tree[root][0])
        preO(tree[root][1])

preO('A')