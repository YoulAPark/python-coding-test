# 1
T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)

    arr = []
    for ch in S:
        arr.append(ch * R)

    print(''.join(arr))

# 2
T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)

    arr = [ch * R for ch in S]

    print(''.join(arr))

# 3
T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)

    for ch in S:
        print(ch * R, end='')

    print()