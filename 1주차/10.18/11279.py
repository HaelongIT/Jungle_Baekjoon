import queue
import sys

N = int(sys.stdin.readline())

data1 = 0
data2 = 0
pq = queue.PriorityQueue()

for i in range(N):
    command = int(sys.stdin.readline())

    if command == 0:
        if pq.qsize() == 0:
            print(0)
            continue
        data1, data2 = pq.get()
        print(data2)
    else:
        pq.put((-command,command))