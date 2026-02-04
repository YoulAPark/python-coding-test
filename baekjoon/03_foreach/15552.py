# 1
import sys

input = sys.stdin.readline
T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(A + B)

# 2
import sys
input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    A, B = map(int, input().split())
    out.append(str(A + B))

sys.stdout.write("\n".join(out))