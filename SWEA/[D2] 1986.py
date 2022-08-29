# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

T = int(input())

for tc in range(T):
    sum = 0
    n = int(input())
    for i in range(n+1):
        if i%2!=0:
            sum += i
        else:
            sum -= i
    print('#{} {}'.format((tc+1), sum))