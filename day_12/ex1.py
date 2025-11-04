import random
text="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def user_id_gen_by_user():
    value=int(input("Number of characters:  "))
    id=int(input('The number of id you want:  '))
    for i in range(id):
        string=''.join(random.choices(text,k=value))
        print(string)

def user_id_gen_by_user():

    tup=tuple()
    for i in range(3):
        tup=tup+(random.randint(0,255),)
    print(f"rgb{tup}")

user_id_gen_by_user()

