a = input("Enter your elements: ")
result, numbers, number = [], [], ''

for i in range(len(a)):
    if a[i] == "|":
        result.append(numbers)
        numbers = []
        continue
    if a[i] == " " and number != '':
        numbers.append(float(number))
        print(numbers)
        number = ''
    else:
        number += a[i]

if numbers:
    numbers.append(float(number))
    result.append(numbers)
print(result)
