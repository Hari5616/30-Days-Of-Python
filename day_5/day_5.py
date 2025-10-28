lst=list()
lst=["Apple","banana","Camel","Dancer","Elephant"]
print(len(lst))
print(lst[0],lst[2],lst[4])
mixed_data_type=("Hari","23","173","Single","Bangalore")
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies,len(it_companies))
print(it_companies[0],it_companies[3],it_companies[6])
it_companies[0]="Netflix"
print(it_companies)
it_companies.append("GIT")
it_companies.insert(4,"LinkedIn")
it_companies[4].upper()
it_companies.append("#")
print("IBM" in it_companies)
it_companies.sort()
it_companies.sort(reverse=True)
print(it_companies[0:3])
print(it_companies[-1:-4])
print(it_companies[5])
del it_companies[0]
del it_companies[4]
del it_companies[-1]
it_companies.clear()
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack=front_end+back_end
full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages[-1],"Is the Max",ages[0],"Is the min")
ages.extend([19,26])
print(ages)
ages.sort()
print("The median is",(ages[5]+ages[6])/2)

country_list=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first , second, third , *scandic=country_list
print(scandic)