data = int(input())

data = str(data)
data = list(data)

# 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고
if len(data) == 1:
    data.append('0')
    data[0], data[1] = data[1], data[0]

# 반복문에서 'data[0] != ans1 or data[1] != ans2' 조건 설정을 위해서 ans1과 ans2로 입력값 저장
ans1 = data[0]
ans2 = data[1]
cnt = 0

################################################
    
# 첫번째 실행 진행
num1 = int(data[0])
num2 = int(data[1])
num3 = num1 + num2

# num3가 두자리 숫자(10이상)가 되면 1의자리만 취하기 위한 부분
if num3 >= 10:
    num3 = str(num3)
    num3 = list(num3)
    num3 = num3[1]
    num3 = int(num3)

data[0] = str(num2)
data[1] = str(num3)
cnt += 1

# 반복문에서 두번째 실행부터 진행(다시 입력받았던 숫자가 될때까지 반복)
while data[0] != ans1 or data[1] != ans2:
    num1 = int(data[0])
    num2 = int(data[1])
    num3 = num1 + num2

    if num3 >= 10:
        num3 = str(num3)
        num3 = list(num3)
        num3 = num3[1]
        num3 = int(num3)

    data[0] = str(num2)
    data[1] = str(num3)
    
    cnt += 1

    # print(data[0], data[1])

print(cnt)