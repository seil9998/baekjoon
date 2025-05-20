N = int(input())
nums = [int(i) for i in input().split()]
v = int(input())
result = 0

for i in nums:
    if v == i:
        result += 1

print(result)