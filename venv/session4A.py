# list in python

students = ["john", "jennie", "jim", "jack" ,"joe"]
print(students, type(students))

# 1. concatenation
print(students + ["fienna", "george"])
print(students)

# 2. repetition #if u want same list to be replocated ------- no. of times.
print(students * 2)
print(students)

# 3. membership testing
print("john" in students)

# 4. indexing
print(students[2])

# 5. slicing
print(students[1:4])

# lists, tuples, strings, sets and dictionary
str = "hello world"
print (str[2:5]) #strings  slicing #2 exclude and 5 include

print(str + "fienna", "george")  #concate done
print(str)

print(str * 2) #repetition done

print("hello" in str) #membership testing works

print(str[3]) #indexing shows 1 every time ERROR

#set
students = { 30, 40, 50}
print(students)
"""
print(students + 60) #no concatination
print(students * 2)  #no repetition
"""
print( 30 in students) #no membership
"""
print(students[2])  # no indexing
print(students[1:2])  # no slicing
"""