def perm(k):
    global data
    if k == R:
        print(t)
    else:
        for i in range(N):
            if visited[i]:
                continue
            t[k] = a[i]
            visited[i] = 1
            perm(k+1)
            visited[i] = 0
a = [1,2,3,4,5,6]
R = 6

N = len(a)
visited = [0] * N
t = [0] * R

data = []
perm(0)
print(data)