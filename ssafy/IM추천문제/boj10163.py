from pprint import pprint
N = int(input())
# li = []
# for i in range(N):
#     li2 = []
#     r, c, w, h = map(int, input().split())
#     for x in range(r, w+r):
#         for y in range(c, h+c):
#             li2.append((x,y))
#     li.append(li2)

# ans = []
# for i in range(len(li[i])):
#     for j in range(i+1, len(li[i])):
#         if li[i] not in li[j]:
#             ans.append(li[i])
# pprint(ans)

li1 = []
for i in range(N):
    set2 = set()
    r, c, w, h = map(int, input().split())
    for x in range(r, w+r):
        for y in range(c, h+c):
            set2.add((x,y))
        li1.append(set2)

print(li1)
print(type(li1[0]))
# ans = []
# for i in range(0, len(li1)-1):
#     for j in range(i+1, len(li1)-1):
#         ans.append(li1[i] & li1[j])
# print(ans)

# pprint(li)
                



# 중복된 값을 제거해주기 위해 set 사용
# field = set()
# for num in range(4):
#     # x,y좌표 입력받기
#     x1, y1, x2, y2 = map(int, input().split())

#     for x in range(x1, x2):
#         for y in range(y1, y2):
#             field.add((x, y))

# print(len(field))