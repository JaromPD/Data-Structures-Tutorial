from BST import create_bst_from_sorted_list 
import BST as bst

def main():

    menu = True
    runners = []
    podium = {}
    print("Marathon Tracker:")

    while menu == True:
        print(f"Runners: {len(runners)}")
        print("What would you like to do?\n    1. Add a runner\n    2. Add an amount of runners.\n    3. Display runners\n    4. Set podium.\n    5. Display podium.\n    6. Exit")
        choice = input("> ") 

        if choice == "1":
            runners.append(len(runners) + 1)

        elif choice == "2":
            amount_to_add = int(input("How many runners would you like to add: "))
            new_runner_number = len(runners)

            for i in range(amount_to_add):
                new_runner_number += 1
                runners.append(new_runner_number)

        elif choice == "3":
            print(f"There are {len(runners)} runners.\n")
            for runner in runners:
                print(runner)

        elif choice == "4":

            runners_bst = create_bst_from_sorted_list(runners)

            print("Who is the first place runner?: ")
            first_place = input("> ")
            print("Who is the second place runner?: ")
            second_place = input("> ")
            print("Who is the third place runner?: ")
            third_place = input("> ")

            if first_place in runners and second_place in runners and third_place in runners_bst:
                podium = {1: first_place, 2: second_place, 3: third_place}
                print(f"Podium set.")
            else:       
                print("One or more of the runners you entered is not in the list.")

        elif choice == "5":
            print(f"The first place runner is {podium[1]}, the second place runner is {podium[2]}, and the third place runner is {podium[3]}.")

        elif choice == "6":
            menu = False
            print("Goodbye!")

if __name__ == "__main__":
    main()