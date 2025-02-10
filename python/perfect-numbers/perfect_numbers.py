from math import sqrt


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors = set()
    for divider in range(1, int(sqrt(number)) + 1):
        if number % divider == 0:
            factors.add(divider)
            factors.add(number // divider)

    factors.remove(number)
    addition = sum(factors)

    if addition == number:
        return "perfect"
    if addition > number:
        return "abundant"

    return "deficient"
