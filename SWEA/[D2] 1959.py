# 두 개의 숫자열

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))

    score_ = 0 
    sum_ = 0 
    tmp_ = 0
    
    if N < M:
        for j in range(abs(N-M)+1):
            for i in range(N):
                sum_ += n_list[i] * m_list[i+j]
                score_ += 1

                if score_ == N:
                    score_ = 0
                    if sum_ > tmp_:
                        tmp_ = sum_
                    sum_ = 0

    elif N > M:
        for j in range(abs(M-N)+1):
            for i in range(M):
                sum_ += m_list[i] * n_list[i+j]
                score_ += 1

                if score_ == M:
                    score_ = 0
                    if sum_ > tmp_:
                        tmp_ = sum_
                    sum_ = 0

    print(f'#{tc} {tmp_}')