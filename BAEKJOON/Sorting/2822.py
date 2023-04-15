import sys
sys.stdin = open("2822.txt")

scores = []  # 점수를 저장할 리스트

for i in range(8):
    scores.append(int(input()))  # 점수를 입력받아 리스트에 추가

top_scores = sorted(scores, reverse=True)[:5]  # 상위 5개 점수를 내림차순으로 정렬하여 추출

total_score = sum(top_scores)  # 상위 5개 점수의 합을 계산

print(total_score)

# 상위 5개 점수의 인덱스를 출력하는 코드
for i, score in enumerate(scores):
    if score in top_scores:
        print(i+1, end=" ")