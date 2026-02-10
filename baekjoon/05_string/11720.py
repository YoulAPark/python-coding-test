# 1
N = int(input())
number = input()

x = 0
for i in range(len(number)):
    x += int(number[i])
print(x)

# 2
N = int(input())
number = input()

x = 0
for ch in number:
    x += int(ch)
print(x)