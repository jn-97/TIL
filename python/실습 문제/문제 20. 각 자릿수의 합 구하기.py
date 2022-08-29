# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

number = int(input())
sum = 0

while number > 10:
    if number > 10:
        sum += (number%10)
        number = int(number/10)
        if number < 10:
            sum += number
            print(sum)


# 2. 
# number = int(input())
# result = 0

# # number가 0일 때 Stop!
# # int는 0일 때 False
# while number:
#     # 몫은 다음 number가 됨
#     # 나머지는 더해나가면 됨

#     # divmod(x, y) = x를 y로 나누고 결과를 tuple(몫, 나머지)로 반환
#     number, remainder = divmod(number, 10)
#     result += remainder
# print(result)