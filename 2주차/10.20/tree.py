class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# 루트노드 만들기

def insert(root, value):
    new_node = Node(value)
    # 삽입할 노드 생성

    if root is None:
        return new_node
    # 만약 루트노드가 없는 상태면 삽입할 노드가 루트노드가 된다

    current_node = root
    # 노드의 탐색 위치 확인

    while current_node:
    
        if value < current_node.value:
        # 만약 해당노드보다 삽입할 노드가 작다면
            if current_node.left is None:
            # 해당노드의 왼쪽이 비어있다면
                current_node.left = new_node
                # 해당노드의 왼쪽 간선에 연결
                break

            current_node = current_node.left
            # 해당노드의 왼쪽으로 이동
        else:
        # 만약 해당노드보다 삽입할 노드가 크다면
            if current_node.right is None:
            # 해당노드의 오른쪽이 비어있다면
                current_node.right = new_node
                # 해당노드의 오른쪽 간선에 연결
                break
            current_node = current_node.right
            # 해당노드의 오른쪽으로 이동

    return root
    # 삽입했으면 그 트리를 리턴

def search(root, value):

    current_node = root
    # 노드 탐색 위치 확인

    while current_node:

        if current_node.value == value:
        # 찾았을 경우 True 리턴
            return True
        
        elif value < current_node.value:
        # 만약 해당노드보다 삽입할 노드가 작다면

            current_node = current_node.left
            # 왼쪽으로 이동
        else:
        # 만약 해당노드보다 삽입할 노드가 크다면
            current_node = current_node.right
            # 오른쪽으로 이동
    return False
    # 결국 못찾은 경우 False 리턴

def find_min_value_node(node):
    current = node
    # 찾기 시작하는 노드

    while current.left is not None:
    # 노드의 왼쪽 자식노드가 있는 동안 반복
        current = current.left
        # 왼쪽으로 내려가기
    return current
    # 가장 작은값(제일 왼쪽노드) 찾았으면 리턴

def delete(root, value):
    if root is None:
    # 만약 루트노드가 없는 상태면 None을 반환(베이스 케이스 부분)
        return root

    if value < root.value:
    # 루트노드보다 삭제할 값이 작다면
        root.left = delete(root.left, value)
        # 왼쪽 부분에서 삭제해서 가져와라(재귀)

    elif value > root.value:
    # 루트노드보다 삭제할 값이 크다면
        root.right = delete(root.right, value)
        # 오른쪽 부분에서 삭제해서 가져와라(재귀)
    else:
    # 삭제할 값을 찾았다면(자식이 하나인 경우 + 없는 경우)
        if root.left is None:
        # 삭제할 값의 왼쪽이 비어있다면
            return root.right
            # 1. 자식이 하나 있을 경우 대체(대체되면서 삭제)
            # 2. 자식이 없을 경우 None이 들어가면서 삭제됨
        elif root.right is None:
        # 위의 상황의 오른쪽 버전
            return root.left

        # 삭제하려는 노드가 두 개의 자식 노드를 가지는 경우
        # 오른쪽 서브트리에서 가장 작은 값을 찾아서 현재 노드의 값을 갱신합니다.
        root.value = find_min_value_node(root.right).value

        # 오른쪽 서브트리에서 최소값을 가진 노드를 삭제합니다.(재귀)
        # (이미 삭제할 부분으로 이동했기 때문에 기존에 있던건 삭제해야됨)
        root.right = delete(root.right, root.value)

    return root
    # 삭제 완료했으면 그 트리상태를 리턴

##################################################################

root = Node(5)  # 루트 노드를 값 5로 초기화

root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 6)
root = insert(root, 8)

result = search(root, 3)  # 6을 찾아봅니다.
if result:
    print("6을 찾았습니다.")
else:
    print("6을 찾지 못했습니다.")

root = delete(root, 3)  # 3을 삭제합니다.
root = delete(root, 7)  # 7을 삭제합니다.