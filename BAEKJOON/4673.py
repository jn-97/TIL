# 셀프 넘버
from pprint import pprint

list_1 = []
for _ in range(1, 10001):
    list_1.append(_)

list_2 = []

for n in list_1: # list_1의 원소 하나하나 꺼내서
    for n_ in str(n): # list_1의 원소의 값 하나하나를
        n += int(n_) # n 원소에 더해준다

    if n <= 10000:
        list_2.append(n)

for n in set(list_2):
    list_1.remove(n)

for n_ in list_1:
    print(n_) 