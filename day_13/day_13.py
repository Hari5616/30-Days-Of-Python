numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
string=[i for i in numbers if i <=0]
#print(string) 

list_of_lists =[[[1, 2, 3],[89]], [[4, 5, 6]], [[7, 8, 9]]]
value=[sli for part in list_of_lists for cut in part for sli in cut]
print(value)

tip=[(i,1,i*1,i*(i*1),i*(i*(i*1)),i*(i*(i*(i*1))),i*(i*(i*(i*(i*1))))) for i in range(11)]
print(tip)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country.upper(), country[:3].upper(), capital.upper()] for [(country, capital)] in countries]
print(output)

result=[{"country":country.upper(),"city":city.upper()} for [(country,city)] in countries]
print(result)


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
proof=[(str1+" "+str2) for [(str1,str2)] in names]
print(proof)

ans=lambda x1,x2,y1,y2 :"undefined" if x1==x2 else (y2-y1)/(x2-x1)
print(ans(4,4,8,3))
