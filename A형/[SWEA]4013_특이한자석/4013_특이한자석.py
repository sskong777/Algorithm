import sys
sys.stdin = open('input.txt', 'r')

def dfs(num,dir):    # 자석 번호와 회전방향을 매개변수로 가지는 함수
    global check
    check[num] = 1
    if num < 3:
        # 자석이 3보다 작을 때 자성이 다를 경우
        if arr[num][2] != arr[num+1][6] and not check[num+1]:
            # 다음 자석번호, 반대 방향 호출
            dfs(num+1, -1 * dir)
    if num > 0:
        # 자석이 0보다 클 때 자성이 다를 경우
        if arr[num][6] != arr[num-1][2] and not check[num-1]:
            dfs(num-1, -1 * dir)

    if dir == 1:
        arr[num] = [arr[num].pop()] + arr[num]
    else:
        arr[num] = arr[num][1:] + [arr[num][0]]


T = int(input())
for tc in range(T):
    K = int(input())
    arr = [list(map(int,input().split())) for _ in range(4)]

    # print(arr)
    for k in range(K):  # K번 회전
        num, rot = map(int,input().split())     #자석번호와 회전방향
        check = [0] * 4     # 각각 자석의 자성 확인
        dfs(num-1,rot)

    res = 0
    for i in range(4):
        res += arr[i][0] * (2 ** i)   # 제곱을 해주는 이유 : 1 2 4 8

    print("#{} {}".format(tc+1, res))
