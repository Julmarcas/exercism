def transform(legacy_data: dict):
    new_data = {}

    for points, letters in legacy_data.items():
        for letter in letters:
            new_data[letter.lower()] = points

    return new_data
