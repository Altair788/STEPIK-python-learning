def is_palindrome(text):
    text = text.lower()
    list = []

    for i in text:
        if i.isdigit():  # тут было isalpha(), но по задаче идут цифры
            list.extend(i)
    for i in range(len(list)):
        if list[:] == list[::-1]:
            return True
        else:
            return False
    #  тут были ошибки: оставлял блок функции
    #  с считыванием данных и вызовом функции
    #  и это мешало выполнению основной задачи


def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False


def is_even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False


def is_valid_password(password):
    password = password.split(':')
    if len(password) == 3:  # здесь потребовалось отдельно прописать ограничение на длину списка
        a = password[0]
        b = password[1]
        c = password[2]
        if is_palindrome(a) == True and is_prime(int(b)) == True and is_even_number(int(c)) == True:
            return True
        else:
            return False
    else:  # и завершить функцию, если длина списка не соответствует условию
        return False


psw = input()

print(is_valid_password(psw))
