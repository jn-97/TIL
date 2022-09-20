# 쉬운 거스름돈

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    result = []
    while n != 0:
        if n//50000 > 0:
            result.append(n//50000)
            n = n%50000
        else:
            result.append(0)
        if n//10000 > 0:
            result.append(n//10000)
            n = n%10000
        else:
            result.append(0)
        if n//5000 > 0:           
            result.append(n//5000)
            n = n%5000
        else:
            result.append(0)
        if n//1000 > 0:
            result.append(n//1000)
            n = n%1000
        else:
            result.append(0)
        if n//500 > 0:
            result.append(n//500)
            n = n%500
        else:
            result.append(0)
        if n//100 > 0:
            result.append(n//100)
            n = n%100
        else:
            result.append(0)
        if n//50 > 0:
            result.append(n//50)
            n = n%50
        else:
            result.append(0)
        if n//10 > 0:
            result.append(n//10)
            n = n%10
        else:
            result.append(0)

    print(f'#{tc}')
    print(*result)
        