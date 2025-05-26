import sys

K, N = [int(i) for i in sys.stdin.readline().split()]
K_len_list = []

for i in range(K):
    K_len = int(sys.stdin.readline())
    K_len_list.append(K_len)

start = 1
end = max(K_len_list)

while start <= end:
    result = 0
    total_result = 0
    mid = (start + end) // 2

    for K_len in K_len_list:
        result = K_len // mid
        total_result += result

    if total_result >= N:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)