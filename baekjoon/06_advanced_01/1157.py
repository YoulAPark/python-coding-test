import string

word = input().upper()

max_count = 0
result = ""

for ch in string.ascii_uppercase: # 모든 알파벳을 대문자로 출력하기 위해 사용하였다.
    count = word.count(ch)

    if count > max_count:
        max_count = count
        result = ch
    elif count == max_count:
        result = "?"

print(result)