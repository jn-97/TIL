# 두 정수(a, b)를 입력받아
# a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력

a, b = map(int, input().split())

if a == b:
    print(True)
else:
    print(False)