import sys

N = int(sys.stdin.readline())
cards = [int(card) for card in sys.stdin.readline().split()]

M = int(sys.stdin.readline())
nums = [int(num) for num in sys.stdin.readline().split()]

check_nums = {int(num):0 for num in nums}

for card in cards:
    if card in check_nums:
        check_nums[card] += 1
    else:
        continue

for num in nums:
    print(check_nums[num], end = " ")

print()