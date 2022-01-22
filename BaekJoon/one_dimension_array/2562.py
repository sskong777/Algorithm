res = []
for i in range(9):
    i = int(input())
    res.append(i)

max = 0
for i in range(len(res)):
    if res[i] > max:
        max = res[i]
        
for i in range(len(res)):
    if res[i] == max:
        max_in = i+1
        
print(max)
print(max_in)