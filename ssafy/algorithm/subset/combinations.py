from itertools import combinations

arr = [1,2,3,4,5,6]
result = []
for i in range(len(arr)+1):  # 공집합도 포함시켜야하기 때문
    result += list(combinations(arr,i))

print(result)

result2 = []
result2 += list(combinations(arr,3))
print(result2)