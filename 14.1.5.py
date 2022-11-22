def get_month(language, number):
    en = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
          'november',
          'december']

    ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
          'декабрь']

    if language == 'ru':
        return ru[number]
    if language == 'en':
        return en[number]

lan = input()
num = int(input())

print(get_month(lan, num))
