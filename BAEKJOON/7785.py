# 회사에 있는 사람

n = int(input())

list_ = []
for _ in range(n):
    name, check = input().split()

    if name not in list_ and check == 'enter':
        list_.append(name)
    elif name in list_ and check == 'leave':
        list_.remove(name)


for _ in range(len(list_)):
    print(list_[_])