import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    rec1 = set()
    rec2 = set()
    n = int(input())
    for _ in range(n):
        r1 ,c1, r2, c2, color  = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2+1):
                if color == 1:
                    rec1.add((r,c))
                elif color == 2:
                    rec2.add((r,c))
        # print(rec1)
        # print(rec2)
    print("#{} {}".format(tc, len(rec1 & rec2)))

    # print(rec1.intersection(rec2))
