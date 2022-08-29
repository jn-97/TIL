T = int(input())

for tc in range(1, T+1):
    word = input()
    re_word = word[::-1]
    if word == re_word:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))