import sys

N, M = [int(i) for i in sys.stdin.readline().split()]

board = [list(sys.stdin.readline().strip()) for _ in range(N)]
result = []

for index_N in range(N - 7):
    for index_M in range(M - 7):
        count_1 = 0
        count_2 = 0
        for i in range(index_N, index_N + 8):
            for j in range(index_M, index_M + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] != "W":
                        count_1 += 1
                    if board[i][j] != "B":
                        count_2 += 1
                elif (i + j) % 2 == 1:
                    if board[i][j] != "B":
                        count_1 += 1
                    if board[i][j] != "W":
                        count_2 += 1
        result.append(count_1)
        result.append(count_2)
            
print(min(result))