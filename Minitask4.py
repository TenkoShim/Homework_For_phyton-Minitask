# Мини-задача #4

# Написать программу, которая по заданном словарю
# составляет обратный словарь, в котором значения и ключи
# поменялись местами. При этом:
#
# 1. Если значения оказались не hashable, то создания
# обратного словаря прерывается с TypeError
# 2. Если разным ключам соответствовало одно и тоже
# значение, то в качестве значения в обратном
# словаре использовать tuple из ключей
def reversed_dictionary(d):
    new_dict = {}
    for i in d.keys():
        key = d[i]
        try:
            if key in new_dict:
                if type(new_dict[key]) == tuple:
                    s = (i,) + new_dict[key]
                else:
                    s = (i, new_dict[key])
                new_dict[d[i]] = s
                continue
            new_dict[key] = i
        except TypeError:
            print(f"{key} is not hashable")

    return new_dict


# d={"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}
d = {"Ivanov": 97832, "Ivanov2": 97832, "Petrov": 55521, "Kuznecov": 97832}
print(reversed_dictionary(d))
