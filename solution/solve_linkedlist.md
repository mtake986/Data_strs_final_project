# Solution: Linked List
``` python
class Linkedlist:
  ################
  # Problem 1
  ################
  def insert_tail(self, value):
    new_node = Linkedlist.Node(value):

    # you need to think about the two cases of linked list: empty and not
    # if the linked list is empty
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    # Although you set both self.head and .tail to None in the __init__ function just above, at this time you need to set them to the new node. 
    
    # if not empty
    else: 
      new_node.prev = self.tail # The current tail, but it'll be the second last node in the list, which will be the prev node of the new_node
      self.tail.next = new_node # Because the current tail will be the second last and the last node will be the new node, you need to connect the nodes. Thus, set the current tail's next to new node. 
      self.tail = new_node # set the new node to the tail.  

  ################
  # Problem 2
  ################
  def remove_head(self):
      # Likely inserting, there are two cases: only one value or more than one value in the linked list
      # if linked list has only one value, the head and tail must be the same and set them to None as the linked list has no value,
    if self.head == self.tail:
      self.head = None
      self.tail = None
  # If the list has more than one item in it, then only self.head
  # will be affected.
    else:
      self.head.next.prev = None # There will be no node before the second first node in the linked list, so set it to None. 
      self.head = self.head.next # Set the second first value to the head

  ################
  # Problem 3
  ################
  def replace(self, old, new):
    current = self.head
      while current is not None:
        if current.data == old:
          current.data = new
        current = current.next
        
  ################
  # Problem 4
  ################
  def remove(self, value):
    current = self.head
    while current is not None:
      if current.data == value: 
        # When there is only one value in the list
        if current = self.tail and current == self.tail:
          self.head = None
          self.tail = None
        # When removing the head value
        elif current == self.head:
          self.remove_head()
        # When removing the tail value
        elif current == self.tail:
          self.remove_tail()
        # When removing a value in the middle
        else:
          current.next.prev = curr.prev
          current.prev.next = curr.next
        return 
      # Continue the journey to find the value 
      current = current.next

```


[Go back to a Stack page](../linked_list.md)