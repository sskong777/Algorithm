word = input()

res = 0
for i in word:
    num = 65
    plus = 3
    for j in range(8):
        if num <= ord(i) <= num + 2:
            res += plus

        num += 3
        plus += 1
    if ord(i) == 90:
        res += 10
print(res)


