# 베스트셀러

N = int(input())
books = {}

for _ in range(N):
    book = input()

    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

max_ = max(books.values())
result = [] 

for book, number in books.items():
    if number == max_:
        result.append(book)
    
print(sorted(result)[0])