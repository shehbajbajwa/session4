technologies = [ " AI", " andriod", "hadoop", "jee"]
technologies[1] = "mobile apps"   #updation/set operation
print(technologies)
print()
del(technologies[2])
print(technologies)
print(technologies[2])

#print(tech[0:2]
print(technologies[-2])





data = [1,2,3,4,5, "john", "jennie", "jim", "jack" ,"joe"]
data.pop(3)  #removes on the basis of index
print(data)

data.remove(3)
print(data) # removes the matching element

data.remove("john")
print(data)

