import re
def coun(string):
    full=list()
    all=list()
    name=re.findall(r"\b\w+\b",string)
    for i in name:
        if i not in full:
            full.append(i)
    for j in full:
        all.append((len(re.findall(rf"\b{j}\b", string)), j))
    all.sort(reverse=True)  
    print(all[0][1],f"IS THE MOST FREQUENT WORD WITH {all[0][0]} REPETITION")


