def convert_to_python_case(text):
    for i in range(1, len(text)):
        s = text[0]
        for i in text[1:]:
            if i.isupper():
                s += '_' + i
            else:
                s += i
        return s.lower()


txt = input()

print(convert_to_python_case(txt))