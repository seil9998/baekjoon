A, B, C = input().split()

A, B, C = int(A), int(B), int(C)

lst = [A, B, C]
st = set(lst)

if len(st) == 1:
    print(10000 + A * 1000)
elif len(st) == 3:
    print(max(A, B, C) * 100)
else:
    for i in lst:
        if lst.count(i) == 2:
            print(1000 + i * 100)
            break