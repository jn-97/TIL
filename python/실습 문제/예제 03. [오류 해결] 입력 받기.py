# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# numbers = input().split()
# print(sum(numbers))

# 원인 : TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 원인 : 변수 numbers는 string형, sum은 int형

# 수정 코드 
numbers = input().split()
numbers = map(int, numbers)
# map은 리스트의 요소를 지정된 함수로 처리해주는 함수
print(sum(numbers))