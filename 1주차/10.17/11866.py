data = []

data = list(map(int, input().split()))

# print(data)

y_data = []

output_list = []

for i in range(1,data[0]+1):
    y_data.append(i)

# print(y_data)

while len(y_data) > 0:

    for i in range(data[1]-1):
        # print('a')
        temp = y_data.pop(0)
        y_data.append(temp)
        # print(y_data)
    output_list.append(y_data.pop(0))
    # print(output_list)

output_str = ", ".join(map(str, output_list))
print("<{}>".format(output_str))