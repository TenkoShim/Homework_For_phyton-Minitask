# Мини-задача #7

# Добавить в функцию flatten из предыдущей задачи параметр
# depth, задающий, сколько уровней вложенности списков
# должно быть сглажено.
#
# Если параметр не указан, поведение должно совпадать с
# предыдущей задачей.
def flatten(array, depth=None):
    if depth is None:
        depth = float('inf')
    new_array = []
    for x in array:
        if isinstance(x, list) and depth > 0:
            new_array.extend(flatten(x, depth=depth - 1))
        else:
            new_array.append(x)
    return new_array


print(flatten([1, 2, 3, [4, [5]], 6, 6]), 1)
