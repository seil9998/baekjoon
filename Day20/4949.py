import sys

T = True

while T:
    stack = [] # []
    sentence = sys.stdin.readline().rstrip()

    if sentence == ".":
        T = False
        break

    for s in sentence:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if not stack or stack[-1] != "(":
                print("no")
                break
            else:
                stack.pop()
        elif s == "]":
            if not stack or stack[-1] != "[":
                print("no")
                break 
            else:
                stack.pop()

    else:
        if not stack:
            print("yes")
        else:
            print("no")