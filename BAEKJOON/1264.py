# 모음의 개수

word = ['a', 'e', 'i', 'o', 'u']

while True:
    str_ = input()
    if str_ == '#':
        break
    str_ = str_.lower()
    cnt = 0
    for char in str_:
        if char in word:
            cnt += 1

    print(cnt)