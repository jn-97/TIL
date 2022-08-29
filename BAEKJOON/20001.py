# 문제가 없는데 고무오리를 출력하면 문제 += 2
# 모든 문제 해결하면 "고무오리야 사랑해" 출력
# 문제 해결 못하면 "힝구" 출력

start = input() # 고무오리 디버깅 시작
answer = ''
cnt = 0

while True: # while문 무한반복
    answer = input()
    if answer=='고무오리 디버깅 끝':
        break
    elif answer=='문제':
        cnt += 1
    elif cnt==0 and answer=='고무오리':
        cnt += 2
    elif answer=='고무오리':
        cnt -= 1

if cnt==0:
    print('고무오리야 사랑해')
else:
    print('힝구')