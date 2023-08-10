# https://www.acmicpc.net/problem/11724
# DFS/ BFS
import time
import sys
input = sys.stdin.readline
# N = 8
# time :2s => 20,000,000
# 시간 복잡도 : O(?)

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def dfs(num):
    if len(str(num)) == N:
        print(num)

    for i in range(1,10,2):
        if isPrime(num*10 + i):
            dfs(num*10 + i)

N = int(input())

dfs(2)
dfs(3)
dfs(5)
dfs(7)
