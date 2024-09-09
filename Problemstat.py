# A programn to store a three digit number and a single digit number in single variable and print each of them individualy.

# Method 1:
# Storing as a list and printing each element of the list.
l= [123,4]
print(l[0],l[1])

# Method 2:
# Storing as a string and printing each element of the string.
s= '1234'
print(s[0:3],s[3])

# Method 3:
# Integer method to store the number and then print each Number.
# Let initial three digit number be 123 and single digit number be 4.
a=123
b=4
# Storing both of them in variable 'c' as a single number.
c = a*10+b
print((c-c%10)//10,c%10)