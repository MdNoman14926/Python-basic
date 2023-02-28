# List or array in python 
#---List is a ordared container 
#Create a list 
car = ["BMW","Marseties","Tesla"]
print(car)
#List Indexing
print(car[1])
print(car[2])
print(car[0])
#Negative Indexing 
print(car[-1])
print(car[-2])
print(car[-3])
#-----Range of index 
print(car[0:3])

#--Adding item to a list by append()
car.append("BMW2")
print(car)
#--Insert()
car.insert(1,"BMW4")
print(car)

#--Delating item from list 
car.pop()
print(car)
car.remove("Tesla")
print(car)

#---Getting the length of a list 
print(len(car))

#Changing an item value 
car[0]="BMP"
print(car)

#--Extending list 
a = [1,2,3,4,5]
b = [6,7,8,9]
a.extend(b)

print(a)

#---Improtant Membership Oparator
