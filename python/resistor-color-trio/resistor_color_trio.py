COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def label(colors):
    value = (COLORS[colors[0]] * 10 + COLORS[colors[1]]) * 10 ** COLORS[colors[2]]
    str_value = str(value)

    num_without_zeros = str_value.rstrip("0")
    zero_count = len(str_value) - len(num_without_zeros)

    if zero_count >= 9:
        prefix = "giga"
        divisor = 1e9
    elif zero_count >= 6:
        prefix = "mega"
        divisor = 1e6
    elif zero_count >= 3:
        prefix = "kilo"
        divisor = 1e3
    else:
        prefix = ""
        divisor = 1

    converted_value = int(value / divisor)

    return f"{converted_value} {prefix}ohms"
