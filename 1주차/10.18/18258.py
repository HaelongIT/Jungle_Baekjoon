from collections import deque
import sys

data_queue = deque()

N = int(sys.stdin.readline())

for i in range(N):
    command = list(sys.stdin.readline().split())
    if len(command) == 2:
        command[1] = int(command[1])
        data_queue.append(command[1])
    else:
        if command[0] == 'pop':
            if len(data_queue) == 0:
                print(-1)
            else:
                print(data_queue.popleft())
        elif command[0] == 'size':
            print(len(data_queue))
        elif command[0] == 'empty':
            if len(data_queue) == 0:
                print(1)
            else:
                print(0)
        elif command[0] == 'front':
            if len(data_queue) == 0:
                print(-1)
            else:
                print(data_queue[0])
        elif command[0] == 'back':
            if len(data_queue) == 0:
                print(-1)
            else:
                print(data_queue[-1])