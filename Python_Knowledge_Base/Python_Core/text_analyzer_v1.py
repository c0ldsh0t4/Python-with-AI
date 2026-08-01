text = ""
menu = -1
vowels = "aeiou"
while menu != 0:
    print()
    print("==================================")
    print("        TEXT ANALYZER v1.0")
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
    elif menu == 7:
        if not text:
            print("No text found. Please enter text first!")
        else:
            print("------------------------------")
            print(f"Upper case: {text.upper()}")
            print("------------------------------")
    elif menu == 8:
        if not text:
            print("No text found. Please enter text first!")
        else:
            print("------------------------------")
            print(f"Lower case: {text.lower()}")
            print("------------------------------")
    elif menu == 9:
        print("------------------------------")
        text = input("Enter new text: ")
        print("Text updated!")
        print("------------------------------")
    elif menu == 0:
        print("Goodbye!")