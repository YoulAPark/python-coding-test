arr = []
for _ in range(9):
    arr.append(int(input()))

n = max(arr)
print(n)
print(arr.index(n) + 1)