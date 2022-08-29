# 콘테스트

W_list = []
K_list = []

for _ in range(10):
    W = int(input())
    W_list.append(W)
W_list = sorted(W_list, reverse=True)

for _ in range(10):
    K = int(input())
    K_list.append(K)
K_list = sorted(K_list, reverse=True)

print('{} {}'.format(
    (W_list[0]+W_list[1]+W_list[2]), 
K_list[0]+K_list[1]+K_list[2])
)