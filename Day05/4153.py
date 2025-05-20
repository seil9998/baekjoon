while True:
    nums = [int(i) for i in input().split()]

    max_value = max(nums)
    other_value = 0

    for i in nums:
        if i != max_value:
            other_value += i ** 2

    if max_value ** 2 == other_value and other_value != 0:
        print("right")
    elif other_value == 0:
        break
    else:
        print("wrong")