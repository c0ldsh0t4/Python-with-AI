# Home Work 6.1

import string
text = input()
start = text[0]
end = text[2]
start_index = string.ascii_letters.find(start)
end_index = string.ascii_letters.find(end)
print(string.ascii_letters[start_index:end_index + 1])

# Home Work 6.2

number = int(input())
seconds_in_day = 24 * 60 * 60
days, remainder = divmod(number, seconds_in_day)
seconds_in_hour = 60 * 60
hours, remainder = divmod(remainder, seconds_in_hour)
seconds_in_minute = 60
minutes, seconds = divmod(remainder, seconds_in_minute)
if days == 1:
    word ="день"
elif days == 2 or days == 3 or days == 4:
    word = "дня"
else :
    word = "дней"
print(days, word, str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))

# Home Work 6.3
number = int(input("enter the number: "))
while number > 9:
    result = 1
    while number > 0:
        digit = number % 10
        result *= digit
        number //= 10

    number = result

print(number)
