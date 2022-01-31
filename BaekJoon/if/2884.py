H,M = map(int,input('').split())
# H가 00시에서 23시로 넘어가는 경우와 
# M이 45분 미만일 때를 고려해야한다.


# 케이스 나누기
# 00시 - 00시 45분 사이일 때 (H,M 모두 고려 )
if H == 0 and M <45:
    H = 24 -1
    M = 60 -45 + M
    print("{} {}".format(H,M))
# 00시 - 00시 59분 사이일 때 (H,M모두 정상적으로 계산)
elif H == 0 and M >=45: 
    M = M - 45
    print("{} {}".format(H,M))
# H가 00시가 아니고/ M만 고려해야되는 상황
elif M < 45:
    H -= 1
    M = 60 - 45 + M
    print("{} {}".format(H,M))
# H와 M모두 고려하지 않아도 된다.
elif M >= 45:
    M = M - 45
    print("{} {}".format(H,M))

'''
# 틀렸다고 나오는데 어느 부분이 잘못됐는지 모르겠습니다.
# A : 시간, B: 분
A,B=map(int,input().split())
if A == 0:
    if B<45:
        A=23
        B+=15
        print(A,B,sep=' ')
    else:
        B-=45
        print(A,B,sep=' ')

else:
    if B>=45:
        B-=45
        print(A,B,sep=' ')
    else:
        A-=1
        B+=15
        print(A,B,sep=' ')
'''