import sys
from decimal import Decimal, ROUND_HALF_UP

n = int(sys.stdin.readline())

if n == 0:
    average_rounded = 0
else:
    opinions = [int(sys.stdin.readline()) for i in range(n)]
    opinions.sort()

    delete_index = Decimal(n * 0.3 / 2)
    delete_index_rounded = int(delete_index.quantize(Decimal("0"), rounding = ROUND_HALF_UP))

    opinions_for_average = opinions[delete_index_rounded : len(opinions) - delete_index_rounded]

    average = Decimal(sum(opinions_for_average) / len(opinions_for_average))
    average_rounded = int(average.quantize(Decimal("0"), rounding = ROUND_HALF_UP))

print(average_rounded)