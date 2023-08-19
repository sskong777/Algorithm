def plus(ex):
    sum = 0
    ex_list = ex.split('+')
    for i in ex_list:
        sum += int(i)
    return sum

expression = input().split('-')
answer = plus(expression[0])
for i in range(1,len(expression)):
    answer -= plus(expression[i])

print(answer)