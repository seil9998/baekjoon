A, B = input().split()
C = input()

A, B, C = int(A), int(B), int(C)

if B + C >= 60:
    A = A + ((B + C) // 60)
    B = (B + C) % 60
    if A >= 24:
        A = A % 24
else:
    B = B + C

print(A, B)