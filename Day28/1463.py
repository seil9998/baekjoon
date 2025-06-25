import sys

def f(n):
    result = 0
    if n == 1:
        return 0
    if results[n] != -1:
        return results[n]
    result = f(n-1) + 1
    if n % 2 == 0:
        result = min(result, f(n//2) + 1)
    if n % 3 == 0:
        result = min(result, f(n//3) + 1)
    
    results[n] = result
    return result
    
N = int(sys.stdin.readline())
results = [-1] * (N+1)

for i in range(1, N+1):
    f(i)

print(f(N))