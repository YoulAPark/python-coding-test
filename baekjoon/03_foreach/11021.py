T = int(input())
for i in range(1, T+1):
    A, B = map(int, input().split())
    print("Case #" + str(i) + ":", A+B)

# f-string : 문자열 내 변수/식을 바로 넣는 문법
# T = input()
# name = "jennifer"
# print(f"나는 {T}")
# print(f"나는 {name}")

# # f-string 사용
# T = int(input())

# for i in range(1, T+1): 
#     A, B = map(int, input().split())
#     print(f"Case #{i}: {A+B}")

# # sep() 출력할 문자열 사이에 넣을 구분자
# # print("A", "B", sep="")
# # print("+82", "1234", "1234", "-")

# # sep() 사용
# T = int(input())

# for i in range(1, T+1):
#     A, B = map(int, input().split())
#     print("Case #" + str(i) + ":", A+B, sep=" ")