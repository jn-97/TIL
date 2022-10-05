# 알파벳 공부

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

T = int(input())

for tc in range(1, T+1):
    str_ = list(input())

    cnt = 0
    for i in range(len(str_)):
        if str_[i] == alphabet[i]:
            cnt += 1
        else:
            break

    print(f'#{tc} {cnt}')