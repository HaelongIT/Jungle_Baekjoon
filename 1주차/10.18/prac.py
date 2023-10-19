def set_open(input_):
    class open:
        def __init__(self, x):
            self.read = lambda: input_

        def __iter__(self):
            return iter(input_.split("\n"))
    return open

def set_input(input_):
    return iter(input_.split("\n")).__next__

input = set_input('''13
0
1
2
0
0
3
2
1
0
0
0
0
0''')
#######################

import queue

N = int(input())

data1 = 0
data2 = 0
pq = queue.PriorityQueue()

for i in range(N):
    command = int(input())

    if command == 0:
        if pq.qsize() == 0:
            print(0)
            continue
        data1, data2 = pq.get()
        print(data2)
    else:
        pq.put((-command,command))