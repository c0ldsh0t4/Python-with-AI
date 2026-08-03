text = ""
words = []
menu = -1
vowels = "aeiou"
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
    print("0. Exit")
    print("--------------------------------------")
    menu = int(input("Enter your choice: "))
    if menu == 1:
        if not text:
            print("No text found. Please enter text first!")
        else:
            vowels_count = 0
            for letter in text.lower():
                if letter in vowels:
                    vowels_count += 1
            print("========== VOWELS COUNT ==========")
            print(f"Vowels: {vowels_count}")

            input("Press Enter to continue...")
    elif menu == 2:
        if not text:
            print("No text found. Please enter text first!")
        else:
            consonants_count = 0
            for letter in text.lower():
                if letter.isalpha() and letter not in vowels:
                    consonants_count += 1
            print("========== CONSONANTS ==========")
            print(f"Consonants: {consonants_count}")
            input("Press Enter to continue...")
    elif menu == 3:
        if not text:
            print("No text found. Please enter text first!")
        else:
            letters_count = 0
            for letter in text.lower():
                if letter.isalpha():
                    letters_count += 1
            print("========== COUNT LETTERS ==========")
            print(f"Letters: {letters_count}")
            input("Press Enter to continue...")
    elif menu == 4:
        if not text:
            print("No text found. Please enter text first!")
        else:
            digits_count = 0
            for letter in text.lower():
                if letter.isdigit():
                    digits_count += 1
            print("========== DIGITS ==========")
            print(f"Digits: {digits_count}")
            input("Press Enter to continue...")
    elif menu == 5:
        if not text:
            print("No text found. Please enter text first!")
        else:
            spaces_count = 0
            for letter in text.lower():
                if letter.isspace():
                    spaces_count += 1
            print("========== SPACES COUNT ==========")
            print(f"Spaces: {spaces_count}")
            input("Press Enter to continue...")
    elif menu == 6:
        if not text:
            print("No text found. Please enter text first!")
        else:
            reverse_text = ""
            for letter in range(len(text) -1, -1, -1):
                reverse_text += text[letter]
            print("========== REVERSE TEXT ==========")
            print(f"Reverse: {reverse_text}")
            input("Press Enter to continue...")
    elif menu == 7:
        if not text:
            print("No text found. Please enter text first!")
        else:
            print("========== UPPER CASE ==========")
            print(f"Upper case: {text.upper()}")
            input("Press Enter to continue...")
    elif menu == 8:
        if not text:
            print("No text found. Please enter text first!")
        else:
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
        if not text:
            print("No text found. Please enter text first!")
        else:
            print("========== WORDS ==========")
            number = 0
            for word in words:
                number += 1
                print(f"{number}: {word}")
            print("===========================")
            input("Press Enter to continue...")
    elif menu == 11:
        if not text:
            print("No text found. Please enter text first!")
        else:
            search_word = input("Enter word: ")

            print("========== COUNT ==========")

            count= words.count(search_word)

            print(f"Word: {search_word}")
            print(f"Count: {count}")

            print("===========================")

            input("Press Enter to continue...")
    elif menu == 12:
        if not text:
            print("No text found. Please enter text first!")
        else:
            print("========== SORT WORDS ==========")
            number = 0
            words.sort()
            for word in words:
                number += 1
                print(f"{number}: {word}")
            input("Press Enter to continue...")
    elif menu == 13:
        if not text:
            print("No text found. Please enter text first!")
        else:
            print("========== REVERSE WORDS ==========")
            number = 0
            words.reverse()
            for word in words:
                number += 1
                print(f"{number}: {word}")
            input("Press Enter to continue...")

    elif menu == 14:
        if not text:
            print("No text found. Please enter text first!")
        else:
            search_word = input("Enter word: ")
            print("========== FIND WORD INDEX ==========")
            index = words.index(search_word)
            print(f"Word: {search_word}")
            print(f"Index: {index}")
            input("Press Enter to continue...")
        # TODO(после
        # темы
        # try/ except)
        #
        # Сделать безопасный поиск слова.
    elif menu == 0:
        print("Goodbye!")