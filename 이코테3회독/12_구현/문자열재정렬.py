def solution(input):
    strings = []
    num = 0
    for i in input:
        if i.isnumeric():
            num += int(i)
        else:
            strings.append(i)
    strings.sort()
    print(''.join(strings)+str(num))
solution("K1KA5CB7")