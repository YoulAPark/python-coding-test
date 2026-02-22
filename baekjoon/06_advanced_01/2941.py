word = input()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for ch in croatia:
    word = word.replace(ch, "*") # 크로아티아 알파벳을 "*"로 치환한다.

print(len(word))