# r, c = map(int, input().split())
# N = int(input())
# stores = []
# 상점들과 동근이의 절대 좌표값을 구해준다.
# for n in range(N+1):
#     d, v = map(int, input().split())
#     if d == 1:
#         stores.append((v,c))
#     elif d == 2:
#         stores.append((v,0))
#     elif d == 3:
#         stores.append((0,c-v))
#     elif d == 4:
#         stores.append((r,c-v))

# 동근이와 상점들의 인코스, 아웃코스 거리 값 비교.
# for i in range(len(stores)-1):
#     pass



# 구글링 힌트..
# 사각형을 펼쳐서 y축으로 계산하여 좌표 계산.
x,y = map(int,input().split())
array = []
n = int(input())

for _ in range(n+1):
    position, value = map(int,input().split())
    if position == 1:
        array.append(y+value)
    elif position == 2:
        array.append(-value)
    elif position == 3:
        array.append(y-value)
    else:
        array.append(-x-y+value)

# print(array)
total = 0
for i in range(len(array)-1):
    # 좌표들의 부호가 같다면,
    if array[n] * array[i] > 0:
        dist = abs(array[n] - array[i])
    # 좌표의 부호가 다르다면
    else:
        # 좌표들의 합이 x+y의 길이보다 크다면 아웃코스
        if abs(array[n]) + abs(array[i]) > x+y:
            dist = 2*(x+y) - abs(array[n] - array[i])

        # 좌표들의 합이 x+y의 길이보다 작다면 인코스
        else:
            dist = abs(array[n] - array[i])

    total += dist

print(total)