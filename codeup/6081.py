str = int(input(), 16) # 16진수로 입력받기

for i in range(1, 16):
    print('%X*%X=%X' %(str, i, (str*i)))