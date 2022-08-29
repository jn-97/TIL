# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

n = 1
while n != 0:
    n = int(input())
    if n != 0:
        print(n)
    else:
        break