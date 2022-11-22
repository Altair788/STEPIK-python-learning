def is_magic(date):
    count1 = 1
    count2 = 1
    date = date.split('.')
    for i in date[:2]:
        i = int(i)
        count1 *= i
    for i in date[2:]:
        i = int(i)
        count2 *= i
    if count1 == count2 % 100:
        return True
    else:
        return False

d = input()

print(is_magic(d))