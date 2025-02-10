def rotate(text: str, key: int):

    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    result = ""
    for letter in list(text):
        is_upper = letter.isupper()

        if is_upper:
            letter = letter.lower()

        if not letter.isalpha():
            result += letter
            continue
        index = alphabet.index(letter)
        index += key
        if index >= len(alphabet):
            index = index - len(alphabet)

        if is_upper:
            result += alphabet[index].upper()
        else:
            result += alphabet[index]

    return result
