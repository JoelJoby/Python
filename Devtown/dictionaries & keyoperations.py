from ast import IsNot


elements = {"hydrogen": 1, "helium": 2,"carbon": 6}

print (elements["helium"]) # printing the value of helium

elements["lithium"] = 3 # adding the elements
print(elements) 

# Functions in Dictionary

print(elements.get('gold')) # get function is used to get the output even if the code runs to an error

print(elements["carbon"])
print("carbon" in elements)

# Key operations 

n = elements.get('dilithium')
print(n is None)
print(n is not None )