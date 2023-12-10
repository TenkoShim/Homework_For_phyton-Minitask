# Мини-задача #2

# Написать программу, принимающую два списка и
# возвращающую список пар из элементов данных списков.
#
# Использовать функцию zip нельзя.
#
# Замечание: если списки были разного размера, то
# результирующий список должен быть минимального
# размера из данных
def zip(a, b, length):
    result = []
    for i in range(length):
        result.append((a[i], b[i]))
    return result


a = list(map(int, input("Enter Elements in int :").split()))
b = list(map(str, input("Enter Elements in str :").split()))
length = min(len(a), len(b))
print(zip(a, b, length))
