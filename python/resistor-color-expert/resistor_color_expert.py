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

TOLERANCE = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}


def resistor_label(colors):

    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"

    if len(colors) == 5:
        value = (
            COLORS[colors[0]] * 100 + COLORS[colors[1]] * 10 + COLORS[colors[2]]
        ) * 10 ** COLORS[colors[3]]
        tolerance = TOLERANCE[colors[4]]
    else:
        value = (COLORS[colors[0]] * 10 + COLORS[colors[1]]) * 10 ** COLORS[colors[2]]
        tolerance = TOLERANCE[colors[3]]

    if value > 1000000:
        value /= 1000000
        prefix = "mega"
    elif value > 1000:
        value /= 1000
        prefix = "kilo"
    else:
        prefix = ""

    if value % 1 == 0:
        value = int(value)

    return f"{value} {prefix}ohms ±{tolerance}"
