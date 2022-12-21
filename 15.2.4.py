def is_valid(n):
    for i in range(1, 101):
        if int(n) == i:
            return True
        else:
            return False
n = input()