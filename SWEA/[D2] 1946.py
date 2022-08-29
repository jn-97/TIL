# 간단한 압축 풀기

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    result = ''
    for i in range(N):
        C, K = input().split()
        K = int(K)
        result += C*K
    print('#{}'.format(tc)) # #1 출력
    
    for i in range(len(result)):
        if (i+1)%10 == 0:
            print(result[i])
        else:
            print(result[i], end='')
    print()