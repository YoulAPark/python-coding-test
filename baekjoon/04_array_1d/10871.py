# list comprehensions 사용
N, X = map(int, input().split())
A = list(map(int, input().split()))

even = [x for x in A if x < X]
print(*even)

# 일반출력
N, X = map(int, input().split())
A = list(map(int, input().split()))

even = []
for x in A:
    if x < X:
        even.append(x)
print(*even)