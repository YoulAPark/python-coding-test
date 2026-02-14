# 1
while True:
    try:
        line = input()
        print(line)
    except EOFError:
        break

# 2
import sys

for word in sys.stdin:
    print(word, end='')