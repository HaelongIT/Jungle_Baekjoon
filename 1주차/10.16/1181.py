import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())

set_lst = set(lst)
lst = list(set_lst)
# 중복 제거

lst.sort()
# 알파벳 순으로 정렬
lst.sort(key = len)
# 문자열 길이 순으로 정렬

for i in lst:
    print(i)