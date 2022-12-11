
def is_correct_bracket(text):
    for i in range(len(text)):
        if '()' in text:
            text = text.replace('()', '')
        else:
            if len(text) == 0:
                return True
            else:
                return False


txt = input()

print(is_correct_bracket(txt))