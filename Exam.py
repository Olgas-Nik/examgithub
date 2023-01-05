# Задание 1
# Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

def card_fun(card):
    return '*' * len(card[:-4]) + card[-4:]


print(card_fun('1234123412341234'))


# Задание 2
# Напишите функцию, которая проверяет: является ли слово палиндромом

#
word = input('Enter world: ')
def check_pal(string):
    if str(word) == str(word)[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

print(check_pal(word))

