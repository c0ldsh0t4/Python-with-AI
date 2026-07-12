# Home work 4.1

numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
count = numbers.count(0)
for i in range(count):
    numbers.remove(0)
    numbers.append(0)
    print(numbers)

# Home work 4.2

numbers = [1, 3, 5]
if len(numbers) == 0:
    print(0)

else:
    result = 0

    for i in range(0, len(numbers), 2):
        result = result + numbers[i]

    result = result * numbers[-1]

    print(result)

# Home work 4.3

import random
SIZE = random.randint(3, 10)
numbers = []
for i in range(SIZE):
    numbers.append(random.randint(3, 10))

result = [
    numbers[0],
    numbers[2],
    numbers[-2]
]
print(numbers)
print(result)

