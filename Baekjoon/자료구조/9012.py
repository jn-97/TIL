# 괄호
import sys
sys.stdin = open("9012.txt")

for _ in range(int(input())):
    VPS = list(input())
    isVPS = True

    list_ = []
    for v in VPS:
        if v == "(":
            list_.append(v)
        else:
            if len(list_) > 0:
                list_.pop()
            else:
                isVPS = False
                break

    if isVPS == True and len(list_) == 0:
        print('YES')
    else:
        print('NO')