import sys
sys.stdin = open('input.txt', 'r')


N,M = map(int,input().split())

print(N*M -1)