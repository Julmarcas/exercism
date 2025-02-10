def color_code(color):

    colors_map = {
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
    return colors_map[color]


def value(colors):
    return int(f"{color_code(colors[0])}{color_code(colors[1])}")
