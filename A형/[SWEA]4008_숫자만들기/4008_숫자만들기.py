import sys
sys.stdin = open('input.txt', 'r')

def dfs(idx, result):
    global max_num
    global min_num
    if idx == N - 1:
        if max_num <= result:
            max_num = result
        if min_num >= result:
            min_num = result
        return

    for i in range(4):  # 연산 4번 만큼 반복
        if operator[i] > 0:
            operator[i] -= 1  # 연산자 사용
            if i == 0:
                new_result = result + number[idx + 1]   # 더하기
            elif i == 1:
                new_result = result - number[idx + 1]   # 빼기
            elif i == 2:
                new_result = result * number[idx + 1]   # 곱하기
            else:  # 음수 나눗셈의 경우 때문에 int캐스팅으로 버림
                new_result = int(result / number[idx + 1])  # 나누기
            dfs(idx + 1, new_result)
            operator[i] += 1


T = int(input())
for t in range(T):
    N = int(input())
    operator = list(map(int, input().split()))  # [+ - * /]순으로 저장
    number = list(map(int, input().split()))
    max_num = -1e9
    min_num = 1e9
    dfs(0, number[0])
    print('#{} {}'.format(t + 1, max_num - min_num))