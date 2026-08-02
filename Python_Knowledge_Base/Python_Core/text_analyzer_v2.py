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
    print("11. Count words")
    print("12. Sort words")
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
            print("------------------------------")
            print(f"Vowels: {vowels_count}")
            print("------------------------------")
            input("Press Enter to continue...")
    elif menu == 2:
        if not text:
            print("No text found. Please enter text first!")
        else:
            print("Count consonants")
            consonants_count = 0
            for letter in text.lower():
                if letter.isalpha() and letter not in vowels:
                    consonants_count += 1
            print("------------------------------")
            print(f"Сonsonants: {consonants_count}")
            print("------------------------------")
            input("Press Enter to continue...")
    elif menu == 3:
        if not text:
            print("No text found. Please enter text first!")
        else:
            print("Count letters")
            letters_count = 0
            for letter in text.lower():
                if letter.isalpha():
                    letters_count += 1
            print("------------------------------")
            print(f"Letters: {letters_count}")
            print("------------------------------")
            input("Press Enter to continue...")
    elif menu == 4:
        if not text:
            print("No text found. Please enter text first!")
        else:
            print("Count digits")
            digits_count = 0
            for letter in text.lower():
                if letter.isdigit():
                    digits_count += 1
            print("------------------------------")
            print(f"Digits: {digits_count}")
            print("------------------------------")
            input("Press Enter to continue...")
    elif menu == 5:
        if not text:
            print("No text found. Please enter text first!")
        else:
            print("Count spaces")
            spaces_count = 0
            for letter in text.lower():
                if letter.isspace():
                    spaces_count += 1
            print("------------------------------")
            print(f"Spaces: {spaces_count}")
            print("------------------------------")
            input("Press Enter to continue...")
    elif menu == 6:
        if not text:
            print("No text found. Please enter text first!")
        else:
            print("Reverse text")
            reverse = ""
            for letter in range(len(text) -1, -1, -1):
                reverse += text[letter]
            print("------------------------------")
            print(f"Reversed text: {reverse}")
            print("------------------------------")
            input("Press Enter to continue...")
    elif menu == 7:
        if not text:
            print("No text found. Please enter text first!")
        else:
            print("------------------------------")
            print(f"Upper case: {text.upper()}")
            print("------------------------------")
            input("Press Enter to continue...")
    elif menu == 8:
        if not text:
            print("No text found. Please enter text first!")
        else:
            print("------------------------------")
            print(f"Lower case: {text.lower()}")
            print("------------------------------")
            input("Press Enter to continue...")
    elif menu == 9:
        print("------------------------------")
        text = input("Enter new text: ")
        words = text.split()
        print("Text updated!")
        print("------------------------------")
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

    elif menu == 0:
        print("Goodbye!")