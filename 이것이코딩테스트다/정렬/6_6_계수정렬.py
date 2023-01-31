array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
N = len(array)

count = [0] * (N+1)

for i in range(N):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')