# 정수 3개를 입력받아 합과 평균을 출력해보자.

a, b, c = map(int, input().split())
sum = a + b + c
avg = (a + b + c) / 3
print(sum, f'{avg:.2f}')