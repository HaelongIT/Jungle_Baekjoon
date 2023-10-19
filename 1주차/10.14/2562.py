import sys

numbers = []

for _ in range(9):
    number = int(sys.stdin.readline())
    numbers.append(number)

# print(numbers)

print(max(numbers))
print(numbers.index(max(numbers))+1)