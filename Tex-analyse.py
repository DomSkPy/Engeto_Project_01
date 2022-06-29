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
author =
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#Welcoming user
login_name = input(f"Please entry your login name:")
login_password = input(f"Please entry your password:")
line = ("-" * 40)
print(line)
print(f"username: {login_name}")
print(f"password: {login_password}")
print(line)
registry_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
name = registry_users.keys
registry = registry_users.values

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

if not number_of_text.isnumeric():
    print(f"Can't allocate.")
    exit()
elif int(number_of_text) == 1:
    text_ch = str(TEXTS[0])
elif int(number_of_text) == 2:
    text_ch = str(TEXTS[1])
elif int(number_of_text) == 3:
    text_ch = str(TEXTS[2])
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
        title_case = title_case + 1
    elif w.isupper():
        upper_case = upper_case + 1
    elif w.islower():
        lower_case = lower_case + 1
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

