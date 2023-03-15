def changeBinary(x):
    x1 = x.replace("0","")
    x2 = bin(len(x1))[2:]
    print(x2)
    return x2

def solution(s):
    answer = [0,0]
    while s != "1":
        answer[1] += s.count("0")
        s = changeBinary(s)
        answer[0] += 1
    return answer

