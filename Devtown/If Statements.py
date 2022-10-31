bike_bal = 99
bank_bal = 1000

print("The Bike Balancce is {} and Bank Balance is {}.".format(bike_bal,bank_bal))

if(bike_bal < 100):
    bike_bal += 500
    bank_bal -= 500

print("The balance amt of bike app balance is {} and that of bank app is {}".format(bike_bal,bank_bal))

# Even Or odd

n = 5

if (n % 2 == 0):
    print("The number is " + str(n) + " even")
else:
    print("The number {} is Odd".format(n))


# Else if Statements

season = "fall"

if season == "spring":
    print("Plant the garden")
elif season == "summer":
    print("Water the garden")
elif season == "winter":
    print('Stay inside')
else:
    print('Unrecognized season')


## **Ouestion**:

#Write an if statement that lets a student know which of these grades they got based on the number they got in exams, which is stored in the integer variable *marks*.
#Marks -> Grade
#100-90 -> A+
#90-80 -> A
#80-70 -> B
#70-60 -> C
#60-50 -> D
#50-40 -> E
#<40 -> F
#> All of the lower and upper bounds here are inclusive, and marks can only take on positive integer values up to 100.
#In your if statement, assign the result variable to a string holding the appropriate message based on the value of marks.
#"you have scored *[Grade]* Grade."


marks = 90

if marks <= 100 and marks >= 90:
    grade = "A+"
    
elif  80 <= marks < 90:
    grade = "A"

else:
    grade = "Not Available"

print("The grade is {}".format(grade))


## **Ouestion**:

#Depending on where an individual is from we need to tax them appropriately. 
#The states of CA, MN, and NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and the corresponding state 
#to assure that they are taxed by the right amount.

state = "CA"
purchace_amt = 5000

if state == "CA":
    tax_amt = .075
    tot_amt = purchace_amt *  (1 + tax_amt)
    result = "Since u r from {}, ur total coast is {}".format(state,tot_amt)


print(result)
