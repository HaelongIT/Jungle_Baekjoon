a = [1,2,3,4,5]

def solve(a: list):
    # print(a)

    sum = 0

    for i in a:
        sum = sum + i
    
    return sum

print(solve(a))

# 문제 : 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

# 입력 : 리스트 a
# 출력 : 리스트 내 있는 모든 정수들의 총합
# 알고리즘 : 