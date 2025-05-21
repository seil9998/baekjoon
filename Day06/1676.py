N = int(input())

N_factorial = 1
count = 0

for i in range(1, N + 1):
    N_factorial *= i

for i in reversed(str(N_factorial)):
    if i == "0":
        count += 1
    else:
        break

print(count)