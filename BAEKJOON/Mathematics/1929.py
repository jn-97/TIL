# 소수 구하기
import sys
sys.stdin = open('1929.txt')

M, N = map(int, input().split())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

primes = []
for i in range(M, N+1):
    if is_prime(i):
        primes.append(i)

for p in primes:
    print(p)