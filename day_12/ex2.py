import random

def list_of_hexa_colors():
    text="abcdefABCDEF0123456789"
    string=''.join(random.choices(text,k=5 ))
    print("#"+string)
list_of_hexa_colors()

