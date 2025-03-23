def get_integer(prompt):
    res = int(input(prompt))
    return res

def exchange(amount):
    count_500 = amount // 500
    amount = amount % 500

    count_100 = amount // 100
    amount = amount % 100

    count_50 = amount // 50
    amount = amount % 50

    count_10 = amount // 10
    amount = amount % 10

    print("500원 동전의 개수: ", count_500)
    print("100원 동전의 개수: ", count_100)
    print("50원 동전의 개수: ", count_50)
    print("10원 동전의 개수: ", count_10)

amount = get_integer("동전으로 교환하고자 하는 금액은?")
exchange(amount)
