a=input("Enter your elements")
result=[]
b=[]
for i in range(len(a)):
    if(a[i]=="|"):
        result.append(b)
        b=[]
        continue
    if(a[i]!=" "):
        b.append(int(a[i]))
if(len(b)!=0):
    result.append(b)
print(result[0][1])