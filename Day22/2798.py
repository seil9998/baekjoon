N, M = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]
results = []

for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if i != j and j != k and i != k and nums[i] + nums[j] + nums[k] <= M:
                results.append([nums[i], nums[j], nums[k]])

result = max(results, key = lambda x: sum(x))

print(sum(result))