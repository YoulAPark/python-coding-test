student = list(range(1, 30+1))

for _ in range(28):
    student.remove(int(input()))

print(min(student))
print(max(student))