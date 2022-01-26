t = int(input())

for i in range(t):
    n , word = input().split()
    ans = ''
    for i in word:
        ans += (i * int(n))
    print(ans)