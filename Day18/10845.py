import sys

N = int(sys.stdin.readline())

Q = []
orders = []

for _ in range(N):
    order = sys.stdin.readline().strip().split()
    orders.append(order)

for order in orders:
    if len(order) == 2:
        Q.append(int(order[1]))
    
    elif order[0] == "pop":
        if Q:
            num = Q.pop(0)
            print(num)
        else:
            print(-1)

    elif order[0] == "size":
        print(len(Q))

    elif order[0] == "empty":
        if Q:
            print(0)
        else:
            print(1)

    elif order[0] == "front":
        if Q:
            print(Q[0])
        else:
            print(-1)

    elif order[0] == "back":
        if Q:
            print(Q[-1])
        else:
            print(-1)      