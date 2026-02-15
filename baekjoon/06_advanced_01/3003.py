# 1
amount = list(map(int, input().split()))
piece = [1, 1, 2, 2, 2, 8]

arr = [piece[i] - amount[i] for i in range(len(amount))]

print(*arr)

# 2
amount = list(map(int, input().split()))
piece = [1, 1, 2, 2, 2, 8]

print(*(p - a for p, a in zip(piece, amount)))