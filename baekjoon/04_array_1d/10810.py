N, M = map(int, input().split())

# basket = [0] * N으로 대체 가능
basket = []
for _ in range(N):
    basket.append(0)

for i in range(M):
    i, j, k = map(int, input().split())

    for n in range(i-1, j):
        basket[n] = k

print(*basket)

