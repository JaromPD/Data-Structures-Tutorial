def list_reverser(original_stack):

    reversed_stack = []

    while len(original_stack) > 0:
        curr_item = original_stack.pop()
        reversed_stack.append(curr_item)

    return reversed_stack

def main():
    menu = True
    word_stack = []
    while menu == True:

        if word_stack != []:
            print(f"Current Stack: {word_stack}")

        print("""
        1. Add a word to the stack
        2. Undo the last word
        3. Reverse the stack
        4. Quit
        """)

        menu_choice = input("Enter your choice: ")
        if menu_choice == "1":
            word = input("Enter a word: ")
            word_stack.append(word)

        elif menu_choice == "2":
            if len(word_stack) > 0:
                word_stack.pop()
            else:
                print("Stack is empty")

        elif menu_choice == "3":
            word_stack = list_reverser(word_stack)

        elif menu_choice == "4":
            menu = False

        else:
            print("Invalid choice")


if __name__ == """__main__""":
    main()