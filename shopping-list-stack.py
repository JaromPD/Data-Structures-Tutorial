
def main():
    menu = True
    shopping_list = []

    print("Welcome to the shopping list program!")

    while menu == True:

        print("\nCurrent Items:")
        for item in shopping_list:
            print(item)

        print("\n")

        print("What would you like to do?\n    (A)dd\n    (U)ndo\n    (Q)uit")
        user_choice = input("> ")
        if user_choice.lower() == "a":
            new_item = input("What item would you like to add?: ")
            shopping_list.append(new_item)
            print("Added " + new_item + " to the list!")
        elif user_choice.lower() == "u":
            if len(shopping_list) > 0:
                removed_item = shopping_list.pop()
                print("Removed " + removed_item + " from the list!")
            else:
                print("There are no items to undo.")


        elif user_choice.lower() == "q":
            menu = False
        else:
            print(f"({user_choice}) is not a valid option.")

if __name__ == "__main__":
    main()