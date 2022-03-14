N = int(input())

# if N < 10:

for i in range(1,N):
    num = i + sum(map(int,str(i)))
    if num == N:
        print(i)
        break
else:
    print(0)


