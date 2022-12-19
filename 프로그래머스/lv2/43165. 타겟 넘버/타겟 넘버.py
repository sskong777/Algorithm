answer = 0

def solution(numbers, target):
    global answer
    ssum = 0
    dfs(0,numbers,target,ssum)
    return answer


def dfs(index, numbers, target,ssum):
    global answer
    if index == len(numbers) and ssum == target:
        answer += 1
        return 
    
    if index == len(numbers):
        return
    
    dfs(index+1, numbers, target, ssum+numbers[index])
    dfs(index+1, numbers, target, ssum-numbers[index])

