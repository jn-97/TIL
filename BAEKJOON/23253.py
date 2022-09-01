# 자료구조는 정말 최고야

N, M = map(int, input().split())

bool_ = True

for _ in range(M):
    k1 = int(input())
    k2 = list(map(int, input().split()))

    for j in range(k1-1):
        if k2[j] < k2[j+1]:
            bool_ = False
            break
    
    if not bool_:
        break

print('Yes' if bool_ else 'No')