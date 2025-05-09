def buy(shopping_bag):
    item = input("상품명? ").strip()
    if item == "":
        return False

    shopping_bag.append(item)
    print(f"장바구니에 {item}가(이) 담겼습니다.")
    return True


def show(shopping_bag):
    print("\n>>> 장바구니 보기:", end=" ")
    print(", ".join(shopping_bag))


shopping_bag = []

print('[구입]')
while True:
    if not buy(shopping_bag):
        break

show(shopping_bag)
