import sys

Y = int(sys.stdin.readline())
count = 0

while count < Y:
    count += 1
    balance = 0
    vps = sys.stdin.readline().strip()

    for i in vps:
        if i == "(":
            balance += 1

        if i == ")":
            balance -= 1
        
        if balance < 0:
            print("NO")
            skip = True
            break
    else:
        if balance == 0:
            print("YES")
        else:
            print("NO")