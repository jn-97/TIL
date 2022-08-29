# 100을 사용자가 입력한 숫자로 나눠서 결과를 출력
number = input()

try:
    print(100/int(number))

except ZeroDivisionError as err: # 오류가 있다면 실행
    print(err)
    print('0으로 나눌 수는 없습니다.')
except ValueError:
    print('숫자 형식을 입력해주세요.')
except Exception: # 가장 상위의 오류라서 가장 나중에 작성하기
    print('오류')
else: # 오류가 없다면 실행
    print('숫자 : ', number)
finally:
    print('종료')