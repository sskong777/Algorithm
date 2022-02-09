n = int(input())
count = 0
for _ in range(n):

    word = list(input())
    word3 = []
    word3.append(word[0])

    for i in range(1, len(word)):
        if word[i-1] != word[i]:

            word3.append(word[i])
    # print(word3)

    if len(set(word3)) == len(word3):
        count += 1
print(count)