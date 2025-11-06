import re
from coun import coun
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
coun(paragraph)

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

let=re.findall(r"-?\d+",text)
post=[]
for i in let:
    post.append(int(i))
post.sort()
print("Distance is ",post[-1]-post[0])

