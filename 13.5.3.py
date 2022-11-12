def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False
# объявление функции
def get_next_prime(num):
    num += 1
    while is_prime(num) == False:
        num += 1
    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))