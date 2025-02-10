def flatten(iterable):

    result = []
    for element in iterable:
        if isinstance(element, list):
            result += flatten(element)
        else:
            result.append(element)
    return list(filter(lambda x: x is not None, result))
