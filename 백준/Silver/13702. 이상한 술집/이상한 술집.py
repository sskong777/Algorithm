N, K = map(int,input().split())
arr = [int(input()) for _ in range(N)]

def sol(arr):
    arr.sort(reverse=True)  # 주전자 용량을 내림차순으로 정렬
    left = 1  # 최소 용량은 1
    right = arr[0]  # 최대 용량은 주전자 중 가장 큰 용량

    while left <= right:
        mid = (left + right) // 2  # 중간 용량 계산
        count = 0  # 몇 명에게 나눠줄 수 있는지 카운트

        for capacity in arr:
            count += capacity // mid  # 각 주전자마다 몫을 구해서 카운트에 더함

        if count >= K:
            left = mid + 1  # 몫의 합이 K보다 크거나 같다면 용량을 더 크게 해서 더 많이 나눌 수 있는지 확인
        else:
            right = mid - 1  # 몫의 합이 K보다 작다면 용량을 더 작게 해서 더 적게 나눌 수 있는지 확인

    return right

print(sol(arr))
