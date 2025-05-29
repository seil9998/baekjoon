import sys

def nums(n):
    while True:
        yield n
        n += 1

count = 0
result = 0

N = int(sys.stdin.readline())

for i in nums(666):
    if "666" in str(i):
        count += 1
        result = i
        if count == N:
            break

print(result)