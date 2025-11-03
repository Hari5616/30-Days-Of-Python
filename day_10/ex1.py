for i in range(11):
    print(i)
i=0
while i<11:
    print(i)
    i+=1

number=int(input("Enter a number: "))
for i in range(1,number+1):
    print("#"*i)
    
for i in range(11):
    print(f"{i} x {i} = {i*i}")
    
list=['Python', 'Numpy','Pandas','Django', 'Flask']
for item in list:
    print(item)
count=0
for i in range(101):
    if i%2==0:
        count+=i

print(count)
         
    
    