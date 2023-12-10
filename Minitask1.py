# Мини-задача #1

# Написать программу, считающую количество
# выставленных битов в произвольном целом числе.
#
# Использовать приведение к строке и bin нельзя.
#
# Замечание: программа должна корректно работать с
# отрицательными числами, с учетом представления в
# дополнительном коде. signed бит считать один раз.
#
# Пример: 10 -> 2 (т.к. 10 - это 0...1010)
# -123 -> 3 (т.к. -123 - это 1...0000101)
def neg_number(n, count) -> int:
    n = abs(n)
    flag = True  # You need to find first 1
    while n:
        if n % 2:
            flag = False  # to check if its 1 and skip counting
        elif not flag:
            count += 1
        n >>= 1
    return count + 1


def pos_number(n, count) -> int:
    while n:
        count += n % 2
        n >>= 1
    return count


n = int(input("Enter you number:"))
count = 0
if n < 0:
    count = 1 + neg_number(n, count)
else:
    count = pos_number(n, count)
print(f"Your bytes={count}")
