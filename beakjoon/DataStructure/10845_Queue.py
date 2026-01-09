queue = []

def push(x):
    queue.append(x)

def pop():
    if not queue:
        return -1
    return queue.pop(0)

def size():
    return len(queue)

def empty():
    if not queue:
        return 1
    return 0

def front():
    if not queue:
        return -1
    return queue[0]

def back():
    if not queue:
        return -1
    return queue[-1]

import sys

input = sys.stdin.readline
orders = int(input())
out = []

for _ in range(orders):
    command = input().split()

    if command[0] =="push":
        push(int(command[1]))
    
    elif command[0] == "pop":
        out.append(pop())
    
    elif command[0] == "size":
        out.append(size())

    elif command[0] == "empty":
        out.append(empty())

    elif command[0] == "front":
        out.append(front())

    elif command[0] == "back":
        out.append(back())

sys.stdout.write('\n'.join(map(str, out)))
    