#   алгоритм игры
def ugaday_ka(a):
    import random
    x = random.randrange(0, 101)
    print(x)
    a = int(input('Я загадал число от 0 до 100. Попробуй его угадать. Введи свой вариант   '))
    for i in range(1):
        while a != x:
            if a > x:
                a = int(input('Слишком много, введи другое число   '))
                continue
            elif a < x:
                a = int(input('Слишком мало, введи другое число   '))
                continue
        if a == x:
            answer = input('Ты угадал! Поздравляю!!! Хочешь попробовать еще раз?  ' )
            if answer.lower() == 'да':
                ugaday_ka(a)
            else:
                disagree(answer)

#   отказ от игры
def disagree(answer):
    for i in range(1):
        if answer.lower() == 'нет':
            print('Возвращайся, когда передумаешь')
            answer = input('А может разок сыграем? "да" или "нет" ?  ')
            if answer.lower() == 'да':
                ugaday_ka(a)
            elif answer.lower() == 'нет':
                print('Хорошо - хорошо :) Возвращайся, когда передумаешь')

answer = input('Привет! Меня зовут Эдуард и я написал код для игры "Угадай-ка". Хочешь в нее поиграть?   ')
a = ''
for i in range(1):
    if answer.lower() == 'да':
        ugaday_ka(a)
    else:
        disagree(answer)
