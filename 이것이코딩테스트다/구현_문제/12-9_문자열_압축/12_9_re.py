import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    s = input()
    ans = 10000
    # n개로 압축
    for n in range(1,len(s)//2+2):  # n은 1부터 S의 길이 //2일 때 까지 (+2를 해준이유는 s의 길이가 1일때고려)
        res = ''    # 압축문자열 초기화
        cnt = 1
        temp = s[:n]
        for i in range(n,len(s)+n,n):
            # n개씩 건너뛰며 비교
            if temp == s[i:i+n]:    # 앞의 n개만큼의 문자열과 현재 n개만큼의 문자열이 같다면
                cnt += 1
            # 앞의 n개만큼의 문자열과 같지않다면
            else:
                # cnt가 1일때는 반복횟수를 붙히면 안되므로
                if cnt == 1:
                    res += temp
                # res에 반복횟수와 반복된 문자열을 더해준다.
                else:
                    res += str(cnt)+ temp
                # 다음 반복문을 위해 temp(비교당할 문자열)을 초기화시켜준다.
                temp = s[i:i+n]
                # 반복횟수도 1로 초기화
                cnt = 1
        ans = min(ans,len(res))
    print(ans)