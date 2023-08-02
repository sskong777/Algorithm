N = int(input())
for tc in range(N):
    answer = ""
    _str = input()
    if _str.upper() == _str[::-1].upper():
        answer = "YES"
    else:
        answer = "NO"
    print(f'#{tc+1} {answer}')
