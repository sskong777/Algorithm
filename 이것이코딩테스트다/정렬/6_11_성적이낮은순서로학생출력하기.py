def chage_char(char):
    if char.isnumeric():
        return int(char)
    else:
        return char

N = int(input())
arr = []
for i in range(N):
    name, score = map(chage_char,input().split())
    arr.append((name,score))

arr.sort(key=lambda x : x[1])
for i in arr:
    print(i[0])