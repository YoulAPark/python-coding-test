## .strip() 공백제거

```python
word = "JENN I \n FER"
word.strip()
```

- 결과 : JENNIFER

# 문자열 반복

## 1. 숫자 반복 : 0부터 5까지 출력하세요

```python
for i in range(6):
    print(i)
```

## 2. 시작값, 끝값 지정 : 2부터 5까지 출력하세요

```python
for i in range(2,6):
    print(i)
```

## 3. 증가폭 - 1부터 10까지 2씩 늘리세요

```python
for i in range(1, 10, 2):
    print(i)
```

## 4. 리스트/문자열 반복

```python
word = "hello"
for ch in word:
    print(ch)
```

```python
word = ["hello", "hi"]
for ch in word:
    print(ch)
```

## 5. 인덱스 + 값

```python
word = "hello"
for i, ch in enumerate(word):
    print(i, ch)
```
