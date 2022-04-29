import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
deque = []
for n in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        deque.insert(0,command[1])
    elif command[0] == 'push_back':
        deque.append(command[1])
    elif command[0] =='front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif command[0] =='back':
        if deque:
            print(deque[-1])
        else:
            print(-1)
    elif command[0] =='size':
        print(len(deque))
    elif command[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif command[0] =='pop_front':
        if deque:
            front_pop = deque.pop(0)
            print(front_pop)
        else:
            print(-1)

    elif command[0] == 'pop_back':
        if deque:
            back_pop = deque.pop()
            print(back_pop)
        else:
            print(-1)
