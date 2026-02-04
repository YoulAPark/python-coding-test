X = int(input()) # 영수증 총 금액
N = int(input()) # 영수증 총 구매개수

amount = 0

for i in range(N):
    price, quantity = map(int, input().split()) # 각 물건의 가격, 개수
    amount += (price * quantity)

if X == amount:
    print("Yes")
else:
    print("No")