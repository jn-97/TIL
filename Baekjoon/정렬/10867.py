# 중복 빼고 정렬하기
import sys
sys.stdin = open("10867.txt")
input = sys.stdin.readline

N = int(input())
numbers = sorted(set(map(int, input().split())))

print(*numbers)