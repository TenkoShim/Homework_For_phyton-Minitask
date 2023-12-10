# Мини-задача #5

# Реализовать функцию specialize, которая принимает
# функцию f и набор значений, а возвращает частично
# примененную к этим значениям функцию f.
def specialize(fun, *args, **kwargs):
    def in_specialize(*new_args, **new_kwargs):
        all_args = args + new_args
        all_kwargs = {**kwargs, **new_kwargs}
        return fun(*all_args, **all_kwargs)

    return in_specialize


def sum(x, y):
    return x + y


plus_one = specialize(sum, y=1)
just_two = specialize(sum, 1, 1)
print(plus_one(10))
print(just_two())
