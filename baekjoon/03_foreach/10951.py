#1
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except EOFError:
        break

#2
# import sys

# for i in sys.stdin:
#     A, B = map(int, i.split())
#     print(A + B)
# sys.stdin = 문자열입력
# sys.stdout = 문자열출력