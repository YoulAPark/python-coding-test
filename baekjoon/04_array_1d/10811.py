N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(i+1)

for _ in range(M):
    i,j = map(int, input().split())
    arr[i-1:j] = arr[i-1:j][::-1] 

print(*arr)

# arr[i:j] = i부터 j까지의 arr
# [::-1] = 배열을 뒤집겠다 라는 의미