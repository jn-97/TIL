# 단어 공부

words = input().upper()
dic = {}

for word in words:
    if dic.get(word):
        dic[word] += 1
    else:
        dic[word] = 1

result = []
for key, value in dic.items():
    if value == max(dic.values()):
        result.append(key)

if len(result) != 1:
    print('?')
else:
    print(result[0])