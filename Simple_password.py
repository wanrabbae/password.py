#MEMBUAT INPUT USERNAME DAN PASSWORD SIMPLE BY ALWAN

usr = input("Username: ")

import getpass

password = getpass.getpass()
if password == "123" and usr == "alwan":
    print("Correct!")
else:
    print("Incorrect!")
