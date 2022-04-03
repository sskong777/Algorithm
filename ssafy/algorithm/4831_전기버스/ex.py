import sys
sys.stdin = open('input.txt', 'r')

T= int(input())
for tc in range(1,T+1):
    K, N ,M = map(int, input().split())
    chargers = list(map(int, input().split()))
    stations = [True if n in chargers else False for n in range(N+1)]

    charge_count = last_charge = 0
    current = K

    while current < N:
        if last_charge == current:
            charge_count = 0
            break
        if stations[current]:
            last_charge = current
            charge_count += 1
            current += K
        else:
            current -= 1

    ans = charge_count
    print("#{} {}".format(tc, ans))
