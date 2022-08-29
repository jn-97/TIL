T = int(input())

for tc in range(1, T+1):
    N = int(input())
    list_ = list(map(int, input().split()))

    sum_ = 0
    last_ = list_[-1]
    
    for i in range(len(list_)-1, -1, -1): # 뒤에서부터 차례대로
        if list_[i] < last_:
            sum_ += (last_ - list_[i])
        else: 
            last_ = list_[i]

    print('#{} {}'.format(tc, sum_))    