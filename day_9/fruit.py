fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=input("Enter the fruit:  ")
if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(fruits)