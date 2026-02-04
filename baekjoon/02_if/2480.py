# 배열 내 요소의 개수와 배열 내 중복요소의 개수를 비교하여 처리하였다.

x, y, z = map(int, input().split())
arr = [x, y, z] # 배열에 담는다.

# len(arr) = 배열 내 요소의 개수
# len(set(arr)) = 배열 내 중복요소의 개수
if len(arr) != len(set(arr)):
    kind = len(set(arr))

    if (kind == 1): # 3개가 같은 값일 경우
        print(10000 + x * 1000)
    elif (kind == 2): # 2개가 같은 값일 경우
        if x == y or x == z:
            print(1000 + x * 100)
        elif y == z: 
            print(1000 + y * 100)

else:
    print(max(arr) * 100)