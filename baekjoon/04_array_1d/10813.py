# 1
N, M = map(int, input().split())

# # 1부터 N+1까지의 list 생성
# basket = list(range(1, N+1))
basket = [0] * N
for i in range(N):
    basket[i] = i + 1

for _ in range(M):
    i, j = map(int, input().split())

    a = basket[i-1]
    b = basket[j-1]

    basket[i-1] = b
    basket[j-1] = a

    # 파이썬 swap 스왑방식
    # basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)

# 2
# N, M = map(int, input().split())

# basket = list(range(1, N+1))

# for _ in range(M):
#     i, j = map(int, input().split())
#     basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

# print(*basket)
