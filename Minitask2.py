def min_len(len_1,len_2):
    if(len_1<len_2):
        return len_1
    else:
        return len_2
def cortege(a,b,lenght):
    result=[]
    for i in range(lenght):
        result.append([a[i], b[i]])
    return result
a=list(map(int,input("Enter Elements in int :").split()))
b=list(map(str,input("Enter Elements in str :").split()))
lenght=min_len(len(a),len(b))
print(cortege(a,b,lenght))
