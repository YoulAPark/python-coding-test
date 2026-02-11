# 1
A, B = input().split() # 슬라이싱[::-1]을 사용하기 위하여 문자열로 입력을 받았다.

A = int(A[::-1]) 
B = int(B[::-1])

if A > B:
    print(int(A))
else:
    print(int(B))

# 2
# max를 활용할 수 있었다.
A, B = input().split()

A = int(A[::-1])
B = int(B[::-1])

print(max(A,B))

# 3
# 진짜 선호하지 않는 코드. 
# 짧게 축약할 수 있으나, 가독성이 보다 떨어지기에 절대 선호하지 않는다.
A, B = input().split()
print(max(int(A[::-1]), int(B[::-1])))
