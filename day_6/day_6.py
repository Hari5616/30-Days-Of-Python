tpl=tuple()
cousin_bro=("harry","potter","jason","mason")
cousin_sis=("Lily","silly","milly","boby")
cousins=cousin_bro+cousin_sis
print(cousins)
print("The number of cousins are",len(cousins))
family_mem=list(cousins)
family_mem.append("mom")
family_mem.append("dad")
print(tuple(family_mem))

fruits=("Apple","Banana")
vegetable=("Drumstick","Ladiesfinger")
animal_products=("milk","curd","butter")
food_stuff_tp=fruits+vegetable+animal_products
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt[3])
print(food_stuff_lt[0:3],food_stuff_lt[-3:])
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)


