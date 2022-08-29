n = int(input())
N = list(map(int, input().split()))

max = N[0]
min = N[0]

for i in N[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min, max)