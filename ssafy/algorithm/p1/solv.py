import sys
sys.stdin = open('input.txt', 'r')

def pre_order(v):
    if v:
        print(v)
        pre_order(ch1[v])
        pre_order(ch2[v])

V = int(input())
arr = list(map(int,input().split()))
# print(arr)
# print(len(arr))
E = V - 1
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c


pre_order(1)