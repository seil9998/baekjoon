N, M = input().split()

N = int(N)
M = int(M)
A = []
B = []

for i in range(N):
    A.append([int(j) for j in input().split()])

for i in range(N):
    B.append([int(j) for j in input().split()])

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end = " ")
    print()
