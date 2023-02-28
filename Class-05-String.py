#---Class 05 Working with string in python
#---Single or double quotes
test = "I am 'Noman'.I live in 'Bangladesh'.I love to write 'Python' code"
print(test)

#--Multiline string
pragraphs='''Python is fun to learn
and it is also easy.You can enjoy with learning python'''
print(pragraphs)

#--Concatenating String
a = "I Love "
b = "Python"
print(a+b)

#---Accessing a part of a string 
#--By indexing
a = "I Live in bangladesh"
print(a[2])
#--By Slicing
a = "Python is really easy"
print(a[0:7])

#---Capitalize string

name = "noman"
print(name.capitalize())

#--Convert to uppercase
name="noman"
print(name.upper())

#--Convert to lowercase
name="noman"
print(name.lower())

#--Get the length of a string 
x ="I live   in bangladesh"
print(len(x))

#---Replace something part on string
x="I love Bangladesh"
print(x.replace("Bangladesh","to Code"))