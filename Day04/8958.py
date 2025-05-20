T = int(input())

for i in range(T):
    score = 0
    result_score = 0
    result = input()
    for i in result:
        if i == "X":
            score = 0
        else:
            score += 1
            result_score += score
    print(result_score)
