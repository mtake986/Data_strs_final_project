# Solution: Stack
``` python

lis = list()
lis.append('G')
lis.append('o')
lis.append('o')
lis.append('d')
lis.append(' ')
lis.append('m')
lis.append('o')
lis.append('r')
lis.append('n')
lis.append('i')
lis.append('n')
lis.append('g')
print(''.join(lis))
### Output Good morning
for i in range(7):
    lis.pop()
lis.append('e')
lis.append('v')
lis.append('e')
lis.append('n')
lis.append('i')
lis.append('n')
lis.append('g')
print(''.join(lis))
### Output Good evening
```

[Go back to the page for stack](../stack.md)
