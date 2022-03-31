from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

def ans(X_list,T_list):
    for o1 in range(len(X_list)):
        for o2 in range(o1 + 1, len(X_list)):
            for o3 in range(o2 + 1, len(X_list)):
                XtoO(o1, o2, o3)
                if T_search(T_list):
                    return True
                return_X(o1, o2, o3)
    return False


def T_search(T_list):
    check = True
    for t in T_list:
        i,j = t
        if not search(i,j):
             check = False
    return check


def search(x,y):
    for i in range(4):
        while 0<=x<N and 0<= y <N:
            if arr[x][y] == 'O':
                break
            elif arr[x][y] == 'S':
                return False

            x += dx[i]
            y += dy[i]
    return True

def XtoO(*O):
    for o in O:
        i,j = X_list[o][0], X_list[o][1]
        arr[i][j] = 'O'

def return_X(*O):
    for o in O:
        i,j = X_list[o][0], X_list[o][1]
        arr[i][j] = 'X'

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input())
arr = [list(input().split()) for _ in range(N)]
# print(arr)

T_list = []
X_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            T_list.append((i,j))
        elif arr[i][j] == 'X':
            X_list.append((i,j))


# for o1 in range(len(X_list)):
#     for o2 in range(o1+1,len(X_list)):
#         for o3 in range(o2+1,len(X_list)):
#             XtoO(o1,o2,o3)
#             if T_search(T_list):
#                 pass
#             return_X(o1,o2,o3)

print(search(1,0))

res = ans(X_list,T_list)
if res:
    print('YES')
else:
    print("NO")
