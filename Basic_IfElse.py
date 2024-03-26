x = 6
if x > 5:
    print("x is greater than 5")
print("Outside if condition")



i = 31
if (i < 25):
	print("i is smaller than 25 , this is if Block")
else:
	print("i is greater than 25, this is else Block")
print("out of if and else Block")



i = 10
print(True) if i < 15 else print(False)



x = 0

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")


num = 4
if num > 0:
    if num < 10:
    	print("The number is positive and less than 10.")
else:
    print("The number is less than or equal to 0")




# Approach 1 using if-else statement
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")




#Approach 2 using nested if statements
year = int(input("Enter a year: "))

# Check if it's a leap year
if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is a leap year.")
    else:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
else:
    print(f"{year} is not a leap year.")
	      
