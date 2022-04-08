n = int(input())
scare = list(map(int,input().split()))

scare.sort(reverse=False)   # 공포도 오름차순으로

count = 0   # 모험가 수
result = 0  # 그룹 수
for i in scare:
    count += 1  # 그룹에 모험가 추가
    if count >= i:  # 그룹에 공포도만큼 수가 채워지면
        result += 1 # 그룹결성
        count = 0   # 및 모험가 수 초기화

print(result)