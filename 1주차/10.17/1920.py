n = int(input())
data = list(map(int, input().split()))
m = int(input())
data2 = list(map(int, input().split()))

# 배열 A를 정렬
data.sort()

def binary_search(data, search):
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == search:
            return 1
        elif data[mid] < search:
            left = mid + 1
        else:
            right = mid - 1

    return 0

# 배열 B의 각 요소를 이진 탐색으로 찾아 결과를 출력
for i in range(m):
    result = binary_search(data, data2[i])
    print(result)