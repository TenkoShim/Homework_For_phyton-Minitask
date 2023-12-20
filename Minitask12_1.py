def cycle(iterable):
    saved=[]
    for i in iterable:
        yield i
        saved.append(i)
    while saved:
        for i in saved:
            yield i
for i in cycle([1,2,4]):
    print(i)