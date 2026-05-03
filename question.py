# Q1: Check if number is between 1 and 100
num = int(input("Enter a number: "))

if 1 <= num <= 100:
    print("The number is between 1 and 100.")
else:
    print("The number is NOT between 1 and 100.")
 
 # Q2: Check if a number is even or odd
num= int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even.")
else:
    print(num, "is Odd.")

# Q3: Display month name from number (1–12)
months = ["January", "February", "March", "April",
          "May", "June", "July", "August",
          "September", "October", "November", "December"]

num = int(input("Enter a number (1-12): "))

if 1 <= num <= 12:
    print("Month:", months[num - 1])
else:
    print("Error: Please enter a number between 1 and 12.")

# Q4: School grading system
marks = int(input("Enter your marks: "))

if marks < 25:
    grade = "F"
elif marks < 45:
    grade = "E"
elif marks < 50:
    grade = "D"
elif marks < 60:
    grade = "C"
elif marks <= 80:
    grade = "B"
else:
    grade = "A"

print(f"Grade: {grade}")

# Q5: Check if a number is divisible by 7
num = int(input("Enter a number: "))

if num % 7 == 0:
    print(num, "is divisible by 7.")
else:
    print(num, "is NOT divisible by 7.")


# Q6: Accept two numbers and an operator
a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b != 0:
        result = a / b
    else:
        print("Error: Division by zero!")
        result = None
else:
    print("Invalid operator!")
    result = None

if result is not None:
    print(f"Your Answer is: {result}")

# Q7: Car loan eligibility check
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))

if salary >= 50000 and credit_score >= 700:
    print("Eligible for car loan.")
else:
    print("Not Eligible for car loan.")

# Q8: FizzBuzz
n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")
elif n % 3 == 0:
    print("Fizz")
else:
    print(n)

# Q9: Check vowel or consonant
char = input("Enter a character: ").lower()

if char in "aeiou":
    print(char, "is a Vowel.")
elif char.isalpha():
    print(char, "is a Consonant.")
else:
    print("Not a valid alphabet character.")

# Q10: Determine grade from marks
marks = int(input("Enter marks: "))

if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks <= 89:
    print("Grade: B")
elif 70 <= marks <= 79:
    print("Grade: C")
else:
    print("Grade: Fail")

# Q11: Categorize age group
age = int(input("Enter your age: "))

if age < 13:
    print("Category: Child")
elif 13 <= age <= 19:
    print("Category: Teenager")
else:
    print("Category: Adult")

# Q12: Check character type
char = input("Enter a character: ")

if char.isupper():
    print(char, "is an Uppercase letter.")
elif char.islower():
    print(char, "is a Lowercase letter.")
elif char.isdigit():
    print(char, "is a Digit.")
else:
    print("Not a letter or digit.")

# Q13: Traffic light — color to action
color = input("Enter color (Red/Yellow/Green): ").strip()

if color == "Red":
    print("Action: Stop")
elif color == "Yellow":
    print("Action: Get Ready")
elif color == "Green":
    print("Action: Go")
else:
    print("Invalid color entered.")

# Q14: Job eligibility based on age and experience
age = int(input("Enter your age: "))
experience = int(input("Enter years of experience: "))

if age > 18 and experience >= 2:
    print("Eligible for the job.")
else:
    print("Not Eligible for the job.")

# Q15: Advice based on temperature
temp = float(input("Enter temperature in °C: "))

if temp > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temp <= 30:
    print("Enjoy the weather!")
else:
    print("It's cold, wear warm clothes!")

# Q16: Menu item prices
item = input("Enter item (Pizza/Burger/Pasta): ").strip()

if item == "Pizza":
    print("Price: $10")
elif item == "Burger":
    print("Price: $7")
elif item == "Pasta":
    print("Price: $8")
else:
    print("Item not found in menu.")

# Q17: Player selection based on height
height = float(input("Enter height in feet: "))

if height >= 6:
    print("Player is Selected.")
else:
    print("Player is Not Selected.")

# Q18: Movie eligibility based on age
age = int(input("Enter your age: "))

if age >= 18:
    print("Allowed to watch the movie.")
else:
    print("Not Allowed — must be 18 or older.")

# Q19: Check login credentials
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "password123":
    print("Access Granted.")
else:
    print("Access Denied.")

# Q20: Season from month number
month = int(input("Enter month number (1-12): "))

if month in [12, 1, 2]:
    print("Season: Winter")
elif month in [3, 4, 5]:
    print("Season: Spring")
elif month in [6, 7, 8]:
    print("Season: Summer")
elif month in [9, 10, 11]:
    print("Season: Autumn")
else:
    print("Invalid month number.")
