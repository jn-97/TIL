import sys
sys.stdin = open('11931.txt')

n = int(input())

arr = []
for _ in range(n):
  x = int(input())
  arr.append(x)
arr.sort(reverse=True)

for a in arr:
  print(a)