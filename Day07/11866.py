import sys

N, K = [int(i) for i in sys.stdin.readline().split()]
nums = [i for i in range(1, N + 1)]
result = []
index = K - 1

while True:
    index %= len(nums)
    result.append(nums[index])
    nums.pop(index)
    index += (K - 1)

    if not nums:
        break

print("<" + ", ".join(map(str, result)) + ">")