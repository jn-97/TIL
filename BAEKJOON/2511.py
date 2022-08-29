A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = A[::-1]
B = B[::-1]

if A == B:
    print('10 10')
    print('D')

else:
    a_score = 0
    b_score = 0
    result = []
    for i in range(10):
        if A[i] > B[i]:
            a_score += 3
            result.append('A')
        elif A[i] == B[i]:
            a_score += 1
            b_score += 1
        else:
            b_score += 3
            result.append('B')

    if a_score > b_score:
        print(a_score, b_score)
        print('A')
    elif a_score < b_score:
        print(a_score, b_score)
        print('B')
    else:
        print(a_score, b_score)
        print(result[0])