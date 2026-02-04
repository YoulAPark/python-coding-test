H, M = map(int, input().split())
time = int(input())

total = (H * 60) + M + time

H = total // 60
M = total % 60

H %= 24

print(H, M)