def vowels_count(text):
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return count
def consonants_count(text):
    count = 0
    for letter in text:
        if letter.isalpha() and letter not in vowels:
            count += 1
    return count
def letters_count(text):
    count = 0
    for letter in text.lower():
        if letter.isalpha():
            count += 1
    return count
def digits_count(text):
    count = 0
    for letter in text:
        if letter.isdigit():
            count += 1
    return count
def count_spaces(text):
    count = 0
    for letter in text:
        if letter.isspace():
            count += 1
    return count
def reverse_text(text):
    reverse = ""
    for letter in range(len(text) - 1, -1, -1):
        reverse += text[letter ]
    return reverse
def count_word(words, search_word):
    count = words.count(search_word)
    return count
def find_word_index(words, search_word):
    index = words.index(search_word)
    return index
def show_words(words):
    number = 0
    for word in words:
        number += 1
        print(f"{number}: {word}")
def letter_frequency(text):
    frequency = {}
    for letter in text:
        if letter.isalpha():
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1
    for letter, count in frequency.items():
        print(f"{letter}: {count}")
def find_word_index (words, search_word):
    try:
        index = words.index(search_word)
        return index
    except ValueError:
        return -1



# переменные
text = ""
words = []
menu = -1
vowels = "aeiou"

# пункты меню, которым нужен текст
text_required = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]

# основной цикл
while menu != 0:
    print()
    print("==================================")
    print("        TEXT ANALYZER v2.0")
    print("==================================")
    if not text:
        print("Current text: <No text entered>")
    else:
        print(f"Current text: {text}")
    print("--------------------------------------")
    print("1. Count vowels")
    print("2. Count consonants")
    print("3. Count letters")
    print("4. Count digits")
    print("5. Count spaces")
    print("6. Reverse text")
    print("7. Upper case")
    print("8. Lower case")
    print("9. Enter text")
    print("10. Show words")
    print("11. Count word")
    print("12. Sort words")
    print ("13. Reverse words")
    print ("14. Find word index")
    print("15. Letter frequency")
    print("0. Exit")
    print("--------------------------------------")
    try:
        menu = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Please enter a number.")
        continue
    if menu in text_required:
        if not text:
            print("No text found. Please enter text first!")
            continue
    if menu == 1:
            result = vowels_count(text)

            print("========== VOWELS COUNT ==========")
            print(f"Vowels: {result}")

            input("Press Enter to continue...")

    elif menu == 2:
            result = consonants_count(text)
            print("========== CONSONANTS ==========")
            print(f"Consonants: {result}")
            input("Press Enter to continue...")

    elif menu == 3:
            result = letters_count(text)
            print("========== COUNT LETTERS ==========")
            print(f"Letters: {result}")
            input("Press Enter to continue...")

    elif menu == 4:

            result = digits_count(text)

            print("========== DIGITS ==========")
            print(f"Digits: {result}")
            input("Press Enter to continue...")

    elif menu == 5:

            result = count_spaces(text)

            print("========== SPACES COUNT ==========")
            print(f"Spaces: {result}")
            input("Press Enter to continue...")

    elif menu == 6:

            result = reverse_text(text)
            print("========== REVERSE TEXT ==========")
            print(f"Reverse: {result}")
            input("Press Enter to continue...")

    elif menu == 7:

            print("========== UPPER CASE ==========")
            print(f"Upper case: {text.upper()}")
            input("Press Enter to continue...")

    elif menu == 8:

            print("========== LOWER CASE ==========")
            print(f"Lower case: {text.lower()}")
            input("Press Enter to continue...")

    elif menu == 9:
        print("========== ENTER NEW TEXT ==========")
        text = input("Enter new text: ")
        words = text.split()
        print("Text updated!")
        input("Press Enter to continue...")

    elif menu == 10:
            print("========== WORDS ==========")
            show_words(words)
            print("===========================")
            input("Press Enter to continue...")

    elif menu == 11:

            search_word = input("Enter word: ")

            print("========== COUNT ==========")

            result = count_word(words, search_word)

            print(f"Word: {search_word}")
            print(f"Count: {result}")

            print("===========================")

            input("Press Enter to continue...")

    elif menu == 12:
            words_copy = words.copy()
            words_copy.sort()
            print("========== SORT WORDS ==========")
            show_words(words_copy)
            input("Press Enter to continue...")

    elif menu == 13:
            words_copy = words.copy()
            words_copy.reverse()
            print("========== REVERSE WORDS ==========")
            show_words(words_copy)
            input("Press Enter to continue...")

    elif menu == 14:
            search_word = input("Enter word: ")
            print("========== FIND WORD INDEX ==========")
            result = find_word_index(words, search_word)
            if result == -1:
                print("No such word!")
            else:
                print(f"Word: {search_word}")
                print(f"Index: {result}")
            input("Press Enter to continue...")
        # TODO(после
        # темы
        # try/ except)
        #
        # Сделать безопасный поиск слова.
    elif menu == 15:
        print("========== LETTER FREQUENCY ==========")
        letter_frequency(text)
        input("Press Enter to continue...")
    elif menu == 0:
        print("Goodbye!")