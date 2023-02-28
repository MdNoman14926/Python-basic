#--If statement in python 
x = 10
y = 5

if x<y:
    print("X ix less then Y")
elif x>y:
    print("Noman is my name")
else:
    print("X is not less then Y")

#--A programe about user smoking eligibal 
user_age=int(input("Write age:"))

if user_age>=18 and user_age<=35:
    print("Sir, Your age is right for smoking")
elif user_age>45 and user_age<60:
    print("Your age is too high so you cant smoke")
else:
    print("You are small so You can't smoke")

