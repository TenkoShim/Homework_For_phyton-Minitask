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
