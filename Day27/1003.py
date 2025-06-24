import sys

T = int(sys.stdin.readline())

for _ in range(T):
    num = int(sys.stdin.readline())
    count_0 = []
    count_1 = []
    for n in range(num+1):
        if n == 0:
            count_0.append(1)
            count_1.append(0)
        elif n == 1:
            count_0.append(0)
            count_1.append(1)
        else:
            count_0.append(count_0[n-1] + count_0[n-2])
            count_1.append(count_1[n-1] + count_1[n-2])
    
    print(count_0[num], count_1[num])
