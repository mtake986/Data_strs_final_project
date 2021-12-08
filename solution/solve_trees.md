```python
class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def inserting(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._inserting(data, self.root)  
    def _inserting(self, data, node): 
        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._inserting(data, node.left)
        elif node.data < data:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._inserting(data, node.right)
```

[Go back to the page](../trees.md)
