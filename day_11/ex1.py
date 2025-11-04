def add_num(a,b):
    return a+b

#print(add_num(1,2))

def area_circle(r):
    return 3.14*r*r

#print(area_circle(2))

def add_all_nums(*num):
    total=0
    for i in num:
        if str(i).isdigit():
            total+=i
        else:
            return "Invalid input"
    return total
#print(add_all_nums(1,2,3,4,7))

def temp(celsius):
    far=(celsius*(9/5))+32
    return far
#print(temp(37))

def calculate_slope(x1,x2,y1,y2):
    if (x2-x1)==0:
        return "Not having defined slope"
    slope=(y2-y1)/(x2-x1)
    return slope

#print(calculate_slope(7,6,6,4))


    
    