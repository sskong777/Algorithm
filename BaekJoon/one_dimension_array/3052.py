
list_input = []
for i in range(10):
    num = int(input())
    list_input.append(num)

list_remain = []
for i in list_input:
    remain = i % 42
    list_remain.append(remain)

set_remain = set(list_remain)

print(len(set_remain))