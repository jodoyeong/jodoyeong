def read_single_digit(integer):
    if integer == 0:
        return '영'
    if integer == 1:
        return '일'
    if integer == 2:
        return '이'
    if integer == 3:
        return '삼'
    if integer == 4:
        return '사'
    if integer == 5:
        return '오'
    if integer == 6:
        return '육'
    if integer == 7:
        return '칠'
    if integer == 8:
        return '팔'
    if integer == 9:
        return '구'
        
def read_number(num):
    hundred = num // 100
    ten = (num % 100) // 10
    one = (num % 100) % 10 % 10
    print(read_single_digit(hundred), read_single_digit(ten), read_single_digit(one))

num = int(input('세 자리 정수 입력: '))
read_number(num)
