N, X = input().split()
N, X = int(N), int(X)
A = [int(i) for i in input().split()]

for i in A:
    if i < X:
        print(i, end = " ")