
  
# Linked Lists

Linked lists are another type of data structure that every developer should be aware of. Linked Lists are lists made out of "nodes". Nodes contain the value to be stored, a next pointer, and a previous pointer. These pointers tell the list which value is next or before in the list. This allows the nodes to be stored anywhere in the system's memory because they simply give directions to the next or previous value.

Taking a look at the visualization below can help you begin to understand how Linked Lists work. Take the value "B" for example. The node "B" contains the value "B", a next pointer to node "C", and a previous pointer to node "A".

Now to talk about the operations shown below. We have a base list of A, B, C, and D. We then remove C which is at index 2 before also removing A at index 0. After that, we add A back at index 1 and then add C back at index 0.

As you can see Linked Lists allow you to add your values anywhere because you just have to change the next pointer of the previous node to the new node, and the previous pointer of the next node to the new node.

```
       ┌─────┐───►┌─────┐───►┌─────┐───►┌─────┐
Base   │  A  │    │  B  │    │  C  │    │  D  │
       └─────┘◄───└─────┘◄───└─────┘◄───└─────┘
       ┌─────┐───►┌─────┐───►┌─────┐
-C @ 2 │  A  │    │  B  │    │  D  │
       └─────┘◄───└─────┘◄───└─────┘
       ┌─────┐───►┌─────┐
-A @ 0 │  B  │    │  D  │
       └─────┘◄───└─────┘
       ┌─────┐───►┌─────┐───►┌─────┐
+A @ 1 │  B  │    │  A  │    │  D  │
       └─────┘◄───└─────┘◄───└─────┘
       ┌─────┐───►┌─────┐───►┌─────┐───►┌─────┐
+C @ 0 │  C  │    │  B  │    │  A  │    │  D  │
       └─────┘◄───└─────┘◄───└─────┘◄───└─────┘
```
# Why Use a Linked List

Now that you know what a Linked List is, it is important to understand why you would use a Linked List instead of other data structures.
**1. Mutability**
Linked lists are mutable, which means they support adding new data to be added to the list as well as removing data from the list. The adding and removing functionality is also considerably faster than other data structures as we will talk about later.

**2. Size** 
Another benefit to Linked Lists is that, unlike other data structures, you do not need to know the size of the list in advance. Linked Lists are able to grow dynamically because the data, which is stored within nodes, does not need to be saved in a specific location in memory. The nodes can be stored anywhere as long as they have the required pointers. This makes the size of Linked Lists nearly infinite depending on the application.

**3.  Performance**
Finally, Linked Lists are very efficient when it comes to adding and removing items to the list. While they are O(N) when searching, the actual act of adding or removing in the found location is O(1). In comparison, Dynamic Arrays are O(N) for searching and O(N) for adding and removing. This is because Dynamic Arrays need to shift every value that changes locations within the array. Linked Lists do not need to do this, they only need to change the pointers of the nodes which is an O(1) operation. 
# Components
Now before we get to programming the operations of a Linked List in Python we need to go over the components one more time.

**Nodes**
Nodes are the individual segments the Linked List is made of. The nodes contain the information the needs stored inside the linked list. These nodes also contain the pointers which we will talk about below.

**Pointers**
Pointers are what make Linked Lists work. These are simple references that show what the previous node is and what the next node is. This is what allows us to iterate through the list.

**The Head**
The Head of a Linked list is the first node in the list. It contains only a forward pointer as there is nothing before it.

**The Tail**
The Tail of a Linked List is the last node in the list. It contains only the previous pointer as there is nothing after it. In a Linked List with only 1 node, that node is simultaneously the Head and Tail.

# Creating a Linked List
To create a linked list in Python we will need 2 classes representing objects. The first object is the Linked List, the second Object is the node. The node object is created within the Linked List object since the Linked List is made out of Nodes.

**Creating the Node Object**
To create our Node object we first need to create the class.
```python
class Node:
```
Then we need to create the constructor which takes the user data for the node as a paramter to set to the member value named "data" and initializes our base pointers to None.
```python
class Node:
    def __init__(self, data)
	    self.data = data
	    self.next = None
	    self.prev = None
```
That's it! That is all you need for the node object, most of the functionality is within the next object, the Linked List.

**Creating the Linked List Object**
For the Linked List object, we start by encasing our Node object inside the new Linked List Object.
```python
class LinkedList:
	class Node():
		def __init__(self, data)
		self.data = data
		self.next = None
		self.prev = None
```
Then we make the constructor. This is what is run when a new instance of Linked List is created. The Linked List object has two member values, the Head and the Tail nodes. These are initially None since we do not have Nodes stored yet.
```python
class LinkedList:
	class Node():
	    ... # To save space the node class will be replaced with ellipses.
    def __init__(self)
        self.head = None
        self.tail = None
```
Next, we need to create the insert_head method for the Linked List object. This method inserts a node as the head of our Linked List.

This method requires us to first create a new node object with the given user value. 
```python
def insert_head(self, value)
	new_node = LinkedList.Node(value)
```
We then must check if the List is currently empty. If it is the Head must also be the Tail. If it isn't the new head replaces the previous head. To do this the new head has it's next value set to the old head, and the old head has it's previous value set to the new head.
```python
def insert_head(self, value)
	new_node = LinkedList.Node(value)
	if self.head is None: # If the list is empty
		self.head = new_node
		self.tail = new_node
	else:
		new_node.next = self.head
		self.head.prev = new_node
		self.head = new_node
```
Now that we have the insert_head method created, we must also create insert_tail. insert_tail is the same as insert_head but flipped.
```python
new_node = LinkedList.Node(value)

if self.tail is None:
	self.head = new_node
	self.tail = new_node
else:
	new_node.prev = self.tail
	self.tail.next = new_node
	self.tail = new_node
```
Now that we have methods to insert heads and tails, we must also make a method to remove heads and tails. Let's start with remove_head.

remove_head operates very simply. First, it checks to make sure the list isn't only 1 node. If it is then both the head and tail values of the list need to be cleared since the single node is both the head and tail.
```python
def remove_head(self):
	if self.head == self.tail:
		self.head = None
		self.tail = None
```
Once that is completed we can tell it what to do if the head isn't already none. The current head's next node has its previous value set to None since it will be the new head. Then the Linked List head is set to be the old head's next node.
```python
def remove_head(self):
	if self.head == self.tail:
		self.head = None
		self.tail = None
	elif self.head is not None:
		self.head.next.prev = None
		self.head = self.head.next
```
Again, remove_tail is similar to remove_head, but the opposite.
```python
def remove_tail(self):
	if self.tail == self.head:
		self.head = None
		self.tail = None
	elif self.tail is not None:
		self.tail = self.tail.prev
		self.tail.next = None
```
Now we must add an insert method. The insert method, which we will call "insert_after", will find a given value's node and insert the new node after that node. Because Linked Lists do not operate with indexes we must do this by searching the whole list until the given value is found.

First, we need to make a while loop that will loop for as long as the current node isn't None. The starting node is the head.
```python
def insert_after(self, value, new_value)
	curr = self.head
	while curr is not None:
```
Now, within the loop, we must check to see if the current node's value is the given value. If it is then we add the node in by swapping around the surrounding pointers. We can also check to see if the given node is the tail. If it is then we can simply use the previous insert_tail method. 

If it isn't the given search value, then we simply move up a node by setting the current node to the next node.
```python
def insert_after(self, value, new_value)
	curr = self.head
	while curr is not None:
		if curr.data == value:
			if curr == self.tail:
				self.insert_tail(new_value)
			else:
				new_node = LinkedList.Node(new_value)
				new_node.prev = curr
				new_node.next = curr.next
				curr.next.prev = new_node
				curr.next = new_node
			return
		curr = curr.next
```
Now that we have a way to add new nodes, we also need a way to remove nodes. This will be done with the remove method. This method takes a given value and removes the node with that value.

It is very similar to insert_after in the way it iterates over the list. The only differences are that if the given value is found, we check to see if it is the head or tail because, if it is either, we can user remove_head or remove_tail from earlier. If it isn't the head or tail, we just have to switch the previous node's next pointer to the given node's next node, and then change the given node's next node's previous pointer to the given node's previous node.
```python
def remove(self. value):
	curr = self.head
	while curr is not None:
		if curr.data == value:
			if curr == self.head:
				self.remove_head()
			elif curr == self.tail:
				self.remove_tail()
			else:
				curr.prev.next = curr.next
				curr.next.prev = curr.prev
		curr = curr.next
```
Another useful method for our linked list is the replace method which will allow us to replace the data in a node rather than having to delete it along with its pointers before creating it again.

replace will iterate with the same while loop as insert_after and remove. The difference is that when the value is found it is replaced.
```python
def replace(self, old_value, new_value):
	curr = self.head
	while curr is not None:
		if curr.data == old_value:
			curr.data = new_value
		curr = curr.next
```
And since we've been iterating through the list so much, we might as well create an iteration method for it. This will allow us to use the for __ in __ loop like python's built-in lists.

All this method does is iterate through the list like before, except it yields the node's data at every iteration and will never stop until it reaches the end of the list.
```python
def __iter__(self):
	curr = self.head
	while curr is not None:
		yield curr.data
		curr = curr.next
```
We can also include the reversed function to do the same thing but backward.
```python
def __reversed__(self):
	curr = self.tail
	while curr is not None:
		yield curr.data
		curr = curr.prev
```
The last method you should include in your linked list is the string method. This allows you to display a string representation of the linked list which is useful for debugging. This method also uses the iteration method we made above in the for loop.
```python
def __str__(self):
	output = linkedlist[]
	first = True
	for value in self:
		if first:
			first = False
		else:
			output += ", "
		output += str(value)
	output += "]"
	return output
```
That's everything! Once all of this code is put together you should have a fully operational Linked List class which will allow you to solve the problem to solve below. Keep in mind that this is a fairly advanced linked list. Some implementations will not require this amount of functionality, so you can pick and choose what you need. In fact some Linked Lists only contain next pointers, this is actually a doubly Linked List because it contains next and previous pointers.
# Example
**Aquarium Tracker Program**
The aquarium tracker is simple program utilizing linked lists to keep track of the amount of fish in an aquarium. I chose to use a linked list for this program since the Aquarium will not know how many fish it will have to keep track of at first. 

**The Program Must**
* Loop through a menu.
* Allow users to add a type of fish.
* Allow users to add to the quantity of fish.
* Allow users to remove from the qauntity of fish.
* Allow users to remove a type of fish
* Display all the fish and their quantitites.
* Allow users to quit the program

```python
import LinkedList as LL

def main():
    menu = True
    fish_list = LL.LinkedList()

    while menu == True:
        print("""
        1. Add type of fish
        2. Add fish
        3. Remove fish
        4. Remove type of fish
        5. Print all fish
        6. Quit
        """)

        choice = input("Enter your choice: ")
        if choice == "1":
            fish = input("Enter a fish: ")
            amount = input("Quantity: ")
            fish_list.insert_tail([fish, amount])

        elif choice == "2":
            fish = input("Fish to add to: ")
            amount = input("Quantity to add: ")
            for fish_data in fish_list:
                if fish_data[0] == fish:
                    fish_data[1] = int(fish_data[1]) + int(amount)
                    break

        elif choice == "3":
            fish = input("Fish to remove from: ")
            amount = input("Quantity to remove: ")
            for fish_data in fish_list:
                if fish_data[0] == fish:
                    fish_data[1] = int(fish_data[1]) - int(amount)
                    if fish_data[1] <= 0:
                        fish_list.remove(fish_data)
                        print("Removed " + fish + " from the list!")
                    break

        elif choice == "4":
            fish = input("Fish to remove: ")
            for fish_data in fish_list:
                if fish_data[0] == fish:
                    fish_list.remove(fish_data)
                    break

        elif choice == "5":
            for fish_data in fish_list:
                print(fish_data[0] + ": " + fish_data[1])

        elif choice == "6":
            menu = False
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
```
# Problem to Solve
**Music Ranker**
On your own try to create a music ranking program. This program will allow a user to create a list of songs. The user can choose where to add a song in the list, as well as songs to remove. The music ranker program should make use of the Linked List class, which I put together for your use [here](https://github.com/JaromPD/Data-Structures-Tutorial/blob/main/LinkedList.py).

**The Program Must**
* Display a menu to Add, Remove, and View Songs
* Display a secondary menu to ask where to add the song.
* The user must be able to add a song:
	* at the beginning of the list
	* at the end of the list
	* after a specified song
* The user must be able to view an ordered list of songs in both menus.

Once you have created your own program, feel free to check your solution with [mine](https://github.com/JaromPD/Data-Structures-Tutorial/blob/main/music_ranker.py).