# import sys

# N = int(sys.stdin.readline())

# data = []

# for i in range(N):
#     command = int(sys.stdin.readline())

#     if command == 0:
#         data.sort()
#         # print(data)
#         if len(data) == 0:
#             print(0)
#             continue
#         print(data.pop())

#     data.append(command)



N = int(input())

data = []

for i in range(N):
    command = int(input())

    if command == 0:
        if len(data) == 0:
            print(0)
            continue
        print(max(data))
        data.remove(max(data))

    data.append(command)