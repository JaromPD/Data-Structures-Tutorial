

# Trees
Linked lists are the last data structure to be covered in this tutorial, and like everything else we've covered so far, they are vital for future developers to learn. Trees are very similar to Linked Lists because they are also made out of nodes and pointers, but are structured in a very different way. Trees contain no previous pointers and 2 next pointers. We call the first node the root, the previous node the parent node, and the 2 next pointers left and right child. In Trees, the nodes do not have pointers that lead to the previous parent node, but there are 2 child pointers that point to the possible left and right child values. In Binary Search Trees, which will be the main type of tree we talk about, the left child pointer leads to the nodes less than the current node and the right child pointer leads to the nodes more than the current node. 

Consider the diagram of a tree below. In the example numbers were added in the order: 5, 6, 3, 4, 2, 9, 7, 1, 8.

To explain how these values were added I will explain the first 5 operations of the process below.
```
				                  ┌───┐
				              ┌───┤ 5 ├───┐
				              │   └───┘   │
				              ▼           ▼
				            ┌───┐       ┌───┐
				        ┌───┤ 3 ├───┐   │ 6 ├───┐
				        │   └───┘   │   └───┘   │
				        ▼           ▼           ▼
				      ┌───┐       ┌───┐       ┌───┐
				  ┌───┤ 2 │       │ 4 │   ┌───┤ 9 │
				  │   └───┘       └───┘   │   └───┘
				  ▼                       ▼
				┌───┐                   ┌───┐
				│ 1 │                   │ 7 ├───┐
				└───┘                   └───┘   │
				                                ▼
				                              ┌───┐
				                              │ 8 │
				                              └───┘
```
1. Add 5.
	* 5 is added as the top value since it is the first added.
2. Add 6.
	* 6 is more than 5 so we go right.
	* The space is empty so we add 6 there.
3. Add 3.
	* 3 is less than 5 so we go left.
	* The space is empty so we add 3 there.
4. Add 4.
	* 4 is less than 5 so we go left.
	* 4 is more than 3 so we go right.
	* The space is empty so we add 4 there.
5. Add 2.
	* 2 is less than 5 so we go left.
	* 2 is less than 3 so we go left.
	* The space is empty so we add 2 there.
# Why Use Trees
So why do we use Trees in our code? What is the difference between trees and something like a Linked List? The main reason is that traversing these Trees is much faster than traversing a linked list. If you look at the diagram above we can see that every value from 1-10 can be accessed in at most 4 steps. Traversing to the value 8 in the Tree is the farthest to reach at 4 steps, whereas in a Linked List it would take 9 steps assuming it was also the last value added. That's a lot faster, especially when these data structures get to larger ranges.

Another advantage to Trees like the Binary Search Tree is that they are automatically sorted if they are traversed correctly. This is because they are placed in such a way that all the smaller values will always be on the left side, and all the larger values will always be on the right.

# Recursion
Recursion is a vital part of the Tree. This is because traversing the tree requires many decisions between left and right to get to the correct value. When we put these decisions in a recursive loop we are able to easily get to the required node whether we are returning the data within, editing it, or even inserting a new child node to it. As we create the Tree class below each use of recursion will be explained and you will see that nearly all the methods we create will use it in some way.

# Creating a Tree
Like Linked Lists, creating a Tree requires two classes or "objects". These are the BST (Binary Search Tree) and Node objects. We will start by creating both these classes with Node being a subclass of BST.
```python
class BST:
    class Node:
```
Now we need to initialize the base values for the Node object. Nodes need at least three member variables, the data, the left child, and the right child.

```python
class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
```
Now the Node object is completed! Easy right? Now it's time to work the Tree's initial member variable which is just the root Node which is initially empty.

```python
class BST:
    class Node:
        ... # Node methods hidden
    def __init__(self):
        self.root = None
```

Now that we have the initial variables we can start working on the methods that we use to manipulate and utilize the tree starting with insert.

```insert()``` is a public method that will take data and call the internal ```_insert()``` method that we will create next as long as the new Node wont be the root of the tree.
```python
def insert(self,data):
    if self.root is None:
        self.root = BST.Node(data)
    else:
        self._insert(data, self.root) # _insert() will be created next.
```
Now that we have the public insert method we can create the internal ``` _insert()``` which makes more decisions on where the new node will go. This is also the first method that utilizes recursion to traverse the list.

```_insert``` works by taking the data to be in the Node and the current Node we are comparing to our new Node. Initially, the Node to be compared will start as the root of the Tree. We compare the data of the current node to see if it is more or less than our new data. If it is less we check the left side, if it is more we check the right side. If the selected side is empty we have found an empty space to place our new Node! If it isn't we will call the _insert method with the node on the selected side as our new comparison node and the process repeats until an empty space is found.

```python
def _insert(self, data, node):
    if node.data != data:
        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self.insert(data.node.left)
        else:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)
    else:
        pass # May be a good spot for an error message. 
```
The next method we need is ```__contains__()``` which will be a method to see if our Tree contains a value. We can also use this method outside of the class with the "in" keyword.
```python
Example: 
If 5 in my_tree
```
To create this we simply need to return the output of the ```_contains()``` method we will be creating next. 

```python
def __contains(self, data):
    return self._contains(data, self.root) 
```
Notice that we pass the root to ```_contains()``` since that is our starting node. 

To create the ```_contains()``` method we need to start by taking parameters of the data to search for and the node to check which will start as the root.

This method first checks to see if the Node's data matches the data it's looking for. If it does we've found it and can return True since the tree does contain it. If it doesn't match however we have to check if the searched for data is less or more than the current node. If the found side is None then we know the data is not in the Tree and return False because we would have found it before the end of the branch if it was there. If there is another node then we call the method again on that node so that we can do the whole comparison again. This goes on until the value is found or we hit the end of the list

```python
def _contains(self, data, node):
    if data == node.data:
        return True
    else:
        if data < node.data:
            if node.left is None:
                return False
            else:
                return self._contains(data, node.left)
        else:
            if node.right is None:
                return False
            else:
                return self._contains(data.right)
```
Another useful method for the tree is the ```__iter__()``` iteration method. This method allows us to use the Tree inside of loops later. This is a simple function because like ```insert()``` it uses a more complicated method we will create next. In this case, it will be ```_traverse_forward()```. All ```__iter__``` does is yield results from```_traverse_forward()``` starting at the root.

```python
def __iter__(self):
    yield from self._traverse_forward(self.root) # Will be created next.
```

Next we will create ```_traverse_forward()```. This method always starts by making sure the current node isn't None, because if it is we have hit the end of the branch. If it isn't None we first yield the return of the left side by calling itself again on the left node. We then yield the current node since it is the middle before yielding the return of the function which is being called on the right side now. Together this will iterate through the tree from least to greatest.

```python
def _traverse_forward(self, node):
    if node is not None:
        yield from self._traverse_forward(node.left)
        yield node.data
        yield from self._traverse_forward(node.right)
```

Now we will create some methods that are the exact opposite of the ```__iter__()``` and ```_traverse_forward()```methods we just created. These are  ```__reversed__``` and ```_traverse_backward()```.

```__reversed__()``` allows us to use the tree in loops that are iterating backward. The only difference is that ```_traverse_backward()``` calls the right side first rather than the left.

```python
def __reversed__(self):
    yield from self._traverse_backward(self.root)

def _traverse_backward(self, node):
    if node is not None:
        yield from self._traverse_backward(node.right)
        yield node.data
        yield from self._traverse_backward(node.left)
```
For the last BST methods we will include ```get_height()``` and ```_get_height()```. These functions find the largest branch of the tree and return an integer value representing it. The public function will check to see if it is an empty tree and return 0 if that is the case, and if it isn't it will call the private function starting at the root.

```python
def get_height(self):
    if self.root is None:
        return 0
    else:
        return self._get_height(self.root)
```
The private ```_get_height()``` function starts by returning a 0 if the current Node is None because it has hit the end of a branch. After it checks that the left and right sides of the node are iterated down recursively. After that, we check which side is long and add one to that side before returning it. All together this recursively iterates down the Trees branches and returns the length of the longest branch.

```python
def _get_height(self, node):
    if node == None:
        return 0
    left_side = self._get_height(node.left)
    right_side = self._get_height(node.right)
    if left_side > right_side:
        return left_side + 1
    else:
        return right_side + 1 
```

# Keeping a Balanced Tree
An important part of keeping the Tree as efficient as possible is by keeping it balanced. Consider a tree with a root of 100 where you added all the numbers below 100 in reverse order. So from 99 to 98 to 97 to 96 and so on. This would create a tree that is basically a Linked List since every value would go on the parent Node's left side. How can we combat this? Well if we already have a sorted list of values to add we can create a function that adds all these values in a way that the Tree is well balanced. This function which is external to the BST class is simply called ```create_bst_from_sorted_list()``` and it does exactly what it says. It creates a balanced BST from a sorted list. 

```create_bst_from_sorted_list()``` is a relatively simple functions that relies heavily on the ```_insert_middle()``` function we will create next. 

```python
def create_bst_from_sorted_list(sorted_list):
    bst = BST()
    _insert_middle(sorted_list, 0, len(sorted_list) - 1, bst)
    return bst
```

```_insert_middle()``` takes the sorted_list, the first index of it, the last index of it, and the bst to insert to. This is also a recursive function as you will see soon.

```insert_middle()``` starts by checking if the first index is larger than the last index. This is because we know we have added everything when first is more than last. If this does happen the function returns and ends the loop. If this doesn't happen we find the middle value of the sorted list and add it to our tree. We then call the same function on each side of our middle value. This makes two sublists that we can find the next middle values of, and then we do it again, and again, and again until all the values are added. This helps us create a tree that is balanced and therefore more efficient than one that is unbalanced.
```python
def _insert_middle(sorted_list, first, last, bst)
    if first > last:
        return
    else:
        middle_i = ((last-first)//2) + first
        bst.insert(sorted_list[middle_i])
        _insert_middle(sorted_list, first, middle_i - 1, bst)
        _insert_middle(sorted_list, first, middle_i + 1, bst)
```
# Example
 

# Problem to Solve
**Lottery Number Program**
On your own create a Lottery Number Program. Imagine there is a lottery with 100 winners out of 100,000 entries. Every entry is given the number of entries as their entry number (ie. entrant 530 gets the number 530.). The program must select 100 winners randomly and store these winning numbers in a tree. The program then must generate a sorted list so that the earlier entrants get their prize first.

**The Program Must**
* Have a looping menu with options to:
	* Roll for Winners.
	* Sort Winners.
	* Display winning numbers.
* The menu must also display if winners have been selected already, but still let the user re-roll.
* Randomly select 100 numbers from a range of 1 - 100,000
* Use a Binary Search Tree for storing winners
* Use the BST to sort the winners.