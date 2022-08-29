list_ = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

words = input()
result = []

for word in words:
    if word not in list_:
        result.append(word)

print(*result, sep='')