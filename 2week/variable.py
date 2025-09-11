from pydoc import tempfilepager


age = 20 
print(age)

age = 21
print(age)

name = 'gunrein'

print(name + ' hello')

a = 5 
a = a + 7
print(a)

a,b = 2,3
a += b
print(a)

a,b = 3,2
a /= b
print(a)

a,b = 7,3
a %= b
print(a)

a = 100
a += 10 
print(a)

a = 7 
b = 11 

temp = a 
a = b 
b = temp

print(a,b)

a,b = b, a
print(a,b)