N = int(input())

data = []

for _ in range(N):
    temp = int(input())
    data.append(temp)
    
data.sort()

for i in range(N):
    print(data[i])