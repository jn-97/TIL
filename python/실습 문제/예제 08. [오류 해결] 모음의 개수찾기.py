# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

# 원인 : 모든 알파벳에서 모음이 있으면 count += 1 이기 때문에 각각의 값에 char을 넣어야 함

# 수정 코드
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or  char == "i" or  char == "o" or char == "u":
        count += 1

print(count)