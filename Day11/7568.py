import sys

N = int(sys.stdin.readline())

people = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
rank = 1

for i in range(len(people)):
    rank = 1
    for j in range(len(people)):
        if i != j and people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    print(rank, end = " ")