import sys

com_num = int(sys.stdin.readline())
link_num = int(sys.stdin.readline())
link = [[] for _ in range(com_num + 1)]
virus = [-1] * (com_num + 1)

for _ in range(link_num):
    a, b = [int(num) for num in sys.stdin.readline().split()]
    link[a].append(b)
    link[b].append(a)

def how_many_virus_com(n):
    virus[n] = 0
    for move in link[n]:
        if virus[move] != 0:
            how_many_virus_com(move)

how_many_virus_com(1)

result = virus.count(0) - 1

print(result)