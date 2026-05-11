
#Question 1 — Manual Trace
import math


import math
from turtle import right
i = 3
j = 5
k = 7
if i < j:
    if j < k: i = j
    else: j = k
else:
    if j > k: j = i
    else: i = k
print(i, j, k)
# a) i=3, j=5, k=7
# 3 < 5 → True. 5 < 7 → True, so i = j = 5.
# Output: 5 5 7
# b) i=-2, j=-5, k=9
# -2 < -5 → False. -5 > 9 → False, so i = k = 9.
# Output: 9 -5 9
# c) i=8, j=15, k=12
# 8 < 15 → True. 15 < 12 → False, so j = k = 12.
# Output: 8 12 12
# d) i=13, j=15, k=13
# 13 < 15 → True. 15 < 13 → False, so j = k = 13.
# Output: 13 13 13
# e) i=3, j=5, k=17
# 3 < 5 → True. 5 < 17 → True, so i = j = 5.
# Output: 5 5 17
# f) i=25, j=15, k=17
# 25 < 15 → False. 15 > 17 → False, so i = k = 17.
# Output: 17 15 17

#Question 2 — Manual Trace

if j < k:
    if i > j: j = i
    else: k = i
else:
    if j > k: i = j
    else: k = i
print(i, j, k)
# a) i=3, j=5, k=7
# 5 < 7 → True. 3 > 5 → False, so k = i = 3.
# Output: 3 5 3
# b) i=-2, j=-5, k=9
# -5 < 9 → True. -2 > -5 → True, so j = i = -2.
# Output: -2 -2 9
# c) i=8, j=15, k=12
# 15 < 12 → False. 15 > 12 → True, so i = j = 15.
# Output: 15 15 12
# d) i=13, j=15, k=13
# 15 < 13 → False. 15 > 13 → True, so i = j = 15.
# Output: 15 15 13
# e) i=3, j=5, k=17
# 5 < 17 → True. 3 > 5 → False, so k = i = 3.
# Output: 3 5 3
# f) i=25, j=15, k=17
# 15 < 17 → True. 25 > 15 → True, so j = i = 25.
# Output: 25 25 17

#Question 3 — Manual Trace

if k < i:
    if i > j: j = i
    else: k = i
else:
    if k > i: i = j
    else: k = i
print(i, j, k)
# a) i=3, j=5, k=7
# 7 < 3 → False. 7 > 3 → True, so i = j = 5.
# Output: 5 5 7
# b) i=-2, j=-5, k=9
# 9 < -2 → False. 9 > -2 → True, so i = j = -5.
# Output: -5 -5 9
# c) i=8, j=15, k=12
# 12 < 8 → False. 12 > 8 → True, so i = j = 15.
# Output: 15 15 12
# d) i=13, j=15, k=13
# 13 < 13 → False. 13 > 13 → False, so k = i = 13.
# Output: 13 15 13
# e) i=3, j=5, k=17
# 17 < 3 → False. 17 > 3 → True, so i = j = 5.
# Output: 5 5 17
# f) i=25, j=15, k=17
# 17 < 25 → True. 25 > 15 → True, so j = i = 25.
# Output: 25 25 17

#Question 4 — Student Resource Portal
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "ad123":
    print("Access Granted: Faculty Dashboard")
elif username == "student" and password == "st2026":
    print("Access Granted: Notes and Practice Questions")
else:
    print("Invalid Credentials. Please try again.")

#Question 5 — Customer Bill Calculator

total = float(input("Enter total purchase amount: "))

if total > 5000:
    membership = input("Do you have a membership card? (yes/no): ")
    if membership.lower() == "yes":
        discount = total * 0.30
        final = total - discount
        print(f"Total Saved: {discount}")
        print(f"Final: {final}")
    else:
        print(f"Total: {total}")
        print("Discount: 0")
else:
    print(f"Total: {total}")
    print("Discount: 0")

#Question 6 — Magic Forest Adventure Game
print("Welcome to the Magic Forest!")

direction = input("Stage 1 - Go North or South? (north/south): ").lower()

if direction == "north" or direction == "south":
    if direction == "north":
        choice = input("Stage 2 - Cross the river or follow the path? (cross/follow): ").lower()
        if choice == "cross":
            print("You cross the river. END.")
        else:
            creature = input("Stage 3 - Choose: fairy, ogre, or elf? ").lower()
            if creature == "fairy":
                print("GAME OVER")
            elif creature == "elf":
                print("YOU WIN!")
            elif creature == "ogre":
                print("GAME OVER")
            else:
                print("Invalid choice. GAME OVER")
    else:
        print("GAME OVER")
else:
    print("GAME OVER")

#Question 7 — Traffic Light System
light = input("Enter light color (red/yellow/green): ").lower()

if light == "red":
    print("STOP")
elif light == "yellow":
    print("GET READY")
elif light == "green":
    print("GO")
else:
    print("Error: Invalid traffic light color!")

#Question 8 — Season Match Statement
num = int(input("Enter a number (1-4): "))

match num:
    case 1:
        print("Spring")
    case 2:
        print("Summer")
    case 3:
        print("Autumn")
    case 4:
        print("Winter")
    case _:
        print("Unknown")

#Question 9 — Bank Loan Approval System
age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
credit = int(input("Enter credit score: "))

if 21 <= age <= 60 and income >= 30000 and credit >= 700:
    print("Loan Approved!")
else:
    print("Loan Not Approved. Reason(s):")
    if not (21 <= age <= 60):
        print("- Age must be between 21 and 60.")
    if income < 30000:
        print("- Monthly income must be at least 30,000.")
    if credit < 700:
        print("- Credit score must be at least 700.")

#Question 10 — BMI Calculator
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)
bmi = round(bmi, 1)

if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi <= 25:
    status = "Normal weight"
elif 25 < bmi <= 30:
    status = "Overweight"
else:
    status = "Obese"

print(f"Weight: {weight}")
print(f"Height: {height}")
print(f"BMI: {bmi} {status}")

#Question 11 — Movie Ticket Booking
age = int(input("Enter age: "))

if age < 12:
    print("Ticket Price: Free")
elif 12 <= age <= 60:
    membership = input("Do you have a membership card? (yes/no): ").lower()
    if membership == "yes":
        print("Ticket Price: Rs. 150")
    else:
        print("Ticket Price: Rs. 200")
else:
    print("Ticket Price: Rs. 100 (Senior Citizen Discount)")

# Question 12 - Employee Bonus
salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years > 5:
    bonus = salary * 0.05
    print(f"Bonus Amount: Rs. {bonus}")
else:
    print("Not eligible for bonus.")

# Question 13 — Area of Circle
import math

radius = float(input("Enter radius of the circle: "))
area = math.pi * radius ** 2
print(f"Area of the circle: {area:.2f}")

# Question 14 — Wage Calculator
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of days worked: "))

if 18 <= age < 30:
    if gender == "M":
        wage = 700 * days
    elif gender == "F":
        wage = 750 * days
    else:
        wage = 0
        print("Invalid gender")
elif 30 <= age <= 40:
    if gender == "M":
        wage = 800 * days
    elif gender == "F":
        wage = 850 * days
    else:
        wage = 0
        print("Invalid gender")
else:
    wage = 0
    print("Age not in valid range for wage calculation.")

if wage > 0:
    print(f"Total Wages: Rs. {wage}")

#Question 15 — FizzBuzz
pythonnum = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

#Question 16 — Electricity Bill
units = float(input("Enter electricity usage in units: "))

if units < 100:
    cost = units * 5
elif 100 <= units <= 300:
    cost = (100 * 5) + ((units - 100) * 8)
else:
    cost = (100 * 5) + (200 * 8) + ((units - 300) * 10)

print(f"Total Electricity Bill: Rs. {cost}")

#Question 17 — Rock Paper Scissors
p1 = input("Player 1 - Enter your move (rock/paper/scissors): ").lower()
p2 = input("Player 2 - Enter your move (rock/paper/scissors): ").lower()

print(f"\nPlayer 1: {p1}  |  Player 2: {p2}")

if p1 == p2:
    print("It's a Tie!")
elif (p1 == "rock" and p2 == "scissors") or \
     (p1 == "scissors" and p2 == "paper") or \
     (p1 == "paper" and p2 == "rock"):
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")

#Question 18 — Positive, Even or Odd
pythonnum = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print(f"{num} is Positive and Even.")
    else:
        print(f"{num} is Positive and Odd.")
else:
    print(f"{num} is not a positive number.")

# Question 19 — Store Discount
total_amount = float(input("Enter total purchase amount: "))
is_member = input("Are you a member? (True/False): ").lower() == "true"

if total_amount > 1000 and is_member:
    discount = total_amount * 0.20
elif total_amount > 1000 and not is_member:
    discount = total_amount * 0.10
else:
    discount = 0

final = total_amount - discount
print(f"Discount Applied: Rs. {discount}")
print(f"Final Amount: Rs. {final}")

#Question 20 — Planet Weight Converter
earth_weight = float(input("Enter your Earth weight (kg): "))
planet_num = int(input("Enter planet number (1-7): "))

if planet_num == 1:
    weight = earth_weight * 0.38
    print(f"Your weight on Mercury: {weight:.2f} kg")
elif planet_num == 2:
    weight = earth_weight * 0.91
    print(f"Your weight on Venus: {weight:.2f} kg")
elif planet_num == 3:
    weight = earth_weight * 0.38
    print(f"Your weight on Mars: {weight:.2f} kg")
elif planet_num == 4:
    weight = earth_weight * 2.53
    print(f"Your weight on Jupiter: {weight:.2f} kg")
elif planet_num == 5:
    weight = earth_weight * 1.07
    print(f"Your weight on Saturn: {weight:.2f} kg")
elif planet_num == 6:
    weight = earth_weight * 0.89
    print(f"Your weight on Uranus: {weight:.2f} kg")
elif planet_num == 7:
    weight = earth_weight * 1.14
    print(f"Your weight on Neptune: {weight:.2f} kg")
else:
    print("Invalid planet number")

#Question 21 — Marks & Grade
s1 = float(input("Enter marks for Subject 1: "))
s2 = float(input("Enter marks for Subject 2: "))
s3 = float(input("Enter marks for Subject 3: "))
s4 = float(input("Enter marks for Subject 4: "))

total = s1 + s2 + s3 + s4
percentage = total / 4

print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")

if percentage > 70:
    print("Grade: Distinction")
elif percentage > 60:
    print("Grade: First")
elif percentage > 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")

#Question 22 — Simple ATM Simulation
is_valid = True
balance = 5000
correct_pin = 123

if is_valid:
    pin = int(input("Enter your PIN: "))
    if pin == correct_pin:
        print("\n1. Withdraw\n2. Check Balance\n3. Exit")
        choice = int(input("Select option: "))
        if choice == 1:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawn: Rs. {amount}")
                print(f"Remaining Balance: Rs. {balance}")
            else:
                print("Insufficient balance.")
        elif choice == 2:
            print(f"Current Balance: Rs. {balance}")
        elif choice == 3:
            print("Thank you for visiting.")
        else:
            print("Invalid option selected.")
    else:
        print("Wrong PIN. Access denied.")
else:
    print("Card is not valid.")

#Question 23 — Elevator Logic System
floor = int(input("Enter target floor (0-10): "))
weight = float(input("Enter total weight (kg): "))
door = input("Is the door closed? (yes/no): ").lower()

if floor < 0 or floor > 10:
    print("INVALID FLOOR")
elif weight > 500:
    print("OVERWEIGHT: LIFT CANNOT MOVE")
elif door != "yes":
    print("WARNING: CLOSE THE DOOR")
else:
    print("ACTIVATE ELEVATOR MOTION")

# Question 23 — Facebook-style Form Validation
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
email = input("Enter email address: ")
re_email = input("Re-enter email address: ")
password = input("Enter password: ")

errors = []

if not first_name or not first_name.isalpha():
    errors.append("First name must not be empty and should contain letters only.")

if not last_name or not last_name.isalpha():
    errors.append("Last name must not be empty and should contain letters only.")

if "@" not in email or "." not in email:
    errors.append("Email must contain '@' and '.'")

if email != re_email:
    errors.append("Emails do not match.")

if len(password) < 6:
    errors.append("Password must be at least 6 characters.")

if errors:
    print("\nSign Up Failed:")
    for e in errors:
        print("-", e)
else:
    print("\nSign Up Successful! Welcome,", first_name)