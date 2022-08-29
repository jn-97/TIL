# 행복한지 슬픈지

str_ = input()
str_ = list(str_)

h = 0
s = 0

for i in range(len(str_)-2):
    if str_[i] == ':':
        if str_[i+1] == '-':
            if str_[i+2] == ')':
                h += 1
            elif str_[i+2] == '(':
                s += 1

if h == 0 and s == 0:
    print('none')
elif h > s:
    print('happy')
elif s > h:
    print('sad')
elif h == s:
    print('unsure')