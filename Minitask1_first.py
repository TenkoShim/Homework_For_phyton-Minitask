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

def mybin(a,result):
    if(result!=1):
        while(a!=0):
            ost=a%2
            if(ost==1):
                result+=1
            a//=2
        return result

    else:
        arr=makeyourarray(a)
        arr=negativeN(arr)
        arr[0]=arr[0]+1
        for i in range(1,len(arr)):
            if(arr[i-1]==2):
                arr[i-1]=0
                arr[i]=arr[i]+1
        result+=arr.count(1)
        return result
def makeyourarray(a):
    arr=[]
    while (a != 0):
        ost = a % 2
        arr.append(ost)
        a //= 2
    return arr
def negativeN(arr):
    for i in range(len(arr)):
        if(arr[i]==1):
            arr[i]=0
        else:
            arr[i]=1
    return arr
n=int(input("Enter your number:"))
result=0
if(n<0):
    result+=1
n=abs(n)
result=mybin(n,result)
print("Your number have this much bites="+str(result))