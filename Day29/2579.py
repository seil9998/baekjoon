import sys

num = int(sys.stdin.readline())
stairs = [0]
results = [0] * (num + 1)

for index in range(1, num+1):
    stair = int(sys.stdin.readline())
    stairs.append(stair)

for n in range(1, num+1):
    if n == 1:
        results[n] = stairs[1]
        continue
    
    if n == 2:
        results[n] = stairs[1] + stairs[2]
        continue
    
    case_1 = stairs[n] + stairs[n-1] +results[n-3]
    case_2 = stairs[n] + results[n-2]

    result = max(case_1, case_2)

    if result == case_1:
        results[n] = case_1
    elif result == case_2:
        results[n] = case_2

print(results[num])
