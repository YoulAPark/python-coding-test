import string

S = input()

result = []
for ch in string.ascii_lowercase:
    result.append(S.find(ch))

print(*result)