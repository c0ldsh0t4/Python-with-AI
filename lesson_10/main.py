#Home work 10.1
# def pow(x):
#    return x ** 2
#
# def some_gen(begin, end, func):
#    yield begin
#
#    for i in range(end -1):
#       begin = func(begin)
#       yield begin
#
# from inspect import isgenerator
#
# gen = some_gen(2, 4, pow)
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')


# Home work 10.2
# def first_word(text):
#    result = text.split()
#    for word in result:
#       word = word.strip(".,")
#       parts = word.split("'")
#       first = word.split(".")
#       word = first[0]
#       if word.isalpha():
#          return word
#       valid = True
#       for part in parts:
#          if not part.isalpha():
#             valid = False
#       if valid:
#          return word
#
#
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')

#Home Work 10.3
# def is_even(digit):
#   # if digit % 2 == 0:
#   #    return True
#   # else:
#   #    return False
#    return digit % 2 == 0
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')
