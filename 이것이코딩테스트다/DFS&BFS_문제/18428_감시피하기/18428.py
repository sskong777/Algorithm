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


def search(i,j):
    # q = deque((i,j))
    #
    # while q:
    #     i,j = q.popleft()
    # global v
    # v = [[0] * N for _ in range(N)]
    # v[i][j] = 1
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        for move in range(1, N):
            ni, nj = i + di * move, j + dj * move
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 'S':
                    return False
                elif arr[ni][nj] == 'O':
                    break
                break

                # v[ni][nj] = 1
            # if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 'O':
            #     v[ni][nj] = 1
            #     if arr[ni][nj] =='S':
            #         return False
    return True

def XtoO(*O):
    for o in O:
        i,j = X_list[o][0], X_list[o][1]
        arr[i][j] = 'O'

def return_X(*O):
    for o in O:
        i,j = X_list[o][0], X_list[o][1]
        arr[i][j] = 'X'


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



res = ans(X_list,T_list)
if res:
    print('YES')
else:
    print("NO")
