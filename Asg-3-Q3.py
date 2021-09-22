import re
paragraph = input(("Enter a paragraph :"))
regex =(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')
phonenumbers = re.findall(regex,paragraph)
print(phonenumbers)