import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    A, B = sys.stdin.readline().rstrip().split()
    A, B = int(A), int(B)
    print(A + B)