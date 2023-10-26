import sys
input = sys.stdin.readline
#recursion error 방지
sys.setrecursionlimit(10**9)

arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break


def solution(A):
    # 받은 배열 길이가 0이면 return
    if len(A) == 0:
        return

    tempL, tempR = [], []
    # 첫번째 값을 루트 노드로 설정
    mid = A[0]
    # 나머지 배열에 대해 for문을 돌면서 루트보다 커지는 부분을 기록해서 L과 R로 나눈다.
    for i in range(1, len(A)):
        if A[i] > mid:
            tempL = A[1:i]
            tempR = A[i:]
            break
    else:
    	#모두 mid보다 작은 경우
        tempL = A[1:]
    
    #왼쪽, 오른쪽 순으로 재귀 후 루트 노드 값 출력
    solution(tempL)
    solution(tempR)
    print(mid)

solution(arr)


#########################################

# 1. 베이스케이스 : []이면 return

# 2. 분해 : 점점 트리가 쪼개지게(왼/루트/오른)

# 3. 조합
# 3-1. 한 단계 위일 때 답을 생각해보기 : '* - 60 - *' 으로 왼쪽서브트리와 오른쪽서브트리가 비어있으면 
# 빈 배열인 * 에서 return 찍히면서 (.)/(.)/60 출력 [왼 - 오 - 루트 순서로 출력] 
# 3-2. 3단계 위일 때 답을 생각해보기 : '30이 루트' 일때 (.)/(.)/5/(.)/(.)/45/30
# 공통점 : 왼쪽(재귀) - 오른쪽(재귀) - 루트출력

# *. 베이스케이스 최적화 : 없음

# 코드 작성 : 베이스케이스 -> 분해/조합

##############################################
# 전위 순회 결과를 리스트에 입력한 상황

def sol(data_list):
    if len(data_list) == 0:
        return
    
    # 분해 로직 : 전위순회를 리스트로 입력받은걸 root/left/right로 나눠줘야 함
    # (어떻게 data_list에서 data_left/data_right/root를 나눌지 분해 알고리즘)
    data_left = []
    data_right = []
    root = data_list[0]

    for i in range(1, len(data_list)):
        if root < data_list[i]:
            data_left = data_list[1:i]
            data_right = data_list[i:]
            break

    else:
        data_left = data_list[1:]

    # (if문과 else문 사이에 다른 로직이 들어가면 else문에서 오류가 나온다)
    # 조합
    sol(data_left)
    sol(data_right)
    print(root)