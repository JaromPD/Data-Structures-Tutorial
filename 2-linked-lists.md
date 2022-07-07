# Linked Lists
Linked lists are another type of data structure that every developer should be aware of. Linked Lists are lists made out of "nodes". Nodes contain the value to be stored, a forward pointer, and a backward pointer. These pointers tell the list which value is next or before in the list. This allows the nodes to be stored anywhere in the system's memory because they simply give directions to the next or previous value.

Taking a look at the visualization below can help you begin to understand how Linked Lists work. Take the value "B" for example. The node "B" contains the value "B", a forward pointer to node "C", and a backward pointer to node "A". 

Now to talk about the operations shown below. We have a base list of A, B, C, D. We then remove C which is at index 2 before also removing A at index 0. After that we add A back at index 1 and then add C back at index 0.

As you can see Linked Lists allow you to add your values in anywhere because you just have to change the forward pointer of the previous node to the new node, and the backward pointer of the next node to the new node.. 
```
         ┌─────┐───►┌─────┐───►┌─────┐───►┌─────┐
 Base    │  A  │    │  B  │    │  C  │    │  D  │
         └─────┘◄───└─────┘◄───└─────┘◄───└─────┘
         ┌─────┐───►┌─────┐───►┌─────┐
 -C @ 2  │  A  │    │  B  │    │  D  │
         └─────┘◄───└─────┘◄───└─────┘
         ┌─────┐───►┌─────┐
 -A @ 0  │  B  │    │  D  │
         └─────┘◄───└─────┘
         ┌─────┐───►┌─────┐───►┌─────┐
 +A @ 1  │  B  │    │  A  │    │  D  │
         └─────┘◄───└─────┘◄───└─────┘
         ┌─────┐───►┌─────┐───►┌─────┐───►┌─────┐
 +C @ 0  │  C  │    │  B  │    │  A  │    │  D  │
         └─────┘◄───└─────┘◄───└─────┘◄───└─────┘
```
# Common Uses
# Components
# Operations
# Creating a Linked List
# Example
# Problem to Solve
