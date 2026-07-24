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

