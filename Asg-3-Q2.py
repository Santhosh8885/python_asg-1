

import re

email = input("Enter email id :")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
if (re.fullmatch(regex,email)):
    print("Valid email")
else:
    print("Invalid email")