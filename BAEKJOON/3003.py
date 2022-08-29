chess = [1, 1, 2, 2, 2, 8] # 체스 말의 개수
user_input = list(map(int, input().split()))
result = [] 

for i in range(len(user_input)): 
    result.append(chess[i]-user_input[i])
   
print(*result)