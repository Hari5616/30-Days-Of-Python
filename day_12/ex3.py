import random
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
print(shuffle_list(["in","unu","iji"]))
    
def rand():
    print(random.sample(range(10),7))
rand()