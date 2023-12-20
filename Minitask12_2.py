def chain(*iterables):
    for iterable in iterables:
        for i in iterable:
            yield i
for i in chain([1,2,4],['a','b'],"ganga"):
    print(i,end=' ')