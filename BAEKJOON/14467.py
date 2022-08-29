# 소가 길을 건너간 이유 1

N = int(input())
result = [[] for _ in range(10)]
p_list = [[] for _ in range(10)] # 비교할 소의 위치 리스트
cnt = 0

for _ in range(N):
    n, p = map(int, input().split()) # 소 번호, 위치

    if result[n-1] == []: # n번째 리스트가 비어있으면
        result[n-1].append(p) # n번째 리스트에 소의 위치 추가
        p_list[n-1].append(p) # 비교할 p_리스트에도 소의 위치 추가
        continue 

    if p_list[n-1] != []: # p_list가 비어있지 않으면
        p_list[n-1].pop() # 반복문이 진행될 때마다 지우고 다시 소의 위치 업데이트
        p_list[n-1].append(p)
    
    if p_list[n-1] != result[n-1]: # p_list랑 result_list랑 값이 다르면
        cnt += 1 # 1 추가
        result[n-1].pop() # result 업데이트
        result[n-1].append(p)
    else:
        pass

print(cnt)