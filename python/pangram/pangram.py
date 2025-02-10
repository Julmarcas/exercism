def is_pangram(sentence: str):

    letters = []
    for letter in sentence.strip().lower():
        if letter.isalpha():
            letters.append(letter)

    return len(set(letters)) == 26
