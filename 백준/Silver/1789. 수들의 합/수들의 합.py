N = int(input())

num = 1
while num*(num+1)/2 <= N:
    num += 1
print(num-1)