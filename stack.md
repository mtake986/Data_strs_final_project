# Stack

A *stack* is a data structure that stores data and takes care of an order of a data set where data can be added into and removed out of. It stores data in "Last In, First Out", or (LIFO). It's implemented easily by a list in Python. 

In stack, an element is added at the end of the list and only the last element at the end of a list is removed. Thus, to insert and delete only happens at the end of a list. 

![Visualize a stack](picture_files/stack_illustration.png)

### The functions for stacks
Name | Description | BigO()
-----| ------------|--------
empty()| returns False if the stack is empty, True for not empty|O(1)
size()| returns the length of the stack|O(1)
top()| returns the first element (index=0) in the stack |O(1)
push(xyz)| Inserts ‘xyz’ at the end of the stack|O(1)
top()| Deletes the end element (index=size()-1) of the stack|O(1)

Good news is that you can easily implement a stack and see what's actually happening to the stack with a list and print() function. Here's the code. Take a closer look at the end of the stack when the operation is either push or pop.
``` python
stack = []
### Create an empty stack
print('push a to the stack')
stack.append('a')
### Output ['a']
print('push b to the stack')
stack.append('b')
### Output ['a', 'b']

print(stack.pop(), stack)
### Output b, ['a']
print('push c to the stack')
stack.append('c')
### Output ['a', 'c']

print(stack.pop(), stack)
### Output c, ['a']

print(stack.pop(), stack)
### Output a, []
print(f'Here is the empty stack. => {stack}')
### []
```

Stack is a simple and easy data structure to implement, but it doesn't mean stack is not used anywhere. 

The most imaginable situation of a stack is an undo shortcut or deleting words on a text editor like Google docs. Let's say you type *I love Python* on a text editor. When you change Python to Java, the first word that is deleted first is *n*, and *o*, *h*, and so on until *p*. Then, you can type *Java* to replace python.
Other examples are: 
* All websites' urls you visited are stored in a stack. When you press the back button in browsers, the current url which is at the end of the stack is removed from the stack, and you'd see the website which was at the second of the stack. 
* Place two parallel mirrors facing each other. Any object in between them would be reflected recursively.

In Python, a stack is used when you implement recursion. Recursion is the process of defining something in terms of itself. Below is the example code of recursion. 

``` python
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 4
print(f"The factorial of {num} is the {factorial(num)} = 4 * 3 * 2 * 1")
### Output 
### The factorial of 4 is the 24 = 4 * 3 * 2 * 1
```
In the example, when the function named *factorial* was called, what's going on inside of it is to check if *x* is 1 or not. Because *x* is 4, the function return *4 * factorial(4-1)* and 4 was in a stack in pc memory. Then, factorial function would be called again and it returned *3 * factrial(3-1)* and 3 was into the stack. When x is 1, it just returned 1, no function here, so there are *4 * 3 * 2 * 1* in the stack now. You can see all values were added at the end of the stack. Also, because of LIFO, the order of deleting is 1 => 2 => 3 => 4. 

Remember that a stack's key concept is LIFO. I don't explain this a lot here, but there is something similar called a queue whose key concept is First In, First Out, FIFO.

## Here is an example problem for you. 
Solve it by using a stack. 
Create a list and add **Good morning** to it. Then, change **morning** to **evening** instead of **morning**.
Note that 
* you need to add one letter or a space at a time. 
* when you pop some words, you an use for loop. 
* in order to connect all words in a list, use
``` python
print(''.join(your_list_name))
```

[See a solution](solution/solve_stack.md)

[back to welcome page](./welcome.md)

[Go to linked list page](./linked_list.md)