import re

def is_valid_variable(name):
    return re.fullmatch(r"[a-zA-Z_]\w*", name) is not None

es = is_valid_variable('1first_name')
if es:
    print(True)
else:
    print(False)



