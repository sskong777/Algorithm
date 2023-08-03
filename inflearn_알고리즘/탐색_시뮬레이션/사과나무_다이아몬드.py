N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

answer = 0
center = N//2
print(center)
for i in range(N):
    print(i)
    print(abs(center - i), N - abs(center - i))

    for j in range(abs(center - i), N - abs(center - i)):

        answer += arr[i][j]

print(answer)

# import sys
# sys.stdin = open("input.txt", 'r')
# n=int(input())
# a=[list(map(int, input().split())) for _ in range(n)]
# res=0
# s=e=n//2
# for i in range(n):
#     for j in range(s, e+1):
#         res+=a[i][j]
#     if i<n//2:
#         s-=1
#         e+=1
#     else:
#         s+=1
#         e-=1
# print(res)
