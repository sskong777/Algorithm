import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op_num = list(map(int, input().split()))  # +, -, *, /
op_list = ['+', '-', '*', '/']
op = []

for k in range(len(op_num)):
    for i in range(op_num[k]):
        op.append(op_list[k])
print(op)