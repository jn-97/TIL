# 사분면

n = int(input()) # 점의 개수

AXIS = 0 # 해당되는 곳이 없는 점의 개수
Q1 = 0
Q2 = 0
Q3 = 0 
Q4 = 0

for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        AXIS += 1
    elif x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    elif x > 0 and y < 0:
        Q4 += 1

print('Q1: {}'.format(Q1))
print('Q2: {}'.format(Q2))
print('Q3: {}'.format(Q3))
print('Q4: {}'.format(Q4))
print('AXIS: {}'.format(AXIS))