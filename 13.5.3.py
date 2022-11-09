# объявление функции
def get_next_prime(num):
    list = []
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
            list.append(num)
            num += 1
    return list[1:]




# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))