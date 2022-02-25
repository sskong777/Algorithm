"""
문제 4. 기본 Queue 구현 - 기본 구현 (내장 모듈 활용)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력해야 함)
"""
import queue

#1. Queue 생성
q = queue.Queue()
print(q.empty())
print()
#2. Queue에 데이터를 삽입
q.put(1)
q.put(2)
q.put(3)
print(q.empty())
print(q.full())
print(q.qsize())
print()
#3. Queue에 삽입한 데이터를 출력(First-In-First-Out)
print(q.get())

print(q.get())
print(q.get())
print(q.empty())