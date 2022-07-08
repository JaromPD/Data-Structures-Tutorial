from xml.etree.ElementTree import TreeBuilder


class locations:
    locations_stack = []
    locations_home_stack = []

    def add_location(self, location):
        self.locations_stack.append(location)

    def undo_location(self):
        self.locations_stack.pop()

    def reverse_locations(self):
        if len(self.locations_stack) > 0:

            while len(self.locations_stack) > 0:
                last_location = self.locations_stack.pop()
                self.locations_home_stack.append(last_location)

            return self.locations_home_stack
                
        else:
            print("No locations to reverse")

def main():
    print("Welcome to the home navigation program")
    menu = True
    locations_object = locations()
    while menu == True:
        if len(locations_object.locations_stack) > 0:
            print("Current locations: " + str(locations_object.locations_stack))

        print("""
        1. Add a location
        2. Undo a location
        3. Reverse locations
        4. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            location = input("Enter a location: ")
            locations_object.add_location(location)
        elif choice == "2":
            locations_object.undo_location()
        elif choice == "3":
            locations_object.reverse_locations()
            print(locations_object.locations_home_stack)
            menu = False
        elif choice == "4":
            menu = False
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()