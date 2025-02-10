def rebase(input_base: int, digits: list[int], output_base: int):

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not all(0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    digits.reverse()
    decimal = sum(digit * input_base**index for index, digit in enumerate(digits))

    if decimal == 0:
        return [0]

    result = []
    while decimal != 0:
        result.append(decimal % output_base)
        decimal = int(decimal / output_base)

    result.reverse()
    return result
