n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.pop(0)
    b.pop(0)
    #
    # a.sort()
    # b.sort()
    for i in range(4, 0, -1):
        # if a == b:
        #     print('D')
        #     break
        if a.count(i) > b.count(i):
            print('A')
            break
        elif a.count(i) < b.count(i):
            print('B')
            break
    else:
        print('D')
