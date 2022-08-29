# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)

# 원인 : AttributeError: 'tuple' object has no attribute 'append'
# 원인 : 튜플은 데이터를 변경할 수 없기 때문에 .append()등 값을 변경하는 메소드는 사용 X

# 수정 코드
N = 10
answer = []
for number in range(N + 1):
    answer.append(number*2)
print(answer)