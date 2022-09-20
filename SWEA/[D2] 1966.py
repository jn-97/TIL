# 숫자를 정렬하자

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    n_list = list(map(int, input().split()))

    n_list = sorted(n_list)
    print(f'#{tc}', *n_list)