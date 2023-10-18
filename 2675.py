import sys

num = int(sys.stdin.readline())

for _ in range(num):
    A, B = sys.stdin.readline().split()

    # print(A, B)

    A = int(A)

    for j in B:
        print(j*A, end='')
    print()