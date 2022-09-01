# 모음이 보이지 않는 사람

list_ = ['a','e','i','o','u']
T = int(input())

for tc in range(1, T+1):
    result = [] 
    words = input()

    for word in words:
        if word not in list_:
            result.append(word)

    print('#'+str(tc)+' ', *result, sep='')