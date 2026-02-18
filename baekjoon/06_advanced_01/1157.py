word = input().upper()

# 1. 알파벳 개수 세기
count_dict = {}

for ch in word:
    if ch in count_dict:
        count_dict[ch] += 1
    else:
        count_dict[ch] = 1

# 2. 최댓값 찾기
max_value = max(count_dict.values())

# 3. 최댓값을 가진 문자들 찾기
max_keys = []

for key in count_dict:
    if count_dict[key] == max_value:
        max_keys.append(key)

# 4. 출력
if len(max_keys) > 1:
    print("?")
else:
    print(max_keys[0])