# 2초대의 코드 성능
# 성능 개선 코드 리팩토링

import sys

sys.stdin = open('input.txt')

# 암호 코드 (앞 쪽 0은 무시)
# 참고 -> dict의 key는 mutable 불가능
PATTERNS = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}


def scanner(arr):
    total = 0
    # 하나의 row씩 체크하며
    for row in range(N):
        # 16진수 -> 2진수 -> 16진수의 최댓값 F는 2진수로 1111 -> 4bit
        # 인덱스 에러 방지를 위해 -1 (마지막 제외)
        col = M * 4 - 1

        # 0 번째 자리까지 탐색할 필요 없음
        # 56개가 최소 자리수이기 때문에
        # 55번째 까지 1을 찾지 못하면 해당 부분은 7비트씩 8자리를 만족하지 못함
        while col >= 55:

            # 현재 값이 존재하고 이전 줄이 0인 경우만 확인 (중복된 라인인지 판별)
            if arr[row][col] != '0' and arr[row - 1][col] == '0':

                code = []
                # 모든 암호코드는 8개의 숫자로 구성 -> 체크
                for _ in range(8):
                    # 암호 코드는 오른쪽 3개의 숫자만 봐도 됨
                    # 우측 3개의 숫자패턴이 배치된 개수를 세어서 몇 배수인지 확인
                    # c2가 2, c3가 2, c4가 4 이되면 비율이 2:2:4 가 되고
                    # 이는 9 의 마지막 패턴 1:1:2 의 2배 임을 확인할 수 있게 된다.

                    # print(row, col, len(arr[row]), arr[row])
                    # c1 = 0  # 첫번째 0 개수 저장 => 체크안해도 됨
                    c2 = 0  # 두번째 1 개수 저장
                    c3 = 0  # 세번째 0 개수 저장
                    c4 = 0  # 마지막 1 개수 저장

                    # 우측의 값이 1일 때 까지 찾기 (스캔 기준점 찾기)
                    while arr[row][col] == '0':
                        col -= 1  # 앞의 비트로 이동

                    # 1이면 -> 하나 앞으로 & c4(1개수) count += 1
                    while arr[row][col] == '1':
                        c4 += 1  # 암호의 마지막 패턴인 1의 개수를 세는 부분
                        col -= 1  # 앞의 비트로 이동

                    # 0이면 -> 하나 앞으로 & c3(0개수) count += 1
                    while arr[row][col] == '0':
                        c3 += 1  # 암호의 세 번째 패턴인 0의 개수를 세는 부분
                        col -= 1  # 앞의 비트로 이동

                    # 1이면 -> 하나 앞으로 & c2(1개수) count += 1
                    while arr[row][col] == '1':
                        c2 += 1  # 암호의 두 번째 패턴인 1의 개수를 세는 부분
                        col -= 1  # 앞의 비트로 이동

                    # 최솟값 찾는다.
                    # 3:1:2 처럼 주어질 수도 있지만
                    # 6:2:4 이렇게 주어질 수도 있다 (2배 비율)
                    # 이 때는 최솟값인 2로 나눠야
                    # 암호패턴을 파악할 수 있다
                    MIN = min(c2, c3, c4)

                    # 최솟값으로 나눠서 암호문에 대응하는 숫자 찾기
                    # 비율이기 때문에 가장 작은 값으로 나눠주는 과정 필요
                    if MIN > 0:  # zero division 방지
                        c2 //= MIN
                        c3 //= MIN
                        c4 //= MIN
                        code.append(PATTERNS[(c2, c3, c4)])

                # 짝수 & 홀수 자리 합
                if len(code) == 8:
                    e_sum = sum(code[::2])
                    o_sum = sum(code[1::2])

                    #  (홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드가 10의 배수
                    if (o_sum * 3 + e_sum) % 10 == 0:
                        total += o_sum + e_sum

            # 한 칸 앞으로
            col -= 1

    return total


T = int(input())
for tc in range(1, T + 1):
    # N: 세로, M: 가로
    N, M = map(int, input().split())
    lst = [''] * N

    # 16진수 -> 2진수 변환 후 배열 입력
    for i in range(N):
        tmp = input()

        bit = ''
        for j in range(M):
            val2 = f'{int(tmp[j], base=16):04b}'
            bit += val2

        lst[i] = bit

    res = scanner(lst)
    print(f'#{tc} {res}')