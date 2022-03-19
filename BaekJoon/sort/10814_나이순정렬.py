def chg(char):
    if char.isnumeric():
        return int(char)
    else:
        return char

N = int(input())
arr = []
for i in range(N):
    age, name = map(chg,input().split())
    arr.append([age,name])

arr.sort(key=lambda x : x[0])

for i in range(N):
    print(arr[i][0],arr[i][1])