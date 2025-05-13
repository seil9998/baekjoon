import sys

T = int(sys.stdin.readline())

for i in range(T):
    A, B = sys.stdin.readline().split()
    A, B = int(A), int(B)
    print(f"Case #{i + 1}: {A + B}")