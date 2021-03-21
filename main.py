# Constants:
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
text_first = 'Пожалуйста, введите номер вашей банковской карты: '
text_try_right = 'Пожалуйста, введите номер карты корректно: '
text_wrong = 'Номер карты введен неверно.'
text_right = 'Номер карты введен корректно.'
text_repeat = 'Убедитесь в правильности номера карты: '


card_num = input(text_first)


def correct_number(card_num):       # This function inquires entering the card number until it only consists of numbers
    while True:
        card_num = input(text_repeat)
        card_num = card_num.replace(' ', '')
        for i in card_num:
            if i not in numbers or len(card_num) < 13 or len(card_num) > 16:
                continue
            else:

                return card_num


card_num = correct_number(card_num)


def card_firm(card_num):           # This function defines the payment system of the card
    if card_num[0] == '4':
        firm = 'Visa'
    elif card_num[0] == '5':
        firm = 'MasterCard'
    elif card_num[0:2] == '37':
        firm = 'American Express'
    elif card_num[0] == '6':
        firm = 'Discover'
    elif card_num[0] == '2':
        firm = 'Мир'
    else:
        firm = text_wrong

    return firm


firm = card_firm(card_num)


def right_number(card_num):           # This function determines if the card is correct
    card_num_invers = card_num[::-1]
    even = int(card_num_invers[::-2])
    odd = int(card_num[::-2])
    sum_odd = 0
    sum_even = 0
    for i in str(odd):
        sum_odd += int(i)
    for i in str(even):
        a = int(i) * 2
        if a > 9:
            a = a//10 + a%10
            sum_even += a
        else:
            sum_even += int(a)
        full_sum = sum_even + sum_odd

    return full_sum


full_sum = right_number(card_num)


def main(full_sum, firm):
    if full_sum % 10 == 0 and firm != text_wrong:
        print(text_right, '{}'.format('Платежная система -'),  firm)
    else:
        print(text_wrong)


finish = main(full_sum, firm)
