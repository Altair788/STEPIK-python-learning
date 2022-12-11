
#   алгоритм игры
def ugaday_ka():
    import random
    x = random.randrange(0, 101)
    print(x)
    a = (input('Введи свой вариант числа     '))
    if a.isdigit() is False:
        digit()
    else:
        a = int(a)
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
                ugaday_ka()
            else:
                disagree(answer)

#   отказ от игры
def disagree(answer):
    for i in range(1):
        if answer.lower() == 'нет':
            print('Возвращайся, когда передумаешь')
            answer = input('А может разок сыграем? "да" или "нет" ?  ')
            if answer.lower() == 'да':
                ugaday_ka()
            elif answer.lower() == 'нет':
                print('Хорошо - хорошо :) Возвращайся, когда передумаешь')


#   правила игры
def rules():
    print('Давай ознакомлю тебя с правилами игры.')
    print('Я загадаю число от 0 до 100, а ты будешь его отгадывать.')
    input('А теперь напиши что-нибудь, чтобы я был уверен, что ты понял правила игры ;-)    ')

#   проверка правильности
def digit():
    print('Это не число :(')
    print('Введи, пожалуйста, число')
    ugaday_ka()

answer = input('Привет! Меня зовут Эдуард и я написал код для игры "Угадай-ка". Хочешь в нее поиграть?   ')

for i in range(1):
    if answer.lower() == 'да':
        rules()
        ugaday_ka()
    else:
        disagree(answer)
