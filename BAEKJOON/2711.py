T = int(input())

for tc in range(T):
    a, b = input().split()
    a = int(a)
    
    list_ = list(b)
    list_.pop(a-1)
    print(*list_, sep='')