a = 'hello, '
b = 'gato.'

print(a + b)

yelling = a.upper()
# can also use .lower() for lowercase transformation 
print(yelling)
# capitalize first letter 
print(b.capitalize())

c = 'I want more cheese'
# this only makes a copy - does not modify first variable
d = c.replace('more', 'less')

print(d)
print(c)

f = 8
# convert to number
g = int(f)
# convert to string 
h = str(f)
e = input('enter a number between (0, 10)')
