# 1. 베이스케이스 : 마지막 원판 하나 남았을 때 옮기는 경우 : print(start, end)

# 2. 분해 : 원판 갯수 (n-1)개로 내리기

# 3. 조합
# 3-1. 한 단계 위일 때 답을 생각해보기 :  
# 3-2. 3단계 위일 때 답을 생각해보기 : 
# 공통점 : 1. 위에것들 mid로 옮기기(재귀) 2. 맨밑것 end로 옮기기 3. 위에것들 end로 옮기기(재귀)

# *. 베이스케이스 합치기 : 없음

# 코드 작성 : 베이스케이스 -> 분해/조합

def hanoi(n, start, end):
    mid = 6-start-end

    if n == 1:
        print(start, end)
        return
    else:
        hanoi(n-1, start, mid)
        print(start, end)
        hanoi(n-1, mid, end)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)
