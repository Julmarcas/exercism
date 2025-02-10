def is_isogram(string: str):

    letters = []
    for letter in string.lower():
        if letter.isalpha() and letter in letters:
            return False
        else:
            letters.append(letter)

    # word = word.lower().replace(" ","").replace("-","")
    # return len(word) == len(set(word))
    return True
