# Home Work 5.1

import keyword
import string

variable =input()

if variable == "":
    print(False)
elif  variable in keyword.kwlist:
    print(False)

elif variable[0] in string.digits:
    print(False)

elif "__" in variable:
    print(False)
else:
    valid = True
    for symbol in variable:
        if symbol in string.punctuation and symbol != "_":
            valid = False
        elif symbol == " ":
            valid = False
        elif symbol.isupper():
            valid = False

    print(valid)

test_data = ['__',
             '___',
             'x',
             'get_value',
             'get value',
             'get!value',
             'some_super_puper_value',
             'Get_value','get_Value',
             'getValue',
             '3m',
             'm3',
             'assert',
             'assert_exception' ]

for variable in test_data:
    if variable == " ":
        print(False)
    elif variable in keyword.kwlist:
        print(False)

    elif variable[0] in string.digits:
        print(False)

    elif "__" in variable:
        print(False)
    else:
        valid = True
        for symbol in variable:
            if symbol in string.punctuation and symbol != "_":
                valid = False
            elif symbol == " ":
                valid = False
            elif symbol.isupper():
                valid = False
        print(variable, "->", valid)


# Home Work 5.2
work = "yes"
while work == "yes":
    number1 = int(input())
    operation = input()
    number2 = int(input())
    match operation:
        case "+":
            print(number1 + number2)

        case "-":
            print(number1 - number2)

        case "*":
            print(number1 * number2)

        case "/":
            if number2 != 0:
                print(number1 / number2)
            else:
                print("can't divide by zero")
    work = input("Continue? (yes/no) ").lower()


# Home Work 5.3

text = input()
text = text.title()
hashtag = "#"
for symbol in text:
    if symbol not in string.punctuation and symbol != " ":
        hashtag += symbol

    if len(hashtag) > 140:
        hashtag = hashtag[:140]
print(hashtag)