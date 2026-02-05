# 1 - 일반적인 출력
N = int(input())
arr = list(map(int, input().split()))

print(min(arr), max(arr))

# 2 - import sys 사용하여 버퍼를 효율적으로 활용한다.
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

print(min(nums), max(nums))