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
