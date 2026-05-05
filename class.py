# # This code prompts the user to enter their first name, and checks if the input is valid.
import math
from unittest import case


first_name = input('enter your first name: ')
if first_name=="":
     print("Error: First name cannot be empty.")
elif not first_name.isalpha():
     print(" First name must contain only letters.")   
else:
     print('valid')

#     # The code then prompts the user to enter their last name and performs similar validation checks.
last_name: str = input('enter your last name: ')
if last_name=="":
   print("Error: Last name cannot be empty.")
elif not last_name.isalpha():
     print("Last name must contain only letters.")
else:
     print('valid')

# # Finally, the code prompts the user to enter their email address and checks if it is valid by ensuring it contains an '@' symbol and ends with '@gmail.com'.
     contact: str = input("Enter your email : ")
if contact=="":
     print(" Contact information cannot be empty.")
elif '@' in contact:
     if contact.endswith('@gmail.com'):
         print("Valid email address.")
else:   
     print("Invalid email format. Email must contain '@' symbol.")

# #re-match email with the first email input
email: str = input("re-enter your email :")
if email == contact:
     print("email matched")    


# #password validation 
password: str = input("enter your password :")
if len(password) <7:
     print("password must be at least 7 letters long and a number")
else:
     if not any(char.isdigit() for char in password):
         print("password must contain at least one number") 
     else:       
         print("password is valid")     

if password == "Pass@123":
     print("password matched")





#     #design a traffic light system given a variable light that can be "red", "yellow", or "green". The program should print the appropriate action for each light color.
     light = input("Enter traffic light color (red, yellow, green): ").lower()
if light == "red":
     print("Stop")
elif light == "yellow":
     print("Get Ready")
elif light == "green":
     print("Go")
else:
     print("Invalid traffic light color entered.")


#     #write a match statement that takes a number 1-4 and prints the corresponding season (1 for Spring, 2 for Summer, 3 for Autumn, 4 for Winter). If the number is outside this range, it should print "Invalid season number."
     number=int(input("enter a number between 1-4: "))
match number:
         case 1:
             print('spring season')
         case 2:
           print('summer season')
         case 3:
            print('autumn season')
         case 4:
             print('winter season')
         case _:
             print("Invalid season number.")

     # write a login system using nested if statements. check:
      #if username equals "admin" , inside that, if password equals "pass123"
      #print appropriate message for:valid login, invalid password, and invalid username.

username = input('enter your username: ' )
password = input('enter your password: ')
if username == "admin":
         if password== "password123":
             print('valid login')
         else:
             print("invalid password")
else:
       print("invalid username")

#a theme park has these ruels: you can ride the roller coaster if you are at least 12 years old and at least 48 inches tall. Write a program that checks if a person meets these requirements based on their age and height input.  

age = int(input("enter your age:"))
height = int(input("enter your height in inches:"))
if age>= 14 and height>= 148: 
     print("you can ride the roller coaster")
else:
   print(" you cannot ride thye roller coaster")


age = int(input("enter your age:"))
if age>= 14:
     height = int(input("enter your height in inches:"))
     if height>= 148:
         print("you can ride the roller coaster")
     else:
         print("height must be at least 148 inches to ride the roller coaster")

else:
    print("age must be at least 14 years old to ride the roller coaster")

 #design a bank loan approval system. approve a lone only if all three condition are met:age is between 21 and 60(inclusive),monthly income is at least 30,000,credit scpre is at least 700.
age = int(input("enter your age:"))
if 21 <= age <= 60:
    income = int(input("enter your monthly income:"))
    if income >= 30000:
        credit_score =int(input("enter your crediut score"))
        if credit_score>=700:
            print("loan approved")
        else:
            print("credit score must be at least 700 for loan approved")
    else:
        print("monthly income must be at least 30,000 for the loan approval")
else:
    print("age must be between 21 and 60 (inclusive) for loan approval")



  #movie ticket pricing system: children under 12 years old get free tickets, adults between 12 and 60 years old pay Rs. 200, and seniors above 60 years old pay Rs. 100. Additionally, if an adult has a membership card, they get a discounted price of Rs. 130.  
age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))

age = int(input("Enter age: "))
has_membership = input("Do you have a membership card? (yes/no): ").lower()

if age < 12:
    price = 0
elif age <= 60:
    if has_membership == "yes":
        price = 130
    else:
        price = 200
else:
    price = 100

print(f"The ticket price is: Rs. {price}")



# A company awards a bonus to employees based on their years of service. If an employee has worked for more than 5 years, they receive a bonus of 5% of their salary. Write a program that calculates the net bonus amount for an employee based on their salary and years of service input.
salary = float(input("Enter salary: "))
service_years = int(input("Enter years of service: "))

if service_years > 5:
    bonus = 0.05 * salary
    print(f"Net bonus amount: {bonus}")
else:
    print("No bonus awarded.")



# Write a program that calculates the area of a circle based on the radius input by the user. Use the math module to access the value of pi.

radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)

print(f"The area of the circle is: {area:.2f}")



# A company has a wage system based on the age and gender of the employee. If the employee is between 18 and 30 years old, males receive a wage of Rs. 700 per day, while females receive Rs. 750 per day. 
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of days: "))

wage_per_day = 0

if age >= 18 and age < 30:
    wage_per_day = 700 if gender == 'M' else 750
elif age >= 30 and age <= 40:
    wage_per_day = 800 if gender == 'M' else 850

if wage_per_day > 0:
    total_wages = wage_per_day * days
    print(f"Total wages: {total_wages}")
else:
    print("No wage criteria met for this age group.")



# Write a program that takes a number as input and checks if it is divisible by 3, 5, or both. If the number is divisible by 3, print "Fizz". If it is divisible by 5, print "Buzz". If it is divisible by both 3 and 5, print "Fizz Buzz". Otherwise, print the number itself.
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
