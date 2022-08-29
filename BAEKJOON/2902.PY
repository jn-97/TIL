# KMP는 왜 KMP일까?

memo = list(input())
result = []
result.append(memo[0])

for i in range(len(memo)):
    if memo[i] == '-':
        result.append(memo[i+1])
print(*result, sep='')