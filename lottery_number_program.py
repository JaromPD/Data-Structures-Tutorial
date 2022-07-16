import random
import BST as bst

def get_winners(num_of_winners, num_of_entrants):
    winners = bst.BST()
    curr_winners_amount = 0
    while curr_winners_amount != num_of_winners:
        winner = random.randint(1, num_of_entrants)
        if winner not in winners:
            curr_winners_amount += 1
            winners.insert(winner)

    return winners
        
def main():
    menu = True
    print("Welcome to the lottery number program!\n")
    amount_of_winners = int(input("How many winners do you want to pick?: "))
    amount_of_entrants = int(input("How many entrants are there?: "))
    print("\n")

    while menu == True:
        if amount_of_winners > amount_of_entrants:
            print("There are not enough entrants to pick that many winners!")
            menu = False

        winners = get_winners(amount_of_winners, amount_of_entrants)

        print("Winners have been selected!\n")

        print("What would you like to do?\n    1. Re-roll for winners\n    2. Print Winners\n    3. Quit")
        choice = input("\n> ")

        if choice == "1":
            winners = get_winners(amount_of_winners, amount_of_entrants)
            print("\n")
        
        elif choice == "2":
            winner_count = 0
            print("\n")
            for winner in winners:
                winner_count += 1
                print(f"Winner #{winner_count}: {winner}")
            print("\n")

        elif choice == "3":
            menu = False
            print("\n")

if __name__ == "__main__":
    main()