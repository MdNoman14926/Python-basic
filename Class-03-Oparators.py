#Class 3 Types of operators 
# Arithmetic operators:
print(3+4) # Addition
print(3-4) # Subtractiuon
print(3*4) # Multipilication
print(10/2) # Division
print(3**2) # Exponentiation
print(10//2) # Floor Division
print(12%5) # Remainder

# Assignment Operator
x = 5
y = 10
x += y
print(x)

# Comparison operator * Note: Comparison operator always return boolean value
x = 5
y = 10
print(x<y)

# Logical Operator * Note : Always return Boolean value
#----Logical and
# 1. TT=True 3.FT = False
# 2. TF=False 4. FF = False
a = 20;
b = 25
logicalAnd = a<b and a==b;
logicalOr = a<b or a==b;
print(logicalAnd)
print(logicalOr)
#Logical not
logicalNot= not a<b
print(logicalNot)

#--Membership Operator
#-----Membership in
country = ["Bangladesh","India","Canada"]
check_item = "Bangladesh" in country
print(check_item)
check_item = "Pakistan" in country
print(check_item)

#Membership not in
check_item="Bangladesh" not in country
print(check_item)