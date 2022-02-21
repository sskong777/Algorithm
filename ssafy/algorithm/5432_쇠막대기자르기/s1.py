import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1,T+1):
    cnt = sol = 0
    arr = list(input())
    # print(arr)
    for i in range(len(arr)):
        if arr[i] == '(':
            cnt += 1
        else:
            if arr[i-1] =='(':
                cnt -= 1
                sol += cnt
            else:
                cnt -= 1
                sol += 1
    print("#{} {}".format(tc,sol))