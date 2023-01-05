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


# Задание 3
class Tomato:

    states = {0: 'sead', 1: 'flower', 2: 'green tomato', 3: 'red tomato'}

    def init(self, index, state):
        self.index = index
        self.state = state

    def grow(self):
        self._change_states()


    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class TomatoBush:

    def _init_(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()


