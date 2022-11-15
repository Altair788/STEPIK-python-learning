def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    counter = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            counter += 1
    if len(word1) == len(word2) and counter == len(word2) - 1:
        return True
    else:
        return False


txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))
