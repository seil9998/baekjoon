import sys

N = int(sys.stdin.readline())

words = list({sys.stdin.readline().strip() for _ in range(N)})

words.sort(key = lambda x:(len(x), x))

for word in words:
    print(word)