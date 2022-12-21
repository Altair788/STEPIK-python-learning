
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
    if is_valid(a) is False:
        print('А может быть введем целое число от 1 до 100?')
        ugaday_ka()
    else:
        a = int(a)
        for i in range(1):
            while a != x:
                if a > x:
                    a = int(input('Слишком много, введи другое число   '))
                    if is_valid(a) is False:
                        print('А может быть введем целое число от 1 до 100?')
                        ugaday_ka()
                    continue
                elif a < x:
                    a = int(input('Слишком мало, введи другое число   '))
                    if is_valid(a) is False:
                        print('А может быть введем целое число от 1 до 100?')
                        ugaday_ka()
                    continue
            if a == x:
                answer = input('Ты угадал! Поздравляю!!! Спасибо, что поиграли в числовую угадайку со мной! Хочешь попробовать еще раз?  ' )
                if answer.lower() == 'да':
                    ugaday_ka()
                else:
                    disagree(answer)

#   отказ от игры
def disagree(answer):
    for i in range(1):
        if answer.lower() == 'нет':
            print('Возвращайся, когда передумаешь')
            print('Спасибо, что поиграли в числовую угадайку со мной!')
            answer = input('А может разок сыграем? "да" или "нет" ?  ')
            if answer.lower() == 'да':
                ugaday_ka()
            elif answer.lower() == 'нет':
                print('Хорошо - хорошо :) Возвращайся, когда передумаешь')
                print('Спасибо, что поиграли в числовую угадайку со мной!')


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
def is_valid(a):
    if 1 <= int(a) <= 100:
        return True
    else:
        return False

answer = input('Привет! Меня зовут Эдуард и я написал код для игры "Угадай-ка". Хочешь в нее поиграть?   ')

for i in range(1):
    if answer.lower() == 'да':
        rules()
        ugaday_ka()
    else:
        disagree(answer)
