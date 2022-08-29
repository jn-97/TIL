T = int(input())

for tc in range(1, T+1):
    # input 가져오기
    N = int(input())
    N1 = N
    # set에 계속 추가 예정
    numbers = set()
    # while 반복
    while True:
        # for 반복 : 숫자를 문자로
        for n in str(N): 
        # numbers set에 추가
            numbers.add(n)
        if len(numbers) == 10:
            break
        # print(n, numbers)
        N += N1
    print(f'#{tc} {N}')