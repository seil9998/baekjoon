X = int(input())
N = int(input())
total_price = 0

for i in range(N):
    a, b = input().split()
    a, b = int(a), int(b)
    total_price += a * b

if X == total_price:
    print("Yes")
else:
    print("No")