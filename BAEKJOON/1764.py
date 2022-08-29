# 듣보잡

N, M = map(int, input().split())

n_list = [] # 듣도 못한 사람 
m_list = [] # 보도 못한 사람

for _ in range(N):
    n_str = input()
    n_list.append(n_str)

for _ in range(M):
    m_str = input()
    m_list.append(m_str)

cnt = 0
result = []
for i in range(len(m_list)):
    if m_list[i] in n_list:
        result.append(m_list[i])
        cnt += 1

print(cnt)
for _ in range(len(result)):
    print(result[_])