# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return True
    flag1 = False
    flag2 = False
    flag3 = False
    for i in password:
        if i.islower():
            flag1 = True
        elif i.isupper():
            flag2 = True
        elif i.isdigit():
            flag3 = True
    return flag2 and flag1 and flag3

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))