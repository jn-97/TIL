ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6 ,5, 4, 3, 2, 1]

numbers = list(map(int, input().split()))

a_cnt = 0
b_cnt = 0
for i in range(len(numbers)):
    if numbers[i] == ascending[i]:
        a_cnt += 1
    elif numbers[i] == descending[i]:
        b_cnt += 1
    else:
        break

if a_cnt == 8:
    print('ascending')
elif b_cnt == 8:
    print('descending')
else:
    print('mixed')