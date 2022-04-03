import sys
N, M = map(int, sys.stdin.readline().split())

arr = [i for i in range(1,N+1)]
check = [False]*len(arr)
a = []

def dfs(x):
  if x == M:
    print(*a,sep=" ")
    return

  for i in range(N):
    if check[i]:
      continue

    check[i]=True
    a.append(arr[i])
    print("check:",check)
    print("a:",a)
    print("x1:",x)
    print("i1:",i)
    dfs(x+1)
    a.pop() #x==M조건 만족하여 return 한다음 다시 여기로 돌아옴
    check[i] = False
    print("after a.pop:a=",a)
    print("check:",check)
    print("x2:",x)
    print("i2:",i)
dfs(0)
