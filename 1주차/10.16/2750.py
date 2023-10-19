N = int(input())

data = []

for _ in range(N):
    A = int(input())
    data.append(A)

# print(data)

for i in range(len(data)-1):
    for index in range(len(data)-1):
        if data[index] > data[index+1]:
            data[index], data[index+1] = data[index+1], data[index]

for i in data:
    print(i)