def even_odd(num):
    count_odd=0
    count_even=0
    for i in range(num+1):
        if i%2==0:
            count_even+=1
        else:
            count_odd+=1
    return(count_odd,count_even)
number=even_odd(100)
#print("The number of odds are",number[0])
#print("The number of evens are",number[1])

def factorial(n):
    lst=list()
    for i in range(1,n+1):
        if n%i==0:
            lst.append(i)
    return lst

for i in factorial(10):
    print(i)

def is_empty(str):
    for i in str:
        if i==" ":
            return "Empty"
    return "Not empty"    

print(is_empty(["huu"]))





