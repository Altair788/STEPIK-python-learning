#   количество должно быть четным
def is_correct_bracket(text):
    if len(text) % 2 != 0:
        return False
    if len(text) % 2 == 0:
        if text[0] == ')' or text[::-1] == '(':
            return False
    counter = 0
    for i in text:
        if i == '(':
            counter += 1
        else:
            counter -= 1
    if counter == 0:
        return True
    else:
        return False

txt = input()

print(is_correct_bracket(txt))