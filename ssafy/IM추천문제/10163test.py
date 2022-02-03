from pprint import pprint
n = int(input())
x1, y1, a, b = map(int, input().split())
x2, y2 = x1 + a, y1 + b     # x2, y2 좌표값 설정
areas = []                  # 색종이별 가능한 좌표들 저장할 리스트
points = set([])            # 집합 연산을 통해 문제를 해결
for i in range(x1, x2):
    for j in range(y1, y2): # 일단 색종이 하나 입력받고 시작
        points.add((i,j))   # 입력받은 색종이별 가능한 모든 좌표를 튜플 자료형으로 set에 저장
areas.append(points)

#
for _ in range(n-1):        # 위에서 하나 입력 받았으니 나머지 n-1회분의 색종이 입력
    x1, y1, a, b = map(int, input().split())
    x2, y2 = x1 + a, y1 + b
    points = set([])            # 연산에 set을 활용할 예정
    for i in range(x1, x2):
        for j in range(y1, y2):
            points.add((i,j))   # set은 add로 추가 자료를 입력받는다
    for i in range(len(areas)):
        areas[i] -= points      # 차집합 연산 -> 먼저 입력받은 색종이의 가능한 모든 구간 좌표들의 집합에서 현재 입력받은 색종이 좌표들의 집합을 뺀다.
    areas.append(points)        # 현재 입력받은 색종이 좌표들 집합을 areas에 저장
for i in range(n):
    print(len(areas[i]))
