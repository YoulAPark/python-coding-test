# # 1번
arr = []
for _ in range(10):
    number = int(input()) % 42
    arr.append(number)
print(len(set(arr)))

# # 2번 - 리스트 컴프리헨션 사용
arr = []
arr = [int(input()) % 42 for i in range(10)]
print(len(set(arr)))