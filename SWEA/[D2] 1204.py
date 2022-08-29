from collections import Counter

T = int(input())

for _ in range(1, T+1):
    tc = int(input()) # tc 번호
    score = list(map(int, input().split()))

    cnt = Counter(score)
    result = cnt.most_common(1)

    print('#{} {}'.format(tc, result[0][0]))