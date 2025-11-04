def is_prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count<=2:
        return "Prime"
    else:
        return "Not Prime"
print(is_prime(9))

def item(last):
    count=0
    lst=list()
    for i in last:
        if i not in lst:
            lst.append(i)
        
        for j in lst:
            if last.count(j)>=2:
                return "Not unique"
                
    return "Unique"
print(item(["fr","hhyu88"]))

def data(content):
    count=list()
    count_2=list()
    for i in content:
        count.append(type(i))
    for j in count:
        if j not in count_2:
            count_2.append(j)
    if len(count_2)==1:
        return "Same type"
    else:
        return "Different data type"       
print(data(["dfv",["ub"]]))  

def variable(stril):
    if stril.isidentifier():
        return "Is Identifier"
    else:
        return "Not identifier"
print(variable("identifer"))
        
        
      