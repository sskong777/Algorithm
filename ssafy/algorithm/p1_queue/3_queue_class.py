"""
문제 3. 기본 Queue 구현 - 클래스 구현
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력해야 함)
"""

class Queue:
    # 생성자 함수
    def __init__(self, size):
        """
        인스턴스 생성 시에 새로운 Queue 생성
        인스턴스 변수 생성
        """
        self.size = size
        self.front = -1
        self.rear = -1
        self.Q = [None] * size
        print("Q 생성!")

    # isEmpty
    def is_empty(self):
        """
        Queue에 비어있는지 여부를 True / False로 반환
        """
        # global rear, front
        if self.rear == self.front:
            return True
        else:
            return False

    # isFull
    def is_full(self):
        """
        Queue에 데이터가 가득 저장되어 있는지 True / False 로 반환
        """
        # global rear
        if self.rear == self.size -1:
            return True
        else:
            return False

        # return self.rear == self.size -1


    # enQueue 
    def enqueue(self,item):
        """
        Queue에 원소 삽입
        """
        # global rear

        if self.is_full():
            # print("Q IS FULL")
            raise Exception("Queue is Full")
        else:
            self.rear += 1
            self.Q[self.rear] = item
    
    # deQueue
    def dequeue(self):
        """
        Queue에서 원소 삭제 후 반환
        """
        # global front
        if self.is_empty():
            raise Exception("Q is Empty")
        else:
            self.front += 1
            return self.Q[self.front]

    def Qpeek(self):
        """
        Queue에서 바로 다음에 나올 값 확인
        """

        if self.is_empty():
            raise Exception("Q is Empty")
        else:
            return self.Q[self.front + 1]

    # length
    def __len__(self):
        """
        Queue의 길이 반환 (들어있는 데이터 개수)
        """
        return self.rear - self.front


#1. queue 인스턴스 생성 size 는 5
q1 = Queue(5)
#2. queue가 비었는지 확인
print(q1.is_empty())     # True

#3. 1, 2, 3 원소를 queue에 삽입
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)

#4. 원소가 정상적으로 삽입되었는지 확인 / 길이 확인 / 비었는지 여부 확인
print(q1.Q)
print(len(q1))
print(q1.is_empty())
#5. queue에서 원소 삭제 후 반환 & 원소 확인 / 길이 확인
item = q1.dequeue()
print(item)
print(len(q1))

#6. queue가 가득차도록 값 추가
q1.enqueue('A')
q1.enqueue('B')
print(q1.is_full())
# q1.enqueue('C')
# print(q1.is_full())
#7. 가득 차 있는 상태에서 값 추가
# q1.enqueue('D')