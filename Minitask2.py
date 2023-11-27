def zip(a, b, length):
    result = []
    for i in range(length):
        result.append((a[i], b[i]))
    return result


a = list(map(int, input("Enter Elements in int :").split()))
b = list(map(str, input("Enter Elements in str :").split()))
length = min(len(a), len(b))
print(zip(a, b, length))
