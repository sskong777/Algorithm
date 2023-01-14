import sys
sys.stdin = open('input.txt', 'r')

array = [i for i in range(1,31)]

for i in range(28):
    n = int(input())
    if n in array:
        array.remove(n)
print(min(array))
print(max(array))
