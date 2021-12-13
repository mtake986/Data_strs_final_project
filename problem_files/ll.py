
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
    new_node = Linkedlist.Node(value)

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
    pass
  def remove_head(self):
    ################
    # Problem 2: write code to implement a function to delete a value at the head of the linked list. Look up the function below called remove_tail if you have no idea here. 
    ################
    pass
  def remove_tail(self):
    # Likely inserting, there are two cases: only one value or more than one value in the linked list
    # if linked list has only one value, the head and tail must be the same and set them to None as the linked list has no value,
    if self.head == self.tail:
      self.head = None
      self.tail = None
    
    else:
      self.tail.prev.next = None # Set the next node of the second to the last value to None. 
      self.tail = self.tail.prev # Set the tail to the second last value. 

  def replace(self):
    ################
    # Problem 3: replace a value to a new value, neither inserting or removing. Make sure you need to add more parameters. 
    ################
    pass
    
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
          current.next = new_node
          current.next.prev = new_node
        return # After inserting is done, just finish the while loop.
      # If current is not the value, go to the next node to continue the journey to find the value
      current = current.next


  def remove_middle(self, value):
    ################
    # Problem 4: write code to implement a function to delete from the middle. When the value == head or the value == tail, use the functions you've created already above, so you don't have to code a lot
    ################
    pass

