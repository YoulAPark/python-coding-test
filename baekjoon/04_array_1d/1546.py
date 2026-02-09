N = int(input())

arr = list(map(int, input().split()))
max_score = max(arr)

for i in range(N):
    arr[i] = arr[i]/max_score*100

print(sum(arr)/N)