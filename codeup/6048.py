# 두 정수(a, b)를 입력받아
# a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력

a, b = map(int, input().split())

if a < b:
    print(True)
else:
    print(False)