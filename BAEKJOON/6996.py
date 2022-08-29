# 애너그램
import sys

sys.stdin = open('6996.txt')

n = int(input())

for _ in range(n):
    a, b = input().split()

    s_a = sorted(a)
    s_b = sorted(b)

    if s_a == s_b:
        print('{} & {} are anagrams.'.format(a, b))
    else:
        print('{} & {} are NOT anagrams.'.format(a, b))