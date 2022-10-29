from unittest import result


my = "DevTown"

print(my.islower())

print(my.count('a'))

print(my.find('a'))


marks = 15
subject = "coding"
semester = "first"

#result = "I scored " + str(marks) + " in " + subject + " during my " + semester + " semester."

result = "i scored {} in {} during my {} semister".format(marks,subject,semester)
print(result)

# Example 1
print("EG:1")
print("Mohammed has {} balloons".format(27))

# Example 2
print("EG:2")
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))

# Example 3
print("EG:3")
maria_string = "Maria loves {} and {}"
print(maria_string.format("math","statistics"))

print(maria_string.format(animal,action))