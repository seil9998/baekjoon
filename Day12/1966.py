import sys

T = int(sys.stdin.readline())

for test in range(T):
    count = 0
    index = 0
    N, M = [int(i) for i in sys.stdin.readline().split()]
    Q_list = [int(Q) for Q in sys.stdin.readline().split()]
    count = 0
    target = M

    while True:
        if index < M:
            if Q_list[index] == max(Q_list):
                del Q_list[index]
                M -= 1
                count += 1
                if index > len(Q_list) - 1:
                    index = 0
            else:
                index += 1
                if index > len(Q_list) - 1:
                    index = 0
                continue

        elif index > M:
            if Q_list[index] == max(Q_list):
                del Q_list[index]
                count += 1
                if index > len(Q_list) - 1:
                    index = 0
            else:
                index += 1
                if index > len(Q_list) - 1:
                    index = 0
                continue

        else:
            if Q_list[index] == max(Q_list):
                count += 1
                print(count)
                break
            else:
                index += 1
                if index > len(Q_list) - 1:
                    index = 0
                continue