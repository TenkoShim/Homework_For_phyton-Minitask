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
def negnumber(n,count):
    n = abs(n)
    F = True#You need to find first
    while (n):
        if (n % 2):
            F= False
        elif (F==False):
            count += 1
        n >>= 1
    return count+1
def posnumber(n,count):
    while n:
        count+= n%2
        n>>=1
    return count
n=int(input("Enter you number:"))
count=0
if(n<0):
    count=1+negnumber(n,count)
    print("Your bytes="+str(count))
else:
    count=posnumber(n,count)
    print("Your bytes="+str(count))
print(count)
