it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")
company=("HCL","IBM","TCS")
it_companies.update(company)
print(it_companies)
it_companies.remove("IBM")
print(it_companies)

print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
A.union(B)
B.union(A)
print(A.symmetric_difference(B))
del A,B

age_set=set(age)
print(len(age)>len(age_set))
words="I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?"
word=words.split(" ")
print(len(word))
word=set(word)
print(len(word))

