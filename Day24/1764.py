import sys

N, M = [int(num) for num in sys.stdin.readline().split()]

persons_1 = set()
result = []

for _ in range(N):
    person = sys.stdin.readline().strip()
    persons_1.add(person)

for _ in range(M):
    person = sys.stdin.readline().strip()
    if person in persons_1:
        result.append(person)

result.sort()

print(len(result))
for person in result:
    print(person)