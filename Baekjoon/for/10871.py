N, X = map(int,input().split())


list_input = list(map(int,input().split()))

for i in list_input:
    if i < X:
        print(i, end=' ')