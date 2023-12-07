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
