import math

n = int(input())
n_list = list(str(n))
list_ = [0, str(n)]
cnt = 0
sum_ = 0
result = 0

if n == result:
    print('1')

else:
    while n != result:
        if n < 10:
            sum_ = int(list_[0]) + int(list_[1])    
            if int(sum_) < 10:
                list_[0] = list_[1]
                list_[1] = sum_
                result = str(list_[0]) + str(list_[1])
                result = int(result)
                sum_ = 0
                cnt += 1
            else: 
                sum_ = math.trunc(int(sum_)%10)
                list_[0] = list_[1]
                list_[1] = sum_
                result = str(list_[0]) + str(list_[1])
                result = int(result)
                cnt += 1

        elif n >= 10:
            sum_ = int(n_list[0]) + int(n_list[1])
            if int(sum_) < 10:
                n_list[0] = n_list[1]
                n_list[1] = sum_
                result = str(n_list[0]) + str(n_list[1])
                result = int(result)
                sum_ = 0
                cnt += 1
                
            else: 
                sum_ = math.trunc(int(sum_)%10)
                n_list[0] = n_list[1]
                n_list[1] = sum_
                result = str(n_list[0]) + str(n_list[1])
                result = int(result)
                cnt += 1
    print(cnt)