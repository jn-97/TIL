# 간단한 369 게임

n = int(input())
n_list = []
for i in range(1, n+1):
    n_list.append(i)

    cnt = 0
    for char in str(i):
        if char == '3' or char == '6' or char == '9':
            cnt += 1
    if cnt == 1:
        n_list.pop()
        n_list.append('-')
    elif cnt == 2:
        n_list.pop()
        n_list.append('--')
    elif cnt == 3:
        n_list.pop()
        n_list.append('---')

print(*n_list)