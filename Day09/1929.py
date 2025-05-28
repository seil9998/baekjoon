import sys

def prime(M, N):
    prime_num = [True] * (N + 1)
    prime_num[0] = False
    prime_num[1] = False

    for i in range(2, int(N ** 0.5) + 1):
        if prime_num[i]:
            for j in range(i * i, N + 1, i):
                prime_num[j] = False

    return [idx for idx, i in enumerate(prime_num) if (i == True and idx >= M)]

M, N = [int(i) for i in sys.stdin.readline().split()]

for prime_num in prime(M, N):
    print(prime_num)