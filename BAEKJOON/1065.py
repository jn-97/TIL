X = int(input())
result = 0
    
for i in range(1, X+1):
    list_ = list(map(int, str(i)))
    if i < 100:
        result += 1
    elif list_[0] - list_[1] == list_[1] - list_[2]:
        result += 1

print(result)