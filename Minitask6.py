# Мини-задача #6

# Реализовать функцию flatten, которая принимает list и
# возвращает новый list, состоящим из:
#
# 1. элементов изначального list, если сами они не
# являются list
# 2. элементов списка, который возвращает вызов flatten
# от элемента оригинального списка в противном
# случае
def flatten(array):
    new_array = []
    for x in array:
        if isinstance(x, list):
            new_array.extend(flatten(x))
        else:
            new_array.append(x)
    return new_array


print(flatten([1, 2, 3, [4, [5]], 6, 6]))
