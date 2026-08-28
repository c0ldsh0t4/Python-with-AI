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
# from operator import truediv

# from pip._internal.commands import search

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

# МЕТОДЫ КОТОРЫЕ ИЗМЕНЯЮТ СПИСОК
# append() -- Добавляет элемент в конец списка
# insert() -- Вставляет элемент по указанному индексу
# remove() -- Удаляет первое найденое значение
# pop() -- Удаляет элемент по индексу и возвращает его
# sort() -- Сортирует список
# reverse() -- Разворачивает список

# МЕТОДЫ КОТОРЫЕ ВОЗВРАЩАЮТ ЗНАЧЕНИЕ
# count() -- Считает количество одинаковых элементов
# index() -- Возвращает индекс первого найденного элемента
    # ВСТРОЕНЫЕ ФУНКЦИИ
# len() -- Выводит количество элементов
# max() -- Максимальный элемент
# min() -- Минимальный элемент
# pop() -- Это исключение и относится к двум,-- Удаляет элемент и возвращает его
# Оператор in -- Проверяет наличие элемента Ответ True or False
# if number % 2 == 0: -- Проверка четности
#
# numbers = [5, 8, 12, 20, 25]
# if not numbers:
#    print("List is empty")
# else:
#     removed = numbers.pop()
#     print(f"Removed: {removed}")
#     print(numbers)
#
# list1 = ["Python", "SQL"]
#
# list2 = list1.copy()

# playlist = [
#     "Eminem",
#     "Linkin Park",
#     "Imagine Dragons"
# ]
# song = input("Enter the name of the song: ")
# if song in playlist:
#     playlist.remove(song)
#     playlist.append(song)
#     print(playlist)
# else:
#     print("The song is not in the playlist")


# tasks = ["Learn Python", "Go to Gym", "Buy Milk"]
# task = input("What do you want? ")
# if task in tasks:
#     new_tasks = tasks.copy()
#     new_tasks.remove(task)
#     print(tasks)
#     print(new_tasks)
# else:
#     print("Task not found.")

# students = ["Alex", "Mike", "John"]
# student = input("What is your name? ")
# if student in students:
#     students.index(student)
#     index = students.index(student)
#     students.insert(index, "⭐")
#     print(students)

# movies = ["Avatar", "Titanic", "Inception"]
# movie = input("Enter movie name: ")
# movies_copy = movies.copy()
# if movie in movies:
#     movies_copy.remove(movie)
#     movies_copy.append("Watched")
#     print(f"{movie} Watched")
#     print(movies)
#     print(movies_copy)
# else:
#     print(f"{movie}  not found")


# users = ["Alex", "Mike", "John", "Mike"]
# user = input("Please enter your name: ")
# user_copy = users.copy()
# if user  in users:
#     index = user_copy.index(user)
#     removed = user_copy.pop(index)
#     remaining = user_copy.count(user)
#
#     print(f"Removed: {removed}")
#     print(f"Remaining: {remaining}")
#     print(user_copy)
#     print(users)
#
#
# else:
#     print("User not found")
#
# numbers = [5, -3, 10, -8, 15, -1, 20]
# for number in numbers:
#     if number < 0:
#         continue
#     print(number)

# users = ["Alex", "", "Mike", "", "John"]
# for user in users:
#     if user == "":
#         continue
#     print(user)




# maximum = numbers[0]

# numbers = [10, 20, 30, 40]
# x = max(numbers)
# print(x)

# for number in numbers:
#     if number > maximum: --- Поиск максимум без max()
#         maximum = number
# print(maximum)

# minimum = numbers[0]
# for number in numbers:
#     if number < minimum: --- Поиск минимум без mix()
#         minimum = number
# print(minimum)


# numbers = [10, 20, 30]
# x = numbers.pop()
# print(x)
# print(numbers)

# numbers = [8, 3, 15, 2, 10]
# minimum = numbers[0]
# for number in numbers:
#     if number < minimum:
#         minimum = number
# x = numbers.index(minimum)
# print(f"Minimum: {minimum}")
# print(f"Index: {x}")

# numbers = [30, 10, 20]
#
# x = numbers.sort()
#
# print(x)
# print(numbers)


# numbers = [5, 10, 20, 40]
# search = int(input("Какое число найти? "))
#
# print(numbers.index(search))


# numbers = [10, 20 ,30]
# numbers.append(40)
# print(numbers)

# numbers = [10, 20 ,30, 40]
# numbers.remove(20)
# print(numbers)

# numbers = [10, 20, 30]
# x = numbers.pop()
# print(x)
# print(numbers)

# numbers = [30, 10, 20]
# numbers.sort()
# print(numbers)




# numbers = [5, 10, 15, 10, 20]
# x = numbers.count(10)
# print(x)

# numbers = [50, 10, 80, 5]
# minimum = min(numbers)
# for number in numbers:
#    if number == minimum:
#        minimum = number
#        index = numbers.index(minimum)
# print(minimum)
# print(index)


# numbers = [50, 10, 80, 5]
# minimum = min(numbers)
# index = numbers.index(minimum)
# print(numbers)
# print(index)

# numbers = [12, 8, 15, 3, 20]
# minimum = numbers[0]
# for number in numbers:
#     if number < minimum:
#         minimum = number
# print(minimum)

# numbers = [12, 25, 18, 40, 9]
# maximum = numbers[0]
# for number in numbers:
#     if number > maximum:
#         maximum = number
# print(maximum)

# numbers = [40, 10 ,30 ,20]
# numbers.remove(10)
# print(numbers)

#
# numbers = [6, 12, 3, 25, 8]
# for number in numbers:
#     if number % 2 == 0:
#         print(number)

# numbers = [6, 12, 3, 25, 8]
# total = 0
# for number in numbers:
#     if number % 2 == 0:
#         total += number
# print(total)

#
# def show_menu():
#     print("==== MENU ====")
#     print("1. Start")
#     print("2. Settings")
#     print("0. Exit")
#
# show_menu()
# show_menu()

# def greet(name):
#         print(f"Hello {name}")
#
# greet("Alex")
# greet("Bob")

# def show_user(name , age):
#     print(f"Name: {name}, Age: {age}")
# show_user("Alex", 18)
# show_user("John", 23)

# def multiply(a, b):
#     return a * b
#
# result = multiply(4, 6)
# print(result)


# def add(a, b):
#     return a + b
#
# print(add(10, 5))

# def last_word(text):
#     return text.split()[-1]

# def square(number):
#     return number ** 2
# print(square(5))
#
# def add(a, b):
#     return a + b
# result = add(10, 5)
# print(result)
# print(add(10 , 5))

# def multiply(a, b):
#     return a * b
# result = multiply(4, 6)
# print(result)

# def user_info(name, age):
#     return f"Name: {name}, Age: {age}"
# info = user_info("Alex" , 25)
# print(info)

# def count_words(text):
#    return len(text.split())
# result = count_words("I love Python")
# print(result)

# def first_word(text):
#     return text.split()[0]
# result = first_word("I love Python")
# print(result)

# def last_word(text):
#     return text.split()[-1]
# result = last_word("I love Python")
# print(result)

# def is_adult(age):
#     if age >= 18:
#         return "Adult"
#     else:
#         return "Not adult"
#
# print(is_adult(25))
# print(is_adult(16))

# def print_positive(numbers):
#     result = []
#     for number in numbers:
#         if number > 0:
#             result.append(number)
#     return result
# numbers = [5, -3, 10, -8, 15, -1, 20]
# result = print_positive(numbers)
# print(result)
#
# def get_even(numbers):
#     results = []
#     for number in numbers:
#         if number % 2 == 0:
#             results.append(number)
#     return results
#yield number*2
# numbers = [3, 8, 11, 20, 7, 14, 5]
# results = get_even(numbers)
# print(results)

# def double_numbers(numbers):
#     result = []
#     for number in numbers:
#        result.append(number * 2)
#     return result
# numbers = [2, 5, 10, 3]
# result = double_numbers(numbers)
# print(result)

# def get_long_words(words):
#     result = []
#     for word in words:
#         if len(word) > 4:
#             result.append(word)
#     return result
# words = ["cat", "Python", "car", "computer", "book", "hello"]
# result = get_long_words(words)
# print(result)

# def get_even_numbers(numbers):
#     result = []
#     for number in numbers:
#         if number % 2 == 0:
#             result.append(number)
#     return result
#
# numbers = [1, 4, 7, 10, 13, 20]
# result = get_even_numbers(numbers)
# print(result)


# def count_uppercase(text):
#     count = 0
#     for letter in text:
#         if letter.isupper():
#             count += 1
#     return count
#
# text = input("Enter text: ")
# print(count_uppercase(text))

# def count_digits(text):
#     digits = 0
#     for char in text:
#         if char.isdigit():
#             digits += 1
#     return digits


# frequency = {
#     "a": 3,
#     "b": 1,
#     "n": 2
# }
#
# frequency["c"] = 5
# frequency["a"] += 1
# if "n" in frequency:
#     print("Yes")
# print(frequency)

# text = "python java python sql python java"
# words = text.split()
# frequency = {}
#
# for word in words:
#     frequency[word] = frequency.get(word, 0) + 1
#
# if word not in frequency:
#     frequency[word] = 1
# else:
#     frequency[word] += 1
#
#
# print(text)
# print(words)
# print(frequency)

# frequency = {
#     "python": 3,
#     "java": 2,
#     "sql": 1
# }
# max_count = max(frequency.values())
# for word, count in frequency.items():
#     if count == max_count:
#         print(word)


# with open("test.txt", "w") as file:
#     file.write("New text\n")
#
# with open("test.txt", "a") as file:
#     file.write("Hello\nPython\n")
#
# with open("test.txt", "r") as file:
#     text = file.read()
# print(text)


# with open("test.txt", "r") as file:
#     line1 = file.readline()
#     line2 = file.readline()
# print(line1)
# print(line2)
#
# with open("test.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)
#     for line in lines:
#         print(line)


# with open("test.txt", "r") as file:
#     for line in file:
#         print(line, end="")

# with open("test.txt", "r", encoding="utf-8") as file:
#     text = file.read()
# print(text)

# try:
#     with open("abc.txt", "r", encoding="utf-8") as file:
#         text = file.read()
# except FileNotFoundError:
#     print("File not found")

# def load_text_from_file(filename):
#     try:
#         with open(filename, "r", encoding="utf-8") as file:
#             return file.read()
#     except FileNotFoundError:
#         return "file not found"
#
# text = load_text_from_file("test.txt")
# print(text)

number = 17
if number % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')