person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
    
if "skills" in person:
    print(person["skills"][2])  
    if "Python" in person["skills"]:
        print("yes it is there")
    else:
        print("No")
if person["is_marred"]:
    if person["country"]=="Finland":
        print("Asabeneh Yetayeh lives in Finland. He is married.")    
        
skills = person['skills']
if skills == ['JavaScript', 'React']:
    print('He is a front end developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')
else:
    print('unknown title')
