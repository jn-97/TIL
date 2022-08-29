# 가장 많은 글자
import sys

words = sys.stdin.read().replace('\n', '').replace(' ','') # 한꺼번에 입력
result = [0]*26

for i in words:
    result[ord(i)-97] += 1

for j in range(26):
    if result[j] == max(result):
        print(chr(97+j), end='')