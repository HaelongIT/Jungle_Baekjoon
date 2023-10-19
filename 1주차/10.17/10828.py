import sys

N = int(sys.stdin.readline())

data = []

def push(N):
    data.append(N)

def pop():
    if len(data) == 0:
        return -1
    return data.pop()

def size():
    return len(data)

def empty():
    if len(data) == 0:
        return 1
    else:
        return 0

def top():
    if len(data) == 0:
        return -1
    else:
        return data[-1]

for i in range(N):
    com = sys.stdin.readline().split()
    command = com[0]

    if com[0] == 'push':
        push(int(com[1]))
    elif com[0] == 'pop':
        print(pop())
    elif com[0] == 'size':
        print(size())
    elif com[0] == 'empty':
        print(empty())
    elif com[0] == 'top':
        print(top())