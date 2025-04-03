def get_fixed_price(discount_rate, discounted_price):
    original_price = discounted_price / (1 - discount_rate / 100)
    return int(original_price) 

discount_rate = int(input('할인율은? '))

a_discounted = int(input('A 상품의 할인된 가격은? '))
b_discounted = int(input('B 상품의 할인된 가격은? '))

a_original = get_fixed_price(discount_rate, a_discounted)
b_original = get_fixed_price(discount_rate, b_discounted)

print('A 상품의 정가는', a_original, '원')
print('B 상품의 정가는', b_original, '원')
