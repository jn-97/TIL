# FBI
from pprint import pprint
import sys

sys.stdin = open('2857.txt')

result = [] 
for i in range(1, 6):
    fbi = input()
    if 'FBI' in fbi:
        result.append(i)

if result:
    print(*result)
else:
    print('HE GOT AWAY!')