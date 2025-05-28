import sys

N = int(sys.stdin.readline())
result = []

for i in range(0, N + 1, 5):
    if (N - i) % 3 == 0:
        result.append((i // 5, (N - i) // 3))

if not result:
    print(-1)
else:
    answer = min(result, key = lambda x: x[0] + x[1])
    print(answer[0] + answer[1])