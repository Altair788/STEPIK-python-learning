    #   количество должно быть четным
def is_correct_bracket(text):
    if len(text) % 2 != 0:
        return False
    if len(text) % 2 == 0 and text[:] == text[::-1]:
        return True
    else:
        return False
txt = input()

print(is_correct_bracket(txt))