n = int(input())
data = []

for _ in range(n):
    A = int(input())
    data.append(A)

def stairs(data):
    if len(data) <= 1:
        return data[0]
    else:
        maxStair = max(stairs(data[:-1]), stairs(data[:-2]))
    
    return maxStair + data[-1]

result = stairs(data)
print(result)