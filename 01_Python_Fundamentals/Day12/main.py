from stringbasics import show_basics
from slicing import slicing
from methods import show_methods
from format import show_formatting
from regexintro import find_words_starting_with_a, has_digits
from emailvalidator import validate_email
from text_analyzer import analyze_text

def main():
    name = input("Enter your name: ")
    text = input("Enter any text: ")
    email = input("Enter email: ")

    while True:
        print("\n--- Text Processing Toolkit ---")
        print("1. String Basics")
        print("2. Slicing")
        print("3. String Methods")
        print("4. Formatting")
        print("5. Regex Demo")
        print("6. Email Validation")
        print("7. Text Analysis")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_basics(text)
        elif choice == "2":
            slicing(text)
        elif choice == "3":
            show_methods(text)
        elif choice == "4":
            pass
            #show_formatting(name, text)
        elif choice == "5":
            print("Words starting with a:", find_words_starting_with_a(text))
            print("Contains digits:", has_digits(text))
        elif choice == "6":
            print("Valid email" if validate_email(email) else "Invalid email")
        elif choice == "7":
            result = analyze_text(text)
            for key, value in result.items():
                print(f"{key}: {value}")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()