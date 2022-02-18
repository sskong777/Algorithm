C, R = map(int,input().split())
arr = [[0]* C for _ in range(R)]
search = int(input())
# print(arr)
# 하 우 상 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0 , -1]

# for r in range(R):
#     for c in range(C):
#         arr[r][c] = 1
# print(arr)
r = 0
c = 0
num = 1
arr[r][c] = num  # 시작은 1로 고정

# 배열 크기만큼 반복
while num < R * C:
    for direct in range(4):
        # 이동하려는 값을 살펴보기 위해 계산
        next_row = r + dr[direct]
        next_col = c + dc[direct]

        # 범위 내이고 현재 값이 0일 때만 반복
        while (0 <= next_row < R and 0 <= next_col < C) and arr[next_row][next_col] == 0:  # 0이 없으면 뚫고 지나가버림
            # 다음 인덱스가 사용가능하면 값 변경
            r = next_row
            c = next_col
            num += 1
            arr[r][c] = num

            # 다음 값이 범위 밖인지 확인하기 위해 계산
            next_row = r + dr[direct]
            next_col = c + dc[direct]
print(arr)
for r in range(R):
    for c in range(C):
        if arr[r][c] == search:
            res = [c+1, r+1]
        elif R*C < search:
            res = [0]

print(*res)