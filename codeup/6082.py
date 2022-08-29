n = int(input())
list_ = []

for i in range(1, n+1):
    if i%10==3 or i%10==6 or i%10==9:
        list_.append('X')
    else:
        list_.append(i)

print(*list_, end='')