H, M = input().split()

H = int(H)
M = int(M)

if M < 45:
    H = H - 1
    M = M + 60 - 45
    if H < 0:
        H = 23
else:
    M = M - 45

print(H, M)