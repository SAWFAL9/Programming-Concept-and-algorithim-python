#Title format for patient name:
name = "rahUl DahaL"
print(name.title())  # Output: Rahul Dahal

#Lowercase password for comparison:
password = "Pass@123"
print(password.lower())  # Output: pass@123

#Movie name in title case:
movie = "spider-man no way home"
print(movie.title())  # Output: Spider-Man No Way Home

#Heading in ALL CAPS:
heading = "annual sports day"
print(heading.upper())  # Output: ANNUAL SPORTS DAY

#CAPS-LOCK reversal (swapcase):.
sentence = "hELLO wORLD"
print(sentence.swapcase())  # Output: Hello World

#Find first position of 'error':
log = 'System error detected, error code 404'
print(log.find('error'))  # Output: 7

#Email ends with '@gmail.com':
pythonemail = "user@gmail.com"
print(email.endswith('@gmail.com'))  # Output: True

# Count occurrences of 'free':
pythonmsg = 'Get free stuff, free gifts and free coupons now!'
print(msg.count('free'))  # Output: 3

# URL starts with 'https':
pythonurl = "https://example.com"
print(url.startswith('https'))  # Output: True

# Keyword 'Python' in resume:
pythonresume = "Experienced in Python and Django"
print('Python' in resume)  # Output: True

# Index of 'FAILED':
pythonmsg = 'Transaction FAILED due to low balance'
print(msg.index('FAILED'))  # Output: 12

# Check PDF file:
pythonfile = 'budget_report.pdf'
print(file.endswith('.pdf'))  # Output: True

# Nepal country code check:
pythonphone = '+977-9841123111'
print(phone.startswith('+977'))  # Output: True

# Government website check:
pythonurl = 'https://www.moha.gov.np/'
print(url.endswith('.gov.np/'))  # Output: True

# Remove extra spaces from feedback:
pythonfeedback = '   Great service!   '
print(feedback.strip())  # Output: Great service!

# Replace banned word in chat:
pythonmsg = 'I hate this, hate it completely'
print(msg.replace('hate', '****'))
# Output: I **** this, **** it completely

# Remove leading slashes from filename:
pythonfilename = '///student_records.pdf'
print(filename.lstrip('/'))  # Output: student_records.pdf

# Clean price string on right side:
pythonprice = 'Price: $120.33   '
print(price.rstrip().rstrip('0123456789.$').rstrip())
# Simpler: price.rstrip()  # Output: Price: $120.33

# Remove dashes from phone number:
pythonphone = '+977 984-123-4567'
print(phone.replace('-', ''))  # Output: +977 984123456

# Split CSV student data:
pythondata = 'Aarav,22,Kathmandu,Computer Science'
fields = data.split(',')
for field in fields:
    print(field)
# Output: Aarav / 22 / Kathmandu / Computer Science
