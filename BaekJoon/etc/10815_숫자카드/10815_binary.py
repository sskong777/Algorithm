import sys
sys.stdin = open('input.txt' ,'r')

def binary_search(array,target,start,end):

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
N = int(input())
cards = list(map(int,input().split()))
cards.sort()


M = int(input())
check = list(map(int,input().split()))

for m in range(M):
    if binary_search(cards,check[m],0,N-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')