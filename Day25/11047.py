import sys

N, K = [int(num) for num in sys.stdin.readline().split()]

coins = []
result = 0
remainder = K

for _ in range(N):
    coins.append(int(sys.stdin.readline()))

for index in range(len(coins)-1, -1, -1):
    coin = coins[index]
    result += remainder // coin
    remainder = remainder % coin
    if remainder == 0:
        break

print(result)