    #  генератор случайных паролей
import random
digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'
punc2= "il1Lo0O"
chars = ''
quantity_password = int(input('Какое количество паролей для генерации вам необходимо?  '))
lenght_password = int(input('Какая длина одного пароля?     '))
numbers_password = input('Включать ли цифры 0123456789? (да/нет)  ')
uppercase_password = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет)    ')
lowercase_password = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет)   ')
punctuation_password = input('Включать ли символы !#$%&*+-=?@^_? (да/нет)    ')
err_symbol_password = input('Исключать ли неоднозначные символы il1Lo0O? (да/нет)   ')

while quantity_password != 0:
    while len(chars) != lenght_password:
        if numbers_password == "да":
            chars += random.choice(digits)
            if len(chars) == lenght_password:
                print(chars)
                break
        if uppercase_password == "да":
            chars += random.choice(uppercase_letters)
            if len(chars) == lenght_password:
                print(chars)
                break
        if lowercase_password == "да":
            chars += random.choice(lowercase_letters)
            if len(chars) == lenght_password:
                print(chars)
                break
        if punctuation_password == "да":
            chars += random.choice(punctuation)
            if len(chars) == lenght_password:
                print(chars)
                break
        if err_symbol_password == "нет":
            chars += random.choice(punc2)
            if len(chars) == lenght_password:
                print(chars)
                break
        if len(chars) < lenght_password:
            continue
    chars = ""
    quantity_password -= 1
    if quantity_password != 0:
        continue
def generate_password(lenght_password, chars):
    password = ""
    for i in range(lenght_password):
        password += random.choice(chars)
    return password

for b in range(quantity_password):
    print(generate_password)
