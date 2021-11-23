# Linked List
In this tutorial, you'll learn what is a linked list and how to implement it in Python. There are several kinds of linked lists: singly, doubly, and circular, but we mainly focus on a doubly-linked list here for now. 

![Visualize a singly linked list](picture_files/LL_singly.jpg)
## What is a linked list??
Features of a linked list :
* a linear data structure
* including data called node
* each node has a data item and an address of the next node. 
* whose first node called Head and the last is called Tail

### Ok, but, Why does each node have a value and an address to the next node?
That's because data in an array can be stored randomly in memory. For, example, when you define an array [1, 2, 3, 4, 5], possibly the order of data in the array is not always the same in memory. Thus, linked lists organize data randomly too. However, each node in a linked list has two stuff, a value and **an pointer to the next node**, we can keep our list together and give us quick access to each element when we need it. 

Most of linked lists have two address in a pointer: an address to previous and next nodes. A doubly linked list is named so because of the number of address a pointer of each node includes. In other words, it's a **bi-directional** list!!!!

![Visualize a doubly linked list](picture_files/LL_doubly.jpg)









[back to welcome page](welcome.md)