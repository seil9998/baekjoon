import sys

N = int(sys.stdin.readline())

stack = []
orders = [sys.stdin.readline().strip().split() for _ in range(N)]

for order in orders:
    if len(order) == 2:
        stack.append(order[1])

    elif order[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif order[0] == "size":
        print(len(stack))
    
    elif order[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)

    elif order[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)