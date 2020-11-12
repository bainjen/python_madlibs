subtotal = 20.20 
tax_rate = 0.14
tax = subtotal * tax_rate
total = subtotal + tax
print(total)
# computes to 23.028 -- doesn't make sense for change - can round
total = round(total, 2)
print(total)

a = -2
b = 12.5
# variables can be reassigned 
c = a + 1
c = a + b
c = c + a
# brackets evaluated first
c = (a + b) * 2 - a
print(c)
# Functions
# python has a lot of built in functions to transform data 
# I want c to be the value of 8.187 rounded to the second decmial point
c = round(8.187, 2)
print(c)
# round number down
d = int(b)
print(d)