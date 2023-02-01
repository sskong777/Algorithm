import sys
sys.stdin = open('input_14_23.txt', 'r')

N = int(input())
arr = []
for i in range(N):
    name, korean, english, math = input().split()
    arr.append((name, int(korean), int(english), int(math)))

arr.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))

for i in range(N):
    print(arr[i][0])