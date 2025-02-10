def is_valid(isbn: str):

    if not isbn:
        return False

    digits = list(isbn.replace("-", ""))

    if len(digits) != 10:
        return False

    if digits[-1].isalpha() and digits[-1] != "X":
        return False

    digits.reverse()
    total = 0

    for index, digit in enumerate(digits):
        if index == 0 and digit == "X":
            total += 10
            continue
        if not digit.isnumeric():
            return False
        total += (index + 1) * int(digit)

    return total % 11 == 0
