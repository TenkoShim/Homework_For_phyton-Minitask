def flatten(array):
    new_array = []
    for x in array:
        if isinstance(x, list):
            new_array.extend(flatten(x))
        else:
            new_array.append(x)
    return new_array


print(flatten([1, 2, 3, [4, [5]], 6, 6]))
