n = int(input())
num = int(input())

a = list(str(num))

total = 0
for i in a:
    total += int(i)
print(total)