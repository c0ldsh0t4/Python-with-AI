# age = int(input("Enter your age: "))
# number = 10
# print(age + 10)
#
# age = int(input("Enter your age: "))
#
# print("After 10 years you will be", age + 10)
#
# nums1 = int(input("Enter your first number: "))
# nums2 = float(input("Enter your second number: "))
# print(nums1 + nums2)

# score = int(input("Enter numbers from 0 to 100: "))
# if   90  <= score <= 100:
#     print("Great Job!")
# elif  75 <= score <= 89:
#     print("good")
# elif  60 <= score <= 74:
#     print("Удовлетворительно")
# else :
#     print("not done")

# traffic_light = input("Enter color: ")
# if traffic_light == "green":
#     print("Green traffic light you can go")
# elif traffic_light == "yellow":
#     print("Yellow traffic light you need wait")
# elif traffic_light == "red":
#     print("Red traffic light you need stop")
# else:
#     print("Another traffic light is Wrong color")


# nums1 = int(input("Enter a number: "))
# nums2 = int(input("Enter a number: "))
# operation = input("Enter operation: ")
# if operation == "+":
#     print(nums1 + nums2)
# elif operation == "-":
#     print(nums1 - nums2)
# elif operation == "*":
#     print(nums1 * nums2)
# elif operation == "/":
#     print(nums1 / nums2)
# else:
#     print("Operation not supported"

# total = int(input("Enter the total amount: "))
# if total <= 0:
#     print("Incorrect amount entered")
# elif total < 20:
#     print("Minimum withdrawal is 20")
# elif total > 500:
#     print("Maximum withdrawal is 500")
# elif 20 <= total <= 500:
#     print("Take your money")
# else:
#     print("Thank you for your money")

#
# size = input("Enter the size of your pizza: ").upper()
# price =0
# if size == "S":
#     price = 8
# elif size == "M":
#     price = 10
# elif size == "L":
#     price = 12
# else:
#     print("Wrong Size")
# if price != 0:
#     print("Size", size, "cost", price)
#

# age = int(input("Enter your age: "))
# if age < 6:
#     print("Ticket: Free")
# elif 6 <= age <= 17:
#     print("Ticket: 5$")
# elif 18 <= age <= 64:
#     print("Ticket: 10$")
# elif age >= 65:
#     print("Ticket: 7$")
#


# password = int(input("Enter your password: "))
#
# while password != 1234:
#       password = int(input("Enter your password: "))


# balance = 1000
# money = int(input("Enter your money: "))
# while money > balance:
#     print("Недостаточно средств!")
#     money = int(input("Enter your money: "))


# choice = int(input("Enter your choice: "))
# while choice != 0:
#
#     if choice == 1:
#         print(" Your choice is Coffe")
#     elif choice == 2:
#         print("Your choice is Tea")
#     elif choice == 3:
#         print("Your choice is Juice")
#     else:
#         print("That is not a valid choice")
#     choice = int(input("Enter your choice: "))
# print("Good bye! Exite")
#

# password = int(input("Enter your password: "))
# pin = 1234
# attempts = 3
# while password != pin and attempts > 0:
#     attempts -= 1
#     if attempts > 0:
#         print("You have", attempts, "attempts")
#         password = int(input("Please enter a password: "))
# if password == pin:
#     print("Welcome, you are now logged in")
# if attempts == 0 and password != pin:
#     print("Access denied!")
#
#


# menu = int(input("Please indicate your choice: "))
# while menu !=0 :
#     if menu == 1:
#         nums = int(input("Please indicate your number: "))
#         nums2 = int(input("Please indicate your number: "))
#         print(nums + nums2)
#     elif menu == 2:
#         nums = int(input("Please indicate your number: "))
#         nums2 = int(input("Please indicate your number: "))
#         print(nums - nums2)
#     else:
#         print("Wrong choice")
#     menu = int(input("Please indicate your choice: "))
# print("Good bye")


# balance = 100
# menu = int(input("Enter your choice: "))
# while menu != 0:
#     if menu == 1:
#         if balance >= 20:
#            print("You bought Bread.")
#            balance -= 20
#            print("Balance:", balance)
#         else :
#            print("Not enough money!")
#
#     if menu == 2:
#         if balance >= 35:
#             print("You bought Milk.")
#             balance -= 35
#             print("Balance:", balance)
#         else:
#             print("Not enough money!")
#
#     if menu == 3:
#         if balance >= 50:
#             print("You bought Cheese.")
#             balance -= 50
#             print("Balance:", balance)
#         else:
#             print("Not enough money!")
#     menu = int(input("Enter your choice: "))
#
# print("Goodbye!")
# print("Thank you for your time!")


# balance = 250
# menu = int(input("Enter the menu :"))
# while menu !=0:
#         if menu == 1:
#             print( "Your balance is" , balance)
#         if menu == 2:
#             deposit = int(input("How much money do you want to deposit?"))
#             balance += deposit
#             print("Your new balance is", balance)
#         if menu == 3:
#             withdraw = int(input("How much money do you want to withdraw?"))
#             if balance >= withdraw:
#                 balance -= withdraw
#                 print("Your new balance is", balance)
#             else:
#                 print("Sorry, you can't withdraw money")
#         menu = int(input("Enter the menu :"))
# print("Goodbye!")
# print("Thank you for your time!")

# login = "admin"
# password = "12345"
# menu = int(input("choice menu: "))
# logged_in = False
# while logged_in == False and menu != 0:
#     if menu == 1:
#         user_login = input("Enter your username: ")
#         if login == user_login:
#             user_password = input("Enter your password: ")
#             if user_password == password:
#                 print("Welcome")
#                 logged_in = True
#             else:
#                 print("Wrong password")
#         else:
#             print("Wrong username ")
#
#
#     menu = int(input("choice menu: "))
# print("Goodbye")
# logged_in = True


# secret_code= "2580"
# menu = int(input("Choice menu: "))
# opened = False
# while  opened != True and menu != 0:
#     if menu == 1:
#       user_code = input("Enter your code: ")
#       if user_code == secret_code:
#          opened = True
#          print("Safe opened!")
#       else:
#          print("Wrong Code!")
#     menu = int(input("Choice menu: "))
# print("Good bye!")

# phone_password = "4321"
# unlocked = False
# battery = 75
# time = "12:30"
# menu = int(input("Choose an option: "))
# while unlocked != True and menu != 0:
#     if menu == 1:
#         user_password = input("Enter your code: ")
#         if user_password == phone_password:
#             unlocked = True
#             print("Phone unlocked!")
#         else:
#             print("Wrong password!")
#     if menu == 2:
#         print("Battery: " + str(battery) + "%")
#     if menu == 3:
#         print("Time:", time)
#
#     menu = int(input("Choose an option: "))
# print("Goodbye!")

# seats = 5
# menu = int(input("Choose menu: "))
# while menu != 0:
#     if menu == 1:
#         print("Buy ticket")
#         if seats > 0:
#            print("Ticket purchased!")
#            seats -= 1
#            print("Free seats: " + str(seats))
#         else:
#             print("No more seats!")
#     if menu == 2:
#      print("Free seats: " + str(seats))
#     menu = int(input("Choose menu: "))
# print("Goodbye!")


# lives = 3
# menu = int(input("Choose your option: "))
# while menu != 0:
#     if menu == 1:
#         if lives > 0:
#             lives -= 1
#             print("lives: " + str(lives))
#             print("You lost one life!")
#         else:
#             print("Game Over!")
#     if menu == 2:
#         print ("lives: " + str(lives))
#     menu = int(input("Choose your option: "))
# print("Goodbye!")

# balance = 1000
# menu = int(input("Enter your choice: "))
# while menu != 0:
#     if menu == 1:
#         deposit = int(input("Enter your deposit: "))
#         if deposit > 0:
#             balance += deposit
#         print("Money added")
#         print("New balance: " + str(balance))
#     if menu == 2:
#         withdraw = int(input("Enter your withdraw: "))
#         if withdraw > balance:
#           print("Not enough money!")
#         if withdraw <= balance:
#             balance -= withdraw
#             print("Money withdrawn ")
#
#         print("You balance: " + str(balance))
#     if menu == 3:
#         print("Balance: " + str(balance))
#     menu = int(input("Enter your choice: "))
# print("Goodbye")


# free_places = 5
# menu = int(input("Enter you choice: "))
# while menu != 0:
#     if menu == 1:
#         if free_places > 0:
#            free_places -= 1
#            print("Car entered!")
#            print("free places: " + str(free_places))
#         else:
#            print("Parking is full!")
#     if menu == 2:
#         print("Free places: " + str(free_places))
#
#     menu = int(input("Enter you choice: "))
# print("Goodbye")

# secret_code = "1234"
# attempts = 3
# opened = False
# menu = int(input("Enter menu: "))
# while menu != 0:
#     if menu == 1:
#         if opened == True:
#             print("Lock is already opened!")
#         if opened == False:
#             if attempts > 0:
#                user_code = input("Enter code: ")
#                if user_code == secret_code:
#                   opened = True
#                   print("Lock opened!")
#                else:
#                   attempts -= 1
#                   print("Wrong code!")
#                   print("Attempts left: " + str(attempts))
#             else:
#                   print("No attempts left!")
#     if menu == 2:
#         print("You have: " + str(attempts) + " attempts")
#
#     menu = int(input("Enter menu: "))
# print("Goodbye!")


# rooms = 3
# menu = int(input("Enter you choice: "))
# while menu != 0:
#     if menu == 1:
#         if rooms > 0:
#             take_room = int(input("How many rooms you need: "))
#             if take_room <= rooms:
#                rooms -= take_room
#                print(f"Guest checked in!")
#                print(f"Free rooms: {rooms} rooms")
#             else :
#                print("Not enough rooms")
#                print(f"Only {rooms} rooms available.")
#
#     if menu == 2:
#         print(f"Free rooms: {rooms} rooms")
#
#     menu = int(input("Enter you choice: "))
# print("Goodbye")
#
# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are not old enough")
# elif  18 <= age <= 60:
#     print("You are old enough to vote!")
# else:
#     print("You are a pensioner!")

# nums1 = int(input("Enter the first number: "))
# operation = input("Enter the operation: ")
# nums2 = int(input("Enter the second number: "))
# if operation == "+":
#     print(nums1 + nums2)
# elif operation == "-":
#     print(nums1 - nums2)
# elif operation == "*":
#     print(nums1 * nums2)
# elif operation == "/":
#     print(nums1 / nums2)
# else:
#     print("Unknown operation")

# menu = int(input("Choose your menu: "))
# while menu != 0:
#     if menu == 1:
#         print(f"You choice  {menu}: Welcome to the Sum!")
#         first_number = int(input("Choose your first number: "))
#         second_number = int(input("Choose your second number: "))
#         result = first_number + second_number
#         print(f"Result: {result}")
#     elif menu == 2:
#         print(f"You choice {menu}: Welcome to the Subtrack!")
#         first_number = int(input("Choose your first number: "))
#         second_number = int(input("Choose your second number: "))
#         result = first_number - second_number
#         print(f"Result: {result}")
#     elif menu == 3:
#         print(f"You choice {menu}: Welcome to the Multiply!")
#         first_number = int(input("Choose your first number: "))
#         second_number = int(input("Choose your second number: "))
#         result = first_number * second_number
#         print(f"Result: {result}")
#     elif menu == 4:
#         print(f"You choice {menu}: Welcome to the Divide!")
#         first_number = int(input("Choose your first number: "))
#         second_number = int(input("Choose your second number: "))
#         if second_number == 0:
#             print("Error! Division by zero is not allowed.")
#         else:
#             result = first_number / second_number
#             print(f"Result: {result}")
#     elif menu == 5:
#         print(f"You choice {menu}: Compare two numbers!")
#         first_number = int(input("Choose your first number: "))
#         second_number = int(input("Choose your second number: "))
#         if first_number > second_number:
#             print(f"The larger number is: {first_number}")
#         elif first_number == second_number:
#             print(f"The numbres are equal!")
#         else:
#             print(f"The larger number is: {second_number}")
#     elif menu == 6:
#         print(f"You choice {menu}: Find the largest number")
#         first_number = int(input("Choose your first number: "))
#         second_number = int(input("Choose your second number: "))
#         third_number = int(input("Choose your third number: "))
#         if first_number > second_number and first_number > third_number:
#             print(f"The largest number is: {first_number}")
#         elif second_number > first_number and second_number > third_number:
#             print(f"The largest number is: {second_number}")
#         elif third_number > first_number and third_number > second_number:
#             print(f"The largest number is: {third_number}")
#         else:
#             print("The numbres are equal!")
#     elif menu == 7:
#         print(f"You choice {menu}: Even or Odd")
#         number = int(input("Enter your number: "))
#         if number % 2 == 0:
#             print(f"{number} is even.")
#         else:
#             print(f"{number} is odd.")
#     else:
#         print(f"You choice {menu}: Invalid choice!")
#     menu = int(input("Choose your menu: "))
# print(f"You chose {menu} Goodbye!")


# text = "Programming"
# print(text[:3])
# print(text[3:7])
# print(text[7:])
# print(text[:])
# print(text[::-1])
#
# text = "Programming"
# print(text.find("Java"))
#
# text = "Programming"
# print(text.count("m"))

# text = "    Python Programming    "
#
# print(text.upper())
# print(text.strip())
# print(text.replace("Programming", "Developer"))
# print(text.count("m"))
# print(text.find("Python"))

# text = "Python Programming"
# print("Python" in text)
# .find() -- Где находится, по какому индексу начинается
# .in (переменная) -- Спрашивает есть или нету - вернет boolen

# text = input("Enter a text: ")
# text = text.strip()
# print(text)
# print(text.upper())
# print(text.count("a"))
# if "python" in text.lower():
#     print("Python found!")
# else:
#     print("Python not found!")

# text = "Python"
#
# for i in range(len(text)):
#     print(i, text[i])
#
# text = "Python"
#
# for letter in text:
#     print(letter)
#
# fruits = ["apple", "banana", "orange"]
#
# for item in fruits:
#     print(item)

# text = input("Enter text: ")
# for letter in text:
#     if letter == "a":
#         print(f"{letter} Found a")
#     else:
#         print(letter)

# text = input("Enter text: ")
# vowels = "aeiou"
# for letter in text.lower():
#     if letter in  vowels:
#         print(f"{letter} -> Vowel")
#     else:
#         print(f"{letter} -> Consonant")

#
# text = input("Enter text: ")
# vowels = "aeiou"
# vowels_count = 0
# consonants_count = 0
# for letter in text.lower():
#     if letter.isalpha():
#         if letter in vowels:
#             vowels_count += 1
#         else:
#             consonants_count += 1
# print(f"Vowels: {vowels_count}")
# print(f"Consonants: {consonants_count}")

# text = ""
# menu = -1
# vowels = "aeiou"
# while menu != 0:
#     print()
#     print("==================================")
#     print("        TEXT ANALYZER v1.0")
#     print("==================================")
#     if not text:
#         print("Current text: <No text entered>")
#     else:
#         print(f"Current text: {text}")
#     print("--------------------------------------")
#     print("1. Count vowels")
#     print("2. Count consonants")
#     print("3. Count letters")
#     print("4. Count digits")
#     print("5. Count spaces")
#     print("6. Reverse text")
#     print("7. Upper case")
#     print("8. Lower case")
#     print("9. Enter text")
#     print("0. Exit")
#     print("--------------------------------------")
#     menu = int(input("Enter your choice: "))
#     if menu == 1:
#         if not text:
#             print("No text found. Please enter text first!")
#         else:
#             vowels_count = 0
#             for letter in text.lower():
#                 if letter in vowels:
#                     vowels_count += 1
#             print("------------------------------")
#             print(f"Vowels: {vowels_count}")
#             print("------------------------------")
#     elif menu == 2:
#         if not text:
#             print("No text found. Please enter text first!")
#         else:
#             print("Count consonants")
#             consonants_count = 0
#             for letter in text.lower():
#                 if letter.isalpha() and letter not in vowels:
#                     consonants_count += 1
#             print("------------------------------")
#             print(f"Сonsonants: {consonants_count}")
#             print("------------------------------")
#     elif menu == 3:
#         if not text:
#             print("No text found. Please enter text first!")
#         else:
#             print("Count letters")
#             letters_count = 0
#             for letter in text.lower():
#                 if letter.isalpha():
#                     letters_count += 1
#             print("------------------------------")
#             print(f"Letters: {letters_count}")
#             print("------------------------------")
#     elif menu == 4:
#         if not text:
#             print("No text found. Please enter text first!")
#         else:
#             print("Count digits")
#             digits_count = 0
#             for letter in text.lower():
#                 if letter.isdigit():
#                     digits_count += 1
#             print("------------------------------")
#             print(f"Digits: {digits_count}")
#             print("------------------------------")
#     elif menu == 5:
#         if not text:
#             print("No text found. Please enter text first!")
#         else:
#             print("Count spaces")
#             spaces_count = 0
#             for letter in text.lower():
#                 if letter.isspace():
#                     spaces_count += 1
#             print("------------------------------")
#             print(f"Spaces: {spaces_count}")
#             print("------------------------------")
#     elif menu == 6:
#         if not text:
#             print("No text found. Please enter text first!")
#         else:
#             print("Reverse text")
#             reverse = ""
#             for letter in range(len(text) -1, -1, -1):
#                 reverse += text[letter]
#             print("------------------------------")
#             print(f"Reversed text: {reverse}")
#             print("------------------------------")
#     elif menu == 7:
#         if not text:
#             print("No text found. Please enter text first!")
#         else:
#             print("------------------------------")
#             print(f"Upper case: {text.upper()}")
#             print("------------------------------")
#     elif menu == 8:
#         if not text:
#             print("No text found. Please enter text first!")
#         else:
#             print("------------------------------")
#             print(f"Lower case: {text.lower()}")
#             print("------------------------------")
#     elif menu == 9:
#         print("------------------------------")
#         text = input("Enter new text: ")
#         print("Text updated!")
#         print("------------------------------")
#     elif menu == 0:
#         print("Goodbye!")

# numbers = [12, 5, 18, 7, 25]
#
# maximum = numbers[0]
# for number in numbers:
#     if maximum < number:
#         maximum = number
# print(maximum)


