dog=set()
dog={
    'colour':'red',
    'breed':'street dog',
    'legs':'short',
    'age':'7',
}
std={
    'first_name':'Hari',
    'last_name':'Ramesh',
    'gender':'Male',
    'age':'15',
    'marital':"single",
    'skill':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country':'Indonesia',
    'city':'London',
    'address':'god is there?'
}

print(len(std))
print(std.get("skill"))
std["skill"].append("Eating")
print(std.get("skill"))
print(std.keys(),std.values())
del std["address"]
del dog
print(std)