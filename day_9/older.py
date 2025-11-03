my_age=18
your_age=int(input("Enter your age:  "))
if my_age < your_age:
    print(f"You are {your_age-my_age} years older than me")
elif my_age==your_age:
    print("We both have same age")
else:
    print(f"I am {my_age-your_age} years older than you")
    