def cortege(d):
    new_dict={}
    for i in d.keys():
        if(d[i] in new_dict):
            s=(new_dict[d[i]],i)
            new_dict[d[i]]=s
            continue
        new_dict[d[i]] = i
    return new_dict
d={"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}
print(cortege(d))