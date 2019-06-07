#data = [ "c++", "java", " python" ,90,80,90]
#length = len(data)
#print(length)
data = [ 90,80,90]
print(len(data))
print(max(data))
print(min(data))
print("**********")
#iteration in list
for i in range(len(data)):
    print(data[i])

print("**********")

# enchanced for loop/for each loop
for elm in data:
    print(elm)  #elm is variable
print("**********")


print([x**2 for x in data])  # ** is exponential

numbers = list(range(1,101,3))
print(numbers)

print([x%10 for x in numbers])


