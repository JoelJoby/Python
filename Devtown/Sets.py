num = [1, 2, 6, 3, 1, 1, 6]
unq = set(num)
print(unq)

#functions in set

fruit = {"apple", "banana", "orange", "grapefruit"}
print("watermelon" in fruit) # check for element

fruit.add('watermelon')
print(fruit)  # add an element

print(fruit.pop())