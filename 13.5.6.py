def is_palindrome(text):
    text.lower()
    list = []

    for i in text:
        if i.isalpha():
            list.append(i)
    for i in range(len(list)):
            if list[:] == list[::-1]:
                return True
            else:
                return False



txt = input()

print(is_palindrome(txt))
