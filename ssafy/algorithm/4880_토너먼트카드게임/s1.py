import sys
sys.stdin = open('input.txt', 'r')

def win(left, right):
    # 1: 가위, 2: 바위, 3: 보
    if cards[left] == 1 or cards[right] == 1:      # 둘 중 하나라도 가위라면
        if (cards[left] % 3) >= (cards[right] % 3):
            return left
        else:
            return right
    else:
        if cards[left] >= cards[right]:
            return left
        else:
            return right


def match(start, end):   # start 시작점 , end 끝점 사이의 승자를 찾는 함수
    if start == end:    # 한 명만 남은 경우
        return start
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾차 최종 승자를 가림
        left = match(start, (start + end) // 2)       # 왼쪽 그룹의 승자
        right = match((start + end) // 2 + 1, end)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수 구현


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    res = match(0, N-1)

    print(f'#{tc} {res+1}')




