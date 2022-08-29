T = int(input())

for tc in range(1, T+1):
    list_ = list(map(int, input().split()))

    max_ = 0
    for i in range(len(list_)):
        if list_[i] > max_:
            max_ = list_[i]

    print('#{} {}'.format(tc, max_))