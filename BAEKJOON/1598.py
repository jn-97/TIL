# 꼬리를 무는 숫자 나열 

x, y = map(int, input().split())

x -= 1 
y -= 1

print(abs(x//4-y//4) + abs(x%4 - y%4))