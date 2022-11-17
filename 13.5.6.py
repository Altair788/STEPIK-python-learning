def is_palindrome(text):
    text = text.lower()     #  при решении трудность была в том, что забыл text = text...
    list = []

    for i in text:
        if i.isalpha():
            list.extend(i)
    for i in range(len(list)):
        if list[:] == list[::-1]:
            return True
        else:
            return False



txt = input()

print(is_palindrome(txt))