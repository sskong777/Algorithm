def sequential_search(N,target,array):
    for i in range(N):
        if array[i] ==target:
            return i


# 생성할 원소 갯수와 타겟 입력받기
N = int(input())
target = input()

# 원소들 입력받기
print('앞서 적은 원소 개수만큼 문자열을 입력하시오 : ', end=' ')
array = input().split()

idx = sequential_search(N,target,array)
print(array[idx])
