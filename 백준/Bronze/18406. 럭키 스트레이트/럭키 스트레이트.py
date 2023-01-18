num = list(map(int,input()))
n1 = num[:len(num)//2]
n2 = num[len(num)//2:]

if sum(n1) == sum(n2):
    print("LUCKY")
else:
    print("READY")