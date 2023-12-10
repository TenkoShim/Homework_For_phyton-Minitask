# Мини-задача #3

# Пусть входные данные имеют вид:
#
# a_00 a_01 a_02 ... | a_10 a_11 a_12 ... | ... | a_n0 a_n1 ... |
#
# И описывают матрицу из значений типа float. Символ |
# отделяет описание элементов очередной строки матрицы
#
# По этим данным необходимо создать список из списков
# значений типа float, соответствующий этой матрице
def custom_splitlines(text, delimiter='\n'):
    lines = []
    current_line = ''
    for char in text:
        if char == delimiter:
            lines.append(current_line)
            current_line = ''
        else:
            current_line += char
    if current_line:
        lines.append(current_line)
    return lines


a = input("Enter your elements: ")
a = custom_splitlines(a, '|')
result = []
for i in a:
    result.append(list(map(float, i.split())))
print(result)
