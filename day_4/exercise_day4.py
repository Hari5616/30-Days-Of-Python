print(f"{"Thirty"} {"Days"} {"Of"} {"Python"}")
print(f"{"Coding"} {"For"} {"All"}")

company="Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company.strip("Coding"))
print(company.index("Coding"))
print(company.replace(company,"Python"))
text="Python For Everyone"
print(text.replace("Everyone","All"))
print(company.split())
text_2="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(text_2.split(","))
print(company[10])
print(company.index("C"))
print(company.index("F"))
print(company.rfind("l"))
text_3= 'You cannot end a sentence with because because because is a conjunction'
print(text_3.find("because"))
print(text_3.rfind("because"))
print(text_3.replace("because because because ",""))
print(text_3.index("because"))
print("Does ''Coding For All' start with a substring Coding",company.startswith("Coding"))
print("Does ''Coding For All' end with a substring coding",company.endswith("coding"))
text_4= '  Coding For All   '
print(text_4.strip(" "))
val1= '30DaysOfPython'
val2= 'thirty_days_of_python'
print(val1.isidentifier())
print(val2.isidentifier())
txt=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(txt))
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
print("radius = 10\narea = 3.14 * radius ** 2\nThe area of a circle with radius 10 is 314 meters square.")
print("8 +6 = 14\n8 - 6 = 2\n8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144")
