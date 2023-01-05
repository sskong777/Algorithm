t = int(input())

for _ in range(t):
    a = list(input().split())
    num = float(a.pop(0))
    for i in range(len(a)):
        if a[i] == '@':
            num *= 3
        elif a[i] == '%':
            num += 5
        elif a[i] == '#':
            num -= 7
    
    print("%0.2f" % num)