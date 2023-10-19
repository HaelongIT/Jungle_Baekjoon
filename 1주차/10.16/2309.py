data = []

for i in range(9):
    n = int(input())
    data.append(n)

data.sort()

SumArray = sum(data)
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if SumArray - data[i] - data[j] == 100:
            for k in range(len(data)):
                if k == i or k == j:
                    pass
                else:
                    print(data[k])
            exit()