# 아래 코드는 숫자의 길이를 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# number = 22020718
# print(len(number))

# 원인 : TypeError: object of type 'int' has no len()
# 원인 : int는 len() 함수를 사용할 수 없으므로 int => str로 형변환해야 함

# 수정 코드
number = 22020718
print(len(str(number)))