
# Trees
Trees are the last data structure to be covered in this tutorial, and like everything else we've covered so far, they are vital for future developers to learn. Trees are very similar to Linked Lists because they are also made out of nodes and pointers, but are structured in a very different way. Trees contain nodes with 1 previous pointer and 2 next pointers. The previous pointer points to the previous value, and the 2 next pointers point to 2 possible next values. The leftmost pointer leads to the nodes less than the current node and the rightmost node leads to the nodes more than the current node. 

Consider the diagram of a tree below. In the example numbers were added in the order: 5, 6, 3, 4, 2, 9, 7, 8, 1.

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
	* 3 is less that 5 so we go left.
	* The space is empty so we add 3 there.
4. Add 4.
	* 4 is less than 5 so we go left.
	* 4 is more than 3 so we go right.
	* The space is empty so we add 4 there.
5. Add 2.
	* 2 is less than 5 so we go left.
	* 2 is less than 3 so we go left.
	* The space is empty so we add 2 there.

# Common Uses of Trees
# Creating a Tree
# Keeping a Balanced Tree
# Example
# Problem to Solve