num_list = []
_input = input()
for i in _input:
    if i.isnumeric():
        num_list.append(i)
num = int(''.join(num_list))
cnt = 0
for i in range(1, int(num ** 0.5) + 1):
    if (num % i == 0) and num**0.5 != i:
        cnt += 1

cnt *= 2
print(num)
print(cnt)

# for i in range(1,num//2+1):
#     if num % i == 0:
#         cnt += 1
# print(cnt)