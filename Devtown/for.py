cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for city in cities:
    print(city)

print("done")


for i in range(3):
    print("Hello")


n = 10 
for i in range(n):
    print(i)

print("seperate")

# printing even

for i in  range(2,11,2):
    print(i)

print("seperate")
#for printingmultiples of 4

for i in range(4,41,4):
    print(i)

#creating a new lis from a old one

cities = ["new york city', 'mountain view', 'chicago', 'los angeles"]
capi_cities = []

for city in cities:
    capi_cities.append(city.title())

print(capi_cities)

# Modifing the list

for i in range(len(cities)):
    cities[i] = cities[i].title()

print(cities)

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive

for i in range(5,30,5):
    print(i)

#Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:

name = ["Joey Tribbiani","Monica Geller", "Chandler Bing", "Phoebe Buffay"]
username = []

# for i in name:
#     temp = i.split(" ")
#     user=temp[0].lower()+'_'+temp[1].lower()
#     username.append(user)

# for i in name:
#     username.append(i.replace(' ',"_").lower())


for i in name:
    print(i.replace(" ","_").lower())

# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags.

# XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">".

# Keep track of the number of tags using the variable count.

# You can assume that the list of strings will not contain empty strings.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
for i in tokens:
    if i.startswith("<") and i.endswith(">"):
        print(i)














