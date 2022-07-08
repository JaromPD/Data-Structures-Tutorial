# Stacks
Stacks are a very important Data Structure for every developer to have in their toolkit. Stacks are a type of data structure that do exactly what they say they will. They stack the data added to them, but what does that mean? Well it means that if you are using a stack to store items the new item will always be added to the end of the stack and when it's time to remove items they will be taken from the end aswell. This is significatn because it results in both addition and removal to happen in O(1) time complexity since it is always adding or removing from the end of the list.

Consider the visualization below. We start with a stack of the characters A, B, and C. We then take from the stack which gives us C before removing it from the stack since it's been taken. Then we take another, this time we will get B and again it is removed from the stack. Now we want to add B back and it is automatically placed at the top of the stack. Then we add C back aswell, again it is placed on top and will be the next in line for removal if we choose to do so.
```     
 ┌───┐                   ┌───┐
 │ C │                   │ C │
 ├───┤ ┌───┐       ┌───┐ ├───┤
 │ B │ │ B │       │ B │ │ B │
 ├───┤ ├───┤ ┌───┐ ├───┤ ├───┤
 │ A │ │ A │ │ A │ │ A │ │ A │
 └───┘ └───┘ └───┘ └───┘ └───┘
   +     -     -     +     +  
```
# Common Uses
Earlier I said that Stacks are an extremely important tool for every developer to have, and that is because they are used all around us! Here we will talk about a few of the most common uses, that you probably already know about.

**The Back Button**

The first and most common examples of stacks are back buttons! Whether its in you web browser or just on your phone back buttons need to use stacks, and it makes sense when you think about. Every time you open a new window or application it is added to a stack so when you want to go back, it simply returns to the last windows or application in the stack.

**The Call Stack**

The call stack is another great example, especially since you've probably used it before in your own programming! Essentially the call stack keeps track of whatever function your program is running. This is important for nested functions, because when one ends we must go back into the one the called it and continue. This is also very similar to the next and final example...

**Recursion**

When we make recursive fictions we are in fact making a stack! This is very similar to The Call Stack because it is a stack of functions, they're just all the same function. This stack is what allows recursive functions to work. Without them being in a stack the functions would never be able to go back to their last iteration and complete the task at hand!

# Python Operations
Alright now that we've covered what a stack is an how it work, we need to talk about how to implement one into your Python Code. Usually this will start with a empty list which will become your stack. 

```python
stack = []
```

Then to add item to the stack we simply need to append the to the list with append().

```python
stack.append('A')
```

Lastly to remove the last item from the stack, we use pop().

```python
stack.pop()
```

To get the value of the item and remove it, you simply need to set the pop to a variable.
```python
removed_last_item = stack.pop()
```

With this new information we can create code that can implement the stack from the diagram in the first section. This is what it would look like:
```python
stack = ["A", "B", "C"] # Initial Stack
stack.pop() # C is removed
stack.pop() # B is removed
stack.append("B") # B is added
stack.append("C") # C is added
```
Also be sure to remember that, as is usual with programming, there a many more ways to implement a stack, including using a linked list instead of a regualr list! However for this tutorial will will just be learning the basics and this is the most basic way to implement a stack.
#  Code Example
**Shopping List Program**

The shopping list program is a simple program that allows users to add items to a shopping list, and undo the last addition they made. This is in order to keep track of what they need to buy, and it allows them to remove the last item in the case of typos.

**The Program Must**
* Loop through a menu.
* Allow users to add items to a stack.
* Allow users to undo the last addition.
* Have an option to quit.

Be sure to pay attention to the use of the stack operations we talked about above!
```python

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
```
# Problem To Solve
**Navigate Home Program**

The navigate home program is a simple program that finds a set of directions to navigate someone home based on the directions they took to get there. The program will add a location to a stack everytime it is reached and then when it is time to return home, the program will reverse the order of those locations in order to lead the user home. In a real program there would also be a system to track the user's location, but for this program we will simply have the enter it.

**The Program Must**
* Display a menu with options to add a location, undo the last location, take the user home, and quit
* Loop the menu until  the user quits or selects the take home option.
* Take user input for locations
* Add locations to a stack using append.
* Undo the last addition.
* Reverse the stack using pop.
* Display the reversed stack to take them home.

This program can be designed in many different ways. [This solution](https://github.com/JaromPD/Data-Structures-Tutorial/blob/main/navigate_home.py) is just one of many. As long as it uses the pop and append methods in a similar way it is most likely done correctly!
