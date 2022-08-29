# 삼각형 외우기

t_list = []
for _ in range(3):
    t = int(input())
    t_list.append(t)

sum_ = 0
for i in range(len(t_list)):
    sum_ += t_list[i]

if sum_ == 180:
    if t_list[0] != t_list[1] and t_list[0] != t_list[2] and t_list[1] != t_list[2]:
        print('Scalene') # 같은 각이 없는 경우
    elif t_list[0] == t_list[1] and t_list[0] == t_list[2] and t_list[1] == t_list[2]:
        print('Equilateral') # 세 각의 크기가 모두 60인 경우
    elif t_list[0] == t_list[1] or t_list[0] == t_list[2] or t_list[1] == t_list[2]:
        print('Isosceles') # 두 각이 같은 경우
else:
    print('Error')