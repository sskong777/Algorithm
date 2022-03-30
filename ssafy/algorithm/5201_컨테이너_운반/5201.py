import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    W = list(map(int,input().split()))      # N개의 화물의 무게
    T = list(map(int,input().split()))      # M개의 트럭의 적재용량

    # 내림차순 정렬
    W.sort(reverse=True)
    T.sort(reverse=True)

    # 화물의 수가 더 많을 수도 있고, 트럭의 수가 더 많을 수도 있다.
    # 횟수를 세어줄 변수, w,t중 더 작은 배열의 길이를 초과하면 break하도록
    count = 0
    res = 0
    w_i, t_i = 0,0  # W,T의 인덱스 번호
    while True:
        if count == min(len(W),len(T)):
            break
        # 헤딩 인덱스에 트럭에 실을 수 있다면,
        if T[t_i] >= W[w_i]:
            res += W[w_i]
            t_i += 1
            w_i += 1
        # 해당 인덱스에 트럭을 실을 수 없다면
        else:
            w_i += 1
        count += 1  # 무게와 트럭용량과 비교할때마다 증가시킨다.

    print(f'#{tc} {res}')