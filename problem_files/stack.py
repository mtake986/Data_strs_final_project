'''
Solve it by using a stack. 
Create a list and add one character in a string **Good morning** at a time by using append() into the list you have created. Then, change **morning** to **evening** instead of **morning**.
Note that 
* when you pop some words, you can use for loop. 
* the code below is to connect all words in a list, use
print(''.join(your_list_name))
'''

# Example problems
lis = list()
lis.append('H')
lis.append('e')
lis.append('l')
lis.append('l')
lis.append('o')
lis.append(' ')
lis.append('w')
lis.append('o')
lis.append('r')
lis.append('l')
lis.append('d')
print(''.join(lis))
### Output Hello world
for i in range(7):
    lis.pop()
lis.append('A')
lis.append('m')
lis.append('e')
lis.append('r')
lis.append('i')
lis.append('c')
lis.append('a')
print(''.join(lis))
### Output Hello America

# Start coding from here

