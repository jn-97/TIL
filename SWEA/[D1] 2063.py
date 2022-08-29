import math

n = int(input())
score = list(map(int, input().split()))
score.sort()

result = math.trunc(n/2) 
print(score[result])