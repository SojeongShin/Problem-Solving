# 스택
import sys

stack = []

def push(x):
    stack.append(x)

def pop():
    if not stack:
        return -1
    return stack.pop()

def size():
    return len(stack)

def empty():
    if not stack:
        return 1
    return 0

def top():
    if not stack:
        return -1
    return stack[-1]

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

    elif command[0] == "top":
        out.append(top())

sys.stdout.write('\n'.join(map(str, out)))