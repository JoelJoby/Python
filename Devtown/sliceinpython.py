students = ['sam', 'pam', 'rocky', 'austin', 'steve', 'banner', 'tony', 'bruce', 
            'henry', 'clark', 'diana']
student = "Barry"

# slice a particular range
marvel = students[4:8]
flash = student[1:3]
dc = students[7:]
other = student[:3]

print(len(student))
print(len( students))

print(marvel)
print(flash)
print(dc)
print(other)

#MODIFICATION OF list

students[2] = "ben"
print (students)

#Functions of List 

print(max(students))
print ( min(students))
print (sorted(students))

#functions using list

print(max(student))
print(min(student))
print(sorted(student))

#Joining Function 

sep_str = "\n".join(students)
print(sep_str)

# Append functions

lettres = ['a',"b" ,'c',"d"]
lettres.append('e')
print(lettres)







