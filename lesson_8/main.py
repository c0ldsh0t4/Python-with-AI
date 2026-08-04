# Home Work 8.1

def add_one(some_list):
    result = ""
    for digit in some_list:
        result = result + str(digit)

    result = str(int(result) + 1)

    result_list = []
    for digit in result:
        result_list.append(int(digit))

    return result_list
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

# Home Work 8.2

def is_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    text = text.replace(",", "")
    text = text.replace(":", "")
    text = text.replace(".", "")
    if text == text[::-1]:
        return True
    else:
        return False
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")


# Home Work 8.3

def find_unique_value(some_list):
   some_list.count(1)
   for number in some_list:
       if some_list.count(number) == 1:
           return number

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
