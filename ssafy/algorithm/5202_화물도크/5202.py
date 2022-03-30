import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    arr =  []
    N = int(input())
    for n in range(N):
        s,e = map(int,input().split())
        arr.append((s,e))
    arr.sort(key=lambda x:x[1])

    cnt = 0
    while arr:
        pick = arr[0][1]
        cnt +=1
        new_arr = []
        for i in range(1,len(arr)):
            # 선택한 화물의 종료시간보다 출발시간이 늦은 화물 추가.
            if arr[i][0] >= pick:
                new_arr.append(arr[i])
        # cnt += 1
        # new_arr를 arr로 복사하여 다시 while문 동작.
        arr = new_arr

    print(f'#{tc} {cnt}')
