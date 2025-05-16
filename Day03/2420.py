N, M = input().split()

N, M = int(N), int(M)

result = N - M

if result < 0:
    result = result * -1

print(result)