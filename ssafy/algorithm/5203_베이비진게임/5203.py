import sys
import itertools
sys.stdin = open('input.txt', 'r')

def rrun(arr):
    if arr[0] == arr[1] == arr[2]:
        return True
def tri(arr):
    if arr[0]+2 == arr[1]+1 == arr[2]:
        return True

def check(data):
    res = False
    for i in data:
        if rrun(i) or tri(i):
                return True

    return res


T = int(input())
for tc in range(1,T+1):
    cards = list(map(int,input().split()))

    player1 = []
    player2 = []
    for i in range(0,12,2):
        player1.append(cards[i])
        player2.append(cards[i+1])

    # 각각 플레이어의 카드를 순회하며 체크
    # 카드 세장부터 babyGin이 나올 수 있다.
    res = 0
    for i in range(3,7):
        p1_data = []
        p2_data = []

        p1 = player1[:i+1]
        # p1에는 뽑은 카드 숫자들을 저장해주고
        p1_data += itertools.permutations(p1,3)
        # p1_data에는 여태 뽑은 카드들 중 3장의 순열을 만들어준다.
        # check함수를 사용해서 p1_data중에 run 혹은 tri가 있으면 res에 1을
        # 저장하고 반복문을 탈출한다.
        if check(p1_data):
            res = 1
            break

        # 플레이어2도 같은 방식으로 처리해준다.
        p2 = player2[:i+1]
        p2_data += itertools.permutations(p2,3)
        if check(p2_data):
            res = 2
            break
        # 같은 루프구간에서 플레이어 1,2가 babygin이 나와도 플레이어 1부터 순차적으로
        # check함수가 실행되므로 승부가 정해진다.
    print(f'#{tc} {res}')
