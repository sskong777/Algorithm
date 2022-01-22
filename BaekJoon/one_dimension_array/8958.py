t = int(input())

answer = []

for i in range(t):
    list_ox = list(input())
    total = 0
    score = 1
    for j in list_ox:
        if j == 'O':
            total += score
            score += 1
        else:
            score = 1

    answer.append(total)

for i in answer:
    print(i)