def is_armstrong_number(number: int):
    lenght = len(str(number))
    return number == sum(int(digit) ** lenght for digit in str(number))
