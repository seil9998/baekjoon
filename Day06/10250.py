T = int(input())

for k in range(T):
    H, W, N = input().split()
    H, W, N = int(H), int(W), int(N)
    hotel = [f"{i}{j:02}" for j in range(1, W + 1) for i in range(1, H + 1)]
    result = hotel[N-1]
    print(result)