# https://school.programmers.co.kr/learn/courses/30/lessons/42628

import heapq
def solution(operations):
    # answer = []
    heap = []
    for oper in operations:
        command, num = oper.split(" ")
        if command =='I':
            heapq.heappush(heap, int(num))
        elif command == 'D':
            if len(heap) < 1:
                continue
            if num == '1':
                heap.pop(heap.index(heapq.nlargest(1,heap)[0]))
            elif num =='-1':
                heapq.heappop(heap)
    # print(heap)
    if len(heap) == 0:
        answer = [0,0]
    else:
        answer = [heapq.nlargest(1,heap)[0], heapq.nsmallest(1,heap)[0]]
    return answer



# ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]	[0,0]
# ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	[333, -45]