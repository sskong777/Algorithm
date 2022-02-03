# from pprint import pprint
#
# N = int(input())
#
# recs = []
# for num in range(N):
#     r, c, w, h = map(int,input().split())
#     rec = []
#     for x in range(r, r+w):
#         for y in range(c, h+c):
#             rec.append((x,y))
#     recs.append(rec)
# # print(recs)
#
# ans = []
# for i in range(0, len(recs)):
#     for j in range(i+1, len(recs)):
#         ans.append(set(recs[i]) - set(recs[j]))
# ans.append(recs[-1])
# for i in ans:
#     print(len(i))




from pprint import pprint

N = int(input())

recs = []
for num in range(N):
    r, c, w, h = map(int,input().split())
    # 좌표들 담을 set 생성
    points = set([])
    # 입력받은 사각형에 포함된 좌표를 points에 좌표단위로 추가
    for x in range(r, r+w):
        for y in range(c, h+c):
            points.add((x,y))
    # 사각형의 겹치는 부분을 다음에 입력받은 좌표들로 빼준다(차집합) - (set -set) 이용
    for i in range(len(recs)):
        recs[i] -= points
    recs.append(points)

print(points)
for i in recs:
    print(i)

# for i in range(N):
#     print(len(recs[i]))
