TaeBo = input()
list_ = list(TaeBo)

cnt = 0
for i in range(len(list_)):
    
    if list_[i] == 0 and list_[i] == '@':
        pass
    elif list_[i] == '@':
        cnt += 1
    elif list_[i] == '(':
        i += 4
        left = cnt
        cnt = 0

print(left, cnt)