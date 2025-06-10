N = int(input())

shirts = [int(i) for i in input().split()]

shirts_group, pen_group = [int(i) for i in input().split()]

shirts_result = 0

for i in shirts:
    if i % shirts_group != 0:
        shirts_result += (i // shirts_group + 1)
    else:
        shirts_result += (i // shirts_group)

pen_result = N // pen_group
pens = N - pen_group * (N // pen_group)

print(shirts_result)
print(pen_result, pens)