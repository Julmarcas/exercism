def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for element in lists:
        if isinstance(element, list):
            result += element
        else:
            result.append(element)
    return result


def filter(function, list1):
    result = []
    for element in list1:
        if function(element):
            result.append(element)
    return result


def length(list1):
    return len(list1)


def map(function, list1):
    result = []
    for element in list1:
        result.append(function(element))
    return result


def foldl(function, list1, initial):
    result = initial
    for element in list1:
        result = function(result, element)
    return result


def foldr(function, list1, initial):
    result = initial
    for element in reverse(list1):
        result = function(result, element)
    return result


def reverse(list1):
    return list1[::-1]
