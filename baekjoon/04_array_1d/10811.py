N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(i+1)

for _ in range(M):
    i,j = map(int, input().split())

    even = arr[i-1:j][::-1]
    even2 = arr[j:N]

    print(even+ even2)
    

    
