    #  генератор случайных паролей
import random
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lowercase_letters = [a for a in 'abcdefghijklmnopqrstuvwxyz']
uppercase_letters = [b for b in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
punctuation = [c for c in '!#$%&*+-=?@^_']
chars = ''
quantity_password = int(input('Какое количество паролей для генерации вам необходимо?  '))
lenght_password = int(input('Какая длина одного пароля?     '))
numbers_password = input('Включать ли цифры 0123456789? (да/нет)  ')
capitalletters_password = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет)    ')
lowercase_password = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет)   ')
symbol_password = input('Включать ли символы !#$%&*+-=?@^_? (да/нет)    ')
ex_password = input('Исключать ли неоднозначные символы il1Lo0O? (да/нет)   ')



