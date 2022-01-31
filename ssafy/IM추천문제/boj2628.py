# 행, 열 입력받기
r, c = map(int, input().split())
# 사각형의 잘려진 점선 번호를 저장할 리스트 생성
x = [0, r]
y = [0, c]

# num번 만큼 반복
num = int(input())
for i in range(num):
    cut , cut_n = map(int, input().split())
    # cut이 1이면 세로로 자르므로 행(x) 리스트에 추가
    if cut == 1:
        x.append(cut_n)
    # cut이 0이면 가로로 자르므로 열(y) 리스트에 추가
    elif cut == 0:
        y.append(cut_n)
# 리스트 x,y를 오름차순으로 정렬   
x.sort()
y.sort()

# 잘려진 사각형의 세로, 가로 길이를 구하기 위한 리스트 생성
x_len, y_len = [], []
for i in range(1, len(x)):
    x_len.append(x[i]- x[i-1])
for i in range(1, len(y)):
    y_len.append(y[i]- y[i-1])

# 잘려진 사각형의 세로, 가로 길이의 최대값끼리 곱해준다. 
print(max(x_len) * max(y_len))