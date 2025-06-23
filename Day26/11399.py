import sys

N = int(sys.stdin.readline())
result = 0
total_result = 0

times = [int(time) for time in sys.stdin.readline().split()]

times.sort()

for time in times:
    result += time
    total_result += result

print(total_result)