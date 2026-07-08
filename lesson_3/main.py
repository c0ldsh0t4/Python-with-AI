# Home work 3.2
from pip._internal.resolution import legacy

numbers = [2 , 7 , 1 , 9 , 5]
print(numbers)

result = numbers.pop(-1)
print(result)

numbers.insert(0, result)
print(numbers)

# Home work 3.3

numbers = [3 , 6 , 8 , 15 , 22 , 11]
length = len(numbers) // 2
print([numbers[0 : length] , numbers[length:]])

numbers = [4 , 7 , 10]
length = len(numbers)  // 2 + 1
print([numbers[0 : length] , numbers[length:]])

numbers = [ 12 , 6 , 1 , 18 , 29]
length = (len(numbers) + 1  )// 2
print([numbers[0 : length] , numbers[length:]])

number = [1]
length = (len(number) +1) // 2
print([number[0 : length] , number[length:]])

number =[]
length = (len(number) +1) // 2
print([number[0 : length] , number[length:]])


# Home work 3.1
