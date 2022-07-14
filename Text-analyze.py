"""
first_project.py: prvni projekt do Engeto Online Python Akademie

autor: Domnik Skrenek
email: skrenekD@gmail.com
discord: DomSk
"""

"""
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+

"""
'''
author = Dominik Skrenek
'''
from task import TEXTS

#Registery users
registry_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
name = registry_users.keys
line = ("-" * 40)
#Welcoming user
print(line)
print((" " * 3) + ("Welcome to text analyzer!"))
print(line)
login_name = input(f"Please entry your login name:")
login_password = input(f"Please entry your password:")
print(line)
print(f"username: {login_name}")
print(line)


#entry for user
if registry_users.get(login_name) == login_password:
    print(f"Welcome to the app {login_name.title()}.\nWe have 1 to {len(TEXTS)} texts to be analyzed.")
else:
    print(f"Unregistered user, terminating the program...")
    exit()
print(line)

#number of the texts
number_of_text = input(f"Enter a number btw. 1 and {len(TEXTS)}:")
print(line)

if not number_of_text.isdigit():
    print(f"Can't allocate.")
    exit()
elif int(number_of_text) == 1:
    text_ch = (TEXTS[0])
elif int(number_of_text) == 2:
    text_ch = (TEXTS[1])
elif int(number_of_text) == 3:
    text_ch = (TEXTS[2])
else:
    print("Wrong number.")
    exit()

# Count of the word, title and upper lower cases, digits and frequencies
title_case = 0
upper_case = 0
lower_case = 0
words = 0
digits = list()
frec = dict()

# w -> shortcut for "word"
for w in text_ch.split():
    w = w.strip(",")
    words += 1
    if len(w) not in frec:
        frec[len(w)] = 1
    else:
        frec[len(w)] += 1

    if w.istitle():
        title_case += w.istitle()
    elif w.isupper():
        upper_case += w.isupper()
    elif w.islower():
        lower_case += w.islower()
    elif w.isdigit():
        digits.append(int(w))

print(
    f"There are {words} words in the selected text",
    f"There are {title_case} title cases words",
    f"There are {lower_case} lower cases words",
    f"There are {len(digits)} digits words",
    f"Sum of nubers in text: {sum(digits)}",
    sep="\n"
)
print(line)

# Graf
print(line)
zah = "|Width|" + (" " * 2) + "|Occurences|" + (" " * 3) + "|Numb.|" + (" " * 3)
print(zah)
print(line)


for a, b in frec.items():
    print(a, int(b) * "*", b)
print(line)

