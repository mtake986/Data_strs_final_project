# Linked List
In this tutorial, you'll learn what is a linked list and how to implement it in Python. There are several kinds of linked lists: singly, doubly, and circular, but we mainly focus on a doubly-linked list here for now. 

![Visualize a singly linked list](picture_files/LL_singly.jpg)
## `WHAT IS A LINKED LIST??`
Features of a linked list :
* a linear data structure
* including data called node
* each node has a data item and an address of the next node. 
* whose first node called Head and the last is called Tail



<!-- ## `Ok, but, Why does each node have a value and an address to the next node?` -->
## `OK, BUT, WHY DOES EACH NODE HAVE A VALUE AND AN ADDRESS TO THE NEXT NODE?`
That's because data in an array can be stored randomly in memory. For, example, when you define an array [1, 2, 3, 4, 5], possibly the order of data in the array is not always the same in memory. Thus, linked lists organize data randomly too. However, each node in a linked list has two stuff, a value and **an pointer to the next node**, we can keep our list together and give us quick access to each element when we need it. 

Most of linked lists have two address in a pointer: an address to previous and next nodes. A doubly linked list is named so because of the number of address a pointer of each node includes. In other words, it's a **bi-directional** list!!!!
![Visualize a doubly linked list](picture_files/LL_doubly.jpg)




## **`INSERTING`**
One of the biggest advantage of a linked list is the speed, in another word, Big O notation. Because of pointers, You only have to do some stuff on neighboring values in the linked list during inserting. Unlike a dynamic array, we don't have to move all of the values when you insert a value into a linked list. 

Representation for inserting a value into a linked list. 
* NEW_NODE = a new node inserted into the linked list
* HEAD = the first value in the linked list
* TAIL = the end value in teh linked list
* CURRENT = a value before NEW_NODE


### **Inserting at the head**
Steps to insert a value in the head:
1. create NEW_NODE
2. set the address for the next value of NEW_NODE to current HEAD
3. set the address for the previous value of HEAD to NEW_NODE
4. set HEAD of the linked list to NEW_NODE

### **Inserting at the tail**
It looks very similar to inserting at the head, so I recommend comparing the both steps for inserting at the head and tail.
1. create NEW_NODE
2. set the address for the previous value of NEW_NODE to current TAIL
3. set the address for the next value of current TAIL to NEW_NODE
4. set TAIL of the linked list to NEW_NODE

### **Inserting in the middle**
It's a bit more complicated. Below are the steps:
1. create NEW_NODE
2. set the address for the next value of NEW_NODE to NODE_AFTER_CURRENT
3. set the address for the previous value of NEW_NODE to CURRENT
4. set the address for the next value of CURRENT to NEW_NODE
5. set the address for the previous value of NODE_AFTER_CURRENT to NEW_NODE

### **Special Case**
If there was no node in the linked list, all we need to do is to set HEAD and TAIL to NEW_NODE.
## **`REMOVING`**
You should be so confused now and not even want to learn about removing a value from a linked lis, but don't leave!! I promise that removing a value from a linked list is much more simple and easier to understand than inserting. So, let's get started. 
* AFTER_NODE is a node after the deleted node.
* BEFORE_NODE is a node before the deleted node.
### **Removing the first value**
What you have to do is just two things: 1. remove the first value from the linked list and 2. set the previous address of the second node to the HEAD.
1. set the address for the previous value of the second node in the linked list to nothing (because the first node is deleted and no address for the previous value of the second node.)
2. set the HEAD to be the second node.

### **Removing the last value**
Likely to the process of inserting, it's very similar to removing the first value. 
1. set the address for the next value of the second to last node in the linked list to nothing (because the last node is deleted and no address for the next value of the second to last node.)
2. set the TAIL to be the second to last node.

### **Removing a value from the middle**
You got lucky, dude!! It won't be as tricky as inserting in the middle. The only two steps necessary are below:
1. set the address for the previous value of AFTER_NODE to BEFORE_NODE
2. set the address for the next value of BEFORE_NODE to AFTER_NODE

### **Special Case**
If there was only one node in the linked list, all we need to do is to set HEAD and 

## **`OPERATIONS FOR LINKED LISTS`**
Name | Description | BigO()
-----| ------------|--------
<!-- insert -->
insert_head(a) | adds a at the head | O(1)
insert_tail(a) | adds a at the end | O(1)
insert_middle(index, a) | adds a after i-th node | O(n) - unlikely inserting at the head or end, the Big O is n because you have to loop through the linked list until you find i-th node. 
<!-- remove -->
remove_head(a) | removes the node at the head | O(1)
remove_tail(index) | removes the node at the end | O(1) - index must be one smaller than the length of the linked list
remove(index) | removes index node | O(n) - similar to inserting in the middle, it requires a loop to find the inde node.
empty()| returns False if the stack is empty, True for not empty | O(1)- just needs to compare to 0
size()| returns the length of the linked list | O(1) 

## **`When linked lists are used??`**
As you learn about a linked list, you may have asked when linked lists are necessary?? Yeah, I asked the same question to my teacher when I learned linked list first because a linked list is almost all same as an array. But, linked list has the faster performance than a dynamic array does. Let's compare both Big O of the operations.
Operation | Dynamic Array | Linked List
-----| ------------|--------
<!-- insert -->
insert front | O(n) | O(1)
insert end | O(1) | O(1)
insert middle | O(n) |  O(n)
<!-- remove -->
remove front | O(n) | O(1)
remove tail | O(1) | O(1)
remove middle | O(n) | O(n)

Operations of inserting or removing a value at the head or in the middle of both linked list and array are O(1) and O(n), but the difference is when inserting and removing at the front. The reason why it takes n is because all of the values in a dynamic array have to be pushed one index back because of the value added at the head. 

## **`It's time to code!!`**
Check the python code below and understand what's going on there. Then, solve the problems I provided. It's better if you fully understand how to use a class and functions in python. You may feel there are so many code below at a glance, but there are so many comments to explain what's happening in class and functions, so don't get scared plz. Scroll all the way down and go to a solution page to see the answers.

``` python
class Linkedlist:
  class Node:
    # Remember a node in a linked list has to have three stuff: data(value), pointer for the next and previous node
    # The function below is called when you create a node like this Linkedlist.Node. 
    def __init__(self, data):
      self.data = data
      self.next_node = None
      self.prev_node = None
      # I said each node needs three things, but pointer for the next and prev node has to be none because you don't know where the node is inserted, so set them to None.
  def __init__(self):
    # Create an empty linked list with this function. 
    self.head = None
    self.tail = None
    # An empty linked list has no value inside, so set the head and tail to None
  
  def insert_head(self, value):
    new_node = Linkedlist.Node(value):

    # you need to think about the two cases of linked list: empty and not
    # if the linked list is empty
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    # Although you set both self.head and .tail to None in the __init__ function just above, at this time you need to set them to the new node. 
    
    # if not empty
    else: 
      new_node.next = self.head # The current head, but it'll be the second node in the list, which is the next node of the new_node
      self.head.prev = new_node # Because the current head will be the second, the first node will be the new node, you need to connect both nodes. Thus, set the current head's prev to new node. 
      self.head = new_node # set the new node as the head 

  def insert_tail(self, value):
    ################
    # Problem 1: write code to implement a function to insert a value at the end of the linked list. 
    ################

  def remove_head(self):
    ################
    # Problem 2: write code to implement a function to delete a value at the head of the linked list. Look up the function below called remove_tail if you have no idea here. 
    ################

  def remove_tail(self):
    # Likely inserting, there are two cases: only one value or more than one value in the linked list
    # if linked list has only one value, the head and tail must be the same and set them to None as the linked list has no value,
    if self.head == self.tail:
      self.head = None
      self.tail = None
    
    else:
      self.tail.prev.next = None # Set the next node of the second to the last value to None. 
      self.tail = self.tail.prev # Set the tail to the second last value. 

  def replace([three, parameters, here]):
    ################
    # Problem 3: replace a value to a new value, neither inserting or removing
    ################

    
  def insert_middle(self, value, new_value):
    # insert in the middle. For example, you have a list[1, 2, 3, 4, 5] and want to insert 6 after 3. What you have to do is first to find the value the new value is added after in the list, in this case 2, by using for or while. Iterate through the list until you get None after the tail. 
    current = self.head # Start with the head
    while current is not None:
      if current.data == value: # You found the value!! If the value is the tail, you can call the fuction, insert_tail. You don't need to call insert_head in this function because when head == tail, you can call insert_tail and when inserting after the head and in the middle are the same thing. 
        if current == self.tail:
          self.insert_tail(new_value)
        else:
          new_node = Linkedlist.Node(new_value)
          # If you forget the process of inserting in the middle, go ahead and check the process in the explanation page. 
          # First, set the next and prev node of the new value to the current and the node after the current. 
          new_node.prev = current
          new_node.next = current.next
          # Then, change the next and prev node of the current and the node after the current.
          curr.next = new_node
          curr.next.prev = new_node
        return # After inserting is done, just finish the while loop.
      # If current is not the value, go to the next node to continue the journey to find the value
      current = current.next


  def remove_middle(self):
    ################
    # Problem 4: write code to implement a function to delete from the middle. When the value == head or the value == tail, use the functions you've created already above, so you don't have to code a lot
    ################

```




[See a solution](solution/solve_linkedlist.md)

[Go to the next page for tree](./tree.md)

[back to welcome page](./welcome.md)